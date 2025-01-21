#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: dataconnect_settings_password
short_description: Resource module for Dataconnect Settings Password
description:
  - Manage operation update of the resource Dataconnect Settings Password.
  - This API updates the Dataconnect user password.
version_added: '2.8.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  password:
    description: 'Password for dataconnect user. Password must satisfy the following criteria - Contains at least one uppercase letter A-Z, Contains
      at least one lowercase letter a-z, Contains at least one digit 0-9, Contains at least one special character #$%&*+,-. ;=?^_~, Has at least
      12 characters, Has not more than 30 characters.'
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    dataconnect_services.DataconnectServices.update_dataconnect_password,
  - Paths used are
    put /api/v1/mnt/data-connect/settings/password,
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.dataconnect_settings_password:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    password: string
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
