#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: allowed_protocols
short_description: Resource module for Allowed Protocols
description:
- Manage operations create, update and delete of the resource Allowed Protocols.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  allowChap:
    description: AllowChap flag.
    type: bool
  allowEapFast:
    description: AllowEapFast flag.
    type: bool
  allowEapMd5:
    description: AllowEapMd5 flag.
    type: bool
  allowEapTls:
    description: AllowEapTls flag.
    type: bool
  allowEapTtls:
    description: AllowEapTtls flag.
    type: bool
  allowLeap:
    description: AllowLeap flag.
    type: bool
  allowMsChapV1:
    description: AllowMsChapV1 flag.
    type: bool
  allowMsChapV2:
    description: AllowMsChapV2 flag.
    type: bool
  allowPapAscii:
    description: AllowPapAscii flag.
    type: bool
  allowPeap:
    description: AllowPeap flag.
    type: bool
  allowPreferredEapProtocol:
    description: AllowPreferredEapProtocol flag.
    type: bool
  allowTeap:
    description: AllowTeap flag.
    type: bool
  allowWeakCiphersForEap:
    description: AllowWeakCiphersForEap flag.
    type: bool
  description:
    description: Allowed Protocols's description.
    type: str
  eapFast:
    description: Allowed Protocols's eapFast.
    suboptions:
      allowEapFastEapGtc:
        description: AllowEapFastEapGtc flag.
        type: bool
      allowEapFastEapGtcPwdChange:
        description: AllowEapFastEapGtcPwdChange flag.
        type: bool
      allowEapFastEapGtcPwdChangeRetries:
        description: Allowed Protocols's allowEapFastEapGtcPwdChangeRetries.
        type: int
      allowEapFastEapMsChapV2:
        description: AllowEapFastEapMsChapV2 flag.
        type: bool
      allowEapFastEapMsChapV2PwdChange:
        description: AllowEapFastEapMsChapV2PwdChange flag.
        type: bool
      allowEapFastEapMsChapV2PwdChangeRetries:
        description: Allowed Protocols's allowEapFastEapMsChapV2PwdChangeRetries.
        type: int
      allowEapFastEapTls:
        description: AllowEapFastEapTls flag.
        type: bool
      allowEapFastEapTlsAuthOfExpiredCerts:
        description: AllowEapFastEapTlsAuthOfExpiredCerts flag.
        type: bool
      eapFastEnableEAPChaining:
        description: EapFastEnableEAPChaining flag.
        type: bool
      eapFastUsePacs:
        description: EapFastUsePacs flag.
        type: bool
      eapFastUsePacsAllowAnonymProvisioning:
        description: EapFastUsePacsAllowAnonymProvisioning flag.
        type: bool
      eapFastUsePacsAllowAuthenProvisioning:
        description: EapFastUsePacsAllowAuthenProvisioning flag.
        type: bool
      eapFastUsePacsAllowMachineAuthentication:
        description: EapFastUsePacsAllowMachineAuthentication flag.
        type: bool
      eapFastUsePacsStatelessSessionResume:
        description: EapFastUsePacsStatelessSessionResume flag.
        type: bool
      eapFastUsePacsTunnelPacTtl:
        description: Allowed Protocols's eapFastUsePacsTunnelPacTtl.
        type: int
      eapFastUsePacsTunnelPacTtlUnits:
        description: Allowed Protocols's eapFastUsePacsTunnelPacTtlUnits.
        type: str
      eapFastUsePacsUseProactivePacUpdatePrecentage:
        description: Allowed Protocols's eapFastUsePacsUseProactivePacUpdatePrecentage.
        type: int
    type: dict
  eapTls:
    description: Allowed Protocols's eapTls.
    suboptions:
      allowEapTlsAuthOfExpiredCerts:
        description: AllowEapTlsAuthOfExpiredCerts flag.
        type: bool
      eapTlsEnableStatelessSessionResume:
        description: EapTlsEnableStatelessSessionResume flag.
        type: bool
    type: dict
  eapTlsLBit:
    description: EapTlsLBit flag.
    type: bool
  eapTtls:
    description: Allowed Protocols's eapTtls.
    suboptions:
      eapTtlsChap:
        description: EapTtlsChap flag.
        type: bool
      eapTtlsEapMd5:
        description: EapTtlsEapMd5 flag.
        type: bool
      eapTtlsEapMsChapV2:
        description: EapTtlsEapMsChapV2 flag.
        type: bool
      eapTtlsEapMsChapV2PwdChange:
        description: EapTtlsEapMsChapV2PwdChange flag.
        type: bool
      eapTtlsEapMsChapV2PwdChangeRetries:
        description: Allowed Protocols's eapTtlsEapMsChapV2PwdChangeRetries.
        type: int
      eapTtlsMsChapV1:
        description: EapTtlsMsChapV1 flag.
        type: bool
      eapTtlsMsChapV2:
        description: EapTtlsMsChapV2 flag.
        type: bool
      eapTtlsPapAscii:
        description: EapTtlsPapAscii flag.
        type: bool
    type: dict
  id:
    description: Id path parameter.
    type: str
  name:
    description: Allowed Protocols's name.
    type: str
  peap:
    description: Allowed Protocols's peap.
    suboptions:
      allowPeapEapGtc:
        description: AllowPeapEapGtc flag.
        type: bool
      allowPeapEapMsChapV2:
        description: AllowPeapEapMsChapV2 flag.
        type: bool
      allowPeapEapMsChapV2PwdChange:
        description: AllowPeapEapMsChapV2PwdChange flag.
        type: bool
      allowPeapEapMsChapV2PwdChangeRetries:
        description: Allowed Protocols's allowPeapEapMsChapV2PwdChangeRetries.
        type: int
      allowPeapEapTls:
        description: AllowPeapEapTls flag.
        type: bool
      allowPeapEapTlsAuthOfExpiredCerts:
        description: AllowPeapEapTlsAuthOfExpiredCerts flag.
        type: bool
      allowPeapV0:
        description: AllowPeapV0 flag.
        type: bool
      requireCryptobinding:
        description: RequireCryptobinding flag.
        type: bool
    type: dict
  preferredEapProtocol:
    description: Allowed Protocols's preferredEapProtocol.
    type: str
  processHostLookup:
    description: ProcessHostLookup flag.
    type: bool
  requireMessageAuth:
    description: RequireMessageAuth flag.
    type: bool
  teap:
    description: Allowed Protocols's teap.
    suboptions:
      acceptClientCertDuringTunnelEst:
        description: AcceptClientCertDuringTunnelEst flag.
        type: bool
      allowTeapEapMsChapV2:
        description: AllowTeapEapMsChapV2 flag.
        type: bool
      allowTeapEapMsChapV2PwdChange:
        description: AllowTeapEapMsChapV2PwdChange flag.
        type: bool
      allowTeapEapMsChapV2PwdChangeRetries:
        description: Allowed Protocols's allowTeapEapMsChapV2PwdChangeRetries.
        type: int
      allowTeapEapTls:
        description: AllowTeapEapTls flag.
        type: bool
      allowTeapEapTlsAuthOfExpiredCerts:
        description: AllowTeapEapTlsAuthOfExpiredCerts flag.
        type: bool
      enableEapChaining:
        description: EnableEapChaining flag.
        type: bool
      requestBasicPwdAuth:
        description: RequestBasicPwdAuth flag.
        type: bool
    type: dict
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.allowed_protocols
# Reference by Internet resource
- name: Allowed Protocols reference
  description: Complete reference of the Allowed Protocols object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.allowed_protocols:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowChap: false
    allowEapFast: true
    allowEapMd5: true
    allowEapTls: true
    allowEapTtls: true
    allowLeap: false
    allowMsChapV1: false
    allowMsChapV2: false
    allowPapAscii: true
    allowPeap: true
    allowPreferredEapProtocol: true
    allowTeap: true
    allowWeakCiphersForEap: false
    description: example allowed protocols
    eapFast:
      allowEapFastEapGtc: true
      allowEapFastEapGtcPwdChange: true
      allowEapFastEapGtcPwdChangeRetries: 1
      allowEapFastEapMsChapV2: true
      allowEapFastEapMsChapV2PwdChange: true
      allowEapFastEapMsChapV2PwdChangeRetries: 1
      allowEapFastEapTls: true
      allowEapFastEapTlsAuthOfExpiredCerts: false
      eapFastEnableEAPChaining: false
      eapFastUsePacs: true
      eapFastUsePacsAllowAnonymProvisioning: false
      eapFastUsePacsAllowAuthenProvisioning: false
      eapFastUsePacsAllowMachineAuthentication: false
      eapFastUsePacsStatelessSessionResume: false
      eapFastUsePacsTunnelPacTtl: 7776000
      eapFastUsePacsTunnelPacTtlUnits: SECONDS
      eapFastUsePacsUseProactivePacUpdatePrecentage: 10
    eapTls:
      allowEapTlsAuthOfExpiredCerts: false
      eapTlsEnableStatelessSessionResume: false
    eapTlsLBit: false
    eapTtls:
      eapTtlsChap: true
      eapTtlsEapMd5: true
      eapTtlsEapMsChapV2: true
      eapTtlsEapMsChapV2PwdChange: true
      eapTtlsEapMsChapV2PwdChangeRetries: 1
      eapTtlsMsChapV1: true
      eapTtlsMsChapV2: true
      eapTtlsPapAscii: true
    name: allowedprotocols1
    peap:
      allowPeapEapGtc: false
      allowPeapEapMsChapV2: true
      allowPeapEapMsChapV2PwdChange: true
      allowPeapEapMsChapV2PwdChangeRetries: 1
      allowPeapEapTls: true
      allowPeapEapTlsAuthOfExpiredCerts: false
      allowPeapV0: false
      requireCryptobinding: false
    preferredEapProtocol: PEAP
    processHostLookup: true
    requireMessageAuth: false
    teap:
      acceptClientCertDuringTunnelEst: true
      allowTeapEapMsChapV2: true
      allowTeapEapMsChapV2PwdChange: true
      allowTeapEapMsChapV2PwdChangeRetries: 3
      allowTeapEapTls: true
      allowTeapEapTlsAuthOfExpiredCerts: false
      enableEapChaining: false
      requestBasicPwdAuth: false

