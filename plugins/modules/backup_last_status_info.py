#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: backup_last_status_info
short_description: Information module for Backup Last Status
description:
- Get all Backup Last Status.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.backup_last_status
# Reference by Internet resource
- name: Backup Last Status reference
  description: Complete reference of the Backup Last Status object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Backup Last Status
  cisco.ise.backup_last_status_info:
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
  type: complex
  sample:
  - {'response': {'repository': 'string', 'type': 'string', 'name': 'string', 'startDate': 'string', 'error': 'string', 'action': 'string', 'scheduled': 'string', 'status': 'string', 'message': 'string', 'justComplete': 'string', 'percentComplete': 'string', 'details': 'string', 'hostName': 'string', 'initiatedFrom': 'string'}, 'version': 'string'}
"""
