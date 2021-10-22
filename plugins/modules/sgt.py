#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sgt
short_description: Resource module for Sgt
description:
- Manage operations create, update and delete of the resource Sgt.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  defaultSGACLs:
    description: Sgt's defaultSGACLs.
    elements: dict
    type: list
  description:
    description: Sgt's description.
    type: str
  generationId:
    description: Sgt's generationId.
    type: int
  id:
    description: Sgt's id.
    type: str
  isReadOnly:
    description: IsReadOnly flag.
    type: bool
  name:
    description: Sgt's name.
    type: str
  propogateToApic:
    description: PropogateToApic flag.
    type: bool
  value:
    description: Value range 2 ot 65519 or -1 to auto-generate.
    type: int
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sgt reference
  description: Complete reference of the Sgt object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultSGACLs:
    - {}
    description: string
    generationId: 0
    id: string
    isReadOnly: true
    name: string
    propogateToApic: true
    value: 0

- name: Delete by id
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultSGACLs:
    - {}
    description: string
    generationId: 0
    isReadOnly: true
    name: string
    propogateToApic: true
    value: 0

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
      "value": 0,
      "generationId": 0,
      "isReadOnly": true,
      "propogateToApic": true,
      "defaultSGACLs": [
        {}
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
