#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_certificate
short_description: Resource module for System Certificate
description:
- Manage operations update and delete of the resource System Certificate.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  admin:
    description: Use certificate to authenticate the ISE Admin Portal.
    type: bool
  allowReplacementOfPortalGroupTag:
    description: Allow Replacement of Portal Group Tag (required).
    type: bool
  description:
    description: Description of System Certificate.
    type: str
  eap:
    description: Use certificate for EAP protocols that use SSL/TLS tunneling.
    type: bool
  expirationTTLPeriod:
    description: System Certificate's expirationTTLPeriod.
    type: int
  expirationTTLUnits:
    description: System Certificate's expirationTTLUnits.
    type: str
  hostName:
    description: HostName path parameter. Name of the host from which the System Certificate
      needs to be deleted.
    type: str
  id:
    description: Id path parameter. The ID of the System Certificate to be deleted.
    type: str
  ims:
    description: Use certificate for the ISE Messaging Service.
    type: bool
  name:
    description: Name of the certificate.
    type: str
  portal:
    description: Use for portal.
    type: bool
  portalGroupTag:
    description: Set Group tag.
    type: str
  pxgrid:
    description: Use certificate for the pxGrid Controller.
    type: bool
  radius:
    description: Use certificate for the RADSec server.
    type: bool
  renewSelfSignedCertificate:
    description: Renew Self Signed Certificate.
    type: bool
  saml:
    description: Use certificate for SAML Signing.
    type: bool
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
- name: Update by id
  cisco.ise.system_certificate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    admin: true
    allowReplacementOfPortalGroupTag: true
    description: string
    eap: true
    expirationTTLPeriod: 0
    expirationTTLUnits: string
    hostName: string
    id: string
    ims: true
    name: string
    portal: true
    portalGroupTag: string
    pxgrid: true
    radius: true
    renewSelfSignedCertificate: true
    saml: true

- name: Delete by id
  cisco.ise.system_certificate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    hostName: string
    id: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
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

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "link": {
          "href": "string",
          "rel": "string",
          "type": "string"
        },
        "message": "string",
        "status": "string"
      },
      "version": "string"
    }
"""
