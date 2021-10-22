#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sponsor_group_member_info
short_description: Information module for Sponsor Group Member
description:
- Get all Sponsor Group Member.
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
  sortasc:
    description:
    - Sortasc query parameter. Sort asc.
    type: str
  sortdsc:
    description:
    - Sortdsc query parameter. Sort desc.
    type: str
  filter:
    description:
    - >
      Filter query parameter. <br/> **Simple filtering** should be available through the filter query string
      parameter. The structure of a filter is a triplet of field operator and value separated with dots. More than
      one filter can be sent. The logical operator common to ALL filter criteria will be by default AND, and can
      be changed by using the "filterType=or" query string parameter. Each resource Data model description should
      specify if an attribute is a filtered field. <br/> Operator | Description <br/>
      ------------|----------------- <br/> EQ | Equals <br/> NEQ | Not Equals <br/> GT | Greater Than <br/> LT |
      Less Then <br/> STARTSW | Starts With <br/> NSTARTSW | Not Starts With <br/> ENDSW | Ends With <br/> NENDSW
      | Not Ends With <br/> CONTAINS | Contains <br/> NCONTAINS | Not Contains <br/>.
    type: list
  filterType:
    description:
    - >
      FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and
      can be changed by using the parameter.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sponsor Group Member reference
  description: Complete reference of the Sponsor Group Member object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Sponsor Group Member
  cisco.ise.sponsor_group_member_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
    sortasc: string
    sortdsc: string
    filter: []
    filterType: AND
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
  version_added: "1.1.0"
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""
