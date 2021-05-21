#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_administration_authentication_rules_info
short_description: Information module for Device Administration Authentication Rules
description:
- Get all Device Administration Authentication Rules.
- Get Device Administration Authentication Rules by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  policyId:
    description:
    -  policyId path parameter. Policy id
    type: str
  id:
    description:
    -  id path parameter. Rule id
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.device_administration_authentication_rules
# Reference by Internet resource
- name: Device Administration Authentication Rules reference
  description: Complete reference of the Device Administration Authentication Rules object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Device Administration Authentication Rules
  cisco.ise.device_administration_authentication_rules_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    policyId: string
  register: result
- name: Get Device Administration Authentication Rules by id
  cisco.ise.device_administration_authentication_rules_info
    policyId: string
    id: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'rule': {'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}}, 'identitySourceId': 'string', 'ifAuthFail': 'string', 'ifUserNotFound': 'string', 'ifProcessFail': 'string'}
  - [{'rule': {'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True}}, 'identitySourceId': 'string', 'ifAuthFail': 'string', 'ifUserNotFound': 'string', 'ifProcessFail': 'string'}]
"""
