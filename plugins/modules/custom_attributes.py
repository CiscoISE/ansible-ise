#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: custom_attributes
short_description: Resource module for Custom Attributes
description:
  - Manage operations create and delete of the resource Custom Attributes.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  attributeName:
    description: Custom Attributes's attributeName.
    type: str
  attributeType:
    description: Custom Attributes's attributeType.
    type: str
  name:
    description: Name path parameter. The name of the custom attribute.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    customattributes.Customattributes.create_custom_attribute,
    customattributes.Customattributes.delete,
  - Paths used are
    post /api/v1/endpoint-custom-attribute,
    delete /api/v1/endpoint-custom-attribute/{name},
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.custom_attributes:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    attributeName: string
    attributeType: string
- name: Delete by name
  cisco.ise.custom_attributes:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    name: string
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
