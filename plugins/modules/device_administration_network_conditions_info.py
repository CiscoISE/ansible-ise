#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_administration_network_conditions_info
short_description: Information module for Device Administration Network Conditions
description:
- Get all Device Administration Network Conditions.
- Get Device Administration Network Conditions by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter. Condition id.
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
- name: Get all Device Administration Network Conditions
  cisco.ise.device_administration_network_conditions_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result

- name: Get Device Administration Network Conditions by id
  cisco.ise.device_administration_network_conditions_info:
    id: string
  register: result

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
