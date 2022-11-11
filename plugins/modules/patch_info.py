#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: patch_info
short_description: Information module for Patch
description:
- Get all Patch.
- List all the installed patches in the system, with the patch number for rollback.
version_added: '2.1.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk >= 2.0.8
- python >= 3.5
seealso:
- name: Cisco ISE documentation for Patching
  description: Complete reference of the Patching API.
  link: https://developer.cisco.com/docs/identity-services-engine/v1/#!patch-and-hot-patch-openapi
notes:
  - SDK Method used are
    patching.Patching.list_installed_patches,

  - Paths used are
    get /api/v1/patch,

"""

EXAMPLES = r"""
- name: Get all Patch
  cisco.ise.patch_info:
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
      "iseVersion": "string",
      "patchVersion": [
        {
          "installDate": "string",
          "patchNumber": 0
        }
      ]
    }
"""
