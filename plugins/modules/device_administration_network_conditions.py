#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_administration_network_conditions
short_description: Resource module for Device Administration Network Conditions
description:
- Manage operations create, update and delete of the resource Device Administration Network Conditions.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  cliDnisList:
    description: Device Administration Network Conditions's cliDnisList.
    elements: str
    type: list
  conditionType:
    description: Device Administration Network Conditions's conditionType.
    type: str
  description:
    description: Device Administration Network Conditions's description.
    type: str
  deviceGroupList:
    description: Device Administration Network Conditions's deviceGroupList.
    elements: str
    type: list
  deviceList:
    description: Device Administration Network Conditions's deviceList.
    elements: str
    type: list
  id:
    description: Device Administration Network Conditions's id.
    type: str
  ipAddrList:
    description: Device Administration Network Conditions's ipAddrList.
    elements: str
    type: list
  macAddrList:
    description: Device Administration Network Conditions's macAddrList.
    elements: str
    type: list
  name:
    description: Device Administration Network Conditions's name.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.device_administration_network_conditions
# Reference by Internet resource
- name: Device Administration Network Conditions reference
  description: Complete reference of the Device Administration Network Conditions object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.device_administration_network_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present

- name: Update by id
  cisco.ise.device_administration_network_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    cliDnisList:
    - string
    conditionType: string
    description: string
    deviceGroupList:
    - string
    deviceList:
    - string
    id: string
    ipAddrList:
    - string
    macAddrList:
    - string
    name: string

- name: Delete by id
  cisco.ise.device_administration_network_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "name": "string",
      "id": "string",
      "description": "string",
      "conditionType": "string",
      "ipAddrList": [
        "string"
      ],
      "macAddrList": [
        "string"
      ],
      "cliDnisList": [
        "string"
      ],
      "deviceList": [
        "string"
      ],
      "deviceGroupList": [
        "string"
      ]
    }
"""
