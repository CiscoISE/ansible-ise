#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pxgrid_security_group_acls_info
short_description: Information module for Pxgrid Security Group Acls Info
description:
- Get Pxgrid Security Group Acls Info.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Pxgrid Security Group Acls Info reference
  description: Complete reference of the Pxgrid Security Group Acls Info object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Pxgrid Security Group Acls Info
  cisco.ise.pxgrid_security_group_acls_info:
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
  sample:
  - {}
"""