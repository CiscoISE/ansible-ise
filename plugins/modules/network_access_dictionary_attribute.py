#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_access_dictionary_attribute
short_description: Resource module for Network Access Dictionary Attribute
description:
- Manage operations create, update and delete of the resource Network Access Dictionary Attribute.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  allowedValues:
    description: All of the allowed values for the dictionary attribute.
    suboptions:
      isDefault:
        description: True if this key value is the default between the allowed values
          of the dictionary attribute.
        type: bool
      key:
        description: Network Access Dictionary Attribute's key.
        type: str
      value:
        description: Network Access Dictionary Attribute's value.
        type: str
    type: list
  dataType:
    description: The data type for the dictionary attribute.
    type: str
  description:
    description: The description of the Dictionary attribute.
    type: str
  dictionaryName:
    description: The name of the dictionary which the dictionary attribute belongs to.
    type: str
  directionType:
    description: The direction for the useage of the dictionary attribute.
    type: str
  id:
    description: Identifier for the dictionary attribute.
    type: str
  internalName:
    description: The internal name of the dictionary attribute.
    type: str
  name:
    description: The dictionary attribute's name.
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
- name: Create
  cisco.ise.network_access_dictionary_attribute:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowedValues:
    - isDefault: true
      key: string
      value: string
    dataType: string
    description: string
    dictionaryName: string
    directionType: string
    id: string
    internalName: string
    name: string

- name: Update by name
  cisco.ise.network_access_dictionary_attribute:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowedValues:
    - isDefault: true
      key: string
      value: string
    dataType: string
    description: string
    dictionaryName: string
    directionType: string
    id: string
    internalName: string
    name: string

- name: Delete by name
  cisco.ise.network_access_dictionary_attribute:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    dictionaryName: string
    name: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
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
    }

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
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
