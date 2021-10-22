#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sxp_connections
short_description: Resource module for Sxp Connections
description:
- Manage operations create, update and delete of the resource Sxp Connections.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Sxp Connections's description.
    type: str
  enabled:
    description: Enabled flag.
    type: bool
  id:
    description: Sxp Connections's id.
    type: str
  ipAddress:
    description: Sxp Connections's ipAddress.
    type: str
  sxpMode:
    description: Sxp Connections's sxpMode.
    type: str
  sxpNode:
    description: Sxp Connections's sxpNode.
    type: str
  sxpPeer:
    description: Sxp Connections's sxpPeer.
    type: str
  sxpVersion:
    description: Sxp Connections's sxpVersion.
    type: str
  sxpVpn:
    description: Sxp Connections's sxpVpn.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sxp Connections reference
  description: Complete reference of the Sxp Connections object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.sxp_connections:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    enabled: true
    id: string
    ipAddress: string
    sxpMode: string
    sxpNode: string
    sxpPeer: string
    sxpVersion: string
    sxpVpn: string

- name: Delete by id
  cisco.ise.sxp_connections:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sxp_connections:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    enabled: true
    ipAddress: string
    sxpMode: string
    sxpNode: string
    sxpPeer: string
    sxpVersion: string
    sxpVpn: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "description": "string",
      "sxpPeer": "string",
      "sxpVpn": "string",
      "sxpNode": "string",
      "ipAddress": "string",
      "sxpMode": "string",
      "sxpVersion": "string",
      "enabled": true,
      "link": {
        "rel": "string",
        "href": "string",
        "type": "string"
      }
    }

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
  type: dict
  sample: >
    {
      "UpdatedFieldsList": {
        "updatedField": {
          "field": "string",
          "oldValue": "string",
          "newValue": "string"
        },
        "field": "string",
        "oldValue": "string",
        "newValue": "string"
      }
    }
"""
