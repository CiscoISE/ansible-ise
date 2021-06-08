from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible.errors import AnsibleActionFail
from urllib.parse import quote
from ansible_collections.cisco.ise.plugins.module_utils.exceptions import (
    PrimaryNodeNotUnique,
    ISEAPIError,
    NodeNotStandalone,
)
import requests
import json
import zipfile
import time
from unicon import Connection

argument_spec = dict(
    host_ip=dict(type="str", required=True),
    host_name=dict(type="str", required=True),
    username=dict(type="str", required=True),
    domain=dict(type="str", required=True),
    password=dict(type="str", required=True, no_log=True),
    roles=dict(type="list", required=True),
    ise_verify=dict(type="bool", default=True),
    ise_version=dict(type="str", default="3.0.0"),
    ise_wait_on_rate_limit=dict(type="bool", default=True), # TODO: verify what the true default value should be 
)

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class Node(object):
    def __init__(self, node):
        self.name = node.get("name")
        self.hostip = node.get("hostip")
        self.hostname = node.get("hostname")
        self.username = node.get("username")
        self.password = node.get("password")
        self.domain = node.get("domain")
        self.roles = {}
        for attribute in node.get("roles"):
            if attribute == 'PPAN':
                self.roles[attribute] = ["PAP", "on", "on", "PRIMARY"]
            if attribute == 'SPAN':
                self.roles[attribute] = ["PAP", "on", "on", "SECONDARY"]
            elif attribute == 'MNT-ACTIVE':
                self.roles[attribute] = ["MNT", "ACTIVE", ""]
            elif attribute == 'MNT-STANDBY':
                self.roles[attribute] = ["MNT", "STANDBY", ""]
            elif attribute == 'PDP':
                self.roles[attribute] = ["PDP", "on", "on", "None"]
            elif attribute == 'PXG':
                self.roles[attribute] = ["PXG"]
    
    def is_standalone(self):
        headers = {'Content-Type': 'text/xml'}
        url = "https://{hostip}/admin/API/Infra/Node/SimpleList".format(hostip=self.hostip)
        response = False
        retries = 3
        for i in range(retries):
            try:
                response = requests.get(url=url, headers=headers, auth=(self.username, self.password), verify=False)
            except Exception as e:
                raise AnsibleActionFail(e)
            if not response:
                raise ISEAPIError("REST API to check 'STANDALONE' status failed: {url}".format(url=url))
            elif "STANDALONE" in response.text:
                return True
            else:
                return False
        return False

    def app_server_is_running(self):
        dev = Connection(hostname=self.hostname,
                         start=["ssh -o UserKnownHostsFile=/dev/null {hostip}".format(hostip=self.hostip)],
                         username=self.username,
                         password=self.password,
                         os='ise')
        dev.settings.LINUX_INIT_EXEC_COMMANDS = []
        dev.connect()
        dev.sendline("term length 0")
        retry = 2
        for i in range(retry):
            res = dev.execute("show application status ise", timeout=120)
            time.sleep(2)
            status = 'Application Server                     running'
            if status in res:
                time.sleep(2)
                dev.disconnect()
                return True
            else:
                time.sleep(5)
                continue
        dev.disconnect()

    def return_id_of_certificate(self):
        url = "https://{hostip}/api/v1/certs/system-certificate/{hostname}".format(self.hostip, self.hostname)
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        response = requests.get(url=url,headers=headers,auth=(self.username, self.password), verify=False)
        json_response = json.loads(response.text)
        for item in json_response.get("response"):
            if item.get("friendlyName") == "Default self-signed server certificate":
                return item.get("id")

    def register_node(self, primary):
        headers = {'Content-Type': 'application/xml'}
        url = "https://{primary_hostip}/admin/API/Infra/Register".format(primary_hostip=primary.hostip)
        xml_template = \
"""
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <infraDeployBean>
        <displayname>{hostname}</displayname>
        <gateway></gateway>
        <hostname>{fqdn}</hostname>
        <nodeIPaddr>{hostip}</nodeIPaddr>
        <username>{username}</username>
        <password>{password}</password>
        <roles>{roles}</roles>
    </infraDeployBean>
"""
        roles_str = ""
        for key in self.roles.keys():
            for value in self.roles.get(key):
                roles_str += "<item>{}</item>".format(value)

        data = xml_template.format(
            hostname=self.hostname,
            fqdn="{}.{}".format(self.hostname,self.domain),
            hostip=self.hostip,
            username=self.username,
            password=self.password,
            roles=roles_str
        )
        
        response = False
        retries = 3

        for i in range(retries):
            try:
                # TODO: Here we're passing the primary node's credentials. In the original script they pass the secondary node's credentials (I believe by mistake)
                response = requests.post(url=url, auth=(primary.username, primary.password), headers=headers, data=data, verify=False)
                pass
            except:
                raise ISEAPIError("FAILED: Got exception for REST API: {url}, data: {data}, status code: {status_code}, response: {response}".format(
                        url=url, 
                        data=data, 
                        status_code=response.status_code,
                        response=response.text
                    )
                )
                continue
            if not response:
                raise ISEAPIError("Failed to register using REST API: {url}, data: {data}, header: {header}, status code: {status_code}, response: {response}".format(
                        url=url, 
                        data=data,
                        header=response.headers,
                        status_code=response.status_code,
                        response=response.text
                    )
                )
                continue
            else:
                raise ISEAPIError("Failed to register secondary using REST API: {url}, data: {data}, status code: {status_code}, response: {response}".format(
                        url=url, 
                        data=data, 
                        status_code=response.status_code,
                        response=response.text
                    )
                )
    

