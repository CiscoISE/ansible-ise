#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: px_grid_direct_sync_info
short_description: Information module for Px Grid Direct Sync
description:
  - Get Px Grid Direct Sync by name.
  - This API is used to get the status for SyncNow Status.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  connectorName:
    description:
      - ConnectorName path parameter. Retrieve the connector syncnow status.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    px_grid_direct.PxGridDirect.get_connector_config_sync_now_status,
  - Paths used are
    get /api/v1/pxgrid-direct/syncNowStatus/{connectorName},
"""

EXAMPLES = r"""
- name: Get Px Grid Direct Sync by name
  cisco.ise.px_grid_direct_sync_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    connectorName: string
  register: result
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
