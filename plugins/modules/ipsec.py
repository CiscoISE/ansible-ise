#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: ipsec
short_description: Resource module for Ipsec
description:
  - Manage operations create and update of the resource Ipsec.
  - Creates an IPsec connection.
  - Updates the configuration of existing IPsec connection.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  authType:
    description: Authentication type for establishing connection.
    type: str
  certId:
    description: ID of the certificate for establishing connection.
    type: str
  configureVti:
    description: Authentication type for establishing connection.
    type: bool
  espAhProtocol:
    description: Encryption protocol used for establishing connection.
    type: str
  hostName:
    description: Hostname of the node.
    type: str
  iface:
    description: Ethernet port of the node.
    type: str
  ikeReAuthTime:
    description: IKE re-authentication time.
    type: int
  ikeVersion:
    description: IKE version.
    type: str
  localInternalIp:
    description: Local Tunnel IP address.
    type: str
  modeOption:
    description: The Mode type used for establishing the connection.
    type: str
  nadIp:
    description: NAD IP address for establishing connection.
    type: str
  phaseOneDHGroup:
    description: Phase-one DH group used for establishing connection.
    type: str
  phaseOneEncryptionAlgo:
    description: Phase-one encryption algorithm used for establishing connection.
    type: str
  phaseOneHashAlgo:
    description: Phase-one hashing algorithm used for establishing connection.
    type: str
  phaseOneLifeTime:
    description: Phase-one connection lifetime.
    type: int
  phaseTwoDHGroup:
    description: Phase-two DH group used for establishing connection.
    type: str
  phaseTwoEncryptionAlgo:
    description: Phase-two encryption algorithm used for establishing connection.
    type: str
  phaseTwoHashAlgo:
    description: Phase-two hashing algorithm used for establishing connection.
    type: str
  phaseTwoLifeTime:
    description: Phase-two connection lifetime.
    type: int
  psk:
    description: Pre-shared key used for establishing connection.
    type: str
  remotePeerInternalIp:
    description: Remote Tunnel IP address.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    native_ipsec.NativeIpsec.create_ipsec_connection,
    native_ipsec.NativeIpsec.update_ipsec_connection_config,
  - Paths used are
    post /api/v1/ipsec,
    put /api/v1/ipsec,
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.ipsec:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    authType: string
    certId: string
    configureVti: true
    espAhProtocol: string
    hostName: string
    iface: string
    ikeReAuthTime: 0
    ikeVersion: string
    localInternalIp: string
    modeOption: string
    nadIp: string
    phaseOneDHGroup: string
    phaseOneEncryptionAlgo: string
    phaseOneHashAlgo: string
    phaseOneLifeTime: 0
    phaseTwoDHGroup: string
    phaseTwoEncryptionAlgo: string
    phaseTwoHashAlgo: string
    phaseTwoLifeTime: 0
    psk: string
    remotePeerInternalIp: string
- name: Create
  cisco.ise.ipsec:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    authType: string
    certId: string
    configureVti: true
    espAhProtocol: string
    hostName: string
    iface: string
    ikeReAuthTime: 0
    ikeVersion: string
    localInternalIp: string
    modeOption: string
    nadIp: string
    phaseOneDHGroup: string
    phaseOneEncryptionAlgo: string
    phaseOneHashAlgo: string
    phaseOneLifeTime: 0
    phaseTwoDHGroup: string
    phaseTwoEncryptionAlgo: string
    phaseTwoHashAlgo: string
    phaseTwoLifeTime: 0
    psk: string
    remotePeerInternalIp: string
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
        "authType": "string",
        "certId": "string",
        "configureVti": true,
        "createTime": "string",
        "espAhProtocol": "string",
        "hostName": "string",
        "id": "string",
        "iface": "string",
        "ikeReAuthTime": 0,
        "ikeVersion": "string",
        "localInternalIp": "string",
        "modeOption": "string",
        "nadIp": "string",
        "phaseOneDHGroup": "string",
        "phaseOneEncryptionAlgo": "string",
        "phaseOneHashAlgo": "string",
        "phaseOneLifeTime": 0,
        "phaseTwoDHGroup": "string",
        "phaseTwoEncryptionAlgo": "string",
        "phaseTwoHashAlgo": "string",
        "phaseTwoLifeTime": 0,
        "psk": "string",
        "remotePeerInternalIp": "string",
        "status": "string",
        "updateTime": "string"
      }
    ]
ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: dict
  sample: >
    {
      "response": {
        "authType": "string",
        "certId": "string",
        "configureVti": true,
        "createTime": "string",
        "espAhProtocol": "string",
        "hostName": "string",
        "id": "string",
        "iface": "string",
        "ikeReAuthTime": 0,
        "ikeVersion": "string",
        "link": {
          "href": "string",
          "rel": "string",
          "type": "string"
        },
        "localInternalIp": "string",
        "modeOption": "string",
        "nadIp": "string",
        "phaseOneDHGroup": "string",
        "phaseOneEncryptionAlgo": "string",
        "phaseOneHashAlgo": "string",
        "phaseOneLifeTime": 0,
        "phaseTwoDHGroup": "string",
        "phaseTwoEncryptionAlgo": "string",
        "phaseTwoHashAlgo": "string",
        "phaseTwoLifeTime": 0,
        "psk": "string",
        "remotePeerInternalIp": "string",
        "status": "string",
        "updateTime": "string"
      },
      "version": "string"
    }
"""
