#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sg_to_vn_to_vlan_bulk_request
short_description: Resource module for Sg To Vn To Vlan Bulk Request
description:
- Manage operation update of the resource Sg To Vn To Vlan Bulk Request.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  operationType:
    description: Sg To Vn To Vlan Bulk Request's operationType.
    type: str
  resourceMediaType:
    description: Sg To Vn To Vlan Bulk Request's resourceMediaType.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sg To Vn To Vlan Bulk Request reference
  description: Complete reference of the Sg To Vn To Vlan Bulk Request object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.sg_to_vn_to_vlan_bulk_request:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    operationType: string
    resourceMediaType: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
