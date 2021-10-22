#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_deployment
short_description: Resource module for Node Deployment
description:
- Manage operations create, update and delete of the resource Node Deployment.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  administration:
    description: Node Deployment's administration.
    suboptions:
      isEnabled:
        description: IsEnabled flag.
        type: bool
      role:
        description: Node Deployment's role.
        type: str
    type: dict
  fdqn:
    description: Node Deployment's fdqn.
    type: str
  generalSettings:
    description: Node Deployment's generalSettings.
    suboptions:
      monitoring:
        description: Node Deployment's monitoring.
        suboptions:
          enablePXGrid:
            description: EnablePXGrid flag.
            type: bool
          isEnabled:
            description: IsEnabled flag.
            type: bool
          isMntDedicated:
            description: IsMntDedicated flag.
            type: bool
          otherMonitoringNode:
            description: Node Deployment's otherMonitoringNode.
            type: str
          policyservice:
            description: Node Deployment's policyservice.
            suboptions:
              enableDeviceAdminService:
                description: EnableDeviceAdminService flag.
                type: bool
              enableNACService:
                description: EnableNACService flag.
                type: bool
              enablePassiveIdentityService:
                description: EnablePassiveIdentityService flag.
                type: bool
              enableProfilingService:
                description: EnableProfilingService flag.
                type: bool
              enabled:
                description: Enabled flag.
                type: bool
              sessionService:
                description: Node Deployment's sessionService.
                suboptions:
                  isEnabled:
                    description: IsEnabled flag.
                    type: bool
                  nodegroup:
                    description: Node Deployment's nodegroup.
                    type: str
                type: dict
              sxpservice:
                description: Node Deployment's sxpservice.
                suboptions:
                  isEnabled:
                    description: IsEnabled flag.
                    type: bool
                  userInterface:
                    description: Node Deployment's userInterface.
                    type: str
                type: dict
            type: dict
          role:
            description: Node Deployment's role.
            type: str
        type: dict
    type: dict
  hostname:
    description: Hostname path parameter. Node name of the existing deployed node.
    type: str
  password:
    description: Node Deployment's password.
    type: str
  profileConfiguration:
    description: Node Deployment's profileConfiguration.
    suboptions:
      activeDirectory:
        description: Node Deployment's activeDirectory.
        suboptions:
          daysBeforeRescan:
            description: Node Deployment's daysBeforeRescan.
            type: int
          description:
            description: Node Deployment's description.
            type: str
          enabled:
            description: Enabled flag.
            type: bool
        type: dict
      dhcp:
        description: Node Deployment's dhcp.
        suboptions:
          description:
            description: Node Deployment's description.
            type: str
          enabled:
            description: Enabled flag.
            type: bool
          interface:
            description: Node Deployment's interface.
            type: str
          port:
            description: Node Deployment's port.
            type: int
        type: dict
      dhcpSpan:
        description: Node Deployment's dhcpSpan.
        suboptions:
          description:
            description: Node Deployment's description.
            type: str
          enabled:
            description: Enabled flag.
            type: bool
          interface:
            description: Node Deployment's interface.
            type: str
        type: dict
      dns:
        description: Node Deployment's dns.
        suboptions:
          description:
            description: Node Deployment's description.
            type: str
          enabled:
            description: Enabled flag.
            type: bool
        type: dict
      http:
        description: Node Deployment's http.
        suboptions:
          description:
            description: Node Deployment's description.
            type: str
          enabled:
            description: Enabled flag.
            type: bool
          interface:
            description: Node Deployment's interface.
            type: str
        type: dict
      netflow:
        description: Node Deployment's netflow.
        suboptions:
          description:
            description: Node Deployment's description.
            type: str
          enabled:
            description: Enabled flag.
            type: bool
          interface:
            description: Node Deployment's interface.
            type: str
          port:
            description: Node Deployment's port.
            type: int
        type: dict
      nmap:
        description: Node Deployment's nmap.
        suboptions:
          description:
            description: Node Deployment's description.
            type: str
          enabled:
            description: Enabled flag.
            type: bool
        type: dict
      pxgrid:
        description: Node Deployment's pxgrid.
        suboptions:
          description:
            description: Node Deployment's description.
            type: str
          enabled:
            description: Enabled flag.
            type: bool
        type: dict
      radius:
        description: Node Deployment's radius.
        suboptions:
          description:
            description: Node Deployment's description.
            type: str
          enabled:
            description: Enabled flag.
            type: bool
        type: dict
      snmpQuery:
        description: Node Deployment's snmpQuery.
        suboptions:
          description:
            description: Node Deployment's description.
            type: str
          enabled:
            description: Enabled flag.
            type: bool
          eventTimeout:
            description: Node Deployment's eventTimeout.
            type: int
          retries:
            description: Node Deployment's retries.
            type: int
          timeout:
            description: Node Deployment's timeout.
            type: int
        type: dict
      snmpTrap:
        description: Node Deployment's snmpTrap.
        suboptions:
          description:
            description: Node Deployment's description.
            type: str
          interface:
            description: Node Deployment's interface.
            type: str
          linkTrapQuery:
            description: LinkTrapQuery flag.
            type: bool
          macTrapQuery:
            description: MacTrapQuery flag.
            type: bool
          port:
            description: Node Deployment's port.
            type: int
        type: dict
    type: dict
  userName:
    description: Node Deployment's userName.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Node Deployment reference
  description: Complete reference of the Node Deployment object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    administration:
      isEnabled: true
      role: string
    fdqn: string
    generalSettings:
      monitoring:
        enablePXGrid: true
        isEnabled: true
        isMntDedicated: true
        otherMonitoringNode: string
        policyservice:
          enableDeviceAdminService: true
          enableNACService: true
          enablePassiveIdentityService: true
          enableProfilingService: true
          enabled: true
          sessionService:
            isEnabled: true
            nodegroup: string
          sxpservice:
            isEnabled: true
            userInterface: string
        role: string
    password: string
    profileConfiguration:
      activeDirectory:
        daysBeforeRescan: 0
        description: string
        enabled: true
      dhcp:
        description: string
        enabled: true
        interface: string
        port: {}
      dhcpSpan:
        description: string
        enabled: true
        interface: string
      dns:
        description: string
        enabled: true
      http:
        description: string
        enabled: true
        interface: string
      netflow:
        description: string
        enabled: true
        interface: string
        port: {}
      nmap:
        description: string
        enabled: true
      pxgrid:
        description: string
        enabled: true
      radius:
        description: string
        enabled: true
      snmpQuery:
        description: string
        enabled: true
        eventTimeout: 0
        retries: 0
        timeout: 0
      snmpTrap:
        description: string
        interface: string
        linkTrapQuery: true
        macTrapQuery: true
        port: {}
    userName: string

