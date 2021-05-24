#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: node_group
short_description: Resource module for Node Group
description:
- Manage operations create, update, delete of the resource Node Group.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    description:
      description: Node Group's description.
      type: str
    mar_cache:
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
      type: string
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
- name: Ise request doc
  cisco.ise.node_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'code': 0, 'message': 'string', 'rootCause': 'string'}
  - {'code': 0, 'message': 'string', 'rootCause': 'string'}
  - {'code': 0, 'message': 'string', 'rootCause': 'string'}
  - 
"""
