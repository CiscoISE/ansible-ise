#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sg_acl
short_description: Resource module for Sg Acl
description:
- Manage operations create, update and delete of the resource Sg Acl.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  aclcontent:
    description: Sg Acl's aclcontent.
    type: str
  description:
    description: Sg Acl's description.
    type: str
  generationId:
    description: Sg Acl's generationId.
    type: str
  id:
    description: Sg Acl's id.
    type: str
  ipVersion:
    description: Allowed values - IPV4, - IPV6, - IP_AGNOSTIC.
    type: str
  isReadOnly:
    description: IsReadOnly flag.
    type: bool
  modelledContent:
    description: Modelled content of contract.
    type: dict
  name:
    description: Sg Acl's name.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sg Acl reference
  description: Complete reference of the Sg Acl object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.sg_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    aclcontent: string
    description: string
    generationId: string
    id: string
    ipVersion: string
    isReadOnly: true
    modelledContent: {}
    name: string

- name: Delete by id
  cisco.ise.sg_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sg_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    aclcontent: string
    description: string
    generationId: string
    ipVersion: string
    isReadOnly: true
    modelledContent: {}
    name: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "generationId": "string",
      "aclcontent": "string",
      "isReadOnly": true,
      "modelledContent": {},
      "ipVersion": "string",
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
