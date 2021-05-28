#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_certificate_export
short_description: Resource module for System Certificate Export
description:
- Manage operation create of the resource System Certificate Export.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  certificateID:
    description: System Certificate Export's certificateID.
    type: str
  export:
    description: System Certificate Export's export.
    type: str
  id:
    description: System Certificate Export's id.
    type: str
  password:
    description: System Certificate Export's password.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.system_certificate_export
# Reference by Internet resource
- name: System Certificate Export reference
  description: Complete reference of the System Certificate Export object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.system_certificate_export:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    certificateID: string
    export: string
    id: string
    password: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: str
  sample: >
    "'string'"
"""
