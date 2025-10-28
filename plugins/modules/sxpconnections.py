#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sxpconnections
short_description: Resource module for SXPconnections
description:
  - Manage operation create of the resource SXPconnections.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description.
    type: str
  enabled:
    description: SXPconnections's enabled.
    type: dict
  id:
    description: Id.
    type: str
  ipAddress:
    description: SXPconnections's ipAddress.
    type: str
  name:
    description: Name.
    type: str
  sxpMode:
    description: SXPconnections's sxpMode.
    type: str
  sxpNode:
    description: SXPconnections's sxpNode.
    type: str
  sxpPeer:
    description: SXPconnections's sxpPeer.
    type: str
  sxpVersion:
    description: SXPconnections's sxpVersion.
    type: str
  sxpVpn:
    description: SXPconnections's sxpVpn.
    type: str
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    sxpconnections.Sxpconnections.create_sxpconnections,
  - Paths used are
    post /sxpconnections/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.sxpconnections:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: Brief description about network peer
    enabled: true
    ipAddress: Sxp Peer IP address
    sxpMode: Sxp Mode
    sxpNode: Sxp Node Name
    sxpPeer: Sxp Peer Name
    sxpVersion: Sxp Version
    sxpVpn: Sxp VPN Name
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
