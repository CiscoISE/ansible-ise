#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sgt
short_description: Resource module for SGt
description:
  - Manage operation create of the resource SGt.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  defaultSGACLs:
    description: SGt's defaultSGACLs.
    elements: str
    type: list
  description:
    description: Description.
    type: str
  id:
    description: Id.
    type: str
  isReadOnly:
    description: IsReadOnly flag.
    type: bool
  name:
    description: Name.
    type: str
  propogateToApic:
    description: PropogateToApic flag.
    type: bool
  value:
    description: Value range 2 ot 65519 or -1 to auto-generate.
    type: dict
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    sgt.Sgt.create_sgt,
  - Paths used are
    post /sgt/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultSGACLs: []
    description: description
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    name: name
    propogateToApic: false
    value: 2
"""
RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""
