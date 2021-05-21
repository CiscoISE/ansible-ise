#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_group_info
short_description: Information module for Node Group
description:
- Get all Node Group.
- Get Node Group by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  node_group_name:
    description:
    -  node-group-name path parameter. ID of the existing node group.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.node_group
# Reference by Internet resource
- name: Node Group reference
  description: Complete reference of the Node Group object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Node Group
  cisco.ise.node_group_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
- name: Get Node Group by name
  cisco.ise.node_group_info
    node_group_name: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'name': 'string', 'description': 'string', 'mar-cache': {'enabled': True, 'replication-timeout': 0, 'replication-attempts': 0, 'query-timeout': 0, 'query-attempts': 0}}
  - {'response': [{'name': 'string', 'description': 'string', 'mar-cache': {'enabled': True, 'replication-timeout': 0, 'replication-attempts': 0, 'query-timeout': 0, 'query-attempts': 0}}]}
"""
