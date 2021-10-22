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
  mar_cache:
    description: Node Group's mar-cache.
    suboptions:
      enabled:
        description: Enabled flag.
        type: bool
      query-attempts:
        description: Node Group's query-attempts.
        type: int
      query-timeout:
        description: Node Group's query-timeout.
        type: int
      replication-attempts:
        description: Node Group's replication-attempts.
        type: int
      replication-timeout:
        description: Node Group's replication-timeout.
        type: int
    type: dict
  node_group_name:
    description: Node-group-name path parameter. ID of the existing node group.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
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
    mar_cache:
      enabled: true
      query-attempts: 0
      query-timeout: 0
      replication-attempts: 0
      replication-timeout: 0

- name: Update by name
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    mar_cache:
      enabled: true
      query-attempts: 0
      query-timeout: 0
      replication-attempts: 0
      replication-timeout: 0
    node_group_name: string

- name: Delete by name
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    node_group_name: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "name": "string",
      "description": "string",
      "mar-cache": {
        "enabled": true,
        "replication-timeout": 0,
        "replication-attempts": 0,
        "query-timeout": 0,
        "query-attempts": 0
      }
    }

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
  type: dict
  sample: >
    {
      "code": 0,
      "message": "string",
      "rootCause": "string"
    }
"""
