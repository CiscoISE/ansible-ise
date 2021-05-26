#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_administration_conditions
short_description: Resource module for Device Administration Conditions
description:
- Manage operations create, update, delete of the resource Device Administration Conditions.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    attributeId:
      description: Device Administration Conditions's attributeId.
      type: str
    attributeName:
      description: Device Administration Conditions's attributeName.
      type: str
    attributeValue:
      description: Device Administration Conditions's attributeValue.
      type: str
    children:
      description: Device Administration Conditions's children.
      suboptions:
        conditionType:
          description: Device Administration Conditions's conditionType.
          type: str
        isNegate:
          description: IsNegate flag.
          type: bool
      type: list
    conditionType:
      description: Device Administration Conditions's conditionType.
      type: str
    datesRange:
      description: Device Administration Conditions's datesRange.
      suboptions:
        endDate:
          description: Device Administration Conditions's endDate.
          type: str
        startDate:
          description: Device Administration Conditions's startDate.
          type: str
      type: dict
    datesRangeException:
      description: Device Administration Conditions's datesRangeException.
      suboptions:
        endDate:
          description: Device Administration Conditions's endDate.
          type: str
        startDate:
          description: Device Administration Conditions's startDate.
          type: str
      type: dict
    description:
      description: Device Administration Conditions's description.
      type: str
    dictionaryName:
      description: Device Administration Conditions's dictionaryName.
      type: str
    dictionaryValue:
      description: Device Administration Conditions's dictionaryValue.
      type: str
    hoursRange:
      description: Device Administration Conditions's hoursRange.
      suboptions:
        endTime:
          description: Device Administration Conditions's endTime.
          type: str
        startTime:
          description: Device Administration Conditions's startTime.
          type: str
      type: dict
    hoursRangeException:
      description: Device Administration Conditions's hoursRangeException.
      suboptions:
        endTime:
          description: Device Administration Conditions's endTime.
          type: str
        startTime:
          description: Device Administration Conditions's startTime.
          type: str
      type: dict
    id:
      description: Device Administration Conditions's id.
      type: str
    isNegate:
      description: IsNegate flag.
      type: bool
    name:
      description: Device Administration Conditions's name.
      type: str
    operator:
      description: Device Administration Conditions's operator.
      type: str
    weekDays:
      description: Device Administration Conditions's weekDays.
      elements: str
      type: list
    weekDaysException:
      description: Device Administration Conditions's weekDaysException.
      elements: str
      type: list
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.device_administration_conditions
# Reference by Internet resource
- name: Device Administration Conditions reference
  description: Complete reference of the Device Administration Conditions object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.device_administration_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present

- name: Update by id
  cisco.ise.device_administration_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
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

- name: Delete by id
  cisco.ise.device_administration_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Delete by name
  cisco.ise.device_administration_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    name: string

- name: Update by name
  cisco.ise.device_administration_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
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

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
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
"""
