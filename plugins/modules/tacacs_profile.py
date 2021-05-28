#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tacacs_profile
short_description: Resource module for Tacacs Profile
description:
- Manage operations create, update and delete of the resource Tacacs Profile.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  description:
    description: Tacacs Profile's description.
    type: str
  id:
    description: Tacacs Profile's id.
    type: str
  name:
    description: Tacacs Profile's name.
    type: str
  sessionAttributes:
    description: Tacacs Profile's sessionAttributes.
    suboptions:
      sessionAttributeList:
        description: Tacacs Profile's sessionAttributeList.
        suboptions:
          name:
            description: Tacacs Profile's name.
            type: str
          type:
            description: Tacacs Profile's type.
            type: str
          value:
            description: Tacacs Profile's value.
            type: str
        type: list
    type: dict
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.tacacs_profile
# Reference by Internet resource
- name: Tacacs Profile reference
  description: Complete reference of the Tacacs Profile object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.tacacs_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    id: string
    name: string
    sessionAttributes:
      sessionAttributeList:
      - name: string
        type: string
        value: string

- name: Update by id
  cisco.ise.tacacs_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    id: string
    name: string
    sessionAttributes:
      sessionAttributeList:
      - name: string
        type: string
        value: string

- name: Delete by id
  cisco.ise.tacacs_profile:
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
