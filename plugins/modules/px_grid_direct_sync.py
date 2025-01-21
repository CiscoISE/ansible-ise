#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: px_grid_direct_sync
short_description: Resource module for Px Grid Direct Sync
description:
  - Manage operation create of the resource Px Grid Direct Sync.
  - This syncNow is used on demand on a URLFetch Type connector only.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  SyncType:
    description: Connector Type list.
    type: str
  connectorName:
    description: ConnectorName.
    type: str
  description:
    description: Description.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    px_grid_direct.PxGridDirect.sync_now_connector,
  - Paths used are
    post /api/v1/pxgrid-direct/syncnow,
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.px_grid_direct_sync:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    SyncType: string
    connectorName: string
    description: string
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "connector": {
        "connectorName": "string",
        "syncStatus": "string"
      }
    }
"""
