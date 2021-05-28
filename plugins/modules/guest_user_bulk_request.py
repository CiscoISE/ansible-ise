#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: guest_user_bulk_request
short_description: Resource module for Guest User Bulk Request
description:
- Manage operation update of the resource Guest User Bulk Request.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    operationType:
      description: Guest User Bulk Request's operationType.
      type: str
    resourceMediaType:
      description: Guest User Bulk Request's resourceMediaType.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.guest_user_bulk_request
# Reference by Internet resource
- name: Guest User Bulk Request reference
  description: Complete reference of the Guest User Bulk Request object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.guest_user_bulk_request:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    operationType: create
    resourceMediaType: vnd.com.cisco.ise.identity.guestuser.2.0+xml

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""