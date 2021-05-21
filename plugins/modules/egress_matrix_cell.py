#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: egress_matrix_cell
short_description: Resource module for Egress Matrix Cell
description:
- Manage operations create, update, delete of the resource Egress Matrix Cell.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    defaultRule:
      description: Egress Matrix Cell's defaultRule.
      type: str
    destinationSgtId:
      description: Egress Matrix Cell's destinationSgtId.
      type: str
    id:
      description: Id path parameter.
      type: string
    matrixCellStatus:
      description: Egress Matrix Cell's matrixCellStatus.
      type: str
    sgacls:
      description: Egress Matrix Cell's sgacls.
      elements:
        type: str
      type: list
    sourceSgtId:
      description: Egress Matrix Cell's sourceSgtId.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.egress_matrix_cell
# Reference by Internet resource
- name: Egress Matrix Cell reference
  description: Complete reference of the Egress Matrix Cell object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.egress_matrix_cell:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultRule: PERMIT_IP
    destinationSgtId: 1ebbc200-7a26-11e4-bc43-000c29ed7428
    matrixCellStatus: MONITOR
    sgacls:
    - 1ebbc100-7a26-11e4-bc43-000c29ed7428
    - 2ebbc100-7a26-11e4-bc43-000c29ed7428
    sourceSgtId: 2ebbc200-7a26-11e4-bc43-000c29ed7428
- name: Update by id
  cisco.ise.egress_matrix_cell:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultRule: PERMIT_IP
    destinationSgtId: 1ebbc200-7a26-11e4-bc43-000c29ed7428
    id: string
    matrixCellStatus: MONITOR
    sgacls:
    - 1ebbc100-7a26-11e4-bc43-000c29ed7428
    - 2ebbc100-7a26-11e4-bc43-000c29ed7428
    sourceSgtId: 2ebbc200-7a26-11e4-bc43-000c29ed7428
- name: Delete by id
  cisco.ise.egress_matrix_cell:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
- name: Ise request doc
  cisco.ise.egress_matrix_cell:
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
  - {}
  - {}
  - {}
  - 
"""
