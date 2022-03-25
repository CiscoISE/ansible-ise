#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trustsec_sg_vn_mapping_bulk_delete
short_description: Resource module for Trustsec Sg Vn Mapping Bulk Delete
description:
- Manage operation create of the resource Trustsec Sg Vn Mapping Bulk Delete.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Trustsec Sg Vn Mapping Bulk Delete's payload.
    elements: str
    type: list
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    sg_vn_mapping.SgVnMapping.bulk_delete_sg_vn_mappings,

  - Paths used are
    post /api/v1/trustsec/sgvnmapping/bulk/delete,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.trustsec_sg_vn_mapping_bulk_delete:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    payload:
    - string

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
