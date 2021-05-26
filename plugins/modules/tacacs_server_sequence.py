#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tacacs_server_sequence
short_description: Resource module for Tacacs Server Sequence
description:
- Manage operations create, update, delete of the resource Tacacs Server Sequence.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    id:
      description: Id path parameter.
      type: str
    localAccounting:
      description: LocalAccounting flag.
      type: bool
    name:
      description: Tacacs Server Sequence's name.
      type: str
    prefixDelimiter:
      description: Tacacs Server Sequence's prefixDelimiter.
      type: str
    prefixStrip:
      description: PrefixStrip flag.
      type: bool
    remoteAccounting:
      description: RemoteAccounting flag.
      type: bool
    serverList:
      description: Tacacs Server Sequence's serverList.
      type: str
    suffixDelimiter:
      description: Tacacs Server Sequence's suffixDelimiter.
      type: str
    suffixStrip:
      description: SuffixStrip flag.
      type: bool
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.tacacs_server_sequence
# Reference by Internet resource
- name: Tacacs Server Sequence reference
  description: Complete reference of the Tacacs Server Sequence object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.tacacs_server_sequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    localAccounting: true
    name: string
    prefixDelimiter: string
    prefixStrip: true
    remoteAccounting: true
    serverList: string
    suffixDelimiter: string
    suffixStrip: true

- name: Update by id
  cisco.ise.tacacs_server_sequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    id: string
    localAccounting: true
    name: string
    prefixDelimiter: string
    prefixStrip: true
    remoteAccounting: true
    serverList: string
    suffixDelimiter: string
    suffixStrip: true

- name: Delete by id
  cisco.ise.tacacs_server_sequence:
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
