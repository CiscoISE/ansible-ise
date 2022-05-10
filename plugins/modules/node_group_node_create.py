#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_group_node_create
short_description: Resource module for Node Group Node Create
description:
- Manage operation create of the resource Node Group Node Create.
- This API adds a node to the node group in the cluster. When a node that.
version_added: '2.1.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  hostname:
    description: Node Group Node Create's hostname.
    type: str
  nodeGroupName:
    description: NodeGroupName path parameter. Name of the existing node group.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
seealso:
- name: Cisco ISE documentation for Node Group
  description: Complete reference of the Node Group API.
  link: https://developer.cisco.com/docs/identity-services-engine/v1/#!deployment-openapi
notes:
  - SDK Method used are
    node_group.NodeGroup.add_node,

  - Paths used are
    post /api/v1/deployment/node-group/{nodeGroupName}/add-node,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.node_group_node_create:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    hostname: string
    nodeGroupName: string

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
