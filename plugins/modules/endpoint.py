#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint
short_description: Resource module for Endpoint
description:
- Manage operation create of the resource Endpoint.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  customAttributes:
    description: Key value map.
    type: dict
  description:
    description: Description.
    type: str
  groupId:
    description: Endpoint's groupId.
    type: str
  id:
    description: Id.
    type: str
  identityStore:
    description: This field is for read only.
    type: str
  identityStoreId:
    description: This field is for read only.
    type: str
  mac:
    description: Endpoint's mac.
    type: str
  mdmAttributes:
    description: MDM Attributes.
    type: dict
  name:
    description: Name.
    type: str
  portalUser:
    description: Endpoint's portalUser.
    type: str
  profileId:
    description: Endpoint's profileId.
    type: str
  staticGroupAssignment:
    description: StaticGroupAssignment flag.
    type: bool
  staticGroupAssignmentDefined:
    description: StaticGroupAssignmentDefined flag.
    type: bool
  staticProfileAssignment:
    description: StaticProfileAssignment flag.
    type: bool
  staticProfileAssignmentDefined:
    description: StaticProfileAssignmentDefined flag.
    type: bool
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    endpoint.Endpoint.create_endpoint,

  - Paths used are
    post /endpoint/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.endpoint:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customAttributes:
      customAttributes:
        key1: value1
        key2: value2
    description: description
    groupId: groupId
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    identityStore: identityStore
    identityStoreId: identityStoreId
    mac: 00:01:02:03:04:05
    mdmAttributes:
      mdmComplianceStatus: false
      mdmEncrypted: false
      mdmEnrolled: false
      mdmIMEI: IMEI
      mdmJailBroken: false
      mdmManufacturer: Apple Inc.
      mdmModel: iPad
      mdmOS: iOS
      mdmPhoneNumber: Phone Number
      mdmPinlock: false
      mdmReachable: true
      mdmSerial: '10000000001'
      mdmServerName: MdmServerName
    name: name
    portalUser: portalUser
    profileId: profileId
    staticGroupAssignment: true
    staticGroupAssignmentDefined: true
    staticProfileAssignment: false
    staticProfileAssignmentDefined: true

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
