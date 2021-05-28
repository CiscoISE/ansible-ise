#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint_register
short_description: Resource module for Endpoint Register
description:
- Manage operation update of the resource Endpoint Register.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  customAttributes:
    description: Endpoint Register's customAttributes.
    suboptions:
      customAttributes:
        description: Endpoint Register's customAttributes.
        suboptions:
          key1:
            description: Endpoint Register's key1.
            type: str
          key2:
            description: Endpoint Register's key2.
            type: str
        type: dict
    type: dict
  description:
    description: Endpoint Register's description.
    type: str
  groupId:
    description: Endpoint Register's groupId.
    type: str
  id:
    description: Endpoint Register's id.
    type: str
  identityStore:
    description: Endpoint Register's identityStore.
    type: str
  identityStoreId:
    description: Endpoint Register's identityStoreId.
    type: str
  mac:
    description: Endpoint Register's mac.
    type: str
  mdmAttributes:
    description: Endpoint Register's mdmAttributes.
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
        description: Endpoint Register's mdmIMEI.
        type: str
      mdmJailBroken:
        description: MdmJailBroken flag.
        type: bool
      mdmManufacturer:
        description: Endpoint Register's mdmManufacturer.
        type: str
      mdmModel:
        description: Endpoint Register's mdmModel.
        type: str
      mdmOS:
        description: Endpoint Register's mdmOS.
        type: str
      mdmPhoneNumber:
        description: Endpoint Register's mdmPhoneNumber.
        type: str
      mdmPinlock:
        description: MdmPinlock flag.
        type: bool
      mdmReachable:
        description: MdmReachable flag.
        type: bool
      mdmSerial:
        description: Endpoint Register's mdmSerial.
        type: str
      mdmServerName:
        description: Endpoint Register's mdmServerName.
        type: str
    type: dict
  name:
    description: Endpoint Register's name.
    type: str
  portalUser:
    description: Endpoint Register's portalUser.
    type: str
  profileId:
    description: Endpoint Register's profileId.
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
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.endpoint_register
# Reference by Internet resource
- name: Endpoint Register reference
  description: Complete reference of the Endpoint Register object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.endpoint_register:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    customAttributes:
      customAttributes:
        key1: value1
        key2: value2
    description: description
    groupId: groupId
    id: id
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
    staticProfileAssignment: false

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
