#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_administration_global_exception_rules_info
short_description: Information module for Device Administration Global Exception Rules
description:
- Get all Device Administration Global Exception Rules.
- Get Device Administration Global Exception Rules by id.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter. Rule id.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Device Administration Global Exception Rules reference
  description: Complete reference of the Device Administration Global Exception Rules object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Device Administration Global Exception Rules
  cisco.ise.device_administration_global_exception_rules_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result

- name: Get Device Administration Global Exception Rules by id
  cisco.ise.device_administration_global_exception_rules_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "commands": [
          "string"
        ],
        "link": {
          "href": "string",
          "rel": "string",
          "type": "string"
        },
        "profile": "string",
        "rule": {
          "condition": {
            "conditionType": "string",
            "isNegate": true,
            "link": {
              "href": "string",
              "rel": "string",
              "type": "string"
            },
            "description": "string",
            "id": "string",
            "name": "string",
            "attributeName": "string",
            "attributeId": "string",
            "attributeValue": "string",
            "dictionaryName": "string",
            "dictionaryValue": "string",
            "operator": "string",
            "children": [
              {
                "conditionType": "string",
                "isNegate": true,
                "link": {
                  "href": "string",
                  "rel": "string",
                  "type": "string"
                }
              }
            ],
            "datesRange": {
              "endDate": "string",
              "startDate": "string"
            },
            "datesRangeException": {
              "endDate": "string",
              "startDate": "string"
            },
            "hoursRange": {
              "endTime": "string",
              "startTime": "string"
            },
            "hoursRangeException": {
              "endTime": "string",
              "startTime": "string"
            },
            "weekDays": [
              "string"
            ],
            "weekDaysException": [
              "string"
            ]
          },
          "default": true,
          "hitCounts": 0,
          "id": "string",
          "name": "string",
          "rank": 0,
          "state": "string"
        }
      },
      "version": "string"
    }
"""
