#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sxpvpns
short_description: Resource module for SXPvpns
description:
- Manage operation create of the resource SXPvpns.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  sxpVpnName:
    description: SXPvpns's sxpVpnName.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    sxpvpns.Sxpvpns.create_sxpvpns,

  - Paths used are
    post /sxpvpns/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sxpvpns:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    sxpVpnName: SxpVpn1

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
