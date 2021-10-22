#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: ise_root_ca_regenerate
short_description: Resource module for Ise Root Ca Regenerate
description:
- Manage operation create of the resource Ise Root Ca Regenerate.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  removeExistingISEIntermediateCSR:
    description: Setting this attribute to true will remove existing ISE Intermediate
      CSR.
    type: bool
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Ise Root Ca Regenerate reference
  description: Complete reference of the Ise Root Ca Regenerate object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.ise_root_ca_regenerate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    removeExistingISEIntermediateCSR: true

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
        "link": {
          "href": "string",
          "rel": "string",
          "type": "string"
        },
        "message": "string"
      },
      "version": "string"
    }
"""
