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
  description:
    description: Node Group's description.
    type: str
  forceDelete:
    description: ForceDelete query parameter. Force delete the group even if the node
      group contains one or more nodes.
    type: bool
  marCache:
    description: Node Group's marCache.
    suboptions:
      query-attempts:
        description: The number of times Cisco ISE attempts to perform the cache entry
          query. (0 - 5).
        type: int
      query-timeout:
        description: The time, in seconds, after which the cache entry query times out.
          (1 - 10).
        type: int
      replication-attempts:
        description: The number of times Cisco ISE attempts to perform MAR cache entry
          replication. (0 - 5).
        type: int
      replication-timeout:
        description: The time, in seconds, after which the cache entry replication times
          out. (1 - 10).
        type: int
    type: dict
  name:
    description: Node Group's name.
    type: str
  nodeGroupName:
    description: NodeGroupName path parameter. Name of the existing node group.
    type: str
requirements:
- ciscoisesdk >= 1.3.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Node Group reference
  description: Complete reference of the Node Group object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    marCache:
      query-attempts: 0
      query-timeout: 0
      replication-attempts: 0
      replication-timeout: 0
    name: string

- name: Update by name
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    marCache:
      query-attempts: 0
      query-timeout: 0
      replication-attempts: 0
      replication-timeout: 0
    name: string
    nodeGroupName: string

- name: Delete by name
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    forceDelete: true
    nodeGroupName: string

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
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
"""
