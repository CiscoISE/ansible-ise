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
author: Rafael Campos (@racampos)
options:
  aclcontent:
    description: Sg Acl's aclcontent.
    type: str
  description:
    description: Sg Acl's description.
    type: str
  id:
    description: Sg Acl's id.
    type: str
  ipVersion:
    description: Sg Acl's ipVersion.
    type: str
  name:
    description: Sg Acl's name.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sg_acl
# Reference by Internet resource
- name: Sg Acl reference
  description: Complete reference of the Sg Acl object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sg_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    aclcontent: Permit IP
    description: description
    id: id
    ipVersion: IPV4
    name: name

- name: Update by id
  cisco.ise.sg_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    aclcontent: Permit IP
    description: description
    id: id
    ipVersion: IPV4
    name: name

- name: Delete by id
  cisco.ise.sg_acl:
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
