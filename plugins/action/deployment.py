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
import requests
import json
import zipfile
import time
from unicon import Connection #TODO: Look for an alternate method of doing this
import io

# Temporary. Remove in final version.
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


argument_spec = dict(
    nodes=dict(type="list", required=True),
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
        self.ip = node.get("ip")
        self.local_ip = node.get("local_ip")
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

    def __str__(self):
        return "{} <{}>".format(self.name, self.ip)

    def __repr__(self):
        return "{} <{}>".format(self.name, self.ip)
    
    def is_standalone(self):
        headers = {'Content-Type': 'text/xml'}
        url = "https://{ip}/admin/API/Infra/Node/SimpleList".format(ip=self.ip)
        response = False
        retries = 3
        for i in range(retries):
            try:
                response = requests.get(url=url, headers=headers, auth=(self.username, self.password), verify=False)
            except Exception as e:
                raise AnsibleActionFail(e)
            if not response:
                raise AnsibleActionFail("REST API to check 'STANDALONE' status failed: {url}".format(url=url))
            elif "STANDALONE" in response.text: #TODO: Parse the XML to look for the nodeRoleStatus tag.
                return True
        return False

    def app_server_is_running(self):
        url = "https://{ip}/ers/config/op/systemconfig/iseversion".format(ip=self.ip)
        headers = {'Accept': 'application/json'}
        try:
            response = requests.get(url=url,headers=headers,auth=(self.username, self.password), verify=False)
            # Application Server is down but API Gateway is up
            if response.status_code == 502:
                return False
            # The Application Server is up
            if response.status_code == 200:
                return True
            # Any other case return False
            else:
                return False
        # Both Application Server and API Gateway are down
        except Exception as e:
            return False

    def return_id_of_certificate(self):
        url = "https://{ip}/api/v1/certs/system-certificate/{hostname}".format(ip=self.ip, hostname=self.hostname)
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        response = requests.get(url=url,headers=headers,auth=(self.username, self.password), verify=False)
        json_response = json.loads(response.text)
        for item in json_response.get("response"):
            if item.get("friendlyName") == "Default self-signed server certificate":
                return item.get("id")

    def register_node(self, primary):
        headers = {'Content-Type': 'application/xml'}
        url = "https://{primary_ip}/admin/API/Infra/Register".format(primary_ip=primary.ip)
        xml_template = \
"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <infraDeployBean>
        <displayname>{hostname}</displayname>
        <gateway></gateway>
        <hostname>{fqdn}</hostname>
        <nodeIPaddr>{ip}</nodeIPaddr>
        <username>{username}</username>
        <password>{password}</password>
        {roles}
    </infraDeployBean>"""
        roles_str = ""
        for key in self.roles.keys():
            roles_str += "<roles>"
            for value in self.roles.get(key):
                roles_str += "<item>{}</item>".format(value)
            roles_str += "</roles>"

        data = xml_template.format(
            hostname=self.hostname,
            fqdn="{}.{}".format(self.hostname,self.domain),
            ip=self.local_ip,
            username=self.username,
            password=self.password,
            roles=roles_str
        )

        try:
            response = requests.post(url=url, auth=(primary.username, primary.password), headers=headers, data=data, verify=False)
            if not response:
                raise AnsibleActionFail("Failed to register secondary using REST API: {url}, data: {data}, header: {header}, status code: {status_code}, response: {response}".format(
                        url=url, 
                        data=data,
                        header=response.headers,
                        status_code=response.status_code,
                        response=response.text
                    )
                )
        except:
            raise AnsibleActionFail("FAILED: Got exception for REST API: {url}, data: {data}, status code: {status_code}, response: {response}".format(
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
                raise AnsibleActionFail("More than one node has the 'PPAN' attribute. Only one primary node can be deployed.")
            else:
                self.primary = Node(node)
        else:
            self.nodes.append(Node(node))

    def export_import_default_self_signed_server_cert(self):
        for node in self.nodes:
            print("Exporting certificate for node {}".format(node.name))
            try:
                cert_id = node.return_id_of_certificate()
                data = json.dumps({"id": cert_id, "export": "CERTIFICATE"})
                url = "https://{ip}/api/v1/certs/system-certificate/export".format(ip=node.ip)
                headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

                response = requests.post(url=url,data=data,headers=headers,auth=(node.username, node.password),verify=False)

                if not response.status_code == 200:
                    raise AnsibleActionFail("Received status code {status_code} when exporting certificate.".format(status_code=str(response.status_code)))

                zf = zipfile.ZipFile(io.BytesIO(response.content), 'r')
                cert_data = zf.read("Defaultselfsignedservercerti.pem")
                data = json.dumps({
                    "allowBasicConstraintCAFalse": True,
                    "allowOutOfDateCert": False,
                    "allowSHA1Certificates": True,
                    "trustForCertificateBasedAdminAuth": True,
                    "trustForCiscoServicesAuth": True,
                    "trustForClientAuth": True,
                    "data": cert_data.decode("utf-8"),
                    "trustForIseAuth": True,
                    "name": node.name,
                    "validateCertificateExtensions": True
                })
                url = "https://{primary_node_ip}/api/v1/certs/trusted-certificate/import".format(primary_node_ip=self.primary.ip)
                headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
                response = requests.post(url=url, data=data, headers=headers, auth=(self.primary.username, self.primary.password), verify=False)
                return_message = json.loads(response.text)["response"]["message"]
                if not response.status_code == 200:
                    if not (return_message == 'Trust certificate was added successfully' or return_message == "Certificates are having same subject, same serial number and they are binary equal. Hence skipping the replace"):                
                        raise AnsibleActionFail("Expected message was 'Trust certificate was added successfully'. Actual message was {message}".format(message=return_message))

            except Exception as e:
                AnsibleActionFail(e)

    def promote_primary_node(self):
        headers = {'Content-Type': 'text/xml'}
        url = "https://{ip}/admin/API/Infra/Edit".format(ip=self.primary.ip)
        xml_template = \
"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <infraDeployBean>
        <displayname>{hostname}</displayname>
        <gateway></gateway>
        <hostname>{hostname}</hostname>
        <nodeIPaddr>{ip}</nodeIPaddr>
        <username>{username}</username>
        <password>{password}</password>
        {roles}
    </infraDeployBean>"""
        roles_str = ""
        for key in self.primary.roles.keys():
            roles_str += "<roles>"
            for value in self.primary.roles.get(key):
                roles_str += "<item>{}</item>".format(value)
            roles_str += "</roles>"

        data = xml_template.format(
            hostname=self.primary.hostname,
            ip=self.primary.ip,
            username=self.primary.username,
            password=self.primary.password,
            roles=roles_str
        )
        try:
            response = requests.put(url=url, data=data, headers=headers, auth=(self.primary.username, self.primary.password), verify=False, timeout=240)
            if "Node updated successfully" not in response.text:
                raise AnsibleActionFail("Could not update node to PRIMARY")
        except:
            raise AnsibleActionFail("Got exception invoking url: {url}, data: {data}, status code: {status_code}, response: {response}".format(
                    url=url, 
                    data=data, 
                    status_code=response.status_code,
                    response=response.text
                )
            )


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
        
        # Check all node are in STANDALONE state and Application Server is running
        if not (ise_deployment.primary.is_standalone() and ise_deployment.primary.app_server_is_running()):
            raise AnsibleActionFail("Primary server is not in STANDALONE state or application server is not running.")
        for node in ise_deployment.nodes:
            if not (node.is_standalone() and node.app_server_is_running()):
                raise AnsibleActionFail("Node {node_name} is not in STANDALONE state or application server is not running.".format(node_name=node.name))

        ise_deployment.export_import_default_self_signed_server_cert()
        ise_deployment.promote_primary_node()
        retries_left = 10
        wait_interval = 120
        time.sleep(wait_interval)
        while retries_left > 0:
            if ise_deployment.primary.app_server_is_running():
                for node in ise_deployment.nodes:
                    node.register_node(ise_deployment.primary)
                break
            else:
                retries_left -= 1
                time.sleep(wait_interval)

        response = "All nodes were successfully updated"

        self._result.update(dict(ise_response=response))
        return self._result
