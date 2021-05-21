#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_administration_conditions_for_authentication_rule_info
short_description: Information module for Device Administration Conditions For Authentication Rule
description:
- Get all Device Administration Conditions For Authentication Rule.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.device_administration_conditions_for_authentication_rule
# Reference by Internet resource
- name: Device Administration Conditions For Authentication Rule reference
  description: Complete reference of the Device Administration Conditions For Authentication Rule object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Device Administration Conditions For Authentication Rule
  cisco.ise.device_administration_conditions_for_authentication_rule_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - [{'conditionType': 'string', 'isNegate': True}]
"""
