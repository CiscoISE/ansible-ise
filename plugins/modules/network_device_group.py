#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_group
short_description: Resource module for Network Device Group
description:
- Manage operations create, update, delete of the resource Network Device Group.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    description:
      description: Network Device Group's description.
      type: str
    id:
      description: Id path parameter.
      type: str
    name:
      description: Network Device Group's name.
      type: str
    othername:
      description: Network Device Group's othername.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_device_group
# Reference by Internet resource
- name: Network Device Group reference
  description: Complete reference of the Network Device Group object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.network_device_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: '...'
    name: Device Type#All Device Types#SDWAN
    othername: Device Type

- name: Update by id
  cisco.ise.network_device_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: SDWAN description
    id: string
    name: Device Type#All Device Types#SDWAN
    othername: Device Type

- name: Delete by id
  cisco.ise.network_device_group:
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
      "UpdatedFieldsList": {
        "updatedField": [
          {
            "field": "string",
            "oldValue": "string",
            "newValue": "string"
          }
        ]
      }
    }
"""
