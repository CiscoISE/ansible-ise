#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: network_access_policy_set
short_description: Resource module for Network Access Policy Set
description:
- Manage operations create, update, delete of the resource Network Access Policy Set.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    condition:
      suboptions:
        attributeId:
          description: Network Access Policy Set's attributeId.
          type: str
        attributeName:
          description: Network Access Policy Set's attributeName.
          type: str
        attributeValue:
          description: Network Access Policy Set's attributeValue.
          type: str
        children:
          description: Network Access Policy Set's children.
          suboptions:
          - suboptions:
              conditionType:
                description: Network Access Policy Set's conditionType.
                type: str
              isNegate:
                description: IsNegate flag.
                type: bool
            type: dict
          type: list
        conditionType:
          description: Network Access Policy Set's conditionType.
          type: str
        datesRange:
          suboptions:
            endDate:
              description: Network Access Policy Set's endDate.
              type: str
            startDate:
              description: Network Access Policy Set's startDate.
              type: str
          type: dict
        datesRangeException:
          suboptions:
            endDate:
              description: Network Access Policy Set's endDate.
              type: str
            startDate:
              description: Network Access Policy Set's startDate.
              type: str
          type: dict
        description:
          description: Network Access Policy Set's description.
          type: str
        dictionaryName:
          description: Network Access Policy Set's dictionaryName.
          type: str
        dictionaryValue:
          description: Network Access Policy Set's dictionaryValue.
          type: str
        hoursRange:
          suboptions:
            endTime:
              description: Network Access Policy Set's endTime.
              type: str
            startTime:
              description: Network Access Policy Set's startTime.
              type: str
          type: dict
        hoursRangeException:
          suboptions:
            endTime:
              description: Network Access Policy Set's endTime.
              type: str
            startTime:
              description: Network Access Policy Set's startTime.
              type: str
          type: dict
        id:
          description: Network Access Policy Set's id.
          type: str
        isNegate:
          description: IsNegate flag.
          type: bool
        name:
          description: Network Access Policy Set's name.
          type: str
        operator:
          description: Network Access Policy Set's operator.
          type: str
        weekDays:
          description: Network Access Policy Set's weekDays.
          elements:
            type: str
          type: list
        weekDaysException:
          description: Network Access Policy Set's weekDaysException.
          elements:
            type: str
          type: list
      type: dict
    default:
      description: Flag which indicates if this policy set is the default one.
      type: bool
    description:
      description: The description for the policy set.
      type: str
    hitCounts:
      description: The amount of times the policy was matched.
      type: int
    id:
      description: Identifier for the policy set.
      type: str
    isProxy:
      description: Flag which indicates if the policy set service is of type 'Proxy Sequence'
        or 'Allowed Protocols'.
      type: bool
    name:
      description: Given name for the policy set, Valid characters are alphanumerics,
        underscore, hyphen, space, period, parentheses.
      type: str
    rank:
      description: The rank(priority) in relation to other policy set. Lower rank is higher
        priority.
      type: int
    serviceName:
      description: Policy set service identifier - Allowed Protocols,Server Sequence..
      type: str
    state_:
      description: The state that the policy set is in. A disabled policy set cannot be
        matched.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_policy_set
# Reference by Internet resource
- name: Network Access Policy Set reference
  description: Complete reference of the Network Access Policy Set object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.network_access_policy_set:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
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
    isProxy: true
    name: string
    rank: 0
    serviceName: string
    state_: string
- name: Update by id
  cisco.ise.network_access_policy_set:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
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
    isProxy: true
    name: string
    rank: 0
    serviceName: string
    state_: string
- name: Delete by id
  cisco.ise.network_access_policy_set:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
- name: Ise request doc
  cisco.ise.network_access_policy_set:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}, 'serviceName': 'string', 'isProxy': True}
  - {'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}, 'serviceName': 'string', 'isProxy': True}
  - {'id': 'string'}
  - 
"""
