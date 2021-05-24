#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: network_access_dictionary
short_description: Resource module for Network Access Dictionary
description:
- Manage operations create, update, delete of the resource Network Access Dictionary.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    description:
      description: The description of the Dictionary.
      type: str
    dictionaryAttrType:
      description: The dictionary attribute type.
      type: str
    id:
      description: Identifier for the dictionary.
      type: str
    name:
      description: The dictionary name.
      type: str
    version:
      description: The dictionary version.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_dictionary
# Reference by Internet resource
- name: Network Access Dictionary reference
  description: Complete reference of the Network Access Dictionary object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.network_access_dictionary:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    dictionaryAttrType: string
    id: string
    name: string
    version: string

- name: Update by name
  cisco.ise.network_access_dictionary:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    dictionaryAttrType: string
    id: string
    name: string
    version: string

- name: Delete by name
  cisco.ise.network_access_dictionary:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    name: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'id': 'string', 'name': 'string', 'description': 'string', 'version': 'string', 'dictionaryAttrType': 'string'}
  - {'id': 'string', 'name': 'string', 'description': 'string', 'version': 'string', 'dictionaryAttrType': 'string'}
  - {'id': 'string', 'name': 'string', 'description': 'string', 'version': 'string', 'dictionaryAttrType': 'string'}
"""
