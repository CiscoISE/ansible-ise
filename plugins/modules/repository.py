#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: repository
short_description: Resource module for Repository
description:
- Manage operations create, update and delete of the resource Repository.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  enablePki:
    description: EnablePki flag.
    type: bool
  name:
    description: Repository's name.
    type: str
  password:
    description: Repository's password.
    type: str
  path:
    description: Repository's path.
    type: str
  protocol:
    description: Repository's protocol.
    type: str
  serverName:
    description: Repository's serverName.
    type: str
  userName:
    description: Repository's userName.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.repository
# Reference by Internet resource
- name: Repository reference
  description: Complete reference of the Repository object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.repository:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    enablePki: true
    name: string
    password: string
    path: string
    protocol: string
    serverName: string
    userName: string

- name: Update by name
  cisco.ise.repository:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    enablePki: true
    name: string
    password: string
    path: string
    protocol: string
    serverName: string
    userName: string

- name: Delete by name
  cisco.ise.repository:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    name: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "error": "string"
    }
"""
