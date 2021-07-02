#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sg_mapping
short_description: Resource module for Sg Mapping
description:
- Manage operations create, update and delete of the resource Sg Mapping.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deployTo:
    description: Sg Mapping's deployTo.
    type: str
  deployType:
    description: Sg Mapping's deployType.
    type: str
  hostName:
    description: Sg Mapping's hostName.
    type: str
  id:
    description: Id path parameter.
    type: str
  name:
    description: Sg Mapping's name.
    type: str
  sgt:
    description: Sg Mapping's sgt.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sg_mapping
# Reference by Internet resource
- name: Sg Mapping reference
  description: Complete reference of the Sg Mapping object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sg_mapping:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    deployTo: network_device_id
    deployType: ND
    hostName: server1.cisco.com
    name: server1.cisco.com
    sgt: sgt_id

- name: Update by id
  cisco.ise.sg_mapping:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    deployTo: network_device_id
    deployType: ND
    hostName: server1.cisco.com
    id: string
    name: server1.cisco.com
    sgt: sgt_id

- name: Delete by id
  cisco.ise.sg_mapping:
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
