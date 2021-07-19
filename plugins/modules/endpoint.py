#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint
short_description: Resource module for Endpoint
description:
- Manage operations create, update and delete of the resource Endpoint.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  customAttributes:
    description: Endpoint's customAttributes.
    suboptions:
      customAttributes:
        description: Key value map.
        type: dict
    type: dict
  description:
    description: Endpoint's description.
    type: str
  groupId:
    description: Endpoint's groupId.
    type: str
  id:
    description: Endpoint's id.
    type: str
  identityStore:
    description: Endpoint's identityStore.
    type: str
  identityStoreId:
    description: Endpoint's identityStoreId.
    type: str
  mac:
    description: Endpoint's mac.
    type: str
  mdmAttributes:
    description: Endpoint's mdmAttributes.
    suboptions:
      mdmComplianceStatus:
        description: MdmComplianceStatus flag.
        type: bool
      mdmEncrypted:
        description: MdmEncrypted flag.
        type: bool
      mdmEnrolled:
        description: MdmEnrolled flag.
        type: bool
      mdmIMEI:
        description: Endpoint's mdmIMEI.
        type: str
      mdmJailBroken:
        description: MdmJailBroken flag.
        type: bool
      mdmManufacturer:
        description: Endpoint's mdmManufacturer.
        type: str
      mdmModel:
        description: Endpoint's mdmModel.
        type: str
      mdmOS:
        description: Endpoint's mdmOS.
        type: str
      mdmPhoneNumber:
        description: Endpoint's mdmPhoneNumber.
        type: str
      mdmPinlock:
        description: MdmPinlock flag.
        type: bool
      mdmReachable:
        description: MdmReachable flag.
        type: bool
      mdmSerial:
        description: Endpoint's mdmSerial.
        type: str
      mdmServerName:
        description: Endpoint's mdmServerName.
        type: str
    type: dict
  name:
    description: Endpoint's name.
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
  staticProfileAssignment:
    description: StaticProfileAssignment flag.
    type: bool
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Endpoint reference
  description: Complete reference of the Endpoint object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.endpoint:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customAttributes:
      customAttributes: {}
    description: string
    groupId: string
    id: string
    identityStore: string
    identityStoreId: string
    mac: string
    mdmAttributes:
      mdmComplianceStatus: true
      mdmEncrypted: true
      mdmEnrolled: true
      mdmIMEI: string
      mdmJailBroken: true
      mdmManufacturer: string
      mdmModel: string
      mdmOS: string
      mdmPhoneNumber: string
      mdmPinlock: true
      mdmReachable: true
      mdmSerial: string
      mdmServerName: string
    name: string
    portalUser: string
    profileId: string
    staticGroupAssignment: true
    staticProfileAssignment: true

- name: Delete by id
  cisco.ise.endpoint:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.endpoint:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customAttributes:
      customAttributes: {}
    description: string
    groupId: string
    identityStore: string
    identityStoreId: string
    mac: string
    mdmAttributes:
      mdmComplianceStatus: true
      mdmEncrypted: true
      mdmEnrolled: true
      mdmIMEI: string
      mdmJailBroken: true
      mdmManufacturer: string
      mdmModel: string
      mdmOS: string
      mdmPhoneNumber: string
      mdmPinlock: true
      mdmReachable: true
      mdmSerial: string
      mdmServerName: string
    name: string
    portalUser: string
    profileId: string
    staticGroupAssignment: true
    staticProfileAssignment: true

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "UpdatedFieldsList": {
        "updatedField": {
          "field": "string",
          "oldValue": "string",
          "newValue": "string"
        },
        "field": "string",
        "oldValue": "string",
        "newValue": "string"
      }
    }
"""
