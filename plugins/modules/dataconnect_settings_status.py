#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: dataconnect_settings_status
short_description: Resource module for Dataconnect Settings Status
description:
  - Manage operation update of the resource Dataconnect Settings Status.
  - This API updates the DataConnect feature status.
version_added: '2.8.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  isEnabled:
    description: IsEnabled flag.
    type: bool
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    dataconnect_services.DataconnectServices.set_data_connect_service,
  - Paths used are
    put /api/v1/mnt/data-connect/settings/status,
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.dataconnect_settings_status:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    isEnabled: true
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
"""
