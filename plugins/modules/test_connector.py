#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: test_connector
short_description: Resource module for Test Connector
description:
- Manage operation create of the resource Test Connector.
- EDDA - test the Connector.
version_added: '3.2_beta'
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
  uniqueID:
    description: Uniqueness to identify.
    type: str
  url:
    description: BulkUrl.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    edda.Edda.test_connector,

  - Paths used are
    post /api/v1/edda/test-connector,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.test_connector:
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
      "status": "string",
      "uniqueID": "string"
    }
"""
