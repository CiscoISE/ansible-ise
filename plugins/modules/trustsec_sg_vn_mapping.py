#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trustsec_sg_vn_mapping
short_description: Resource module for Trustsec Sg Vn Mapping
description:
- Manage operations create, update and delete of the resource Trustsec Sg Vn Mapping.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Identifier of the SG-VN mapping.
    type: str
  lastUpdate:
    description: Timestamp for the last update of the SG-VN mapping.
    type: str
  sgName:
    description: Name of the associated Security Group to be used for identity if id
      is not provided.
    type: str
  sgtId:
    description: Identifier of the associated Security Group which is required unless
      its name is provided.
    type: str
  vnId:
    description: Identifier for the associated Virtual Network which is required unless
      its name is provided.
    type: str
  vnName:
    description: Name of the associated Virtual Network to be used for identity if id
      is not provided.
    type: str
requirements:
- ciscoisesdk >= 1.2.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Trustsec Sg Vn Mapping reference
  description: Complete reference of the Trustsec Sg Vn Mapping object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.trustsec_sg_vn_mapping:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    id: string
    lastUpdate: string
    sgName: string
    sgtId: string
    vnId: string
    vnName: string

- name: Update by id
  cisco.ise.trustsec_sg_vn_mapping:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    id: string
    lastUpdate: string
    sgName: string
    sgtId: string
    vnId: string
    vnName: string

- name: Delete by id
  cisco.ise.trustsec_sg_vn_mapping:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

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
        "id": "string",
        "lastUpdate": "string",
        "sgName": "string",
        "sgtId": "string",
        "vnId": "string",
        "vnName": "string"
      }
    ]

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
  type: dict
  sample: >
    {
      "code": 0,
      "message": "string"
    }
"""
