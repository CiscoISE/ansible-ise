#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: radius_server_sequence
short_description: Resource module for Radius Server Sequence
description:
- Manage operations create, update and delete of the resource Radius Server Sequence.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  BeforeAcceptAttrManipulatorsList:
    description: The beforeAcceptAttrManipulators is required only if useAttrSetBeforeAcc
      is true.
    suboptions:
      action:
        description: Allowed Values - ADD, - UPDATE, - REMOVE, - REMOVEANY.
        type: str
      attributeName:
        description: Radius Server Sequence's attributeName.
        type: str
      changedVal:
        description: The changedVal is required only if the action equals to 'UPDATE'.
        type: str
      dictionaryName:
        description: Radius Server Sequence's dictionaryName.
        type: str
      value:
        description: Radius Server Sequence's value.
        type: str
    type: list
  OnRequestAttrManipulatorList:
    description: The onRequestAttrManipulators is required only if useAttrSetOnRequest
      is true.
    suboptions:
      action:
        description: Allowed Values - ADD, - UPDATE, - REMOVE, - REMOVEANY.
        type: str
      attributeName:
        description: Radius Server Sequence's attributeName.
        type: str
      changedVal:
        description: The changedVal is required only if the action equals to 'UPDATE'.
        type: str
      dictionaryName:
        description: Radius Server Sequence's dictionaryName.
        type: str
      value:
        description: Radius Server Sequence's value.
        type: str
    type: list
  RadiusServerList:
    description: Radius Server Sequence's RadiusServerList.
    elements: str
    type: list
  continueAuthorzPolicy:
    description: ContinueAuthorzPolicy flag.
    type: bool
  description:
    description: Radius Server Sequence's description.
    type: str
  id:
    description: Radius Server Sequence's id.
    type: str
  localAccounting:
    description: LocalAccounting flag.
    type: bool
  name:
    description: Radius Server Sequence's name.
    type: str
  prefixSeparator:
    description: The prefixSeparator is required only if stripPrefix is true. The maximum
      length is 1 character.
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
    description: The suffixSeparator is required only if stripSuffix is true. The maximum
      length is 1 character.
    type: str
  useAttrSetBeforeAcc:
    description: UseAttrSetBeforeAcc flag.
    type: bool
  useAttrSetOnRequest:
    description: UseAttrSetOnRequest flag.
    type: bool
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Radius Server Sequence reference
  description: Complete reference of the Radius Server Sequence object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.radius_server_sequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    BeforeAcceptAttrManipulatorsList:
    - action: string
      attributeName: string
      changedVal: string
      dictionaryName: string
      value: string
    OnRequestAttrManipulatorList:
    - action: string
      attributeName: string
      changedVal: string
      dictionaryName: string
      value: string
    RadiusServerList:
    - string
    continueAuthorzPolicy: true
    description: string
    id: string
    localAccounting: true
    name: string
    prefixSeparator: string
    remoteAccounting: true
    stripPrefix: true
    stripSuffix: true
    suffixSeparator: string
    useAttrSetBeforeAcc: true
    useAttrSetOnRequest: true

- name: Delete by id
  cisco.ise.radius_server_sequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.radius_server_sequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    BeforeAcceptAttrManipulatorsList:
    - action: string
      attributeName: string
      changedVal: string
      dictionaryName: string
      value: string
    OnRequestAttrManipulatorList:
    - action: string
      attributeName: string
      changedVal: string
      dictionaryName: string
      value: string
    RadiusServerList:
    - string
    continueAuthorzPolicy: true
    description: string
    localAccounting: true
    name: string
    prefixSeparator: string
    remoteAccounting: true
    stripPrefix: true
    stripSuffix: true
    suffixSeparator: string
    useAttrSetBeforeAcc: true
    useAttrSetOnRequest: true

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "stripPrefix": true,
      "stripSuffix": true,
      "prefixSeparator": "string",
      "suffixSeparator": "string",
      "remoteAccounting": true,
      "localAccounting": true,
      "useAttrSetOnRequest": true,
      "useAttrSetBeforeAcc": true,
      "continueAuthorzPolicy": true,
      "RadiusServerList": [
        "string"
      ],
      "OnRequestAttrManipulatorList": [
        {
          "action": "string",
          "dictionaryName": "string",
          "attributeName": "string",
          "value": "string",
          "changedVal": "string"
        }
      ],
      "BeforeAcceptAttrManipulatorsList": [
        {
          "action": "string",
          "dictionaryName": "string",
          "attributeName": "string",
          "value": "string",
          "changedVal": "string"
        }
      ],
      "link": {
        "rel": "string",
        "href": "string",
        "type": "string"
      }
    }

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
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
