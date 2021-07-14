#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sg_to_vn_to_vlan_info
short_description: Information module for Sg To Vn To Vlan
description:
- Get all Sg To Vn To Vlan.
- Get Sg To Vn To Vlan by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  page:
    description:
    - Page query parameter. Page number.
    type: int
  size:
    description:
    - Size query parameter. Number of objects returned per page.
    type: int
  id:
    description:
    - Id path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sg_to_vn_to_vlan
# Reference by Internet resource
- name: Sg To Vn To Vlan reference
  description: Complete reference of the Sg To Vn To Vlan object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Sg To Vn To Vlan
  cisco.ise.sg_to_vn_to_vlan_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result

- name: Get Sg To Vn To Vlan by id
  cisco.ise.sg_to_vn_to_vlan_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
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
      "id": "string",
      "name": "string",
      "description": "string",
      "sgtId": "string",
      "virtualnetworklist": [
        {
          "id": "string",
          "name": "string",
          "description": "string",
          "defaultVirtualNetwork": true,
          "vlans": [
            {
              "id": "string",
              "name": "string",
              "description": "string",
              "defaultVlan": true,
              "maxValue": 0,
              "data": true
            }
          ]
        }
      ]
    }
"""