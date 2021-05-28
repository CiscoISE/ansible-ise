#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: downloadable_acl
short_description: Resource module for Downloadable Acl
description:
- Manage operations create, update and delete of the resource Downloadable Acl.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  dacl:
    description: Downloadable Acl's dacl.
    type: str
  daclType:
    description: Downloadable Acl's daclType.
    type: str
  description:
    description: Downloadable Acl's description.
    type: str
  id:
    description: Id path parameter.
    type: str
  name:
    description: Downloadable Acl's name.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.downloadable_acl
# Reference by Internet resource
- name: Downloadable Acl reference
  description: Complete reference of the Downloadable Acl object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.downloadable_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    dacl: permit ip any any
    daclType: IPV4
    description: MyDACL
    name: MyDACL6

- name: Update by id
  cisco.ise.downloadable_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    dacl: deny ip any any
    daclType: IPV4
    description: MyDACL6
    id: string
    name: MyDACL6

- name: Delete by id
  cisco.ise.downloadable_acl:
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
