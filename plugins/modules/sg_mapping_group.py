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
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  deployTo:
    description: Mandatory unless mappingGroup is set or unless deployType=ALL.
    type: str
  deployType:
    description: Allowed values - ALL, - ND, - NDG.
    type: str
  id:
    description: Id path parameter.
    type: str
  name:
    description: Sg Mapping Group's name.
    type: str
  sgt:
    description: Mandatory unless mappingGroup is set.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sg Mapping Group reference
  description: Complete reference of the Sg Mapping Group object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.sg_mapping_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    deployTo: string
    deployType: string
    id: string
    name: string
    sgt: string

- name: Delete by id
  cisco.ise.sg_mapping_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sg_mapping_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    deployTo: string
    deployType: string
    name: string
    sgt: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "name": "string",
      "sgt": "string",
      "deployTo": "string",
      "deployType": "string",
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
