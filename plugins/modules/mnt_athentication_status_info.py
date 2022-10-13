#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: mnt_athentication_status_info
short_description: Information module for Mnt Athentication Status
description:
- Get all Mnt Athentication Status.
version_added: '1.0.0'
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
- ciscoisesdk >= 2.0.5
- python >= 3.5
notes:
  - SDK Method used are
    misc.Misc.get_authentication_status_by_mac,

  - Paths used are
    get /AuthStatus/MACAddress/{MAC}/{SECONDS}/{RECORDS}/All,
seealso:
# Reference by module name
- module: cisco.ise.mnt_authentication_status_info
"""

EXAMPLES = r"""
- name: Get all Mnt Athentication Status
  cisco.ise.mnt_athentication_status_info:
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
