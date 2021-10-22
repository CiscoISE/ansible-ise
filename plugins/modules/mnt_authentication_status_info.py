#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: mnt_authentication_status_info
short_description: Information module for Mnt Authentication Status
description:
- Get all Mnt Authentication Status.
version_added: '1.1.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  MAC:
    description:
    - MAC path parameter.
    type: str
  SECONDS:
    description:
    - SECONDS path parameter.
    type: str
  RECORDS:
    description:
    - RECORDS path parameter.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Mnt Authentication Status reference
  description: Complete reference of the Mnt Authentication Status object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Mnt Authentication Status
  cisco.ise.mnt_authentication_status_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    MAC: string
    SECONDS: string
    RECORDS: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample:
  - {}
"""
