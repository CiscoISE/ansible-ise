#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sxplocalbindings
short_description: Resource module for SXPlocalbindings
description:
- Manage operation create of the resource SXPlocalbindings.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  bindingName:
    description: This field is depricated from ISE 3.0.
    type: str
  description:
    description: Description.
    type: str
  id:
    description: Id.
    type: str
  ipAddressOrHost:
    description: IP address for static mapping (hostname is not supported).
    type: str
  name:
    description: Name.
    type: str
  sgt:
    description: SGT name or ID.
    type: str
  sxpVpn:
    description: List of SXP Domains, separated with comma. At least one of sxpVpn or
      vns should be defined.
    type: str
  vns:
    description: List of Virtual Networks, separated with comma. At least one of sxpVpn
      or vns should be defined.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    sxplocalbindings.Sxplocalbindings.create_sxplocalbindings,

  - Paths used are
    post /sxplocalbindings/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sxplocalbindings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    ipAddressOrHost: ipAddressOrHost
    sgt: sgt_id
    sxpVpn: Sxp Vpn Name
    vns: virtualNetwork

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
