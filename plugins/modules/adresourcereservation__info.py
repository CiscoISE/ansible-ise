#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: adresourcereservation__info
short_description: Information module for Adresourcereservation
description:
  - Get Adresourcereservation  by id.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  id:
    description:
      - Id path parameter.
    type: str
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    adresourcereservation.Adresourcereservation.get_adresourcereservation_by_id,
  - Paths used are
    get /adresourcereservation/{id},
"""
EXAMPLES = r"""
---
- name: Get Adresourcereservation  by id
  cisco.ise.adresourcereservation__info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
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
