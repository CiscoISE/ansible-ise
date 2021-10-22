#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

try:
    from ansible.errors import AnsibleActionFail
except ImportError:
    ANSIBLE_ERRORS_INSTALLED = False
else:
    ANSIBLE_ERRORS_INSTALLED = True
try:
    import requests
except ImportError:
    REQUESTS_INSTALLED = False
else:
    REQUESTS_INSTALLED = True
import json
import zipfile
import io


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
        if node.get("roles"):
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
        return "{name} <{ip}>".format(name=self.name, ip=self.ip)

    def __repr__(self):
        return "{name} <{ip}>".format(name=self.name, ip=self.ip)

    def is_standalone(self):
        headers = {'Content-Type': 'text/xml'}
        url = "https://{ip}/admin/API/Infra/Node/SimpleList".format(ip=self.ip)
        response = False
        try:
            response = requests.get(url=url, headers=headers, auth=(self.username, self.password), verify=False)
        except Exception as e:
            raise AnsibleActionFail("Couldn't connect, the node might be still initializing, try again in a few minutes. Error received: {e}".format(e=e))
        if not response:
            raise AnsibleActionFail("Couldn't get a valid response from the API. Maybe the node is still initializing, try again in a few minutes.")
        elif "STANDALONE" in response.text:  # TODO: Parse the XML to look for the nodeRoleStatus tag.
            return True
        return False

    def app_server_is_running(self):
        url = "https://{ip}/ers/config/op/systemconfig/iseversion".format(ip=self.ip)
        headers = {'Accept': 'application/json'}
        try:
            response = requests.get(url=url, headers=headers, auth=(self.username, self.password), verify=False)
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
        try:
            response = requests.get(url=url, timeout=15, headers=headers, auth=(self.username, self.password), verify=False)
        except requests.exceptions.ReadTimeout:
            raise AnsibleActionFail("The request timed out. Please verify that the API is enabled on the node.")
        except Exception as e:
            raise AnsibleActionFail(e)
        json_response = json.loads(response.text)
        for item in json_response.get("response"):
            if item.get("friendlyName") == "Default self-signed server certificate":
                return item.get("id")

    def register_node(self, primary):
        headers = {'Content-Type': 'application/xml'}
        url = "https://{primary_ip}/admin/API/Infra/Register".format(primary_ip=primary.ip)
        xml_template = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                        '<infraDeployBean>\n'
                        '    <displayname>{hostname}</displayname>\n'
                        '    <gateway></gateway>\n'
                        '    <hostname>{fqdn}</hostname>\n'
                        '    <nodeIPaddr>{ip}</nodeIPaddr>\n'
                        '    <username>{username}</username>\n'
                        '    <password>{password}</password>\n'
                        '    {roles}'
                        '</infraDeployBean>')
        roles_str = ""
        for key in self.roles.keys():
            roles_str += "<roles>"
            for value in self.roles.get(key):
                roles_str += "<item>{value}</item>".format(value=value)
            roles_str += "</roles>"

        data = xml_template.format(
            hostname=self.hostname,
            fqdn="{hostname}.{domain}".format(hostname=self.hostname, domain=self.domain),
            ip=self.local_ip,
            username=self.username,
            password=self.password,
            roles=roles_str
        )
        try:
            response = requests.post(url=url, timeout=300, auth=(primary.username, primary.password), headers=headers, data=data, verify=False)
        except Exception as e:
            raise AnsibleActionFail(e)
        if not response:
            raise AnsibleActionFail("Failed to receive a valid response from the API. The actual response was: {response}".format(response=response.text))


class ISEDeployment(object):
    def __init__(self):
        self.primary = None
        self.nodes = []

    def add_primary(self, node):
        self.primary = Node(node)

    def add_node(self, node):
        self.nodes.append(Node(node))

    def export_import_default_self_signed_server_cert(self):
        for node in self.nodes:
            cert_id = node.return_id_of_certificate()
            data = json.dumps({"id": cert_id, "export": "CERTIFICATE"})
            url = "https://{ip}/api/v1/certs/system-certificate/export".format(ip=node.ip)
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            try:
                response = requests.post(url=url, timeout=15, data=data, headers=headers, auth=(node.username, node.password), verify=False)
            except Exception as e:
                AnsibleActionFail(e)

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
            try:
                response = requests.post(url=url, timeout=15, data=data, headers=headers, auth=(self.primary.username, self.primary.password), verify=False)
                return_message = json.loads(response.text)["response"]["message"]
            except Exception as e:
                AnsibleActionFail(e)

            if not response.status_code == 200:
                if not (return_message == 'Trust certificate was added successfully' or
                        return_message == "Certificates are having same subject, same serial number and they are binary equal. Hence skipping the replace"):
                    raise AnsibleActionFail("Unexpected response from API. Received response was {message}".format(message=return_message))

    def promote_primary_node(self):
        headers = {'Content-Type': 'text/xml'}
        url = "https://{ip}/admin/API/Infra/Edit".format(ip=self.primary.ip)
        xml_template = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                        '   <infraDeployBean>\n'
                        '       <displayname>{hostname}</displayname>\n'
                        '       <gateway></gateway>\n'
                        '       <hostname>{hostname}</hostname>\n'
                        '       <nodeIPaddr>{ip}</nodeIPaddr>\n'
                        '       <username>{username}</username>\n'
                        '       <password>{password}</password>\n'
                        '       {roles}\n'
                        '   </infraDeployBean>')
        roles_str = ""
        for key in self.primary.roles.keys():
            roles_str += "<roles>"
            for value in self.primary.roles.get(key):
                roles_str += "<item>{value}</item>".format(value=value)
            roles_str += "</roles>"

        data = xml_template.format(
            hostname=self.primary.hostname,
            ip=self.primary.ip,
            username=self.primary.username,
            password=self.primary.password,
            roles=roles_str
        )
        response = None
        try:
            response = requests.put(url=url, data=data, headers=headers, auth=(self.primary.username, self.primary.password), verify=False, timeout=60)
            if response:
                if "Node updated successfully" not in response.text:
                    raise AnsibleActionFail("Could not update node to PRIMARY")
        except Exception as e:
            raise AnsibleActionFail(e)
