#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: duo_mfa_testconnection
short_description: Resource module for Duo Mfa Testconnection
description:
  - Manage operation create of the resource Duo Mfa Testconnection.
  - Duo-MFA - Verify the Auth and Admin API keys of the Duo Host.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  adminApi:
    description: API type.
    suboptions:
      ikey:
        description: Integration Key.
        type: str
      sKey:
        description: Secret Key.
        type: str
    type: dict
  apiHostName:
    description: Duo API HostName.
    type: str
  authenticationApi:
    description: API type.
    suboptions:
      ikey:
        description: Integration Key.
        type: str
      sKey:
        description: Secret Key.
        type: str
    type: dict
  connectionName:
    description: ConnectionName path parameter. This name is used to retrieve secret keys for testing connection of the specified Duo-MFA configuration
      in case none are specified.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    duo_mfa.DuoMfa.test_connection,
  - Paths used are
    post /api/v1/duo-mfa/mfa/testconnection/{connectionName},
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.duo_mfa_testconnection:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    adminApi:
      ikey: string
      sKey: string
    apiHostName: string
    authenticationApi:
      ikey: string
      sKey: string
    connectionName: string
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: str
  sample: >
    "'string'"
"""
