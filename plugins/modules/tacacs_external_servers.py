#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tacacs_external_servers
short_description: Resource module for Tacacs External Servers
description:
- Manage operations create, update and delete of the resource Tacacs External Servers.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  connectionPort:
    description: Tacacs External Servers's connectionPort.
    type: int
  description:
    description: Tacacs External Servers's description.
    type: str
  hostIP:
    description: Tacacs External Servers's hostIP.
    type: str
  id:
    description: Id path parameter.
    type: str
  name:
    description: Tacacs External Servers's name.
    type: str
  sharedSecret:
    description: Tacacs External Servers's sharedSecret.
    type: str
  singleConnect:
    description: SingleConnect flag.
    type: bool
  timeout:
    description: Tacacs External Servers's timeout.
    type: int
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.tacacs_external_servers
# Reference by Internet resource
- name: Tacacs External Servers reference
  description: Complete reference of the Tacacs External Servers object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.tacacs_external_servers:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    connectionPort: 0
    description: string
    hostIP: string
    name: string
    sharedSecret: string
    singleConnect: true
    timeout: 0

- name: Update by id
  cisco.ise.tacacs_external_servers:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    connectionPort: 0
    description: string
    hostIP: string
    id: string
    name: string
    sharedSecret: string
    singleConnect: true
    timeout: 0

- name: Delete by id
  cisco.ise.tacacs_external_servers:
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
