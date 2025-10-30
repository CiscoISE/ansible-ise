#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tacacscommandsets
short_description: Resource module for TACACScommandsets
description:
  - Manage operation create of the resource TACACScommandsets.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  commands:
    description: TACACScommandsets's commands.
    suboptions:
      commandList:
        description: List of Commands.
        elements: dict
        type: list
    type: dict
  description:
    description: Description.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  permitUnmatched:
    description: PermitUnmatched flag.
    type: bool
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    tacacscommandsets.Tacacscommandsets.create_tacacscommandsets,
  - Paths used are
    post /tacacscommandsets/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.tacacscommandsets:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    commands:
      - arguments: value
        command: create
        grant: PERMIT
      - arguments: value1 value2
        command: attr
        grant: DENY
    description: description
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    name: name
    permitUnmatched: false
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
