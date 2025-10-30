#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
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
      clientId:
        description: KeyType.
        type: str
      clientSecret:
        description: KeyType.
        type: str
      flow:
        description: KeyType.
        type: str
      headerName:
        description: KeyType.
        type: str
      key:
        description: KeyType.
        type: str
      keyType:
        description: KeyType.
        type: str
      paramName:
        description: KeyType.
        type: str
      password:
        description: Password.
        type: str
      requestBody:
        description: KeyType.
        type: str
      scope:
        description: KeyType.
        type: str
      tokenIssuingUrl:
        description: KeyType.
        type: str
      userName:
        description: UserName.
        type: str
    type: dict
  connectorName:
    description: ConnectorName.
    type: str
  flexibleUrl:
    description: Px Grid Direct Test Connector's flexibleUrl.
    suboptions:
      bulk:
        description: Px Grid Direct Test Connector's bulk.
        suboptions:
          additionalHeaders:
            description: Px Grid Direct Test Connector's additionalHeaders.
            elements: dict
            suboptions:
              name:
                description: Px Grid Direct Test Connector's name.
                type: str
              value:
                description: Px Grid Direct Test Connector's value.
                type: str
            type: list
          apiKeyProperties:
            description: Api key auth properties.
            suboptions:
              headerName:
                description: Header name.
                type: str
              key:
                description: Key.
                type: str
              keyType:
                description: Key type.
                type: str
              paramName:
                description: Param name.
                type: str
              requestBody:
                description: Request body that will be templated.
                type: str
            type: dict
          authenticationType:
            description: Authentication Type list.
            type: str
          basicAuthProperties:
            description: Basic auth properties.
            suboptions:
              password:
                description: Password.
                type: str
              requestBody:
                description: Request body that will be templated.
                type: str
              userName:
                description: UserName.
                type: str
            type: dict
          method:
            description: Px Grid Direct Test Connector's method.
            type: str
          oauthProperties:
            description: OAuth properties.
            suboptions:
              clientId:
                description: Client id for oauth.
                type: str
              clientSecret:
                description: Client secret for oauth.
                type: str
              flow:
                description: Oauth flow type.
                type: str
              password:
                description: Password for the password flow.
                type: str
              scope:
                description: The scope of the oauth token.
                type: str
              tokenIssuingUrl:
                description: The url that will issue the bearer token.
                type: str
              userName:
                description: Username for the password flow.
                type: str
            type: dict
          url:
            description: The url to fetch.
            type: str
        type: dict
      incremental:
        description: Px Grid Direct Test Connector's incremental.
        suboptions:
          additionalHeaders:
            description: Px Grid Direct Test Connector's additionalHeaders.
            elements: dict
            suboptions:
              name:
                description: Px Grid Direct Test Connector's name.
                type: str
              value:
                description: Px Grid Direct Test Connector's value.
                type: str
            type: list
          apiKeyProperties:
            description: Api key auth properties.
            suboptions:
              headerName:
                description: Header name.
                type: str
              key:
                description: Key.
                type: str
              keyType:
                description: Key type.
                type: str
              paramName:
                description: Param name.
                type: str
              requestBody:
                description: Request body that will be templated.
                type: str
            type: dict
          authenticationType:
            description: Authentication Type list.
            type: str
          basicAuthProperties:
            description: Basic auth properties.
            suboptions:
              password:
                description: Password.
                type: str
              requestBody:
                description: Request body that will be templated.
                type: str
              userName:
                description: UserName.
                type: str
            type: dict
          method:
            description: Px Grid Direct Test Connector's method.
            type: str
          oauthProperties:
            description: OAuth properties.
            suboptions:
              clientId:
                description: Client id for oauth.
                type: str
              clientSecret:
                description: Client secret for oauth.
                type: str
              flow:
                description: Oauth flow type.
                type: str
              password:
                description: Password for the password flow.
                type: str
              scope:
                description: The scope of the oauth token.
                type: str
              tokenIssuingUrl:
                description: The url that will issue the bearer token.
                type: str
              userName:
                description: Username for the password flow.
                type: str
            type: dict
          url:
            description: The url to fetch.
            type: str
        type: dict
    type: dict
  incrementalUrl:
    description: IncrementalUrl.
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
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    px_grid_direct.PxGridDirect.test_connector,
  - Paths used are
    post /api/v1/pxgrid-direct/test-connector,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.px_grid_direct_test_connector:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    authType: string
    authValues:
      clientId: string
      clientSecret: string
      flow: string
      headerName: string
      key: string
      keyType: string
      paramName: string
      password: string
      requestBody: string
      scope: string
      tokenIssuingUrl: string
      userName: string
    connectorName: string
    flexibleUrl:
      bulk:
        additionalHeaders:
          - name: string
            value: string
        apiKeyProperties:
          headerName: string
          key: string
          keyType: string
          paramName: string
          requestBody: string
        authenticationType: string
        basicAuthProperties:
          password: string
          requestBody: string
          userName: string
        method: string
        oauthProperties:
          clientId: string
          clientSecret: string
          flow: string
          password: string
          scope: string
          tokenIssuingUrl: string
          userName: string
        url: string
      incremental:
        additionalHeaders:
          - name: string
            value: string
        apiKeyProperties:
          headerName: string
          key: string
          keyType: string
          paramName: string
          requestBody: string
        authenticationType: string
        basicAuthProperties:
          password: string
          requestBody: string
          userName: string
        method: string
        oauthProperties:
          clientId: string
          clientSecret: string
          flow: string
          password: string
          scope: string
          tokenIssuingUrl: string
          userName: string
        url: string
    incrementalUrl: string
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