class ISEDeployment(object):
    def __init__(self):
        self.primary = None
        self.nodes = []

    def has_primary(self):
        return self.primary is not None

    def add_node(self, node):
        if "PPAN" in node.get("roles"):
            if self.has_primary():
                raise PrimaryNodeNotUnique("More than one node has the 'PPAN' attribute. Only one primary node can be deployed.")
            else:
                self.primary = Node(node)
        else:
            self.nodes.append(Node(node))

    def export_import_default_self_signed_server_cert(self):
        for node in self.nodes:
            try:
                cert_id = node.return_id_of_certificate()
                data = json.dumps({"id": cert_id, "export": "CERTIFICATE"})
                url = "https://{hostip}/api/v1/certs/system-certificate/export".format(self.hostip)
                headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

                response = requests.post(url=url,data=data,headers=headers,auth=(node.username, node.password),verify=False)

                if not response.status_code == 200:
                    raise ISEAPIError("Received status code {status_code} when exporting certificate.".format(status_code=str(response.status_code)))

                zf = zipfile.ZipFile(response.content, 'r')
                cert_data = zf.read("Defaultselfsignedservercerti.pem")
                cert_data[len(cert_data)-1] = "-----END CERTIFICATE-----"
                cert_data = "".join(cert_data)
                data = json.dumps({
                    "allowBasicConstraintCAFalse": True,
                    "allowOutOfDateCert": False,
                    "allowSHA1Certificates": True,
                    "trustForCertificateBasedAdminAuth": True,
                    "trustForCiscoServicesAuth": True,
                    "trustForClientAuth": True,
                    "data": cert_data,
                    "trustForIseAuth": True,
                    "name": "testTrustCertBaltimore",
                    "validateCertificateExtensions": True
                })
                url = "https://{primary_node_ip}/api/v1/certs/trusted-certificate/import".format(primary_node_ip=self.primary.hostip)
                headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
                response = requests.post(url=url, data=data, headers=headers, auth=(self.primary.username, self.primary.password), verify=False)
                output = json.loads(response.text)
                if not response.status_code == 200:
                    raise ISEAPIError("Received status code {status_code} when importing certificate.".format(status_code=str(response.status_code)))
                if not output['response']['message'] == 'Trust certificate was added successfully':
                    raise ISEAPIError("Expected message was 'Trust certificate was added successfully'. Actual message was {message}".format(message=output['response']['message']))
                if not output['response']['status'] == 'Success':
                    raise ISEAPIError("Expected response status was 'Success'. Actual message was {message}".format(message=output['response']['status']))

            except Exception as e:
                print(e)
                assert False

    def promote_primary_node(self):
        headers = {'Content-Type': 'text/xml'}
        url = "https://{hostip}/admin/API/Infra/Edit".format(hostip=self.primary.hostip)
        xml_template = \
"""
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <infraDeployBean>
        <displayname>{hostname}</displayname>
        <gateway></gateway>
        <hostname>{hostname}</hostname>
        <nodeIPaddr>{hostip}</nodeIPaddr>
        <username>{username}</username>
        <password>{password}</password>
        <roles>{roles}</roles>
    </infraDeployBean>
"""
        roles_str = ""
        for key in self.primary.roles.keys():
            for value in self.primary.roles.get(key):
                roles_str += "<item>{}</item>".format(value)

        data = xml_template.format(
            hostname=self.primary.hostname,
            hostip=self.primary.hostip,
            username=self.primary.username,
            password=self.primary.password,
            roles=roles_str
        )

        retries = 3
        for i in range(retries):
            try:
                response = requests.put(url=url, data=data, headers=headers, auth=(self.primary.username, self.primary.password), verify=False, timeout=240)
                pass
            except:
                raise ISEAPIError("Got exception retrying url: {url}, data: {data}, status code: {status_code}, response: {response}".format(
                        url=url, 
                        data=data, 
                        status_code=response.status_code,
                        response=response.text
                    )
                )
                time.sleep(10)
                continue


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail("ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(
                required_if=required_if,
                required_one_of=required_one_of,
                mutually_exclusive=mutually_exclusive,
                required_together=required_together,
            ),
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            raise AnsibleActionFail(errors)

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()
        
        ise_deployment = ISEDeployment()
        for node in self._task.args.get("nodes"):
            ise_deployment.add_node(node)
        
        # Check all node are in STANDALONE state
        if not (ise_deployment.primary.is_standalone() and ise_deployment.primary.app_server_is_running()):
            raise NodeNotStandalone("Primary server is not in STANDALONE state or application server is not running.")
        for node in ise_deployment.nodes:
            if not (node.is_standalone() and node.app_server_is_running()):
                raise NodeNotStandalone("Node {node_name} is not in STANDALONE state or application server is not running.".format(node_name=self.name))

        ise_deployment.export_import_default_self_signed_server_cert()
        ise_deployment.promote_primary_node()
        for node in ise_deployment.nodes:
            node.register_node()

        wait_time = 120
        retries = 5
        retries_sleep_time = 30
        time.sleep(wait_time)
        for retry in range(retries):
            if not ise_deployment.primary.app_server_is_running():
                if retry == retries - 1:
                    raise Exception("App server did not come up even after {0} retries with each retry sleep {1}".format(retries, retries_sleep_time))
                time.sleep(retries_sleep_time)

        response = None

        self._result.update(dict(ise_response=response))
        return self._result
