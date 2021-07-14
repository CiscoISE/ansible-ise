#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: anc_endpoint_clear
short_description: Resource module for Anc Endpoint Clear
description:
- Manage operation update of the resource Anc Endpoint Clear.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  additionalData:
    description: Anc Endpoint Clear's additionalData.
    suboptions:
      name:
        description: Anc Endpoint Clear's name.
        type: str
      value:
        description: Anc Endpoint Clear's value.
        type: str
    type: list
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.anc_endpoint_clear
# Reference by Internet resource
- name: Anc Endpoint Clear reference
  description: Complete reference of the Anc Endpoint Clear object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.anc_endpoint_clear:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    additionalData:
    - name: macAddress
      value: value_1
    - name: ipAddress
      value: value_2
    - name: policyName
      value: value_3

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""