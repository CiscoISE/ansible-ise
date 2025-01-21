#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: dataconnect_settings_info
short_description: Information module for Dataconnect Settings
description:
  - Get all Dataconnect Settings.
  - This API retrieves the status of the Dataconnect feature.
version_added: '2.8.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    dataconnect_services.DataconnectServices.get_dataconnect_service,
  - Paths used are
    get /api/v1/mnt/data-connect/settings,
"""

EXAMPLES = r"""
- name: Get all Dataconnect Settings
  cisco.ise.dataconnect_settings_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "isEnabled": true,
      "isPasswordChanged": true,
      "passwordExpiresInDays": 0,
      "passwordExpiresOn": "string"
    }
"""
