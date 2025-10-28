#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: telemetryinfo_info
short_description: Information module for Telemetryinfo
description:
- Get all Telemetryinfo.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  filter:
    description:
    - Filter query parameter. Filter Supported Fields deploymentId.
    - Each resource Data model description should specify if an attribute is a filtered field.
    - The 'EQ' operator describes 'Equals'.
    - The 'NEQ' operator describes 'Not Equals'.
    - The 'GT' operator describes 'Greater Than'.
    - The 'LT' operator describes 'Less Than'.
    - The 'STARTSW' operator describes 'Starts With'.
    - The 'NSTARTSW' operator describes 'Not Starts With'.
    - The 'ENDSW' operator describes 'Ends With'.
    - The 'NENDSW' operator describes 'Not Ends With'.
    - The 'CONTAINS' operator describes 'Contains'.
    - The 'NCONTAINS' operator describes 'Not Contains'.
    type: str
  page:
    description:
    - Page query parameter. Page Number (0...N).
    type: int
  size:
    description:
    - Size query parameter. Items by Page.
    type: int
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    telemetryinfo.Telemetryinfo.get_telemetryinfo_generator,

  - Paths used are
    get /telemetryinfo/,

"""

EXAMPLES = r"""
- name: Get all Telemetryinfo
  cisco.ise.telemetryinfo_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    filter: toDate.CONTAINS.SEP
    page: 0
    size: 0
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]

ise_responses:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""
