#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_access_dictionary_attributes_authorization_info
short_description: Information module for Network Access Dictionary Attributes Authorization
description:
- Get all Network Access Dictionary Attributes Authorization.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
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
  type: dict
  sample: >
    {
      "response": [
        {
          "allowedValues": [
            {
              "isDefault": true,
              "key": "string",
              "value": "string"
            }
          ],
          "dataType": "string",
          "description": "string",
          "dictionaryName": "string",
          "directionType": "string",
          "id": "string",
          "internalName": "string",
          "name": "string"
        }
      ],
      "version": "string"
    }
"""
