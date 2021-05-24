#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: endpoint_get_rejected_endpoints_info
short_description: Information module for Endpoint Get Rejected Endpoints
description:
- Get all Endpoint Get Rejected Endpoints.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.endpoint_get_rejected_endpoints
# Reference by Internet resource
- name: Endpoint Get Rejected Endpoints reference
  description: Complete reference of the Endpoint Get Rejected Endpoints object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Endpoint Get Rejected Endpoints
  cisco.ise.endpoint_get_rejected_endpoints_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'OperationResult': {'resultValue': [{'value': 'string', 'name': 'string'}]}}
"""
