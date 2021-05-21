#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_certificate_info
short_description: Information module for System Certificate
description:
- Get System Certificate by id.
- Get System Certificate by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  hostName:
    description:
    -  hostName path parameter. Name of the host of which system certificates should be returned
    type: str
  page:
    description:
    -  page query parameter. Page number
    type: int
  size:
    description:
    -  size query parameter. Number of objects returned per page
    type: int
  sort:
    description:
    -  sort query parameter. sort type - asc or desc
    type: str
  sortBy:
    description:
    -  sortBy query parameter. sort column by which objects needs to be sorted
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
    -  id path parameter. The id of the system certificate
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.system_certificate
# Reference by Internet resource
- name: System Certificate reference
  description: Complete reference of the System Certificate object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get System Certificate by id
  cisco.ise.system_certificate_info
    hostName: string
    id: string
  register: result
- name: Get System Certificate by name
  cisco.ise.system_certificate_info
    page: 1
    size: 20
    sort: asc
    sortBy: string
    filter: []
    filterType: AND
    hostName: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'response': {'id': 'string', 'friendlyName': 'string', 'serialNumberDecimalFormat': 'string', 'issuedTo': 'string', 'issuedBy': 'string', 'validFrom': 'string', 'expirationDate': 'string', 'usedBy': 'string', 'keySize': 0, 'groupTag': 'string', 'selfSigned': True, 'signatureAlgorithm': 'string', 'portalsUsingTheTag': 'string', 'sha256Fingerprint': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}, 'version': 'string'}
"""
