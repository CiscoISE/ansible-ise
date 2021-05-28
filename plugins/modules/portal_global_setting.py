#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: portal_global_setting
short_description: Resource module for Portal Global Setting
description:
- Manage operation update of the resource Portal Global Setting.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  customization:
    description: Portal Global Setting's customization.
    type: str
  id:
    description: Portal Global Setting's id.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.portal_global_setting
# Reference by Internet resource
- name: Portal Global Setting reference
  description: Complete reference of the Portal Global Setting object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.portal_global_setting:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customization: HTMLANDJAVASCRIPT
    id: 21013cb2-d030-4fb1-9ba2-35757634d770

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "UpdatedFieldsList": {
        "updatedField": [
          "string"
        ]
      }
    }
"""
