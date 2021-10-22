#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trusted_certificate
short_description: Resource module for Trusted Certificate
description:
- Manage operations update and delete of the resource Trusted Certificate.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  authenticateBeforeCRLReceived:
    description: Switch to enable/disable CRL Verification if CRL is not Received.
    type: bool
  automaticCRLUpdate:
    description: Switch to enable/disable automatic CRL update.
    type: bool
  automaticCRLUpdatePeriod:
    description: Automatic CRL update period.
    type: int
  automaticCRLUpdateUnits:
    description: Unit of time for automatic CRL update.
    type: str
  crlDistributionUrl:
    description: CRL Distribution URL.
    type: str
  crlDownloadFailureRetries:
    description: If CRL download fails, wait time before retry.
    type: int
  crlDownloadFailureRetriesUnits:
    description: Unit of time before retry if CRL download fails.
    type: str
  description:
    description: Description for trust certificate.
    type: str
  downloadCRL:
    description: Switch to enable/disable download of CRL.
    type: bool
  enableOCSPValidation:
    description: Switch to enable/disable OCSP Validation.
    type: bool
  enableServerIdentityCheck:
    description: Switch to enable/disable verification if HTTPS or LDAP server certificate
      name fits the configured server URL.
    type: bool
  id:
    description: Id path parameter. The ID of the Trusted Certificate to be deleted.
    type: str
  ignoreCRLExpiration:
    description: Switch to enable/disable ignore CRL Expiration.
    type: bool
  name:
    description: Friendly name of the certificate.
    type: str
  nonAutomaticCRLUpdatePeriod:
    description: Non automatic CRL update period.
    type: int
  nonAutomaticCRLUpdateUnits:
    description: Unit of time of non automatic CRL update.
    type: str
  rejectIfNoStatusFromOCSP:
    description: Switch to reject certificate if there is no status from OCSP.
    type: bool
  rejectIfUnreachableFromOCSP:
    description: Switch to reject certificate if unreachable from OCSP.
    type: bool
  selectedOCSPService:
    description: Name of selected OCSP Service.
    type: str
  status:
    description: Trusted Certificate's status.
    type: str
  trustForCertificateBasedAdminAuth:
    description: Trust for Certificate based Admin authentication.
    type: bool
  trustForCiscoServicesAuth:
    description: Trust for authentication of Cisco Services.
    type: bool
  trustForClientAuth:
    description: Trust for client authentication and Syslog.
    type: bool
  trustForIseAuth:
    description: Trust for authentication within ISE.
    type: bool
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Trusted Certificate reference
  description: Complete reference of the Trusted Certificate object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.trusted_certificate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    authenticateBeforeCRLReceived: true
    automaticCRLUpdate: true
    automaticCRLUpdatePeriod: 0
    automaticCRLUpdateUnits: string
    crlDistributionUrl: string
    crlDownloadFailureRetries: 0
    crlDownloadFailureRetriesUnits: string
    description: string
    downloadCRL: true
    enableOCSPValidation: true
    enableServerIdentityCheck: true
    id: string
    ignoreCRLExpiration: true
    name: string
    nonAutomaticCRLUpdatePeriod: 0
    nonAutomaticCRLUpdateUnits: string
    rejectIfNoStatusFromOCSP: true
    rejectIfUnreachableFromOCSP: true
    selectedOCSPService: string
    status: string
    trustForCertificateBasedAdminAuth: true
    trustForCiscoServicesAuth: true
    trustForClientAuth: true
    trustForIseAuth: true

- name: Delete by id
  cisco.ise.trusted_certificate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "authenticateBeforeCRLReceived": "string",
      "automaticCRLUpdate": "string",
      "automaticCRLUpdatePeriod": "string",
      "automaticCRLUpdateUnits": "string",
      "crlDistributionUrl": "string",
      "crlDownloadFailureRetries": "string",
      "crlDownloadFailureRetriesUnits": "string",
      "description": "string",
      "downloadCRL": "string",
      "enableOCSPValidation": "string",
      "enableServerIdentityCheck": "string",
      "expirationDate": "string",
      "friendlyName": "string",
      "id": "string",
      "ignoreCRLExpiration": "string",
      "internalCA": true,
      "isReferredInPolicy": true,
      "issuedBy": "string",
      "issuedTo": "string",
      "keySize": "string",
      "link": {
        "href": "string",
        "rel": "string",
        "type": "string"
      },
      "nonAutomaticCRLUpdatePeriod": "string",
      "nonAutomaticCRLUpdateUnits": "string",
      "rejectIfNoStatusFromOCSP": "string",
      "rejectIfUnreachableFromOCSP": "string",
      "selectedOCSPService": "string",
      "serialNumberDecimalFormat": "string",
      "sha256Fingerprint": "string",
      "signatureAlgorithm": "string",
      "status": "string",
      "subject": "string",
      "trustedFor": "string",
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
        "message": "string"
      },
      "version": "string"
    }
"""
