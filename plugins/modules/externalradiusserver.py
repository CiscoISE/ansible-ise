#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: externalradiusserver
short_description: Resource module for Externalradiusserver
description:
- Manage operation create of the resource Externalradiusserver.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  accountingPort:
    description: Valid Range 1 to 65535.
    type: dict
  authenticationPort:
    description: Valid Range 1 to 65535.
    type: dict
  authenticatorKey:
    description: The authenticatorKey is required only if enableKeyWrap is true, otherwise
      it must be ignored or empty. The maximum length is 20 ASCII characters or 40 HEXADECIMAL
      characters (depend on selection in field 'keyInputFormat').
    type: str
  description:
    description: Description.
    type: str
  enableKeyWrap:
    description: KeyWrap may only be enabled if it is supported on the device. When
      running in FIPS mode this option should be enabled for such devices.
    type: bool
  encryptionKey:
    description: The encryptionKey is required only if enableKeyWrap is true, otherwise
      it must be ignored or empty. The maximum length is 16 ASCII characters or 32 HEXADECIMAL
      characters (depend on selection in field 'keyInputFormat').
    type: str
  hostIP:
    description: The IP of the host - must be a valid IPV4 address.
    type: str
  id:
    description: Id.
    type: str
  keyInputFormat:
    description: Specifies the format of the input for fields 'encryptionKey' and 'authenticatorKey'.
      Allowed Values ASCII or HEXADECIMAL.
    type: str
  msgAuthIsRequiredOnResponse:
    description: Should ISE validate the existence of Message-Authenticator on responses
      from the eternal RADIUS server.
    type: bool
  name:
    description: Name.
    type: str
  proxyTimeout:
    description: Valid Range 1 to 600.
    type: dict
  retries:
    description: Valid Range 1 to 9.
    type: dict
  sharedSecret:
    description: Shared secret maximum length is 128 characters.
    type: str
  timeout:
    description: Valid Range 1 to 120.
    type: dict
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    externalradiusserver.Externalradiusserver.create_externalradiusserver,

  - Paths used are
    post /externalradiusserver/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.externalradiusserver:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accountingPort: 1813
    authenticationPort: 1812
    authenticatorKey: '20202020202020202020'
    description: example external radius server
    enableKeyWrap: true
    encryptionKey: '1616161616161616'
    hostIP: 1.1.1.1
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    keyInputFormat: ASCII
    msgAuthIsRequiredOnResponse: true
    name: externalRadiusServer1
    proxyTimeout: 300
    retries: 3
    sharedSecret: sharedSecret
    timeout: 5

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
