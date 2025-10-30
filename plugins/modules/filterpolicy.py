#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: filterpolicy
short_description: Resource module for Filterpolicy
description:
  - Manage operation create of the resource Filterpolicy.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description.
    type: str
  domains:
    description: List of SXP Domains, separated with comma.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  sgt:
    description: SGT name or ID. At least one of subnet or sgt or vn should be defined.
    type: str
  subnet:
    description: Subnet for filter policy (hostname is not supported). At least one
      of subnet or sgt or vn should be defined.
    type: str
  vn:
    description: Virtual Network. At least one of subnet or sgt or vn should be defined.
    type: str
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    filterpolicy.Filterpolicy.create_filterpolicy,
  - Paths used are
    post /filterpolicy/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.filterpolicy:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    domains: Sxp Vpn Name
    sgt: sgt
    subnet: subnetAddress
    vn: virtualNetwork
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
        "name": "string",
        "description": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""
