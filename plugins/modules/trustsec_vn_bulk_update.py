#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trustsec_vn_bulk_update
short_description: Resource module for Trustsec Vn Bulk Update
description:
- Manage operation create of the resource Trustsec Vn Bulk Update.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Trustsec Vn Bulk Update's payload.
    suboptions:
      additionalAttributes:
        description: JSON String of additional attributes for the Virtual Network.
        type: str
      id:
        description: Identifier of the Virtual Network.
        type: str
      lastUpdate:
        description: Timestamp for the last update of the Virtual Network.
        type: str
      name:
        description: Name of the Virtual Network.
        type: str
    type: list
requirements:
- ciscoisesdk >= 1.3.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Trustsec Vn Bulk Update reference
  description: Complete reference of the Trustsec Vn Bulk Update object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.trustsec_vn_bulk_update:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string"
    }
"""
