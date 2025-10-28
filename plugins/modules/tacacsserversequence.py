#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tacacsserversequence
short_description: Resource module for TACACSserversequence
description:
- Manage operation create of the resource TACACSserversequence.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
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
  prefixDelimiter:
    description: The delimiter that will be used for prefix strip.
    type: str
  prefixStrip:
    description: Define if a delimiter will be used for prefix strip.
    type: bool
  remoteAccounting:
    description: RemoteAccounting flag.
    type: bool
  serverList:
    description: The names of TACACS external servers separated by commas. The order
      of the names in the string is the order of servers that will be used during authentication.
    type: str
  suffixDelimiter:
    description: The delimiter that will be used for suffix strip.
    type: str
  suffixStrip:
    description: Define if a delimiter will be used for suffix strip.
    type: bool
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    tacacsserversequence.Tacacsserversequence.create_tacacsserversequence,

  - Paths used are
    post /tacacsserversequence/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.tacacsserversequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: TacacsServerSequenceForSDK
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    localAccounting: false
    name: TacacsServerSequence1
    prefixDelimiter: \
    prefixStrip: false
    remoteAccounting: true
    serverList: TacacsExternalServer1,TacacsExternalServer2
    suffixDelimiter: '@'
    suffixStrip: false

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
