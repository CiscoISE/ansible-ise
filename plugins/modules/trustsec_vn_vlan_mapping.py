#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trustsec_vn_vlan_mapping
short_description: Resource module for Trustsec Vn Vlan Mapping
description:
- Manage operations create, update and delete of the resource Trustsec Vn Vlan Mapping.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Identifier of the VN-Vlan Mapping.
    type: str
  isData:
    description: Flag which indicates whether the Vlan is data or voice type.
    type: bool
  isDefaultVlan:
    description: Flag which indicates if the Vlan is default.
    type: bool
  lastUpdate:
    description: Timestamp for the last update of the VN-Vlan Mapping.
    type: str
  maxValue:
    description: Max value.
    type: int
  name:
    description: Name of the Vlan.
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
- name: Trustsec Vn Vlan Mapping reference
  description: Complete reference of the Trustsec Vn Vlan Mapping object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.trustsec_vn_vlan_mapping:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    id: string
    isData: true
    isDefaultVlan: true
    lastUpdate: string
    maxValue: 0
    name: string
    vnId: string
    vnName: string

- name: Update by id
  cisco.ise.trustsec_vn_vlan_mapping:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    id: string
    isData: true
    isDefaultVlan: true
    lastUpdate: string
    maxValue: 0
    name: string
    vnId: string
    vnName: string

- name: Delete by id
  cisco.ise.trustsec_vn_vlan_mapping:
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
        "isData": true,
        "isDefaultVlan": true,
        "lastUpdate": "string",
        "maxValue": 0,
        "name": "string",
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
