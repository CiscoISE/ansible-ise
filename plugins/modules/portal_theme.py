#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: portal_theme
short_description: Resource module for Portal Theme
description:
- Manage operations create, update, delete of the resource Portal Theme.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    id:
      description: Id path parameter.
      type: string
    name:
      description: Portal Theme's name.
      type: str
    themeData:
      description: Portal Theme's themeData.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.portal_theme
# Reference by Internet resource
- name: Portal Theme reference
  description: Complete reference of the Portal Theme object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.portal_theme:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    name: New Theme
    themeData: Base64 encoded string of CSS file

- name: Update by id
  cisco.ise.portal_theme:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    id: 935e5e90-bd06-4cba-9465-e71c475bfe1d
    name: New Theme
    themeData: More Base64 encoded string of CSS file

- name: Delete by id
  cisco.ise.portal_theme:
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
