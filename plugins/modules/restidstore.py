#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: restidstore
short_description: Resource module for RESTidstore
description:
  - Manage operation create of the resource RESTidstore.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description.
    type: str
  ersRESTIDStoreAdvanceSettings:
    description: RESTidstore's ersRESTIDStoreAdvanceSettings.
    suboptions:
      deviceQuerySetting:
        description: DeviceQuerySetting values must be one of NONE,ENTRA_DEVICE_NAME,ENTRA_DEVICE_ID.
        type: dict
      identifyDeviceCertificate:
        description: IdentifyDeviceCertificate values must be one of NONE,SNF,SAN.
        type: dict
      regex:
        description: Regex values must be pattren.
        type: str
      regexType:
        description: RegexType values must be one of NONE,PREDEFINED,CUSTOM.
        type: dict
      sanAttribute:
        description: SanAttribute values must be one of NONE,URI,EMAIL,DNS.
        type: dict
      sanAttributeValue:
        description: SanAttributeValue values must be empty.
        type: str
      subjectNameFormat:
        description: SubjectNameFormat values must be empty.
        type: str
    type: dict
  ersRESTIDStoreAttributes:
    description: RESTidstore's ersRESTIDStoreAttributes.
    suboptions:
      headers:
        description: Headers for the RESTIDStore.
        elements: dict
        type: list
      predefined:
        description: The cloud provider connected to of the RESTIDStore. Only Microsoft
          Entra ID is supported.
        type: dict
      rootUrl:
        description: Url of the root of the RESTIDStore. Can't Update this field.
        type: str
      usernameSuffix:
        description: Suffix of the username domain.
        type: str
    type: dict
  ersRESTIDStoreDeviceAttributes:
    description: RESTidstore's ersRESTIDStoreDeviceAttributes.
    suboptions:
      name:
        description: Name and Type of attribute.
        type: str
    type: dict
  ersRESTIDStoreUserAttributes:
    description: RESTidstore's ersRESTIDStoreUserAttributes.
    suboptions:
      name:
        description: Name and Type of attribute.
        type: str
    type: dict
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    restidstore.Restidstore.create_restidstore,
  - Paths used are
    post /restidstore/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.restidstore:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: Object that represents the restID store
    ersRestIDStoreAdvanceSettings:
      deviceQuerySetting: ENTRA_DEVICE_NAME
      identifyDeviceCertificate: SAN
      regex: ^(.+)@(\S+)$
      regexType: CUSTOM
      sanAttribute: EMAIL
      sanAttributeValue: username@domain.com
      subjectNameFormat: ''
    ersRestIDStoreAttributes:
      headers:
        - key: tenantID
          value: tenantID_value
        - key: clientID
          value: clientID_value
        - key: clientSecret
          value: clientSecret_value
      rootUrl: rootUrl
      usernameSuffix: '@place.com'
    ersRestIDStoreDeviceAttributes:
      attributes:
        - name: ''
          type: ''
    ersRestIDStoreUserAttributes:
      attributes:
        - name: AttributeName1
          type: String
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    name: RestIdStore1
"""
RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""
