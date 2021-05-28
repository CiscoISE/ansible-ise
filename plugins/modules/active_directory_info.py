#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: active_directory_info
short_description: Information module for Active Directory
description:
- Get all Active Directory.
- Get Active Directory by id.
- Get Active Directory by name.
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
  name:
    description:
    - Name path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.active_directory
# Reference by Internet resource
- name: Active Directory reference
  description: Complete reference of the Active Directory object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Active Directory
  cisco.ise.active_directory_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result

- name: Get Active Directory by id
  cisco.ise.active_directory_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

- name: Get Active Directory by name
  cisco.ise.active_directory_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "ERSActiveDirectory": {
        "name": "string",
        "description": "string",
        "domain": "string",
        "adgroups": {
          "groups": [
            {
              "name": "string",
              "sid": "string",
              "type": "string"
            }
          ]
        },
        "advancedSettings": {
          "enablePassChange": true,
          "enableMachineAuth": true,
          "enableMachineAccess": true,
          "agingTime": 0,
          "enableDialinPermissionCheck": true,
          "enableCallbackForDialinClient": true,
          "plaintextAuth": true,
          "identityNotInAdBehaviour": "string",
          "unreachableDomainsBehaviour": "string",
          "enableRewrites": true,
          "rewriteRules": [
            {
              "rowId": 0,
              "rewriteMatch": "string",
              "rewriteResult": "string"
            }
          ],
          "firstName": "string",
          "department": "string",
          "lastName": "string",
          "organizationalUnit": "string",
          "jobTitle": "string",
          "locality": "string",
          "email": "string",
          "stateOrProvince": "string",
          "telephone": "string",
          "country": "string",
          "streetAddress": "string",
          "schema": "string"
        },
        "adAttributes": {
          "attributes": [
            {
              "name": "string",
              "type": "string",
              "defaultValue": "string",
              "internalName": "string"
            }
          ]
        },
        "adScopesNames": "string"
      }
    }
"""
