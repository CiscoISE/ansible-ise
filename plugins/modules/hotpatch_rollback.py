#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: hotpatch_rollback
short_description: Resource module for Hotpatch Rollback
description:
- Manage operation create of the resource Hotpatch Rollback.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  hotpatchName:
    description: Hotpatch Rollback's hotpatchName.
    type: str
  repositoryName:
    description: Hotpatch Rollback's repositoryName.
    type: str
requirements:
- ciscoisesdk >= 1.3.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Hotpatch Rollback reference
  description: Complete reference of the Hotpatch Rollback object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.hotpatch_rollback:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    hotpatchName: string
    repositoryName: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "message": "string"
      },
      "version": "string"
    }
"""
