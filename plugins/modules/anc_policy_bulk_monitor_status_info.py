#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: anc_policy_bulk_monitor_status_info
short_description: Information module for Anc Policy Bulk Monitor Status
description:
- Get Anc Policy Bulk Monitor Status by id.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  bulkid:
    description:
    - Bulkid path parameter.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Anc Policy Bulk Monitor Status reference
  description: Complete reference of the Anc Policy Bulk Monitor Status object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Anc Policy Bulk Monitor Status by id
  cisco.ise.anc_policy_bulk_monitor_status_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    bulkid: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "BulkStatus": {
        "bulkID": "string",
        "executionStatus": "string",
        "operationType": "string",
        "startTime": "string",
        "resourcesCount": 0,
        "successCount": 0,
        "failCount": 0,
        "resourcesStatus": [
          {
            "id": "string",
            "name": "string",
            "description": "string",
            "resourceExecutionStatus": "string",
            "status": "string"
          }
        ]
      }
    }
"""
