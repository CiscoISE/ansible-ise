#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: mnt_session_reauthentication_info
short_description: Information module for Mnt Session Reauthentication
description:
- Get Mnt Session Reauthentication by id.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  PSN_NAME:
    description:
    - PSN_NAME path parameter.
    type: str
  ENDPOINT_MAC:
    description:
    - ENDPOINT_MAC path parameter.
    type: str
  REAUTH_TYPE:
    description:
    - REAUTH_TYPE path parameter.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Mnt Session Reauthentication reference
  description: Complete reference of the Mnt Session Reauthentication object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Mnt Session Reauthentication by id
  cisco.ise.mnt_session_reauthentication_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    PSN_NAME: string
    ENDPOINT_MAC: string
    REAUTH_TYPE: string
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
