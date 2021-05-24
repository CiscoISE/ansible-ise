#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: id_store_sequence
short_description: Resource module for Id Store Sequence
description:
- Manage operations create, update, delete of the resource Id Store Sequence.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    description:
      description: Id Store Sequence's description.
      type: str
    id:
      description: Id Store Sequence's id.
      type: str
    name:
      description: Id Store Sequence's name.
      type: str
    parent:
      description: Id Store Sequence's parent.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.id_store_sequence
# Reference by Internet resource
- name: Id Store Sequence reference
  description: Complete reference of the Id Store Sequence object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.id_store_sequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: description
    id: id
    name: name
    parent: parent

- name: Update by id
  cisco.ise.id_store_sequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: description
    id: id
    name: name
    parent: parent

- name: Delete by id
  cisco.ise.id_store_sequence:
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
  type: complex
  sample:
  - {}
  - {}
  - {}
"""
