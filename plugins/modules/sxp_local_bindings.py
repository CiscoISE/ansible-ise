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
author: Rafael Campos (@racampos)
options:
  bindingName:
    description: Sxp Local Bindings's bindingName.
    type: str
  description:
    description: Sxp Local Bindings's description.
    type: str
  id:
    description: Sxp Local Bindings's id.
    type: str
  ipAddressOrHost:
    description: Sxp Local Bindings's ipAddressOrHost.
    type: str
  name:
    description: Sxp Local Bindings's name.
    type: str
  sgt:
    description: Sxp Local Bindings's sgt.
    type: str
  sxpVpn:
    description: Sxp Local Bindings's sxpVpn.
    type: str
  vns:
    description: Sxp Local Bindings's vns.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sxp_local_bindings
# Reference by Internet resource
- name: Sxp Local Bindings reference
  description: Complete reference of the Sxp Local Bindings object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sxp_local_bindings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    bindingName: ''
    ipAddressOrHost: ipAddressOrHost
    name: ''
    sgt: sgt_id
    sxpVpn: Sxp Vpn Name
    vns: virtualNetwork

- name: Update by id
  cisco.ise.sxp_local_bindings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    bindingName: ''
    id: string
    ipAddressOrHost: ipAddressOrHost
    name: ''
    sgt: sgt_id
    sxpVpn: Sxp Vpn Name
    vns: virtualNetwork

- name: Delete by id
  cisco.ise.sxp_local_bindings:
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
  type: dict
  sample: >
    {}
"""
