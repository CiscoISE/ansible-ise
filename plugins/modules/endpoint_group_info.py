#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint_group_info
short_description: Information module for Endpoint Group
description:
- Get all Endpoint Group.
- Get Endpoint Group by id.
- Get Endpoint Group by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  page:
    description:
    -  page query parameter. Page number
    type: int
  size:
    description:
    -  size query parameter. Number of objects returned per page
    type: int
  sortasc:
    description:
    -  sortasc query parameter. sort asc
    type: str
  sortdec:
    description:
    -  sortdec query parameter. sort desc
    type: str
  filter:
    description:
    -  filter query parameter. <br/>
**Simple filtering** should be available through the filter query string parameter. The structure of a filter is
a triplet of field operator and value separated with dots. More than one filter can be sent. The logical operator
common to ALL filter criteria will be by default AND, and can be changed by using the "filterType=or" query
string parameter. Each resource Data model description should specify if an attribute is a filtered field.
<br/>

              Operator    | Description <br/>
              ------------|----------------- <br/>
              EQ          | Equals <br/>
              NEQ         | Not Equals <br/>
              GT          | Greater Than <br/>
              LT          | Less Then <br/>
              STARTSW     | Starts With <br/>
              NSTARTSW    | Not Starts With <br/>
              ENDSW       | Ends With <br/>
              NENDSW      | Not Ends With <br/>
              CONTAINS	  | Contains <br/>
              NCONTAINS	  | Not Contains <br/>

    type: list
  filterType:
    description:
    -  filterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and can be changed by using the parameter
    type: str
  id:
    description:
    -  id path parameter.
    type: str
  name:
    description:
    -  name path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.endpoint_group
# Reference by Internet resource
- name: Endpoint Group reference
  description: Complete reference of the Endpoint Group object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Endpoint Group
  cisco.ise.endpoint_group_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
    sortasc: asc
    sortdec: string
    filter: []
    filterType: AND
  register: result
- name: Get Endpoint Group by id
  cisco.ise.endpoint_group_info
    id: string
  register: result
- name: Get Endpoint Group by name
  cisco.ise.endpoint_group_info
    name: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'EndPointGroup': {'id': 'string', 'name': 'string', 'description': 'string', 'systemDefined': True}}
  - {'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': {'rel': 'string', 'href': 'string', 'type': 'string'}, 'previousPage': {'rel': 'string', 'href': 'string', 'type': 'string'}}}
"""
