#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_access_dictionary_attribute_info
short_description: Information module for Network Access Dictionary Attribute
description:
- Get all Network Access Dictionary Attribute.
- Get Network Access Dictionary Attribute by name.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  dictionaryName:
    description:
    - DictionaryName path parameter. The name of the dictionary the dictionary attribute belongs to.
    type: str
  name:
    description:
    - Name path parameter. The dictionary attribute name.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Network Access Dictionary Attribute reference
  description: Complete reference of the Network Access Dictionary Attribute object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Network Access Dictionary Attribute
  cisco.ise.network_access_dictionary_attribute_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    dictionaryName: string
  register: result

- name: Get Network Access Dictionary Attribute by name
  cisco.ise.network_access_dictionary_attribute_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string
    dictionaryName: string
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
        "allowedValues": [
          {
            "isDefault": true,
            "key": "string",
            "value": "string"
          }
        ],
        "dataType": "string",
        "description": "string",
        "dictionaryName": "string",
        "directionType": "string",
        "id": "string",
        "internalName": "string",
        "name": "string"
      },
      "version": "string"
    }
"""
