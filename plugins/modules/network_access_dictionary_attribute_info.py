#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_access_dictionary_attribute_info
short_description: Information module for Network Access Dictionary Attribute
description:
- Get Network Access Dictionary Attribute by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  name:
    description:
    - Name path parameter. The dictionary attribute name.
    type: str
  dictionaryName:
    description:
    - DictionaryName path parameter. The name of the dictionary the dictionary attribute belongs to.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_dictionary_attribute
# Reference by Internet resource
- name: Network Access Dictionary Attribute reference
  description: Complete reference of the Network Access Dictionary Attribute object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Network Access Dictionary Attribute by name
  cisco.ise.network_access_dictionary_attribute_info:
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
      "id": "string",
      "directionType": "string",
      "name": "string",
      "description": "string",
      "internalName": "string",
      "dataType": "string",
      "dictionaryName": "string",
      "allowedValues": [
        {
          "key": "string",
          "value": "string",
          "isDefault": true
        }
      ]
    }
"""
