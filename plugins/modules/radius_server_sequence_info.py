#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: radius_server_sequence_info
short_description: Information module for Radius Server Sequence
description:
- Get all Radius Server Sequence.
- Get Radius Server Sequence by id.
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
  id:
    description:
    - Id path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.radius_server_sequence
# Reference by Internet resource
- name: Radius Server Sequence reference
  description: Complete reference of the Radius Server Sequence object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Radius Server Sequence
  cisco.ise.radius_server_sequence_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result

- name: Get Radius Server Sequence by id
  cisco.ise.radius_server_sequence_info:
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
      "stripPrefix": true,
      "stripSuffix": true,
      "prefixSeparator": "string",
      "suffixSeparator": "string",
      "remoteAccounting": true,
      "localAccounting": true,
      "useAttrSetOnRequest": true,
      "useAttrSetBeforeAcc": true,
      "continueAuthorzPolicy": true,
      "RadiusServerList": [
        "string"
      ],
      "OnRequestAttrManipulatorList": [
        {
          "action": "string",
          "dictionaryName": "string",
          "attributeName": "string",
          "value": "string",
          "changedVal": "string"
        }
      ],
      "BeforeAcceptAttrManipulatorsList": [
        {
          "action": "string",
          "dictionaryName": "string",
          "attributeName": "string",
          "value": "string",
          "changedVal": "string"
        }
      ]
    }
"""
