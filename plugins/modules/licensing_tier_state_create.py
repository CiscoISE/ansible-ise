#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: licensing_tier_state_create
short_description: Resource module for Licensing Tier State Create
description:
  - Manage operation create of the resource Licensing Tier State Create.
  - Applicable values for **name** & **status** parameters.
version_added: '2.1.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Licensing Tier State Create's payload.
    elements: dict
    suboptions:
      name:
        description: License tier list.
        type: str
      status:
        description: Current Smart Licensing State.
        type: str
    type: list
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
seealso:
  - name: Cisco ISE documentation for Licensing
    description: Complete reference of the Licensing API.
    link: https://developer.cisco.com/docs/identity-services-engine/v1/#!license-openapi
notes:
  - SDK Method used are
    licensing.Licensing.update_tier_state_info,
  - Paths used are
    post /api/v1/license/system/tier-state,
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.licensing_tier_state_create:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    payload:
      - name: string
        status: string
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": [
        {
          "name": "string",
          "status": "string",
          "message": "string"
        }
      ]
    }
"""
