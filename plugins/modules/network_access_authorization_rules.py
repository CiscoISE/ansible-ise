#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_access_authorization_rules
short_description: Resource module for Network Access Authorization Rules
description:
- Manage operations create, update, delete of the resource Network Access Authorization Rules.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    id:
      description: Id path parameter. Rule id.
      type: str
    policyId:
      description: PolicyId path parameter. Policy id.
      type: str
    profile:
      description: The authorization profile/s.
      elements: str
      type: list
    rule:
      description: Common attributes in rule authentication/authorization.
      suboptions:
        condition:
          description: Network Access Authorization Rules's condition.
          suboptions:
            attributeId:
              description: Network Access Authorization Rules's attributeId.
              type: str
            attributeName:
              description: Network Access Authorization Rules's attributeName.
              type: str
            attributeValue:
              description: Network Access Authorization Rules's attributeValue.
              type: str
            children:
              description: Network Access Authorization Rules's children.
              suboptions:
                conditionType:
                  description: Network Access Authorization Rules's conditionType.
                  type: str
                isNegate:
                  description: IsNegate flag.
                  type: bool
              type: list
            conditionType:
              description: Network Access Authorization Rules's conditionType.
              type: str
            datesRange:
              description: Network Access Authorization Rules's datesRange.
              suboptions:
                endDate:
                  description: Network Access Authorization Rules's endDate.
                  type: str
                startDate:
                  description: Network Access Authorization Rules's startDate.
                  type: str
              type: dict
            datesRangeException:
              description: Network Access Authorization Rules's datesRangeException.
              suboptions:
                endDate:
                  description: Network Access Authorization Rules's endDate.
                  type: str
                startDate:
                  description: Network Access Authorization Rules's startDate.
                  type: str
              type: dict
            description:
              description: Network Access Authorization Rules's description.
              type: str
            dictionaryName:
              description: Network Access Authorization Rules's dictionaryName.
              type: str
            dictionaryValue:
              description: Network Access Authorization Rules's dictionaryValue.
              type: str
            hoursRange:
              description: Network Access Authorization Rules's hoursRange.
              suboptions:
                endTime:
                  description: Network Access Authorization Rules's endTime.
                  type: str
                startTime:
                  description: Network Access Authorization Rules's startTime.
                  type: str
              type: dict
            hoursRangeException:
              description: Network Access Authorization Rules's hoursRangeException.
              suboptions:
                endTime:
                  description: Network Access Authorization Rules's endTime.
                  type: str
                startTime:
                  description: Network Access Authorization Rules's startTime.
                  type: str
              type: dict
            id:
              description: Network Access Authorization Rules's id.
              type: str
            isNegate:
              description: IsNegate flag.
              type: bool
            name:
              description: Network Access Authorization Rules's name.
              type: str
            operator:
              description: Network Access Authorization Rules's operator.
              type: str
            weekDays:
              description: Network Access Authorization Rules's weekDays.
              elements: str
              type: list
            weekDaysException:
              description: Network Access Authorization Rules's weekDaysException.
              elements: str
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
    securityGroup:
      description: Security group used in authorization policies.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_authorization_rules
# Reference by Internet resource
- name: Network Access Authorization Rules reference
  description: Complete reference of the Network Access Authorization Rules object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.network_access_authorization_rules:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    profile:
    - string
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
    securityGroup: string

- name: Update by id
  cisco.ise.network_access_authorization_rules:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    id: string
    policyId: string
    profile:
    - string
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
    securityGroup: string

- name: Delete by id
  cisco.ise.network_access_authorization_rules:
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
  type: dict
  sample: >
    {
      "rule": {
        "id": "string",
        "name": "string",
        "description": "string",
        "hitCounts": 0,
        "rank": 0,
        "state": "string",
        "default": true,
        "condition": {
          "conditionType": "string",
          "isNegate": true,
          "name": "string",
          "id": "string",
          "description": "string",
          "dictionaryName": "string",
          "attributeName": "string",
          "attributeId": "string",
          "operator": "string",
          "dictionaryValue": "string",
          "attributeValue": "string",
          "children": [
            {
              "conditionType": "string",
              "isNegate": true
            }
          ],
          "hoursRange": {
            "startTime": "string",
            "endTime": "string"
          },
          "hoursRangeException": {
            "startTime": "string",
            "endTime": "string"
          },
          "weekDays": [
            "string"
          ],
          "weekDaysException": [
            "string"
          ],
          "datesRange": {
            "startDate": "string",
            "endDate": "string"
          },
          "datesRangeException": {
            "startDate": "string",
            "endDate": "string"
          }
        }
      },
      "profile": [
        "string"
      ],
      "securityGroup": "string"
    }
"""
