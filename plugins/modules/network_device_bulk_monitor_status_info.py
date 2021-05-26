#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_bulk_monitor_status_info
short_description: Information module for Network Device Bulk Monitor Status
description:
- Get Network Device Bulk Monitor Status by id.
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
- module: cisco.ise.plugins.module_utils.definitions.network_device_bulk_monitor_status
# Reference by Internet resource
- name: Network Device Bulk Monitor Status reference
  description: Complete reference of the Network Device Bulk Monitor Status object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Network Device Bulk Monitor Status by id
  cisco.ise.network_device_bulk_monitor_status_info:
    bulkid: string
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
