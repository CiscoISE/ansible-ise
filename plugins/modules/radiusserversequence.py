#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: radiusserversequence
short_description: Resource module for RADIUSserversequence
description:
  - Manage operation create of the resource RADIUSserversequence.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  BeforeAcceptAttrManipulatorsList:
    description: The beforeAcceptAttrManipulators is required only if useAttrSetBeforeAcc
      is true.
    elements: dict
    type: list
  OnRequestAttrManipulatorList:
    description: The onRequestAttrManipulators is required only if useAttrSetOnRequest
      is true.
    elements: dict
    type: list
  RADIUSServerList:
    description: List with names of external radius server. The order of the names
      in the list is the order of servers that will be used during authentication.
    type: list
  continueAuthorzPolicy:
    description: ContinueAuthorzPolicy flag.
    type: bool
  description:
    description: Description.
    type: str
  id:
    description: Id.
    type: str
  localAccounting:
    description: LocalAccounting flag.
    type: bool
  name:
    description: Name.
    type: str
  prefixSeparator:
    description: The prefixSeparator is required only if stripPrefix is true. The
      maximum length is 1 character.
    type: str
  remoteAccounting:
    description: RemoteAccounting flag.
    type: bool
  stripPrefix:
    description: StripPrefix flag.
    type: bool
  stripSuffix:
    description: StripSuffix flag.
    type: bool
  suffixSeparator:
    description: The suffixSeparator is required only if stripSuffix is true. The
      maximum length is 1 character.
    type: str
  useAttrSetBeforeAcc:
    description: UseAttrSetBeforeAcc flag.
    type: bool
  useAttrSetOnRequest:
    description: UseAttrSetOnRequest flag.
    type: bool
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    radiusserversequence.Radiusserversequence.create_radiusserversequence,
  - Paths used are
    post /radiusserversequence/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.radiusserversequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    BeforeAcceptAttrManipulatorsList:
      - action: ADD
        attributeName: cisco-prev-hop-ip
        changedVal: test2
        dictionaryName: Cisco
        value: test1
      - action: UPDATE
        attributeName: Cisco:cisco-ppp-vj-slot-comp
        changedVal: '13'
        dictionaryName: Cisco
        value: '12'
    OnRequestAttrManipulatorList:
      - action: ADD
        attributeName: cisco-prev-hop-ip
        changedVal: test2
        dictionaryName: Cisco
        value: test1
      - action: UPDATE
        attributeName: Cisco:cisco-ppp-vj-slot-comp
        changedVal: '13'
        dictionaryName: Cisco
        value: '12'
    RadiusServerList:
      - externalRadiusServer1
      - externalRadiusServer2
    continueAuthorzPolicy: false
    description: description
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    localAccounting: false
    name: name
    prefixSeparator: \
    remoteAccounting: true
    stripPrefix: false
    stripSuffix: false
    suffixSeparator: '@'
    useAttrSetBeforeAcc: false
    useAttrSetOnRequest: false
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
