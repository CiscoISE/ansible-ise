#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: custom_attributes_rename
short_description: Resource module for Custom Attributes Rename
description:
  - Manage operation create of the resource Custom Attributes Rename.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  currentName:
    description: Custom Attributes Rename's currentName.
    type: str
  newName:
    description: Custom Attributes Rename's newName.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    customattributes.Customattributes.rename,
  - Paths used are
    post /api/v1/endpoint-custom-attribute/rename,
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.custom_attributes_rename:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    currentName: string
    newName: string
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: str
  sample: >
    "'string'"
"""
