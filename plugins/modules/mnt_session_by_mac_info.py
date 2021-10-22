#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: mnt_session_by_mac_info
short_description: Information module for Mnt Session By Mac
description:
- Get Mnt Session By Mac by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  mac:
    description:
    - Mac path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Mnt Session By Mac reference
  description: Complete reference of the Mnt Session By Mac object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Mnt Session By Mac by id
  cisco.ise.mnt_session_by_mac_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    mac: string
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