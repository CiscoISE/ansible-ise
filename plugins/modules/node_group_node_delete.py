#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_group_node_delete
short_description: Resource module for Node Group Node Delete
description:
  - Remove a node from a node group.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  nodeGroupName:
    description:
      - NodeGroupName path parameter. Name of the node group.
    type: str
    required: true
  hostname:
    description:
      - Hostname of the ISE node to remove from the group.
    type: str
    required: true
requirements:
  - ciscoisesdk >= 2.2.1
  - python >= 3.5
notes:
  - SDK Method used are
    node_group.NodeGroup.remove_node,
  - Paths used are
    post /api/v1/deployment/node-group/{nodeGroupName}/remove-node,
"""

EXAMPLES = r"""
---
- name: Remove node from node group
  cisco.ise.node_group_node_delete:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    nodeGroupName: mygroup
    hostname: isenode.example.com
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
"""
