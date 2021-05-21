#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: network_access_dictionary_attributes_authorization_info
short_description: Information module for Network Access Dictionary Attributes Authorization
description:
- Get all Network Access Dictionary Attributes Authorization.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_dictionary_attributes_authorization
# Reference by Internet resource
- name: Network Access Dictionary Attributes Authorization reference
  description: Complete reference of the Network Access Dictionary Attributes Authorization object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Network Access Dictionary Attributes Authorization
  cisco.ise.network_access_dictionary_attributes_authorization_info:
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
  - [{'id': 'string', 'directionType': 'string', 'name': 'string', 'description': 'string', 'internalName': 'string', 'dataType': 'string', 'dictionaryName': 'string', 'allowedValues': [{'key': 'string', 'value': 'string', 'isDefault': True}]}]
"""
