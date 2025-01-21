#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: duo_identity_sync_status
short_description: Resource module for Duo Identity Sync Status
description:
  - Manage operation update of the resource Duo Identity Sync Status.
  - Duo-identitysync - update sync status.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  errorList:
    description: Duo Identity Sync Status's errorList.
    elements: dict
    suboptions:
      reason:
        description: Reason user failed sync.
        type: str
      user:
        description: User to be synced to Duo.
        suboptions:
          directoryname:
            description: Active directory that duo user is contained in.
            type: str
          email:
            description: Email of Duo user.
            type: str
          firstname:
            description: First name of Duo user.
            type: str
          groupname:
            description: Acrive directory group that duo user is contained in.
            type: str
          lastname:
            description: Last name of duo user.
            type: str
          notes:
            description: Notes of Duo user.
            type: str
          realname:
            description: Realname of Duo user.
            type: str
          status:
            description: Status of Duo user.
            type: str
          username:
            description: Username of Duo user.
            type: str
        type: dict
    type: list
  status:
    description: Status of sync.
    type: str
  syncName:
    description: SyncName path parameter. Sync connection to be updated.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    duo_identity_sync.DuoIdentitySync.update_status,
  - Paths used are
    put /api/v1/duo-identitysync/identitysync/status/{syncName},
"""

EXAMPLES = r"""
- name: Update by name
  cisco.ise.duo_identity_sync_status:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    errorList:
      - reason: string
        user:
          directoryname: string
          email: string
          firstname: string
          groupname: string
          lastname: string
          notes: string
          realname: string
          status: string
          username: string
    status: string
    syncName: string
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: str
  sample: >
    "'string'"
"""