- name: Update by id
  cisco.ise.allowed_protocols:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowChap: false
    allowEapFast: true
    allowEapMd5: true
    allowEapTls: true
    allowEapTtls: true
    allowLeap: false
    allowMsChapV1: false
    allowMsChapV2: false
    allowPapAscii: true
    allowPeap: true
    allowPreferredEapProtocol: true
    allowTeap: true
    allowWeakCiphersForEap: false
    description: example allowed protocols
    eapFast:
      allowEapFastEapGtc: true
      allowEapFastEapGtcPwdChange: true
      allowEapFastEapGtcPwdChangeRetries: 1
      allowEapFastEapMsChapV2: true
      allowEapFastEapMsChapV2PwdChange: true
      allowEapFastEapMsChapV2PwdChangeRetries: 1
      allowEapFastEapTls: true
      allowEapFastEapTlsAuthOfExpiredCerts: false
      eapFastEnableEAPChaining: false
      eapFastUsePacs: true
      eapFastUsePacsAllowAnonymProvisioning: false
      eapFastUsePacsAllowAuthenProvisioning: false
      eapFastUsePacsAllowMachineAuthentication: false
      eapFastUsePacsStatelessSessionResume: false
      eapFastUsePacsTunnelPacTtl: 7776000
      eapFastUsePacsTunnelPacTtlUnits: SECONDS
      eapFastUsePacsUseProactivePacUpdatePrecentage: 10
    eapTls:
      allowEapTlsAuthOfExpiredCerts: false
      eapTlsEnableStatelessSessionResume: false
    eapTlsLBit: false
    eapTtls:
      eapTtlsChap: true
      eapTtlsEapMd5: true
      eapTtlsEapMsChapV2: true
      eapTtlsEapMsChapV2PwdChange: true
      eapTtlsEapMsChapV2PwdChangeRetries: 1
      eapTtlsMsChapV1: true
      eapTtlsMsChapV2: true
      eapTtlsPapAscii: true
    id: string
    name: allowedprotocols1
    peap:
      allowPeapEapGtc: false
      allowPeapEapMsChapV2: true
      allowPeapEapMsChapV2PwdChange: true
      allowPeapEapMsChapV2PwdChangeRetries: 1
      allowPeapEapTls: true
      allowPeapEapTlsAuthOfExpiredCerts: false
      allowPeapV0: false
      requireCryptobinding: false
    preferredEapProtocol: PEAP
    processHostLookup: true
    requireMessageAuth: false
    teap:
      acceptClientCertDuringTunnelEst: true
      allowTeapEapMsChapV2: true
      allowTeapEapMsChapV2PwdChange: true
      allowTeapEapMsChapV2PwdChangeRetries: 3
      allowTeapEapTls: true
      allowTeapEapTlsAuthOfExpiredCerts: false
      enableEapChaining: false
      requestBasicPwdAuth: false

- name: Delete by id
  cisco.ise.allowed_protocols:
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
    {}
"""
