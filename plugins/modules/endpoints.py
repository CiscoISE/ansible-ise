#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: endpoints
short_description: Resource module for Endpoints
description:
  - Manage operations create, update and delete of the resource Endpoints.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  connectedLinks:
    description: Endpoints's connectedLinks.
    type: dict
  customAttributes:
    description: Endpoints's customAttributes.
    type: dict
  description:
    description: Endpoints's description.
    type: str
  deviceType:
    description: Endpoints's deviceType.
    type: str
  groupId:
    description: Endpoints's groupId.
    type: str
  hardwareRevision:
    description: Endpoints's hardwareRevision.
    type: str
  id:
    description: Endpoints's id.
    type: str
  identityStore:
    description: Endpoints's identityStore.
    type: str
  identityStoreId:
    description: Endpoints's identityStoreId.
    type: str
  ipAddress:
    description: Endpoints's ipAddress.
    type: str
  mac:
    description: Endpoints's mac.
    type: str
  mdmAttributes:
    description: Endpoints's mdmAttributes.
    type: dict
  name:
    description: Endpoints's name.
    type: str
  portalUser:
    description: Endpoints's portalUser.
    type: str
  productId:
    description: Endpoints's productId.
    type: str
  profileId:
    description: Endpoints's profileId.
    type: str
  protocol:
    description: Endpoints's protocol.
    type: str
  serialNumber:
    description: Endpoints's serialNumber.
    type: str
  softwareRevision:
    description: Endpoints's softwareRevision.
    type: str
  staticGroupAssignment:
    description: StaticGroupAssignment flag.
    type: bool
  staticProfileAssignment:
    description: StaticProfileAssignment flag.
    type: bool
  value:
    description: Value path parameter. The id or MAC of the endpoint.
    type: str
  vendor:
    description: Endpoints's vendor.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    endpoints.Endpoints.create_end_point,
    endpoints.Endpoints.delete_endpoint,
    endpoints.Endpoints.update_endpoint,
  - Paths used are
    post /api/v1/endpoint,
    delete /api/v1/endpoint/{value},
    put /api/v1/endpoint/{value},
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.endpoints:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    connectedLinks: {}
    customAttributes: {}
    description: string
    deviceType: string
    groupId: string
    hardwareRevision: string
    id: string
    identityStore: string
    identityStoreId: string
    ipAddress: string
    mac: string
    mdmAttributes: {}
    name: string
    portalUser: string
    productId: string
    profileId: string
    protocol: string
    serialNumber: string
    softwareRevision: string
    staticGroupAssignment: true
    staticProfileAssignment: true
    vendor: string
- name: Update by id
  cisco.ise.endpoints:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    connectedLinks: {}
    customAttributes: {}
    description: string
    deviceType: string
    groupId: string
    hardwareRevision: string
    id: string
    identityStore: string
    identityStoreId: string
    ipAddress: string
    mac: string
    mdmAttributes: {}
    name: string
    portalUser: string
    productId: string
    profileId: string
    protocol: string
    serialNumber: string
    softwareRevision: string
    staticGroupAssignment: true
    staticProfileAssignment: true
    value: string
    vendor: string
- name: Delete by id
  cisco.ise.endpoints:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    value: string
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "connectedLinks": {},
      "customAttributes": {},
      "description": "string",
      "deviceType": "string",
      "groupId": "string",
      "hardwareRevision": "string",
      "id": "string",
      "identityStore": "string",
      "identityStoreId": "string",
      "ipAddress": "string",
      "mac": "string",
      "mdmAttributes": {},
      "name": "string",
      "portalUser": "string",
      "productId": "string",
      "profileId": "string",
      "protocol": "string",
      "serialNumber": "string",
      "softwareRevision": "string",
      "staticGroupAssignment": true,
      "staticProfileAssignment": true,
      "vendor": "string"
    }
ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: dict
  sample: >
    {
      "connectedLinks": {},
      "customAttributes": {},
      "description": "string",
      "deviceType": "string",
      "groupId": "string",
      "hardwareRevision": "string",
      "id": "string",
      "identityStore": "string",
      "identityStoreId": "string",
      "ipAddress": "string",
      "mac": "string",
      "mdmAttributes": {},
      "name": "string",
      "portalUser": "string",
      "productId": "string",
      "profileId": "string",
      "protocol": "string",
      "serialNumber": "string",
      "softwareRevision": "string",
      "staticGroupAssignment": true,
      "staticProfileAssignment": true,
      "vendor": "string"
    }
"""
