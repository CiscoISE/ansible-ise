#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: external_radius_server_info
short_description: Information module for External Radius Server
description:
- Get all External Radius Server.
- Get External Radius Server by id.
- Get External Radius Server by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  page:
    description:
    - Page query parameter. Page number.
    type: int
  size:
    description:
    - Size query parameter. Number of objects returned per page.
    type: int
  id:
    description:
    - Id path parameter.
    type: str
  name:
    description:
    - Name path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.external_radius_server
# Reference by Internet resource
- name: External Radius Server reference
  description: Complete reference of the External Radius Server object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all External Radius Server
  cisco.ise.external_radius_server_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result

- name: Get External Radius Server by id
  cisco.ise.external_radius_server_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

- name: Get External Radius Server by name
  cisco.ise.external_radius_server_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "ExternalRadiusServer": {
        "id": "string",
        "name": "string",
        "description": "string",
        "hostIP": "string",
        "sharedSecret": "string",
        "enableKeyWrap": true,
        "encryptionKey": "string",
        "authenticatorKey": "string",
        "keyInputFormat": "string",
        "authenticationPort": 0,
        "accountingPort": 0,
        "timeout": 0,
        "retries": 0,
        "proxyTimeout": 0
      }
    }
"""
