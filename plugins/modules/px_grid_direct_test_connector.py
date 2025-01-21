#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: px_grid_direct_test_connector
short_description: Resource module for Px Grid Direct Test Connector
description:
  - Manage operation create of the resource Px Grid Direct Test Connector.
  - PxGrid Direct - test the Connector.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  authType:
    description: Authentication Type list.
    type: str
  authValues:
    description: Request to test Connector.
    suboptions:
      password:
        description: Password.
        type: str
      userName:
        description: UserName.
        type: str
    type: dict
  connectorName:
    description: ConnectorName.
    type: str
  responseParsing:
    description: Uniqueness to identify.
    type: str
  skipCertificateValidations:
    description: SkipCertificateValidations.
    type: bool
  uniqueID:
    description: Uniqueness to identify.
    type: str
  url:
    description: BulkUrl.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    px_grid_direct.PxGridDirect.test_connector,
  - Paths used are
    post /api/v1/pxgrid-direct/test-connector,
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.px_grid_direct_test_connector:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    authType: string
    authValues:
      password: string
      userName: string
    connectorName: string
    responseParsing: string
    skipCertificateValidations: true
    uniqueID: string
    url: string
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "connectorName": "string",
      "data": "string",
      "error": "string",
      "skipCertificateValidations": true,
      "status": "string",
      "uniqueID": "string"
    }
"""
