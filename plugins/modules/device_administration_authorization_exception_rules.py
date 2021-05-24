#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: device_administration_authorization_exception_rules
short_description: Resource module for Device Administration Authorization Exception Rules
description:
- Manage operations create, update, delete of the resource Device Administration Authorization Exception Rules.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    commands:
      description: Command sets enforce the specified list of commands that can be executed
        by a device administrator.
      elements:
        type: str
      type: list
    id:
      description: Id path parameter. Rule id.
      type: string
    policyId:
      description: PolicyId path parameter. Policy id.
      type: string
    profile:
      description: Device admin profiles control the initial login session of the device
        administrator.
      type: str
    rule:
      suboptions:
        condition:
          suboptions:
            attributeId:
              description: Device Administration Authorization Exception Rules's attributeId.
              type: str
            attributeName:
              description: Device Administration Authorization Exception Rules's attributeName.
              type: str
            attributeValue:
              description: Device Administration Authorization Exception Rules's attributeValue.
              type: str
            children:
              description: Device Administration Authorization Exception Rules's children.
              suboptions:
              - suboptions:
                  conditionType:
                    description: Device Administration Authorization Exception Rules's
                      conditionType.
                    type: str
                  isNegate:
                    description: IsNegate flag.
                    type: bool
                type: dict
              type: list
            conditionType:
              description: Device Administration Authorization Exception Rules's conditionType.
              type: str
            datesRange:
              suboptions:
                endDate:
                  description: Device Administration Authorization Exception Rules's endDate.
                  type: str
                startDate:
                  description: Device Administration Authorization Exception Rules's startDate.
                  type: str
              type: dict
            datesRangeException:
              suboptions:
                endDate:
                  description: Device Administration Authorization Exception Rules's endDate.
                  type: str
                startDate:
                  description: Device Administration Authorization Exception Rules's startDate.
                  type: str
              type: dict
            description:
              description: Device Administration Authorization Exception Rules's description.
              type: str
            dictionaryName:
              description: Device Administration Authorization Exception Rules's dictionaryName.
              type: str
            dictionaryValue:
              description: Device Administration Authorization Exception Rules's dictionaryValue.
              type: str
            hoursRange:
              suboptions:
                endTime:
                  description: Device Administration Authorization Exception Rules's endTime.
                  type: str
                startTime:
                  description: Device Administration Authorization Exception Rules's startTime.
                  type: str
              type: dict
            hoursRangeException:
              suboptions:
                endTime:
                  description: Device Administration Authorization Exception Rules's endTime.
                  type: str
                startTime:
                  description: Device Administration Authorization Exception Rules's startTime.
                  type: str
              type: dict
            id:
              description: Device Administration Authorization Exception Rules's id.
              type: str
            isNegate:
              description: IsNegate flag.
              type: bool
            name:
              description: Device Administration Authorization Exception Rules's name.
              type: str
            operator:
              description: Device Administration Authorization Exception Rules's operator.
              type: str
            weekDays:
              description: Device Administration Authorization Exception Rules's weekDays.
              elements:
                type: str
              type: list
            weekDaysException:
              description: Device Administration Authorization Exception Rules's weekDaysException.
              elements:
                type: str
              type: list
          type: dict
        default:
          description: Indicates if this rule is the default one.
          type: bool
        description:
          description: The description of the rule.
          type: str
        hitCounts:
          description: The amount of times the rule was matched.
          type: int
        id:
          description: The identifier of the rule.
          type: str
        name:
          description: Rule name, Valid characters are alphanumerics, underscore, hyphen,
            space, period, parentheses.
          type: str
        rank:
          description: The rank(priority) in relation to other rules. Lower rank is higher
            priority.
          type: int
        state:
          description: The state that the rule is in. A disabled rule cannot be matched.
          type: str
      type: dict
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.device_administration_authorization_exception_rules
# Reference by Internet resource
- name: Device Administration Authorization Exception Rules reference
  description: Complete reference of the Device Administration Authorization Exception Rules object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.device_administration_authorization_exception_rules:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    commands:
    - string
    profile: string
    rule:
      condition:
        attributeId: string
        attributeName: string
        attributeValue: string
        children:
        - conditionType: string
          isNegate: true
        conditionType: string
        datesRange:
          endDate: string
          startDate: string
        datesRangeException:
          endDate: string
          startDate: string
        description: string
        dictionaryName: string
        dictionaryValue: string
        hoursRange:
          endTime: string
          startTime: string
        hoursRangeException:
          endTime: string
          startTime: string
        id: string
        isNegate: true
        name: string
        operator: string
        weekDays:
        - string
        weekDaysException:
        - string
      default: true
      description: string
      hitCounts: 0
      id: string
      name: string
      rank: 0
      state: string

- name: Update by id
  cisco.ise.device_administration_authorization_exception_rules:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    commands:
    - string
    id: string
    policyId: string
    profile: string
    rule:
      condition:
        attributeId: string
        attributeName: string
        attributeValue: string
        children:
        - conditionType: string
          isNegate: true
        conditionType: string
        datesRange:
          endDate: string
          startDate: string
        datesRangeException:
          endDate: string
          startDate: string
        description: string
        dictionaryName: string
        dictionaryValue: string
        hoursRange:
          endTime: string
          startTime: string
        hoursRangeException:
          endTime: string
          startTime: string
        id: string
        isNegate: true
        name: string
        operator: string
        weekDays:
        - string
        weekDaysException:
        - string
      default: true
      description: string
      hitCounts: 0
      id: string
      name: string
      rank: 0
      state: string

- name: Delete by id
  cisco.ise.device_administration_authorization_exception_rules:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
    policyId: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'rule': {'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}}, 'commands': ['string'], 'profile': 'string'}
  - {'rule': {'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}}, 'commands': ['string'], 'profile': 'string'}
  - {'id': 'string'}
"""
