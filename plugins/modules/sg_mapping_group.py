#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sg_mapping_group
short_description: Resource module for Sg Mapping Group
description:
- Manage operations create, update and delete of the resource Sg Mapping Group.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deployTo:
    description: Sg Mapping Group's deployTo.
    type: str
  deployType:
    description: Sg Mapping Group's deployType.
    type: str
  id:
    description: Id path parameter.
    type: str
  name:
    description: Sg Mapping Group's name.
    type: str
  sgt:
    description: Sg Mapping Group's sgt.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sg_mapping_group
# Reference by Internet resource
- name: Sg Mapping Group reference
  description: Complete reference of the Sg Mapping Group object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sg_mapping_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    deployTo: network_device_id
    deployType: ND
    name: groupA
    sgt: sgt_id

- name: Update by id
  cisco.ise.sg_mapping_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    deployTo: network_device_id
    deployType: ND
    id: string
    name: groupA
    sgt: sgt_id

- name: Delete by id
  cisco.ise.sg_mapping_group:
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
