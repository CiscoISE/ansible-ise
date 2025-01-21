#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: duo_mfa
short_description: Resource module for Duo Mfa
description:
  - Manage operations create, update and delete of the resource Duo Mfa.
  - Duo-MFA - Create a new Duo-MFA configuration.
  - Duo-MFA - Delete the Duo-MFA configuration specified in the connectionName.
  - Duo-MFA - Update the Duo-MFA configuration specified in the connectionName.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  accountConfigurations:
    description: Duo Mfa's accountConfigurations.
    suboptions:
      adminApi:
        description: API type.
        suboptions:
          ikey:
            description: Integration Key.
            type: str
          sKey:
            description: Secret Key.
            type: str
        type: dict
      apiHostName:
        description: Duo API HostName.
        type: str
      authenticationApi:
        description: API type.
        suboptions:
          ikey:
            description: Integration Key.
            type: str
          sKey:
            description: Secret Key.
            type: str
        type: dict
    type: dict
  connectionName:
    description: Name of the Duo-MFA configuration.
    type: str
  description:
    description: Description of the Duo-MFA configuration.
    type: str
  identitySync:
    description: Name of the Identity Sync configuration.
    type: str
  type:
    description: Protocol type for which this Duo-MFA can be used.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    duo_mfa.DuoMfa.create_mfa,
    duo_mfa.DuoMfa.delete_mfa_by_connection_name,
    duo_mfa.DuoMfa.update_m_fa_by_connection_name,
  - Paths used are
    post /api/v1/duo-mfa/mfa,
    delete /api/v1/duo-mfa/mfa/{connectionName},
    put /api/v1/duo-mfa/mfa/{connectionName},
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.duo_mfa:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accountConfigurations:
      adminApi:
        ikey: string
        sKey: string
      apiHostName: string
      authenticationApi:
        ikey: string
        sKey: string
    connectionName: string
    description: string
    identitySync: string
    type: string
- name: Update by name
  cisco.ise.duo_mfa:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accountConfigurations:
      adminApi:
        ikey: string
        sKey: string
      apiHostName: string
      authenticationApi:
        ikey: string
        sKey: string
    connectionName: string
    description: string
    identitySync: string
    type: string
- name: Delete by name
  cisco.ise.duo_mfa:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    connectionName: string
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
ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: str
  sample: >
    "'string'"
"""
