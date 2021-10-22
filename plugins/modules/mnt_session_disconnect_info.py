#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: mnt_session_disconnect_info
short_description: Information module for Mnt Session Disconnect
description:
- Get Mnt Session Disconnect by id.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  ENDPOINT_IP:
    description:
    - ENDPOINT_IP path parameter.
    type: str
  PSN_NAME:
    description:
    - PSN_NAME path parameter.
    type: str
  MAC:
    description:
    - MAC path parameter.
    type: str
  DISCONNECT_TYPE:
    description:
    - DISCONNECT_TYPE path parameter.
    type: str
  NAS_IPV4:
    description:
    - NAS_IPV4 path parameter.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Mnt Session Disconnect reference
  description: Complete reference of the Mnt Session Disconnect object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Mnt Session Disconnect by id
  cisco.ise.mnt_session_disconnect_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    ENDPOINT_IP: string
    PSN_NAME: string
    MAC: string
    DISCONNECT_TYPE: string
    NAS_IPV4: string
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
