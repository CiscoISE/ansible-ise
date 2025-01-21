#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: upgrade_proceed_info
short_description: Information module for Upgrade Proceed
description:
  - Get the status of upgrade process for the requested nodes
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  preCheckReportID:
    description: preCheckReportID.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    full_upgrade.FullUpgrade.proceed_status,
  - Paths used are
    get /api/v1/upgrade/proceed/get-status,
"""

EXAMPLES = r"""
- name: Get status of upgrade process for the requested nodes
  cisco.ise.upgrade_proceed_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    preCheckReportID: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "message": "string",
      "preCheckReportID": "string"
    }
"""
