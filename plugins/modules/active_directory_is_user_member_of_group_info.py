#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: active_directory_is_user_member_of_group_info
short_description: Information module for Active Directory Is User Member Of Group
description:
- Get all Active Directory Is User Member Of Group.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter.
    type: str
  additionalData:
    description: Active Directory Is User Member Of Group's additionalData.
    suboptions:
      name:
        description: Active Directory Is User Member Of Group's name.
        type: str
      value:
        description: Active Directory Is User Member Of Group's value.
        type: str
    type: list
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Active Directory Is User Member Of Group reference
  description: Complete reference of the Active Directory Is User Member Of Group object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Active Directory Is User Member Of Group
  cisco.ise.active_directory_is_user_member_of_group_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
    additionalData:
    - name: username
      value: Required. Perform the check on this user
    - name: groupsids
      value: Required. Membership is looked for. The result will be a subset of this list
        of the groups the user is a member of
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
          "groupName": "string",
          "sid": "string",
          "type": "string"
        }
      ]
    }
"""
