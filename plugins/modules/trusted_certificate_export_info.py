#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trusted_certificate_export_info
short_description: Information module for Trusted Certificate Export
description:
- Get Trusted Certificate Export by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    -  id path parameter. The ID of the Trusted Certificate to be exported.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.trusted_certificate_export
# Reference by Internet resource
- name: Trusted Certificate Export reference
  description: Complete reference of the Trusted Certificate Export object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Trusted Certificate Export by id
  cisco.ise.trusted_certificate_export_info
    id: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - 'string'
"""
