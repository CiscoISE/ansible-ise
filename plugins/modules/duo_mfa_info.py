#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: duo_mfa_info
short_description: Information module for Duo Mfa Info
description:
  - Get all Duo Mfa Info.
  - Get Duo Mfa Info by name.
  - Duo-MFA - Get the Duo-MFA configuration specified in the connectionName.
  - Duo-MFA - List of Duo-MFA configurations.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  connectionName:
    description:
      - ConnectionName path parameter. This name is used to update, delete or retrieve the specific Duo-MFA configuration.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    duo_mfa.DuoMfa.get_mfa,
    duo_mfa.DuoMfa.get_mfa_byconnection_name,
  - Paths used are
    get /api/v1/duo-mfa/mfa,
    get /api/v1/duo-mfa/mfa/{connectionName},
"""

EXAMPLES = r"""
- name: Get all Duo Mfa Info
  cisco.ise.duo_mfa_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
- name: Get Duo Mfa Info by name
  cisco.ise.duo_mfa_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    connectionName: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "mfa": {
        "accountConfigurations": {
          "adminApi": {
            "ikey": "string",
            "sKey": "string"
          },
          "apiHostName": "string",
          "authenticationApi": {
            "ikey": "string",
            "sKey": "string"
          }
        },
        "connectionName": "string",
        "description": "string",
        "identitySync": "string",
        "type": "string"
      }
    }
"""
