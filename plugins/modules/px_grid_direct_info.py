#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: px_grid_direct_info
short_description: Information module for Px Grid Direct Info
description:
  - Get all Px Grid Direct Info.
  - Get Px Grid Direct Info by name.
  - PxGrid Direct - Get ALL connectorConfig information.
  - PxGrid Direct - Get connectorConfig information based on ConnectorName.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  connectorName:
    description:
      - ConnectorName path parameter. Update or delete or retrieve the connector config.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    px_grid_direct.PxGridDirect.get_connector_config,
    px_grid_direct.PxGridDirect.get_connector_config_by_connector_name,
  - Paths used are
    get /api/v1/pxgrid-direct/connector-config,
    get /api/v1/pxgrid-direct/connector-config/{connectorName},
"""

EXAMPLES = r"""
- name: Get all Px Grid Direct Info
  cisco.ise.px_grid_direct_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
- name: Get Px Grid Direct Info by name
  cisco.ise.px_grid_direct_info:
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
        "additionalProperties": {},
        "attributes": {
          "attributeMapping": [
            {
              "dictionaryAttribute": "string",
              "includeInDictionary": true,
              "jsonAttribute": "string"
            }
          ],
          "correlationIdentifier": "string",
          "topLevelObject": "string",
          "uniqueIdentifier": "string",
          "versionIdentifier": "string"
        },
        "connectorName": "string",
        "connectorType": "string",
        "deltasyncSchedule": {
          "interval": 0,
          "intervalUnit": "string",
          "startDate": "string"
        },
        "description": "string",
        "enabled": true,
        "fullsyncSchedule": {
          "interval": 0,
          "intervalUnit": "string",
          "startDate": "string"
        },
        "protocol": "string",
        "skipCertificateValidations": true,
        "url": {
          "authenticationType": "string",
          "bulkUrl": "string",
          "incrementalUrl": "string",
          "password": "string",
          "userName": "string"
        }
      }
    }
"""
