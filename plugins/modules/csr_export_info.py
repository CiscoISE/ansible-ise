#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: csr_export_info
short_description: Information module for Csr Export
description:
- Get Csr Export by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  hostname:
    description:
    -  hostname path parameter. The hostname to which the CSR belongs.
    type: str
  id:
    description:
    -  id path parameter. The ID of the CSR to be exported.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.csr_export
# Reference by Internet resource
- name: Csr Export reference
  description: Complete reference of the Csr Export object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Csr Export by id
  cisco.ise.csr_export_info
    hostname: string
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
