#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: acisettings_info
short_description: Information module for ACIsettings
description:
  - Get all ACIsettings.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    acisettings.Acisettings.get_acisettings,
  - Paths used are
    get /acisettings/,
"""
EXAMPLES = r"""
---
- name: Get all ACIsettings
  cisco.ise.acisettings_info:
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
      "enableAci": true,
      "aci50": true,
      "ipAddressHostName": "string",
      "adminName": "string",
      "adminPassword": "string",
      "tenantName": "string",
      "l3RouteNetwork": "string",
      "suffixToEpg": "string",
      "suffixToSgt": "string",
      "allSxpDomain": true,
      "specificSxpDomain": true,
      "specifixSxpDomainList": [
        "string"
      ],
      "aci51": true,
      "aciipaddress": "string",
      "aciuserName": "string",
      "acipassword": "string",
      "enableDataPlane": true,
      "untaggedPacketIepgName": "string",
      "defaultSgtName": "string",
      "enableElementsLimit": true,
      "maxNumIepgFromAci": {},
      "maxNumSgtToAci": {},
      "name": "string",
      "id": "string",
      "description": "string",
      "link": {
        "rel": "string",
        "href": "string",
        "type": "string"
      }
    }
"""
