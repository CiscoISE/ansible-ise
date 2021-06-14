#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: guest_type_info
short_description: Information module for Guest Type
description:
- Get all Guest Type.
- Get Guest Type by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  page:
    description:
    - Page query parameter. Page number.
    type: int
  size:
    description:
    - Size query parameter. Number of objects returned per page.
    type: int
  sortasc:
    description:
    - Sortasc query parameter. Sort asc.
    type: str
  sortdsc:
    description:
    - Sortdsc query parameter. Sort desc.
    type: str
  filter:
    description:
    - >
      Filter query parameter. <br/> **Simple filtering** should be available through the filter query string
      parameter. The structure of a filter is a triplet of field operator and value separated with dots. More than
      one filter can be sent. The logical operator common to ALL filter criteria will be by default AND, and can
      be changed by using the "filterType=or" query string parameter. Each resource Data model description should
      specify if an attribute is a filtered field. <br/> Operator | Description <br/>
      ------------|----------------- <br/> EQ | Equals <br/> NEQ | Not Equals <br/> GT | Greater Than <br/> LT |
      Less Then <br/> STARTSW | Starts With <br/> NSTARTSW | Not Starts With <br/> ENDSW | Ends With <br/> NENDSW
      | Not Ends With <br/> CONTAINS | Contains <br/> NCONTAINS | Not Contains <br/>.
    type: list
  filterType:
    description:
    - >
      FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and
      can be changed by using the parameter.
    type: str
  id:
    description:
    - Id path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.guest_type
# Reference by Internet resource
- name: Guest Type reference
  description: Complete reference of the Guest Type object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Guest Type
  cisco.ise.guest_type_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
    sortasc: string
    sortdsc: string
    filter: []
    filterType: AND
  register: result

- name: Get Guest Type by id
  cisco.ise.guest_type_info:
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
      "id": "string",
      "name": "string",
      "description": "string",
      "accessTime": {
        "fromFirstLogin": true,
        "maxAccountDuration": 0,
        "durationTimeUnit": "string",
        "defaultDuration": 0,
        "allowAccessOnSpecificDaysTimes": true,
        "dayTimeLimits": [
          {
            "startTime": "string",
            "endTime": "string",
            "days": [
              "string"
            ]
          }
        ]
      },
      "loginOptions": {
        "limitSimultaneousLogins": true,
        "maxSimultaneousLogins": 0,
        "failureAction": "string",
        "maxRegisteredDevices": 0,
        "identityGroupId": "string",
        "allowGuestPortalBypass": true
      },
      "expirationNotification": {
        "enableNotification": true,
        "advanceNotificationDuration": 0,
        "advanceNotificationUnits": "string",
        "sendEmailNotification": true,
        "emailText": "string",
        "sendSmsNotification": true,
        "smsText": "string"
      },
      "sponsorGroups": [
        "string"
      ]
    }
"""
