#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: guest_ssid
short_description: Resource module for Guest Ssid
description:
- Manage operations create, update, delete of the resource Guest Ssid.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    id:
      description: Guest Ssid's id.
      type: str
    name:
      description: Guest Ssid's name.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.guest_ssid
# Reference by Internet resource
- name: Guest Ssid reference
  description: Complete reference of the Guest Ssid object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.guest_ssid:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    id: id
    name: ssid value

- name: Update by id
  cisco.ise.guest_ssid:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    id: id
    name: ssid value

- name: Delete by id
  cisco.ise.guest_ssid:
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
