#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: duo_identity_sync
short_description: Resource module for Duo Identity Sync
description:
  - Manage operations create, update and delete of the resource Duo Identity Sync.
  - Duo-IdentitySync - Create a new IdentitySync configuration.
  - Duo-Identitysync - Delete the Identitysync configuration specified in the syncName.
  - Duo-Identitysync - Update the Identitysync configuration specified in the syncName.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  adGroups:
    description: Duo Identity Sync's adGroups.
    elements: dict
    suboptions:
      name:
        description: Active Directory Group ID.
        type: str
      source:
        description: Source of the Active Directory Group.
        type: str
    type: list
  configurations:
    description: Duo Identity Sync's configurations.
    suboptions:
      activeDirectories:
        description: Duo Identity Sync's activeDirectories.
        elements: dict
        suboptions:
          directoryID:
            description: Active Directory ID.
            type: str
          domain:
            description: Active Directory domain name.
            type: str
          name:
            description: Name of the Active Directory.
            type: str
        type: list
    type: dict
  lastSync:
    description: Time of the last Sync.
    type: str
  syncName:
    description: Name of the Identitysync configuration.
    type: str
  syncSchedule:
    description: Duo Identity Sync's syncSchedule.
    suboptions:
      interval:
        description: Frequency of the sync schedule.
        type: int
      intervalUnit:
        description: Unit of the time interval.
        type: str
      schedulerSync:
        description: Type of Sync Schedule - If "Recurring", please specify schedule details.
        type: str
      startDate:
        description: Start date and start time of the sync schedule.
        type: str
    type: dict
  syncStatus:
    description: Duo Identity Sync's syncStatus.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    duo_identity_sync.DuoIdentitySync.create_identitysync,
    duo_identity_sync.DuoIdentitySync.delete_identity_sync_by_sync_name,
    duo_identity_sync.DuoIdentitySync.update_identitysync_by_sync_name,
  - Paths used are
    post /api/v1/duo-identitysync/identitysync,
    delete /api/v1/duo-identitysync/identitysync/{syncName},
    put /api/v1/duo-identitysync/identitysync/{syncName},
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.duo_identity_sync:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    adGroups:
      - name: string
        source: string
    configurations:
      activeDirectories:
        - directoryID: string
          domain: string
          name: string
    lastSync: string
    syncName: string
    syncSchedule:
      interval: 0
      intervalUnit: string
      schedulerSync: string
      startDate: string
    syncStatus: string
- name: Update by name
  cisco.ise.duo_identity_sync:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    adGroups:
      - name: string
        source: string
    configurations:
      activeDirectories:
        - directoryID: string
          domain: string
          name: string
    lastSync: string
    syncName: string
    syncSchedule:
      interval: 0
      intervalUnit: string
      schedulerSync: string
      startDate: string
    syncStatus: string
- name: Delete by name
  cisco.ise.duo_identity_sync:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    syncName: string
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
ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: str
  sample: >
    "'string'"
"""
