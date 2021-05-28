#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: backup_cancel
short_description: Resource module for Backup Cancel
description:
- Manage operation create of the resource Backup Cancel.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.backup_cancel
# Reference by Internet resource
- name: Backup Cancel reference
  description: Complete reference of the Backup Cancel object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.backup_cancel:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "repository": "string",
        "type": "string",
        "name": "string",
        "startDate": "string",
        "error": "string",
        "action": "string",
        "scheduled": "string",
        "status": "string",
        "message": "string",
        "justComplete": "string",
        "percentComplete": "string",
        "details": "string",
        "hostName": "string",
        "initiatedFrom": "string"
      },
      "version": "string"
    }
"""