#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: px_grid_direct
short_description: Resource module for Px Grid Direct
description:
  - Manage operations create, update and delete of the resource Px Grid Direct.
  - PxGrid Direct - Configure connectorconfig information.
  - PxGrid Direct - Delete Configure connectorConfig information based on ConnectorName.
  - PxGrid Direct - update Configure connectorConfig information based on ConnectorName.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  additionalProperties:
    description: Px Grid Direct's additionalProperties.
    type: dict
  attributes:
    description: ConnectorName.
    suboptions:
      attributeMapping:
        description: <p>List of feature names</p>.
        elements: dict
        suboptions:
          dictionaryAttribute:
            description: Px Grid Direct's dictionaryAttribute.
            type: str
          includeInDictionary:
            description: IncludeInDictionary flag.
            type: bool
          jsonAttribute:
            description: Px Grid Direct's jsonAttribute.
            type: str
        type: list
      correlationIdentifier:
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
    description: Px Grid Direct's deltasyncSchedule.
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
    description: Px Grid Direct's fullsyncSchedule.
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
    description: Px Grid Direct's url.
    suboptions:
      authenticationType:
        description: Authentication Type list.
        type: str
      bulkUrl:
        description: BulkUrl.
        type: str
      incrementalUrl:
        description: IncrementalUrl.
        type: str
      password:
        description: Password.
        type: str
      userName:
        description: UserName.
        type: str
    type: dict
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    px_grid_direct.PxGridDirect.create_connector_config,
    px_grid_direct.PxGridDirect.delete_connector_config_by_connector_name,
    px_grid_direct.PxGridDirect.update_connector_config_by_connector_name,
  - Paths used are
    post /api/v1/pxgrid-direct/connector-config,
    delete /api/v1/pxgrid-direct/connector-config/{connectorName},
    put /api/v1/pxgrid-direct/connector-config/{connectorName},
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.px_grid_direct:
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
      correlationIdentifier: string
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
      authenticationType: string
      bulkUrl: string
      incrementalUrl: string
      password: string
      userName: string
- name: Update by name
  cisco.ise.px_grid_direct:
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
      correlationIdentifier: string
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
      authenticationType: string
      bulkUrl: string
      incrementalUrl: string
      password: string
      userName: string
- name: Delete by name
  cisco.ise.px_grid_direct:
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
ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: str
  sample: >
    "'string'"
"""
