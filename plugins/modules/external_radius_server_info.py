#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

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
  cisco.ise.external_radius_server_info
    id: string
  register: result

- name: Get External Radius Server by name
  cisco.ise.external_radius_server_info
    name: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'ExternalRadiusServer': {'id': 'string', 'name': 'string', 'description': 'string', 'hostIP': 'string', 'sharedSecret': 'string', 'enableKeyWrap': True, 'encryptionKey': 'string', 'authenticatorKey': 'string', 'keyInputFormat': 'string', 'authenticationPort': 0, 'accountingPort': 0, 'timeout': 0, 'retries': 0, 'proxyTimeout': 0}}
  - {'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': {'rel': 'string', 'href': 'string', 'type': 'string'}, 'previousPage': {'rel': 'string', 'href': 'string', 'type': 'string'}}}
"""
