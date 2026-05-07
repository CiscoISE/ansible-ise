#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_group
short_description: Resource module for Node Group
description:
  - Manage operations create, update and delete of the resource Node Group.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  state:
    description:
      - The state of the resource.
    type: str
    default: present
    choices: [present, absent]
  nodeGroupName:
    description:
      - NodeGroupName path parameter. Name of the existing node group (used for update/delete).
    type: str
  name:
    description:
      - Name of the node group to create.
    type: str
  description:
    description:
      - Description of the node group.
    type: str
  marCache:
    description:
      - MAR (Machine Access Restriction) cache settings for the node group.
    type: dict
    suboptions:
      query-attempts:
        description: Number of query attempts.
        type: int
      query-timeout:
        description: Query timeout in seconds.
        type: int
      replication-attempts:
        description: Number of replication attempts.
        type: int
      replication-timeout:
        description: Replication timeout in seconds.
        type: int
  forceDelete:
    description:
      - Force deletion even if the node group has nodes assigned.
    type: bool
    default: false
requirements:
  - ciscoisesdk >= 2.2.1
  - python >= 3.5
notes:
  - SDK Method used are
    node_group.NodeGroup.create_node_group,
    node_group.NodeGroup.update_node_group,
    node_group.NodeGroup.delete_node_group,
    node_group.NodeGroup.get_node_group,
    node_group.NodeGroup.get_node_groups,
  - Paths used are
    post /api/v1/deployment/node-group,
    put /api/v1/deployment/node-group/{nodeGroupName},
    delete /api/v1/deployment/node-group/{nodeGroupName},
    get /api/v1/deployment/node-group/{nodeGroupName},
    get /api/v1/deployment/node-group,
"""

EXAMPLES = r"""
---
- name: Create a node group
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    name: mygroup
    description: My ISE node group

- name: Update a node group description
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    nodeGroupName: mygroup
    description: Updated description

- name: Delete a node group
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    nodeGroupName: mygroup
    forceDelete: false
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "description": "string",
      "marCache": {
        "query-attempts": 0,
        "query-timeout": 0,
        "replication-attempts": 0,
        "replication-timeout": 0
      },
      "name": "string"
    }
ise_update_response:
  description: A dictionary with the update response from the Cisco ISE Python SDK
  returned: always, on update
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
ise_create_response:
  description: A dictionary with the create response from the Cisco ISE Python SDK
  returned: always, on create
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
"""
