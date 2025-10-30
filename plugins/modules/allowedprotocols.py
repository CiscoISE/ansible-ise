#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: allowedprotocols
short_description: Resource module for Allowedprotocols
description:
  - Manage operation create of the resource Allowedprotocols.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
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
    description: Description.
    type: str
  displayAdditionalTLSParams:
    description: DisplayAdditionalTLSParams flag.
    type: bool
  eapFast:
    description: Allowedprotocols's eapFast.
    suboptions:
      allowEapFastEapGtc:
        description: AllowEapFastEapGtc flag.
        type: bool
      allowEapFastEapGtcPwdChange:
        description: The allowEapFastEapGtcPwdChange is required only if allowEapFastEapGtc
          is true, otherwise it must be ignored.
        type: bool
      allowEapFastEapGtcPwdChangeRetries:
        description: The allowEapFastEapGtcPwdChangeRetries is required only if allowEapFastEapGtc
          is true, otherwise it must be ignored. Valid range is 0-3.
        type: dict
      allowEapFastEapMsChapV2:
        description: AllowEapFastEapMsChapV2 flag.
        type: bool
      allowEapFastEapMsChapV2PwdChange:
        description: The allowEapFastEapMsChapV2PwdChange is required only if allowEapFastEapMsChapV2
          is true, otherwise it must be ignored.
        type: bool
      allowEapFastEapMsChapV2PwdChangeRetries:
        description: The allowEapFastEapMsChapV2PwdChangeRetries is required only
          if eapTtlsEapMsChapV2 is true, otherwise it must be ignored. Valid range
          is 0-3.
        type: dict
      allowEapFastEapTls:
        description: AllowEapFastEapTls flag.
        type: bool
      allowEapFastEapTlsAuthOfExpiredCerts:
        description: The allowEapFastEapTlsAuthOfExpiredCerts is required only if
          allowEapFastEapTls is true, otherwise it must be ignored.
        type: bool
      eapFastDontUsePacsAcceptClientCert:
        description: The eapFastDontUsePacsAcceptClientCert is required only if eapFastUsePacs
          is FALSE, otherwise it must be ignored.
        type: bool
      eapFastDontUsePacsAllowMachineAuthentication:
        description: The eapFastDontUsePacsAllowMachineAuthentication is required
          only if eapFastUsePacs is FALSE, otherwise it must be ignored.
        type: bool
      eapFastEnableEAPChaining:
        description: EapFastEnableEAPChaining flag.
        type: bool
      eapFastUsePacs:
        description: EapFastUsePacs flag.
        type: bool
      eapFastUsePacsAcceptClientCert:
        description: The eapFastUsePacsAcceptClientCert is required only if eapFastUsePacsAllowAuthenProvisioning
          is true, otherwise it must be ignored.
        type: bool
      eapFastUsePacsAllowAnonymProvisioning:
        description: The eapFastUsePacsAllowAnonymProvisioning is required only if
          eapFastUsePacs is true, otherwise it must be ignored.
        type: bool
      eapFastUsePacsAllowAuthenProvisioning:
        description: The eapFastUsePacsAllowAuthenProvisioning is required only if
          eapFastUsePacs is true, otherwise it must be ignored.
        type: bool
      eapFastUsePacsAllowMachineAuthentication:
        description: The eapFastUsePacsAllowMachineAuthentication is required only
          if eapFastUsePacs is true, otherwise it must be ignored.
        type: bool
      eapFastUsePacsAuthorizationPacTtl:
        description: The eapFastUsePacsAuthorizationPacTtl is required only if eapFastUsePacsStatelessSessionResume
          is true, otherwise it must be ignored.
        type: dict
      eapFastUsePacsAuthorizationPacTtlUnits:
        description: The eapFastUsePacsAuthorizationPacTtlUnits is required only if
          eapFastUsePacsStatelessSessionResume is true, otherwise it must be ignored.
          Allowed Values SECONDS, MINUTES, HOURS, DAYS, WEEKS.
        type: str
      eapFastUsePacsMachinePacTtl:
        description: The eapFastUsePacsMachinePacTtl is required only if eapFastUsePacsAllowMachineAuthentication
          is true, otherwise it must be ignored.
        type: dict
      eapFastUsePacsMachinePacTtlUnits:
        description: The eapFastUsePacsMachinePacTtlUnits is required only if eapFastUsePacsAllowMachineAuthentication
          is true, otherwise it must be ignored. Allowed Values SECONDS, MINUTES,
          HOURS, DAYS, WEEKS.
        type: str
      eapFastUsePacsServerReturns:
        description: The eapFastUsePacsServerReturns is required only if eapFastUsePacsAllowAuthenProvisioning
          is true, otherwise it must be ignored.
        type: bool
      eapFastUsePacsStatelessSessionResume:
        description: The eapFastUsePacsStatelessSessionResume is required only if
          eapFastUsePacs is true, otherwise it must be ignored.
        type: bool
      eapFastUsePacsTunnelPacTtl:
        description: The eapFastUsePacsTunnelPacTtl is required only if eapFastUsePacs
          is true, otherwise it must be ignored.
        type: dict
      eapFastUsePacsTunnelPacTtlUnits:
        description: The eapFastUsePacsTunnelPacTtlUnits is required only if eapFastUsePacs
          is true, otherwise it must be ignored. Allowed Values SECONDS, MINUTES,
          HOURS, DAYS, WEEKS.
        type: str
      eapFastUsePacsUseProactivePacUpdatePrecentage:
        description: The eapFastUsePacsUseProactivePacUpdatePrecentage is required
          only if eapFastUsePacs is true, otherwise it must be ignored.
        type: dict
    type: dict
  eapTls:
    description: Allowedprotocols's eapTls.
    suboptions:
      allowEapTlsAuthOfExpiredCerts:
        description: AllowEapTlsAuthOfExpiredCerts flag.
        type: bool
      eapTlsEnableStatelessSessionResume:
        description: EapTlsEnableStatelessSessionResume flag.
        type: bool
      eapTlsSessionTicketPrecentage:
        description: The eapTlsSessionTicketPrecentage is required only if eapTlsEnableStatelessSessionResume
          is true, otherwise it must be ignored.
        type: dict
      eapTlsSessionTicketTtl:
        description: Time to live. The eapTlsSessionTicketTtl is required only if
          eapTlsEnableStatelessSessionResume is true, otherwise it must be ignored.
        type: dict
      eapTlsSessionTicketTtlUnits:
        description: Time to live time units. The eapTlsSessionTicketTtlUnits is required
          only if eapTlsEnableStatelessSessionResume is true, otherwise it must be
          ignored. Allowed Values SECONDS, MINUTES, HOURS, DAYS, WEEKS.
        type: dict
    type: dict
  eapTlsLBit:
    description: EapTlsLBit flag.
    type: bool
  eapTtls:
    description: Allowedprotocols's eapTtls.
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
        description: The eapTtlsEapMsChapV2PwdChange is required only if eapTtlsEapMsChapV2
          is true, otherwise it must be ignored.
        type: bool
      eapTtlsEapMsChapV2PwdChangeRetries:
        description: The eapTtlsEapMsChapV2PwdChangeRetries is required only if eapTtlsEapMsChapV2
          is true, otherwise it must be ignored. Valid range is 0-3.
        type: dict
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
  fiveG:
    description: FiveG flag.
    type: bool
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  peap:
    description: Allowedprotocols's peap.
    suboptions:
      allowPeapEapGtc:
        description: AllowPeapEapGtc flag.
        type: bool
      allowPeapEapGtcPwdChange:
        description: The allowPeapEapGtcPwdChange is required only if allowPeapEapGtc
          is true, otherwise it must be ignored.
        type: bool
      allowPeapEapGtcPwdChangeRetries:
        description: The allowPeapEapGtcPwdChangeRetries is required only if allowPeapEapGtc
          is true, otherwise it must be ignored. Valid range is 0-3.
        type: dict
      allowPeapEapMsChapV2:
        description: AllowPeapEapMsChapV2 flag.
        type: bool
      allowPeapEapMsChapV2PwdChange:
        description: The allowPeapEapMsChapV2PwdChange is required only if allowPeapEapMsChapV2
          is true, otherwise it must be ignored.
        type: bool
      allowPeapEapMsChapV2PwdChangeRetries:
        description: The allowPeapEapMsChapV2PwdChangeRetries is required only if
          allowPeapEapMsChapV2 is true, otherwise it must be ignored. Valid range
          is 0-3.
        type: dict
      allowPeapEapTls:
        description: AllowPeapEapTls flag.
        type: bool
      allowPeapEapTlsAuthOfExpiredCerts:
        description: The allowPeapEapTlsAuthOfExpiredCerts is required only if allowPeapEapTls
          is true, otherwise it must be ignored.
        type: bool
      allowPeapV0:
        description: AllowPeapV0 flag.
        type: bool
      requireCryptobinding:
        description: RequireCryptobinding flag.
        type: bool
    type: dict
  preferredEapProtocol:
    description: The preferredEapProtocol is required only if allowPreferredEapProtocol
      is true, otherwise it must be ignored. Allowed Values EAP_FAST, PEAP, LEAP,
      EAP_MD5, EAP_TLS, EAP_TTLS, TEAP.
    type: str
  processHostLookup:
    description: ProcessHostLookup flag.
    type: bool
  requireMessageAuth:
    description: RequireMessageAuth flag.
    type: bool
  rsaPss:
    description: RsaPss flag.
    type: bool
  teap:
    description: Allowedprotocols's teap.
    suboptions:
      acceptClientCertDuringTunnelEst:
        description: AcceptClientCertDuringTunnelEst flag.
        type: bool
      allowDowngradeMsk:
        description: AllowDowngradeMsk flag.
        type: bool
      allowTeapEapMsChapV2:
        description: AllowTeapEapMsChapV2 flag.
        type: bool
      allowTeapEapMsChapV2PwdChange:
        description: The allowTeapEapMsChapV2PwdChange is required only if allowTeapEapMsChapV2
          is true, otherwise it must be ignored.
        type: bool
      allowTeapEapMsChapV2PwdChangeRetries:
        description: The allowTeapEapMsChapV2PwdChangeRetries is required only if
          allowTeapEapMsChapV2 is true, otherwise it must be ignored. Valid range
          is 0-3.
        type: dict
      allowTeapEapTls:
        description: AllowTeapEapTls flag.
        type: bool
      allowTeapEapTlsAuthOfExpiredCerts:
        description: The allowTeapEapTlsAuthOfExpiredCerts is required only if allowTeapEapTls
          is true, otherwise it must be ignored.
        type: bool
      enableEapChaining:
        description: EnableEapChaining flag.
        type: bool
    type: dict
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    allowedprotocols.Allowedprotocols.create_allowedprotocols,
  - Paths used are
    post /allowedprotocols/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.allowedprotocols:
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
    displayAdditionalTLSParams: false
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
    fiveG: false
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
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
    rsaPss: false
    teap:
      acceptClientCertDuringTunnelEst: true
      allowDowngradeMsk: true
      allowTeapEapMsChapV2: true
      allowTeapEapMsChapV2PwdChange: true
      allowTeapEapMsChapV2PwdChangeRetries: 3
      allowTeapEapTls: true
      allowTeapEapTlsAuthOfExpiredCerts: false
      enableEapChaining: false
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
        "description": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""
