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
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  attributeId:
    description: Dictionary attribute id (Optional), used for additional verification.
    type: str
  attributeName:
    description: Dictionary attribute name.
    type: str
  attributeValue:
    description: <ul><li>Attribute value for condition</li> <li>Value type is specified
      in dictionary object</li> <li>if multiple values allowed is specified in dictionary
      object</li></ul>.
    type: str
  children:
    description: In case type is andBlock or orBlock addtional conditions will be aggregated
      under this logical (OR/AND) condition.
    suboptions:
      conditionType:
        description: <ul><li>Inidicates whether the record is the condition itself(data)
          or a logical(or,and) aggregation</li> <li>Data type enum(reference,single)
          indicates than "conditonId" OR "ConditionAttrs" fields should contain condition
          data but not both</li> <li>Logical aggreation(and,or) enum indicates that
          additional conditions are present under the children field</li></ul>.
        type: str
      isNegate:
        description: Indicates whereas this condition is in negate mode.
        type: bool
      link:
        description: Network Access Time Date Conditions's link.
        suboptions:
          href:
            description: Network Access Time Date Conditions's href.
            type: str
          rel:
            description: Network Access Time Date Conditions's rel.
            type: str
          type:
            description: Network Access Time Date Conditions's type.
            type: str
        type: dict
    type: list
  conditionType:
    description: <ul><li>Inidicates whether the record is the condition itself(data)
      or a logical(or,and) aggregation</li> <li>Data type enum(reference,single) indicates
      than "conditonId" OR "ConditionAttrs" fields should contain condition data but
      not both</li> <li>Logical aggreation(and,or) enum indicates that additional conditions
      are present under the children field</li></ul>.
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
    description: Dictionary name.
    type: str
  dictionaryValue:
    description: Dictionary value.
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
    description: Indicates whereas this condition is in negate mode.
    type: bool
  link:
    description: Network Access Time Date Conditions's link.
    suboptions:
      href:
        description: Network Access Time Date Conditions's href.
        type: str
      rel:
        description: Network Access Time Date Conditions's rel.
        type: str
      type:
        description: Network Access Time Date Conditions's type.
        type: str
    type: dict
  name:
    description: Condition name.
    type: str
  operator:
    description: Equality operator.
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
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
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
    attributeId: string
    attributeName: string
    attributeValue: string
    children:
    - conditionType: string
      isNegate: true
      link:
        href: string
        rel: string
        type: string
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
    link:
      href: string
      rel: string
      type: string
    name: string
    operator: string
    weekDays:
    - string
    weekDaysException:
    - string

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
      link:
        href: string
        rel: string
        type: string
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
    link:
      href: string
      rel: string
      type: string
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
      "response": {},
      "version": "string"
    }

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
