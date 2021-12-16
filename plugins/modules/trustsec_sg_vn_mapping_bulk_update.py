#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trustsec_sg_vn_mapping_bulk_update
short_description: Resource module for Trustsec Sg Vn Mapping Bulk Update
description:
- Manage operation create of the resource Trustsec Sg Vn Mapping Bulk Update.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Trustsec Sg Vn Mapping Bulk Update's payload.
    suboptions:
      id:
        description: Identifier of the SG-VN mapping.
        type: str
      lastUpdate:
        description: Timestamp for the last update of the SG-VN mapping.
        type: str
      sgName:
        description: Name of the associated Security Group to be used for identity if
          id is not provided.
        type: str
      sgtId:
        description: Identifier of the associated Security Group which is required unless
          its name is provided.
        type: str
      vnId:
        description: Identifier for the associated Virtual Network which is required
          unless its name is provided.
        type: str
      vnName:
        description: Name of the associated Virtual Network to be used for identity
          if id is not provided.
        type: str
    type: list
requirements:
- ciscoisesdk >= 1.3.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Trustsec Sg Vn Mapping Bulk Update reference
  description: Complete reference of the Trustsec Sg Vn Mapping Bulk Update object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.trustsec_sg_vn_mapping_bulk_update:
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
