#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tacacs_server_sequence_info
short_description: Information module for Tacacs Server Sequence
description:
- Get all Tacacs Server Sequence.
- Get Tacacs Server Sequence by id.
- Get Tacacs Server Sequence by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  page:
    description:
    -  page query parameter. Page number
    type: int
  size:
    description:
    -  size query parameter. Number of objects returned per page
    type: int
  id:
    description:
    -  id path parameter.
    type: str
  name:
    description:
    -  name path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.tacacs_server_sequence
# Reference by Internet resource
- name: Tacacs Server Sequence reference
  description: Complete reference of the Tacacs Server Sequence object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Tacacs Server Sequence
  cisco.ise.tacacs_server_sequence_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result
- name: Get Tacacs Server Sequence by id
  cisco.ise.tacacs_server_sequence_info
    id: string
  register: result
- name: Get Tacacs Server Sequence by name
  cisco.ise.tacacs_server_sequence_info
    name: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'TacacsServerSequence': {'name': 'string', 'serverList': 'string', 'localAccounting': True, 'remoteAccounting': True, 'prefixStrip': True, 'prefixDelimiter': 'string', 'suffixStrip': True, 'suffixDelimiter': 'string'}}
  - {'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': {'rel': 'string', 'href': 'string', 'type': 'string'}, 'previousPage': {'rel': 'string', 'href': 'string', 'type': 'string'}}}
"""
