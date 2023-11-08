#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: connector_config_info
short_description: Information module for Connector Config
description:
- Get all Connector Config.
- Get Connector Config by name.
- EDDA - Get ALL connectorConfig information.
- EDDA - Get connectorConfig information based on ConnectorName.
version_added: '3.2_beta'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  connectorName:
    description:
    - ConnectorName path parameter. Update or delete or retrieve the connector config.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    edda.Edda.get_connector_config,
    edda.Edda.get_connector_config_by_connector_name,

  - Paths used are
    get /api/v1/edda/connector-config,
    get /api/v1/edda/connector-config/{connectorName},

"""

EXAMPLES = r"""
- name: Get all Connector Config
  cisco.ise.connector_config_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result

- name: Get Connector Config by name
  cisco.ise.connector_config_info:
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
          "bulkUniqueIdentifier": "string",
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
          "accessKey": "string",
          "authenticationType": "string",
          "bulkUrl": "string",
          "clientId": "string",
          "clientSecret": "string",
          "incrementalUrl": "string",
          "password": "string",
          "refreshToken": "string",
          "tokenHeader": "string",
          "userName": "string"
        }
      }
    }
"""
