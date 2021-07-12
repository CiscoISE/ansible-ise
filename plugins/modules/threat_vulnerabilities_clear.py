#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: threat_vulnerabilities_clear
short_description: Resource module for Threat Vulnerabilities Clear
description:
- Manage operation update of the resource Threat Vulnerabilities Clear.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  description:
    description: Threat Vulnerabilities Clear's description.
    type: str
  id:
    description: Threat Vulnerabilities Clear's id.
    type: str
  macAddresses:
    description: Threat Vulnerabilities Clear's macAddresses.
    elements: str
    type: list
  name:
    description: Threat Vulnerabilities Clear's name.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.threat_vulnerabilities_clear
# Reference by Internet resource
- name: Threat Vulnerabilities Clear reference
  description: Complete reference of the Threat Vulnerabilities Clear object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.threat_vulnerabilities_clear:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    description: string
    id: string
    macAddresses:
    - string
    name: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
