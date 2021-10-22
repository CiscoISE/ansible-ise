#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_certificate_info
short_description: Information module for System Certificate
description:
- Get System Certificate by id.
- Get System Certificate by name.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  hostName:
    description:
    - HostName path parameter. Name of the host of which system certificates should be returned.
    type: str
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
  filter:
    description:
    - >
      Filter query parameter. <div> <style type="text/css" scoped> .apiServiceTable td, .apiServiceTable th {
      padding 5px 10px !important; text-align left; } </style> <span> <b>Simple filtering</b> should be available
      through the filter query string parameter. The structure of a filter is a triplet of field operator and
      value separated with dots. More than one filter can be sent. The logical operator common to ALL filter
      criteria will be by default AND, and can be changed by using the <i>"filterType=or"</i> query string
      parameter. Each resource Data model description should specify if an attribute is a filtered field. </span>
      <br /> <table class="apiServiceTable"> <thead> <tr> <th>OPERATOR</th> <th>DESCRIPTION</th> </tr> </thead>
      <tbody> <tr> <td>EQ</td> <td>Equals</td> </tr> <tr> <td>NEQ</td> <td>Not Equals</td> </tr> <tr> <td>GT</td>
      <td>Greater Than</td> </tr> <tr> <td>LT</td> <td>Less Then</td> </tr> <tr> <td>STARTSW</td> <td>Starts
      With</td> </tr> <tr> <td>NSTARTSW</td> <td>Not Starts With</td> </tr> <tr> <td>ENDSW</td> <td>Ends With</td>
      </tr> <tr> <td>NENDSW</td> <td>Not Ends With</td> </tr> <tr> <td>CONTAINS</td> <td>Contains</td> </tr> <tr>
      <td>NCONTAINS</td> <td>Not Contains</td> </tr> </tbody> </table> </div>.
    type: list
  filterType:
    description:
    - >
      FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and
      can be changed by using the parameter.
    type: str
  id:
    description:
    - Id path parameter. The id of the system certificate.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: System Certificate reference
  description: Complete reference of the System Certificate object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get System Certificate by id
  cisco.ise.system_certificate_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    hostName: string
    id: string
  register: result

- name: Get System Certificate by name
  cisco.ise.system_certificate_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
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
  type: dict
  sample: >
    {
      "response": {
        "expirationDate": "string",
        "friendlyName": "string",
        "groupTag": "string",
        "id": "string",
        "issuedBy": "string",
        "issuedTo": "string",
        "keySize": 0,
        "link": {
          "href": "string",
          "rel": "string",
          "type": "string"
        },
        "portalsUsingTheTag": "string",
        "selfSigned": true,
        "serialNumberDecimalFormat": "string",
        "sha256Fingerprint": "string",
        "signatureAlgorithm": "string",
        "usedBy": "string",
        "validFrom": "string"
      },
      "version": "string"
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
        "expirationDate": "string",
        "friendlyName": "string",
        "groupTag": "string",
        "id": "string",
        "issuedBy": "string",
        "issuedTo": "string",
        "keySize": 0,
        "link": {
          "href": "string",
          "rel": "string",
          "type": "string"
        },
        "portalsUsingTheTag": "string",
        "selfSigned": true,
        "serialNumberDecimalFormat": "string",
        "sha256Fingerprint": "string",
        "signatureAlgorithm": "string",
        "usedBy": "string",
        "validFrom": "string"
      }
    ]
"""
