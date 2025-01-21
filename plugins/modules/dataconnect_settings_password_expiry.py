#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: dataconnect_settings_password_expiry
short_description: Resource module for Dataconnect Settings Password Expiry
description:
  - Manage operation update of the resource Dataconnect Settings Password Expiry.
  - This API updates the number of days of Dataconnect password expiry.
version_added: '2.8.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  passwordExpiresInDays:
    description: Dataconnect Settings Password Expiry's passwordExpiresInDays.
    type: int
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    dataconnect_services.DataconnectServices.update_dataconnect_password_expiry,
  - Paths used are
    put /api/v1/mnt/data-connect/settings/password/expiry,
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.dataconnect_settings_password_expiry:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    passwordExpiresInDays: 0
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
