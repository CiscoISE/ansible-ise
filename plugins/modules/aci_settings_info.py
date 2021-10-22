#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: aci_settings_info
short_description: Information module for Aci Settings
description:
- Get all Aci Settings.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Aci Settings reference
  description: Complete reference of the Aci Settings object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Aci Settings
  cisco.ise.aci_settings_info:
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
      "id": "string",
      "enableAci": true,
      "ipAddressHostName": "string",
      "adminName": "string",
      "adminPassword": "string",
      "aciipaddress": "string",
      "aciuserName": "string",
      "acipassword": "string",
      "tenantName": "string",
      "l3RouteNetwork": "string",
      "suffixToEpg": "string",
      "suffixToSgt": "string",
      "allSxpDomain": true,
      "specificSxpDomain": true,
      "specifixSxpDomainList": [
        "string"
      ],
      "enableDataPlane": true,
      "untaggedPacketIepgName": "string",
      "defaultSgtName": "string",
      "enableElementsLimit": true,
      "maxNumIepgFromAci": 0,
      "maxNumSgtToAci": 0,
      "aci50": true,
      "aci51": true
    }
"""
