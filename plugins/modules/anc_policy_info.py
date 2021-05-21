#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: anc_policy_info
short_description: Information module for Anc Policy
description:
- Get all Anc Policy.
- Get Anc Policy by id.
- Get Anc Policy by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
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
- module: cisco.ise.plugins.module_utils.definitions.anc_policy
# Reference by Internet resource
- name: Anc Policy reference
  description: Complete reference of the Anc Policy object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Anc Policy
  cisco.ise.anc_policy_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
- name: Get Anc Policy by id
  cisco.ise.anc_policy_info
    id: string
  register: result
- name: Get Anc Policy by name
  cisco.ise.anc_policy_info
    name: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'ErsAncPolicy': {'name': 'string', 'actions': ['string']}}
  - {'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': {'rel': 'string', 'href': 'string', 'type': 'string'}, 'previousPage': {'rel': 'string', 'href': 'string', 'type': 'string'}}}
"""
