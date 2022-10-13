#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: csr_info
short_description: Information module for CSR
description:
- Get all CSR.
- Get CSR by id.
- This API displays details of a Certificate Signing Request of a particular node for given HostName and ID.
- This API supports Filtering, Sorting and Pagination.
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
  filter:
    description:
    - >
      Filter query parameter. .. Container **Simple filtering** should be available through the filter query
      string parameter. The structure of a filter is a triplet of field operator and value separated with dots.
      More than one filter can be sent. The logical operator common to ALL filter criteria will be by default AND,
      and can be changed by using the *"filterType=or"* query string parameter.
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
    elements: str
    type: list
  filterType:
    description:
    - >
      FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and
      can be changed by using the parameter.
    type: str
  hostName:
    description:
    - HostName path parameter. Name of the host of which CSR's should be returned.
    type: str
  id:
    description:
    - Id path parameter. ID of the Certificate Signing Request returned.
    type: str
requirements:
- ciscoisesdk >= 2.0.5
- python >= 3.5
seealso:
- name: Cisco ISE documentation for Certificates
  description: Complete reference of the Certificates API.
  link: https://developer.cisco.com/docs/identity-services-engine/v1/#!certificate-openapi
notes:
  - SDK Method used are
    certificates.Certificates.get_csr_by_id,
    certificates.Certificates.get_csrs_generator,

  - Paths used are
    get /api/v1/certs/certificate-signing-request,
    get /api/v1/certs/certificate-signing-request/{hostName}/{id},

"""

EXAMPLES = r"""
- name: Get all CSR
  cisco.ise.csr_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 0
    size: 0
    sort: string
    sortBy: string
    filter: []
    filterType: string
  register: result

- name: Get CSR by id
  cisco.ise.csr_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    hostName: string
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
      "csrContents": "string",
      "friendlyName": "string",
      "groupTag": "string",
      "hostName": "string",
      "id": "string",
      "keySize": "string",
      "link": {
        "href": "string",
        "rel": "string",
        "type": "string"
      },
      "signatureAlgorithm": "string",
      "subject": "string",
      "timeStamp": "string",
      "usedFor": "string"
    }

ise_responses:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: list
  elements: dict
  sample: >
    [
      {
        "csrContents": "string",
        "friendlyName": "string",
        "groupTag": "string",
        "hostName": "string",
        "id": "string",
        "keySize": "string",
        "link": {
          "href": "string",
          "rel": "string",
          "type": "string"
        },
        "signatureAlgorithm": "string",
        "subject": "string",
        "timeStamp": "string",
        "usedFor": "string"
      }
    ]
"""
