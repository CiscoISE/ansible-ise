#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sxp_local_bindings
short_description: Resource module for Sxp Local Bindings
description:
- Manage operations create, update and delete of the resource Sxp Local Bindings.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  bindingName:
    description: This field is depricated from Cisco ISE 3.0.
    type: str
  description:
    description: Sxp Local Bindings's description.
    type: str
  id:
    description: Sxp Local Bindings's id.
    type: str
  ipAddressOrHost:
    description: IP address for static mapping (hostname is not supported).
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
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sxp Local Bindings reference
  description: Complete reference of the Sxp Local Bindings object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.sxp_local_bindings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    bindingName: string
    description: string
    id: string
    ipAddressOrHost: string
    sgt: string
    sxpVpn: string
    vns: string

- name: Delete by id
  cisco.ise.sxp_local_bindings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sxp_local_bindings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    bindingName: string
    description: string
    id: string
    ipAddressOrHost: string
    sgt: string
    sxpVpn: string
    vns: string

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
      "bindingName": "string",
      "ipAddressOrHost": "string",
      "sxpVpn": "string",
      "sgt": "string",
      "vns": "string",
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
