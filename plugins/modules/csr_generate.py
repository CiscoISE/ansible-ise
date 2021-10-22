#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: csr_generate
short_description: Resource module for Csr Generate
description:
- Manage operation create of the resource Csr Generate.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  allowWildCardCert:
    description: AllowWildCardCert flag.
    type: bool
  certificatePolicies:
    description: Csr Generate's certificatePolicies.
    type: str
  digestType:
    description: Csr Generate's digestType.
    type: str
  hostnames:
    description: Csr Generate's hostnames.
    elements: str
    type: list
  keyLength:
    description: Csr Generate's keyLength.
    type: str
  keyType:
    description: Csr Generate's keyType.
    type: str
  portalGroupTag:
    description: Csr Generate's portalGroupTag.
    type: str
  sanDNS:
    description: Csr Generate's sanDNS.
    elements: str
    type: list
  sanDir:
    description: Csr Generate's sanDir.
    elements: str
    type: list
  sanIP:
    description: Csr Generate's sanIP.
    elements: str
    type: list
  sanURI:
    description: Csr Generate's sanURI.
    elements: str
    type: list
  subjectCity:
    description: Csr Generate's subjectCity.
    type: str
  subjectCommonName:
    description: Csr Generate's subjectCommonName.
    type: str
  subjectCountry:
    description: Csr Generate's subjectCountry.
    type: str
  subjectOrg:
    description: Csr Generate's subjectOrg.
    type: str
  subjectOrgUnit:
    description: Csr Generate's subjectOrgUnit.
    type: str
  subjectState:
    description: Csr Generate's subjectState.
    type: str
  usedFor:
    description: Csr Generate's usedFor.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Csr Generate reference
  description: Complete reference of the Csr Generate object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.csr_generate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    allowWildCardCert: true
    certificatePolicies: string
    digestType: string
    hostnames:
    - string
    keyLength: string
    keyType: string
    portalGroupTag: string
    sanDNS:
    - string
    sanDir:
    - string
    sanIP:
    - string
    sanURI:
    - string
    subjectCity: string
    subjectCommonName: string
    subjectCountry: string
    subjectOrg: string
    subjectOrgUnit: string
    subjectState: string
    usedFor: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "link": {
            "href": "string",
            "rel": "string",
            "type": "string"
          },
          "message": "string"
        }
      ],
      "version": "string"
    }
"""
