#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: guest_user_change_sponsor_password
short_description: Resource module for Guest User Change Sponsor Password
description:
- Manage operation update of the resource Guest User Change Sponsor Password.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  additionalData:
    description: Guest User Change Sponsor Password's additionalData.
    suboptions:
      name:
        description: Guest User Change Sponsor Password's name.
        type: str
      value:
        description: Guest User Change Sponsor Password's value.
        type: str
    type: list
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Guest User Change Sponsor Password reference
  description: Complete reference of the Guest User Change Sponsor Password object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.guest_user_change_sponsor_password:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    additionalData:
    - name: currentPassword
      value: password
    - name: newPassword
      value: password
    portalId: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
