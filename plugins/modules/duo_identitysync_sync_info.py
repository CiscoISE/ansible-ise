#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: duo_identitysync_sync_info
short_description: Information module for Duo Identitysync Sync Info
description:
  - Get Duo Identitysync Sync Info by name.
  - Initiate the sync between the Active Directory and the corresponding Mfa provider associated with this Identitysync config.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  syncName:
    description:
      - SyncName path parameter. Name of the Identitysync configuration used to initiate sync.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    duo_identity_sync.DuoIdentitySync.sync,
  - Paths used are
    get /api/v1/duo-identitysync/identitysync/sync/{syncName},
"""

EXAMPLES = r"""
- name: Get Duo Identitysync Sync Info by name
  cisco.ise.duo_identitysync_sync_info:
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
  type: str
  sample: >
    "'string'"
"""
