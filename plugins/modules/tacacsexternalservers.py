#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tacacsexternalservers
short_description: Resource module for TACACSexternalservers
description:
  - Manage operation create of the resource TACACSexternalservers.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  connectionPort:
    description: The port to connect the server.
    type: float
  description:
    description: Description.
    type: str
  hostIP:
    description: The server IPV4 address.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  sharedSecret:
    description: The server shared secret.
    type: str
  singleConnect:
    description: Define the use of single connection.
    type: bool
  timeout:
    description: The server timeout.
    type: float
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    tacacsexternalservers.Tacacsexternalservers.create_tacacsexternalservers,
  - Paths used are
    post /tacacsexternalservers/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.tacacsexternalservers:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    connectionPort: 49
    description: TacacsExternalServerForSDK
    hostIP: 1.1.1.1
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    name: TacacsExternalServer1
    sharedSecret: SharedSecret
    singleConnect: true
    timeout: 20
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
