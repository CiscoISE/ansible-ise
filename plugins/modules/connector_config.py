#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: connector_config
short_description: Resource module for Connector Config
description:
- Manage operations create, update and delete of the resource Connector Config.
- EDDA - Configure connectorconfig information.
- EDDA - Delete Configure connectorConfig information based on ConnectorName.
- EDDA - update Configure connectorConfig information based on ConnectorName.
version_added: '3.2_beta'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  additionalProperties:
    description: Connector Config's additionalProperties.
    type: dict
  attributes:
    description: ConnectorName.
    suboptions:
      attributeMapping:
        description: <p>List of feature names</p>.
        elements: dict
        suboptions:
          dictionaryAttribute:
            description: Connector Config's dictionaryAttribute.
            type: str
          includeInDictionary:
            description: IncludeInDictionary flag.
            type: bool
          jsonAttribute:
            description: Connector Config's jsonAttribute.
            type: str
        type: list
      bulkUniqueIdentifier:
        description: Uniqueness to identify.
        type: str
      topLevelObject:
        description: Root level of json.
        type: str
      uniqueIdentifier:
        description: Uniqueness to identify.
        type: str
      versionIdentifier:
        description: Version uniqueness to identify.
        type: str
    type: dict
  connectorName:
    description: ConnectorName.
    type: str
  connectorType:
    description: Connector Type list.
    type: str
  deltasyncSchedule:
    description: Connector Config's deltasyncSchedule.
    suboptions:
      interval:
        description: Run at interval (hours).
        type: int
      intervalUnit:
        description: Interval Units.
        type: str
      startDate:
        description: Start date and Time.
        type: str
    type: dict
  description:
    description: Description.
    type: str
  enabled:
    description: Enabled flag.
    type: bool
  fullsyncSchedule:
    description: Connector Config's fullsyncSchedule.
    suboptions:
      interval:
        description: Run at interval (hours).
        type: int
      intervalUnit:
        description: Interval Units.
        type: str
      startDate:
        description: Start date and Time.
        type: str
    type: dict
  protocol:
    description: Protocol.
    type: str
  skipCertificateValidations:
    description: SkipCertificateValidations flag.
    type: bool
  url:
    description: Connector Config's url.
    suboptions:
      accessKey:
        description: Accesskey.
        type: str
      authenticationType:
        description: Authentication Type list.
        type: str
      bulkUrl:
        description: BulkUrl.
        type: str
      clientId:
        description: Clientid.
        type: str
      clientSecret:
        description: Clientsecret.
        type: str
      incrementalUrl:
        description: IncrementalUrl.
        type: str
      password:
        description: Password.
        type: str
      refreshToken:
        description: Refreshtoken.
        type: str
      tokenHeader:
        description: TokenHeader.
        type: str
      userName:
        description: UserName.
        type: str
    type: dict
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    edda.Edda.create_connector_config,
    edda.Edda.delete_connector_config_by_connector_name,
    edda.Edda.update_connector_config_by_connector_name,

  - Paths used are
    post /api/v1/edda/connector-config,
    delete /api/v1/edda/connector-config/{connectorName},
    put /api/v1/edda/connector-config/{connectorName},

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.connector_config:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    additionalProperties: {}
    attributes:
      attributeMapping:
      - dictionaryAttribute: string
        includeInDictionary: true
        jsonAttribute: string
      bulkUniqueIdentifier: string
      topLevelObject: string
      uniqueIdentifier: string
      versionIdentifier: string
    connectorName: string
    connectorType: string
    deltasyncSchedule:
      interval: 0
      intervalUnit: string
      startDate: string
    description: string
    enabled: true
    fullsyncSchedule:
      interval: 0
      intervalUnit: string
      startDate: string
    protocol: string
    skipCertificateValidations: true
    url:
      accessKey: string
      authenticationType: string
      bulkUrl: string
      clientId: string
      clientSecret: string
      incrementalUrl: string
      password: string
      refreshToken: string
      tokenHeader: string
      userName: string

- name: Update by name
  cisco.ise.connector_config:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    additionalProperties: {}
    attributes:
      attributeMapping:
      - dictionaryAttribute: string
        includeInDictionary: true
        jsonAttribute: string
      bulkUniqueIdentifier: string
      topLevelObject: string
      uniqueIdentifier: string
      versionIdentifier: string
    connectorName: string
    connectorType: string
    deltasyncSchedule:
      interval: 0
      intervalUnit: string
      startDate: string
    description: string
    enabled: true
    fullsyncSchedule:
      interval: 0
      intervalUnit: string
      startDate: string
    protocol: string
    skipCertificateValidations: true
    url:
      accessKey: string
      authenticationType: string
      bulkUrl: string
      clientId: string
      clientSecret: string
      incrementalUrl: string
      password: string
      refreshToken: string
      tokenHeader: string
      userName: string

- name: Delete by name
  cisco.ise.connector_config:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    connectorName: string

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

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: str
  sample: >
    "'string'"
"""
