#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: duo_identity_sync_info
short_description: Information module for Duo Identity Sync Info
description:
  - Get all Duo Identity Sync Info.
  - Get Duo Identity Sync Info by name.
  - Duo-IdentitySync - Get the Identitysync config specified in the syncName.
  - Duo-IdentitySync - Get the list of all Identitysync configurations.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  syncName:
    description:
      - SyncName path parameter. This name is used to update, delete or retrieve the specific Identitysync config.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    duo_identity_sync.DuoIdentitySync.get_identitysync,
    duo_identity_sync.DuoIdentitySync.get_identitysync_by_sync_name,
  - Paths used are
    get /api/v1/duo-identitysync/identitysync,
    get /api/v1/duo-identitysync/identitysync/{syncName},
"""

EXAMPLES = r"""
- name: Get all Duo Identity Sync Info
  cisco.ise.duo_identity_sync_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
- name: Get Duo Identity Sync Info by name
  cisco.ise.duo_identity_sync_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    syncName: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "identitySync": {
        "adGroups": [
          {
            "name": "string",
            "sid": "string",
            "source": "string"
          }
        ],
        "configurations": {
          "activeDirectories": [
            {
              "directoryID": "string",
              "domain": "string",
              "name": "string"
            }
          ]
        },
        "lastSync": "string",
        "syncName": "string",
        "syncSchedule": {
          "interval": 0,
          "intervalUnit": "string",
          "schedulerSync": "string",
          "startDate": "string"
        },
        "syncStatus": "string"
      }
    }
"""
