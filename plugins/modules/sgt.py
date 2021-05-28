#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sgt
short_description: Resource module for Sgt
description:
- Manage operations create, update and delete of the resource Sgt.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    description:
      description: Sgt's description.
      type: str
    generationId:
      description: Sgt's generationId.
      type: str
    id:
      description: Id path parameter.
      type: str
    name:
      description: Sgt's name.
      type: str
    propogateToApic:
      description: PropogateToApic flag.
      type: bool
    value:
      description: Sgt's value.
      type: int
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sgt
# Reference by Internet resource
- name: Sgt reference
  description: Complete reference of the Sgt object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: Printers
    generationId: '0'
    name: Printers
    propogateToApic: true
    value: 999

- name: Update by id
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: Printers
    generationId: '0'
    id: string
    name: Printers
    propogateToApic: true
    value: 999

- name: Delete by id
  cisco.ise.sgt:
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
