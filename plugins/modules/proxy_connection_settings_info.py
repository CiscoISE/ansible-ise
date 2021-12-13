#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: proxy_connection_settings_info
short_description: Information module for Proxy Connection Settings
description:
- Get all Proxy Connection Settings.
version_added: '2.1.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk >= 1.3.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Proxy Connection Settings reference
  description: Complete reference of the Proxy Connection Settings object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Proxy Connection Settings
  cisco.ise.proxy_connection_settings_info:
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
  sample: >
    {
      "bypassHosts": "string",
      "fqdn": "string",
      "password": "string",
      "passwordRequired": true,
      "port": 0,
      "userName": "string"
    }
"""
