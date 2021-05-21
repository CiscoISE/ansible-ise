#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: tacacs_command_sets_info
short_description: Information module for Tacacs Command Sets
description:
- Get all Tacacs Command Sets.
- Get Tacacs Command Sets by id.
- Get Tacacs Command Sets by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter.
    type: str
  name:
    description:
    - Name path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.tacacs_command_sets
# Reference by Internet resource
- name: Tacacs Command Sets reference
  description: Complete reference of the Tacacs Command Sets object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Tacacs Command Sets
  cisco.ise.tacacs_command_sets_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
- name: Get Tacacs Command Sets by id
  cisco.ise.tacacs_command_sets_info
    id: string
  register: result
- name: Get Tacacs Command Sets by name
  cisco.ise.tacacs_command_sets_info
    name: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'TacacsCommandSets': {'name': 'string', 'description': 'string', 'permitUnmatched': True, 'commands': {'commandList': [{'grant': 'string', 'command': 'string', 'arguments': 'string'}]}}}
  - {'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': {'rel': 'string', 'href': 'string', 'type': 'string'}, 'previousPage': {'rel': 'string', 'href': 'string', 'type': 'string'}}}
"""
