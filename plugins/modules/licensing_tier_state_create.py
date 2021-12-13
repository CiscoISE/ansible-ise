#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: licensing_tier_state_create
short_description: Resource module for Licensing Tier State Create
description:
- Manage operation create of the resource Licensing Tier State Create.
version_added: '2.1.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Licensing Tier State Create's payload.
    suboptions:
      name:
        description: Licensing Tier State Create's name.
        type: str
      status:
        description: Licensing Tier State Create's status.
        type: str
    type: list
requirements:
- ciscoisesdk >= 1.3.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Licensing Tier State Create reference
  description: Complete reference of the Licensing Tier State Create object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.licensing_tier_state_create:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"

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
        "compliance": "string",
        "consumptionCounter": 0,
        "daysOutOfCompliance": "string",
        "lastAuthorization": "string",
        "name": "string",
        "status": "string"
      }
    ]
"""
