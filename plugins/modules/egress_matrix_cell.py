#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: egress_matrix_cell
short_description: Resource module for Egress Matrix Cell
description:
- Manage operations create, update and delete of the resource Egress Matrix Cell.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  defaultRule:
    description: Allowed values - NONE, - DENY_IP, - PERMIT_IP.
    type: str
  description:
    description: Egress Matrix Cell's description.
    type: str
  destinationSgtId:
    description: Egress Matrix Cell's destinationSgtId.
    type: str
  id:
    description: Egress Matrix Cell's id.
    type: str
  matrixCellStatus:
    description: Allowed values - DISABLED, - ENABLED, - MONITOR.
    type: str
  name:
    description: Egress Matrix Cell's name.
    type: str
  sgacls:
    description: Egress Matrix Cell's sgacls.
    elements: str
    type: list
  sourceSgtId:
    description: Egress Matrix Cell's sourceSgtId.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Egress Matrix Cell reference
  description: Complete reference of the Egress Matrix Cell object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.egress_matrix_cell:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultRule: string
    description: string
    destinationSgtId: string
    id: string
    matrixCellStatus: string
    name: string
    sgacls:
    - string
    sourceSgtId: string

- name: Delete by id
  cisco.ise.egress_matrix_cell:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.egress_matrix_cell:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultRule: string
    description: string
    destinationSgtId: string
    matrixCellStatus: string
    name: string
    sgacls:
    - string
    sourceSgtId: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "sourceSgtId": "string",
      "destinationSgtId": "string",
      "matrixCellStatus": "string",
      "defaultRule": "string",
      "sgacls": [
        "string"
      ],
      "link": {
        "rel": "string",
        "href": "string",
        "type": "string"
      }
    }

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
  type: dict
  sample: >
    {
      "UpdatedFieldsList": {
        "updatedField": {
          "field": "string",
          "oldValue": "string",
          "newValue": "string"
        },
        "field": "string",
        "oldValue": "string",
        "newValue": "string"
      }
    }
"""
