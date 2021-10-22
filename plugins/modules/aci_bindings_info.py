#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: aci_bindings_info
short_description: Information module for Aci Bindings
description:
- Get all Aci Bindings.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  page:
    description:
    - Page query parameter. Page number.
    type: int
  size:
    description:
    - Size query parameter. Number of objects returned per page.
    type: int
  sort:
    description:
    - Sort query parameter. Sort type - asc or desc.
    type: str
  sortBy:
    description:
    - SortBy query parameter. Sort column by which objects needs to be sorted.
    type: str
  filterBy:
    description:
    - FilterBy query parameter.
    type: list
  filterValue:
    description:
    - FilterValue query parameter.
    type: list
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Aci Bindings reference
  description: Complete reference of the Aci Bindings object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Aci Bindings
  cisco.ise.aci_bindings_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
    sort: asc
    sortBy: string
    filterBy: []
    filterValue: []
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
      "name": "string",
      "description": "string",
      "ip": "string",
      "sgtValue": "string",
      "vn": "string",
      "psn": "string",
      "learnedFrom": "string",
      "learnedBy": "string"
    }
ise_responses:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "ip": "string",
        "sgtValue": "string",
        "vn": "string",
        "psn": "string",
        "learnedFrom": "string",
        "learnedBy": "string"
      }
    ]
"""
