#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: endpoints_task
short_description: Resource module for Endpoints Task
description:
  - Manage operation create of the resource Endpoints Task.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  connectedLinks:
    description: Endpoints Task's connectedLinks.
    type: dict
  customAttributes:
    description: Endpoints Task's customAttributes.
    type: dict
  description:
    description: Endpoints Task's description.
    type: str
  deviceType:
    description: Endpoints Task's deviceType.
    type: str
  groupId:
    description: Endpoints Task's groupId.
    type: str
  hardwareRevision:
    description: Endpoints Task's hardwareRevision.
    type: str
  id:
    description: Endpoints Task's id.
    type: str
  identityStore:
    description: Endpoints Task's identityStore.
    type: str
  identityStoreId:
    description: Endpoints Task's identityStoreId.
    type: str
  ipAddress:
    description: Endpoints Task's ipAddress.
    type: str
  mac:
    description: Endpoints Task's mac.
    type: str
  mdmAttributes:
    description: Endpoints Task's mdmAttributes.
    type: dict
  name:
    description: Endpoints Task's name.
    type: str
  portalUser:
    description: Endpoints Task's portalUser.
    type: str
  productId:
    description: Endpoints Task's productId.
    type: str
  profileId:
    description: Endpoints Task's profileId.
    type: str
  protocol:
    description: Endpoints Task's protocol.
    type: str
  serialNumber:
    description: Endpoints Task's serialNumber.
    type: str
  softwareRevision:
    description: Endpoints Task's softwareRevision.
    type: str
  staticGroupAssignment:
    description: StaticGroupAssignment flag.
    type: bool
  staticProfileAssignment:
    description: StaticProfileAssignment flag.
    type: bool
  vendor:
    description: Endpoints Task's vendor.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    endpoints.Endpoints.create_end_point_task,
  - Paths used are
    post /api/v1/endpointTask,
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.endpoints_task:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
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
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string"
    }
"""
