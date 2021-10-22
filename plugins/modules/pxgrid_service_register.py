#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pxgrid_service_register
short_description: Resource module for Pxgrid Service Register
description:
- Manage operation create of the resource Pxgrid Service Register.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  name:
    description: Pxgrid Service Register's name.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Pxgrid Service Register reference
  description: Complete reference of the Pxgrid Service Register object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.pxgrid_service_register:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: com.cisco.ise.pubsub

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
