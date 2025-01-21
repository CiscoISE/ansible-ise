#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: custom_attributes_info
short_description: Information module for Custom Attributes Info
description:
  - Get all Custom Attributes Info.
  - Get Custom Attributes Info by name.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  name:
    description:
      - Name path parameter. Name of the custom attribute.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    customattributes.Customattributes.get,
    customattributes.Customattributes.list,
  - Paths used are
    get /api/v1/endpoint-custom-attribute,
    get /api/v1/endpoint-custom-attribute/{name},
"""

EXAMPLES = r"""
- name: Get all Custom Attributes Info
  cisco.ise.custom_attributes_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
- name: Get Custom Attributes Info by name
  cisco.ise.custom_attributes_info:
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
      "attributeName": "string",
      "attributeType": "string"
    }
"""
