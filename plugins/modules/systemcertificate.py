#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: systemcertificate
short_description: Resource module for Systemcertificate
description:
- Manage operation create of the resource Systemcertificate.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description.
    type: str
  ersLocalCertStub:
    description: Systemcertificate's ersLocalCertStub.
    suboptions:
      allowWildcardCerts:
        description: AllowWildcardCerts.
        type: str
      certificatePolicies:
        description: CertificatePolicies.
        type: str
      certificateSanDns:
        description: CertificateSanDns.
        type: str
      certificateSanIp:
        description: CertificateSanIp.
        type: str
      certificateSanUri:
        description: CertificateSanUri.
        type: str
      digest:
        description: Digest.
        type: str
      expirationTTL:
        description: ExpirationTTL.
        type: str
      friendlyName:
        description: FriendlyName.
        type: str
      groupTagDD:
        description: GroupTagDD.
        type: str
      keyLength:
        description: KeyLength.
        type: str
      keyType:
        description: KeyType.
        type: str
      samlCertificate:
        description: SamlCertificate.
        type: str
      selectedExpirationTTLUnit:
        description: SelectedExpirationTTLUnit.
        type: str
      subjectStub:
        description: Systemcertificate's subjectStub.
        suboptions:
          commonName:
            description: Common name.
            type: str
          countryName:
            description: CountryName.
            type: str
          localityName:
            description: LocalityName.
            type: str
          organizationName:
            description: OrganizationName.
            type: str
          organizationalUnitName:
            description: Organizational UnitName.
            type: str
          stateOrProvinceName:
            description: StateOrProvinceName.
            type: str
        type: dict
      xgridCertificate:
        description: XgridCertificate.
        type: str
    type: dict
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  nodeId:
    description: NodeId of ISE application.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    systemcertificate.Systemcertificate.create_systemcertificate,

  - Paths used are
    post /systemcertificate/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.systemcertificate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    ersLocalCertStub:
      allowWildcardCerts: on OR off
      certificatePolicies: certificate policies
      certificateSanDns: cisco.com
      certificateSanIp: <<IP-ADDRESS>>
      certificateSanUri: <<URI>>
      digest: SHA-256 OR SHA-384 OR SHA-512
      ersSubjectStub:
        commonName: $FQDN$
        countryName: Country
        localityName: City
        organizationName: HCL
        organizationalUnitName: HCL-SAMLCert
        stateOrProvinceName: State
      expirationTTL: '2'
      friendlyName: HCL
      groupTagDD: add-group-tag
      keyLength: 512 OR 1024 OR 2048 OR 4096
      keyType: RSA OR ECDSA
      samlCertificate: on OR off
      selectedExpirationTTLUnit: days OR weeks OR months OR years
      xgridCertificate: on OR off
    nodeId: ISE-01

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "operation": "string",
      "messages": [
        {
          "title": "string",
          "type": "string",
          "code": "string"
        }
      ]
    }
"""
