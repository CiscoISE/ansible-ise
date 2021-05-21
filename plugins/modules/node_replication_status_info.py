#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_replication_status_info
short_description: Information module for Node Replication Status
description:
- Get Node Replication Status by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  node:
    description:
    -  node path parameter. ID of the existing node.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.node_replication_status
# Reference by Internet resource
- name: Node Replication Status reference
  description: Complete reference of the Node Replication Status object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Node Replication Status by id
  cisco.ise.node_replication_status_info
    node: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'NodeStatus': 'string'}
"""
