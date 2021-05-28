#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: active_directory_user_groups_info
short_description: Information module for Active Directory User Groups
description:
- Get all Active Directory User Groups.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter.
    type: str
    additionalData:
      description: Active Directory Get User Groups's additionalData.
      suboptions:
        name:
          description: Active Directory Get User Groups's name.
          type: str
        value:
          description: Active Directory Get User Groups's value.
          type: str
      type: list
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.active_directory_user_groups
# Reference by Internet resource
- name: Active Directory User Groups reference
  description: Complete reference of the Active Directory User Groups object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Active Directory User Groups
  cisco.ise.active_directory_user_groups_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
    additionalData:
    - name: username
      value: '{{username}}'
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "groups": [
        {
          "name": "string",
          "sid": "string",
          "type": "string"
        }
      ]
    }
"""
