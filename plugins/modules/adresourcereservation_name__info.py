#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: adresourcereservation_name__info
short_description: Information module for Adresourcereservation Name 
description:
- Get Adresourcereservation Name  by name.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  name:
    description:
    - Name path parameter.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    adresourcereservation.Adresourcereservation.get_adresourcereservation_name_by_name,

  - Paths used are
    get /adresourcereservation/name/{name},

"""

EXAMPLES = r"""
- name: Get Adresourcereservation Name  by name
  cisco.ise.adresourcereservation_name__info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "node": "string",
      "joinPointNames": "string",
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
