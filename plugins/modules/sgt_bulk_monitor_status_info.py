#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: sgt_bulk_monitor_status_info
short_description: Information module for Sgt Bulk Monitor Status
description:
- Get Sgt Bulk Monitor Status by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  bulkid:
    description:
    - Bulkid path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sgt_bulk_monitor_status
# Reference by Internet resource
- name: Sgt Bulk Monitor Status reference
  description: Complete reference of the Sgt Bulk Monitor Status object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Sgt Bulk Monitor Status by id
  cisco.ise.sgt_bulk_monitor_status_info
    bulkid: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
"""
