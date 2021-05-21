#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_access_dictionary_info
short_description: Information module for Network Access Dictionary
description:
- Get Network Access Dictionary by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  name:
    description:
    -  name path parameter. the dictionary name
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
- name: Get Network Access Dictionary by name
  cisco.ise.network_access_dictionary_info
    name: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'id': 'string', 'name': 'string', 'description': 'string', 'version': 'string', 'dictionaryAttrType': 'string'}
"""
