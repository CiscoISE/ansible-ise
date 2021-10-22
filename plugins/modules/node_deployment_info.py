#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_deployment_info
short_description: Information module for Node Deployment
description:
- Get all Node Deployment.
- Get Node Deployment by name.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  hostname:
    description:
    - Hostname path parameter. ID of the existing deployed node.
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
- name: Get all Node Deployment
  cisco.ise.node_deployment_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result

- name: Get Node Deployment by name
  cisco.ise.node_deployment_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    hostname: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
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
    }
"""