- name: Update by name
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    generalSettings:
      monitoring:
        enablePXGrid: true
        isEnabled: true
        isMntDedicated: true
        otherMonitoringNode: string
        policyservice:
          enableDeviceAdminService: true
          enableNACService: true
          enablePassiveIdentityService: true
          enableProfilingService: true
          enabled: true
          sessionService:
            isEnabled: true
            nodegroup: string
          sxpservice:
            isEnabled: true
            userInterface: string
        role: string
    hostname: string
    profileConfiguration:
      activeDirectory:
        daysBeforeRescan: 0
        description: string
        enabled: true
      dhcp:
        description: string
        enabled: true
        interface: string
        port: {}
      dhcpSpan:
        description: string
        enabled: true
        interface: string
      dns:
        description: string
        enabled: true
      http:
        description: string
        enabled: true
        interface: string
      netflow:
        description: string
        enabled: true
        interface: string
        port: {}
      nmap:
        description: string
        enabled: true
      pxgrid:
        description: string
        enabled: true
      radius:
        description: string
        enabled: true
      snmpQuery:
        description: string
        enabled: true
        eventTimeout: 0
        retries: 0
        timeout: 0
      snmpTrap:
        description: string
        interface: string
        linkTrapQuery: true
        macTrapQuery: true
        port: {}

- name: Delete by name
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    hostname: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "hostname": "string",
      "fqdn": "string",
      "ipAddress": "string",
      "nodeType": "string",
      "administration": {
        "isEnabled": true,
        "role": "string"
      },
      "generalSettings": {
        "monitoring": {
          "isEnabled": true,
          "role": "string",
          "otherMonitoringNode": "string",
          "isMntDedicated": true,
          "policyservice": {
            "enabled": true,
            "sessionService": {
              "isEnabled": true,
              "nodegroup": "string"
            },
            "enableProfilingService": true,
            "enableNACService": true,
            "sxpservice": {
              "isEnabled": true,
              "userInterface": "string"
            },
            "enableDeviceAdminService": true,
            "enablePassiveIdentityService": true
          },
          "enablePXGrid": true
        }
      },
      "profilingConfiguration": {
        "netflow": {
          "enabled": true,
          "interface": "string",
          "port": {},
          "description": "string"
        },
        "dhcp": {
          "enabled": true,
          "interface": "string",
          "port": {},
          "description": "string"
        },
        "dhcpSpan": {
          "enabled": true,
          "interface": "string",
          "description": "string"
        },
        "http": {
          "enabled": true,
          "interface": "string",
          "description": "string"
        },
        "radius": {
          "enabled": true,
          "description": "string"
        },
        "nmap": {
          "enabled": true,
          "description": "string"
        },
        "dns": {
          "enabled": true,
          "description": "string"
        },
        "snmpQuery": {
          "enabled": true,
          "description": "string",
          "retries": 0,
          "timeout": 0,
          "eventTimeout": 0
        },
        "snmpTrap": {
          "linkTrapQuery": true,
          "macTrapQuery": true,
          "interface": "string",
          "port": {},
          "description": "string"
        },
        "activeDirectory": {
          "enabled": true,
          "daysBeforeRescan": 0,
          "description": "string"
        },
        "pxgrid": {
          "enabled": true,
          "description": "string"
        }
      }
    }

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
  type: dict
  sample: >
    {
      "code": 0,
      "message": "string",
      "rootCause": "string"
    }
"""
