#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_access_time_date_conditions
short_description: Resource module for Network Access Time Date Conditions
description:
- Manage operations create, update and delete of the resource Network Access Time Date Conditions.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    attributeId:
      description: Network Access Time Date Conditions's attributeId.
      type: str
    attributeName:
      description: Network Access Time Date Conditions's attributeName.
      type: str
    attributeValue:
      description: Network Access Time Date Conditions's attributeValue.
      type: str
    children:
      description: Network Access Time Date Conditions's children.
      suboptions:
        conditionType:
          description: Network Access Time Date Conditions's conditionType.
          type: str
        isNegate:
          description: IsNegate flag.
          type: bool
      type: list
    conditionType:
      description: Network Access Time Date Conditions's conditionType.
      type: str
    datesRange:
      description: <p>Defines for which date/s TimeAndDate condition will be matched or
        NOT matched if used in exceptionDates prooperty<br> Options are - Date range,
        for specific date, the same date should be used for start/end date <br> Default
        - no specific dates<br> In order to reset the dates to have no specific dates
        Date format - yyyy-mm-dd (MM = month, dd = day, yyyy = year)</p>.
      suboptions:
        endDate:
          description: Network Access Time Date Conditions's endDate.
          type: str
        startDate:
          description: Network Access Time Date Conditions's startDate.
          type: str
      type: dict
    datesRangeException:
      description: <p>Defines for which date/s TimeAndDate condition will be matched or
        NOT matched if used in exceptionDates prooperty<br> Options are - Date range,
        for specific date, the same date should be used for start/end date <br> Default
        - no specific dates<br> In order to reset the dates to have no specific dates
        Date format - yyyy-mm-dd (MM = month, dd = day, yyyy = year)</p>.
      suboptions:
        endDate:
          description: Network Access Time Date Conditions's endDate.
          type: str
        startDate:
          description: Network Access Time Date Conditions's startDate.
          type: str
      type: dict
    description:
      description: Condition description.
      type: str
    dictionaryName:
      description: Network Access Time Date Conditions's dictionaryName.
      type: str
    dictionaryValue:
      description: Network Access Time Date Conditions's dictionaryValue.
      type: str
    hoursRange:
      description: <p>Defines for which hours a TimeAndDate condition will be matched
        or not matched if used in exceptionHours property<br> Time foramt - hh mm ( h
        = hour , mm = minutes ) <br> Default - All Day </p>.
      suboptions:
        endTime:
          description: Network Access Time Date Conditions's endTime.
          type: str
        startTime:
          description: Network Access Time Date Conditions's startTime.
          type: str
      type: dict
    hoursRangeException:
      description: <p>Defines for which hours a TimeAndDate condition will be matched
        or not matched if used in exceptionHours property<br> Time foramt - hh mm ( h
        = hour , mm = minutes ) <br> Default - All Day </p>.
      suboptions:
        endTime:
          description: Network Access Time Date Conditions's endTime.
          type: str
        startTime:
          description: Network Access Time Date Conditions's startTime.
          type: str
      type: dict
    id:
      description: Network Access Time Date Conditions's id.
      type: str
    isNegate:
      description: IsNegate flag.
      type: bool
    name:
      description: Condition name.
      type: str
    operator:
      description: Network Access Time Date Conditions's operator.
      type: str
    weekDays:
      description: <p>Defines for which days this condition will be matched<br> Days format
        - Arrays of WeekDay enums <br> Default - List of All week days</p>.
      elements: str
      type: list
    weekDaysException:
      description: <p>Defines for which days this condition will NOT be matched<br> Days
        format - Arrays of WeekDay enums <br> Default - Not enabled</p>.
      elements: str
      type: list
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_time_date_conditions
# Reference by Internet resource
- name: Network Access Time Date Conditions reference
  description: Complete reference of the Network Access Time Date Conditions object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.network_access_time_date_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present

- name: Update by id
  cisco.ise.network_access_time_date_conditions:
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
  cisco.ise.network_access_time_date_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

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
