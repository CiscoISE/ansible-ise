#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tacacsprofile
short_description: Resource module for TACACSprofile
description:
  - Manage operation create of the resource TACACSprofile.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  sessionAttributes:
    description: TACACSprofile's sessionAttributes.
    suboptions:
      sessionAttributeList:
        description: List of SessionAttributes.
        elements: dict
        type: list
    type: dict
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    tacacsprofile.Tacacsprofile.create_tacacsprofile,
  - Paths used are
    post /tacacsprofile/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.tacacsprofile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: description
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    name: name
    sessionAttributes:
      sessionAttributeList:
        - name: attr1
          type: MANDATORY
          value: value
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
