#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networkdevice
short_description: Resource module for Networkdevice
description:
  - Manage operation create of the resource Networkdevice.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  NetworkDeviceGroupList:
    description: List of NDG names for this node.
    elements: str
    type: list
  NetworkDeviceIPList:
    description: List of IPSubnets for this node.
    elements: dict
    type: list
  authenticationSettings:
    description: Networkdevice's authenticationSettings.
    suboptions:
      dtlsRequired:
        description: This value enforces use of dtls.
        type: bool
      enableKeyWrap:
        description: EnableKeyWrap flag.
        type: bool
      enableMultiSecret:
        description: EnableMultiSecret flag.
        type: bool
      enabled:
        description: Enabled flag.
        type: bool
      keyEncryptionKey:
        description: Networkdevice's keyEncryptionKey.
        type: str
      keyInputFormat:
        description: Allowed values ASCII,HEXADECIMAL.
        type: dict
      messageAuthenticatorCodeKey:
        description: Networkdevice's messageAuthenticatorCodeKey.
        type: str
      networkProtocol:
        description: Allowed values RADIUS,TACACS_PLUS.
        type: dict
      radiusSharedSecret:
        description: Networkdevice's radiusSharedSecret.
        type: str
      secondRADIUSSharedSecret:
        description: Networkdevice's secondRADIUSSharedSecret.
        type: str
    type: dict
  coaPort:
    description: Since 2.0 (for 3rd party).
    type: float
  description:
    description: Description.
    type: str
  dtlsDnsName:
    description: This value is used to verify the client identity contained in the
      X.509 RADIUS/DTLS client certificate.
    type: str
  id:
    description: Id.
    type: str
  modelName:
    description: Networkdevice's modelName.
    type: str
  name:
    description: Name.
    type: str
  profileName:
    description: Since 2.0 (for 3rd party).
    type: str
  snmpsettings:
    description: Networkdevice's snmpsettings.
    suboptions:
      authPassword:
        description: SNMP Authentication password. Required for snmp version 3 and
          securityLevel AUTH,PRIV.
        type: str
      authProtocol:
        description: SNMP Authentication protocol. Allowed values MD5,SHA,SHA2. Required
          for snmp version 3 and securityLevel AUTH,PRIV.
        type: str
      linkTrapQuery:
        description: SNMP link Trap Query.
        type: bool
      macTrapQuery:
        description: SNMP mac Trap Query.
        type: bool
      originatingPolicyServicesNode:
        description: Originating Policy Services Node.
        type: str
      pollingInterval:
        description: SNMP Polling Interval in seconds (Valid Range 600 to 86400).
        type: dict
      privacyPassword:
        description: SNMP Privacy password. Required for snmp version 3 and securityLevel
          PRIV.
        type: str
      privacyProtocol:
        description: SNMP Privacy protocol. Required for snmp version 3 and securityLevel
          PRIV.
        type: str
      roCommunity:
        description: SNMP RO Community, Required for snmp version 1,2.
        type: str
      securityLevel:
        description: SNMP Security level. Allowed values NO_AUTH,AUTH,PRIV. Required
          for snmp version 3.
        type: str
      username:
        description: Required for snmp version 3.
        type: str
      version:
        description: Allowed values ONE,TWO_C,THREE.
        type: str
    type: dict
  softwareVersion:
    description: Networkdevice's softwareVersion.
    type: str
  tacacsSettings:
    description: Networkdevice's tacacsSettings.
    suboptions:
      connectModeOptions:
        description: Allowed values OFF,ON_LEGACY,ON_DRAFT_COMPLIANT.
        type: dict
      previousSharedSecret:
        description: Retired shared secret.
        type: str
      previousSharedSecretExpiry:
        description: Expiry period for the previous shared secret, given as seconds
          since epoch.
        type: dict
      sharedSecret:
        description: Since 2.0.
        type: str
    type: dict
  tacacsTlsSettings:
    description: Networkdevice's tacacsTlsSettings.
    suboptions:
      connectModeOptions:
        description: Allowed values OFF,ON_DRAFT_COMPLIANT.
        type: dict
      enableSanIpValidation:
        description: Enable SAN IP validation for TACACS+ TLS connections.
        type: bool
      enableTls:
        description: Enable TACACS+ TLS Settings.
        type: bool
      sanValues:
        description: Networkdevice's sanValues.
        suboptions:
          directoryNames:
            description: List of DirectoryNames to be used for validating the Subject
              Alternative Name extension.
            type: list
          dnsNames:
            description: List of dnsNames to be used for validating the Subject Alternative
              Name extension.
            type: list
        type: dict
    type: dict
  trustsecsettings:
    description: Networkdevice's trustsecsettings.
    suboptions:
      deviceAuthenticationSettings:
        description: Networkdevice's deviceAuthenticationSettings.
        suboptions:
          restApiPassword:
            description: Networkdevice's restApiPassword.
            type: str
          restApiUsername:
            description: Networkdevice's restApiUsername.
            type: str
          sgaDeviceId:
            description: Networkdevice's sgaDeviceId.
            type: str
          sgaDevicePassword:
            description: Networkdevice's sgaDevicePassword.
            type: str
        type: dict
      deviceConfigurationDeployment:
        description: Networkdevice's deviceConfigurationDeployment.
        suboptions:
          enableModePassword:
            description: Networkdevice's enableModePassword.
            type: str
          execModePassword:
            description: Networkdevice's execModePassword.
            type: str
          execModeUsername:
            description: Networkdevice's execModeUsername.
            type: str
          includeWhenDeployingSGTUpdates:
            description: Networkdevice's includeWhenDeployingSGTUpdates.
            type: dict
        type: dict
      sgaNotificationAndUpdates:
        description: Networkdevice's sgaNotificationAndUpdates.
        suboptions:
          coaSourceHost:
            description: Must be a node of type Standalone/PPAN/Policy with Session
              services.
            type: str
          downlaodEnvironmentDataEveryXSeconds:
            description: Networkdevice's downlaodEnvironmentDataEveryXSeconds.
            type: dict
          downlaodPeerAuthorizationPolicyEveryXSeconds:
            description: Networkdevice's downlaodPeerAuthorizationPolicyEveryXSeconds.
            type: dict
          downloadSGACLListsEveryXSeconds:
            description: Networkdevice's downloadSGACLListsEveryXSeconds.
            type: dict
          otherSGADevicesToTrustThisDevice:
            description: Networkdevice's otherSGADevicesToTrustThisDevice.
            type: dict
          reAuthenticationEveryXSeconds:
            description: Networkdevice's reAuthenticationEveryXSeconds.
            type: dict
          sendConfigurationToDevice:
            description: Networkdevice's sendConfigurationToDevice.
            type: dict
          sendConfigurationToDeviceUsing:
            description: Allowed values ENABLE,ENABLE_USING_CLI,DISABLE_ALL.
            type: str
        type: dict
    type: dict
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    networkdevice.Networkdevice.create_networkdevice,
  - Paths used are
    post /networkdevice/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.networkdevice:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    NetworkDeviceGroupList:
      - Location#All Locations
      - Device Type#All Device Types
    NetworkDeviceIPList:
      - ipaddress: 1.1.1.1
        mask: 32
    authenticationSettings:
      dtlsRequired: true
      enableKeyWrap: true
      keyEncryptionKey: '1234567890123456'
      keyInputFormat: ASCII
      messageAuthenticatorCodeKey: '12345678901234567890'
      radiusSharedSecret: sharedSecret
    coaPort: 1700
    description: example nd
    dtlsDnsName: ISE213.il.com
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    name: networkDevice1
    profileName: Cisco
    snmpsettings:
      linkTrapQuery: true
      macTrapQuery: true
      originatingPolicyServicesNode: Auto
      pollingInterval: 3600
      roCommunity: aaa
      version: ONE
    tacacsSettings:
      connectModeOptions: ON_LEGACY
      previousSharedSecret: previousSecretSecret
      previousSharedSecretExpiry: 1759562336
      sharedSecret: sharedSecret
    tacacsTlsSettings:
      connectModeOptions: ON_DRAFT_COMPLIANT
      enableSanIpValidation: true
      enableTls: true
      sanValues: {}
    trustsecsettings:
      deviceAuthenticationSettings:
        sgaDeviceId: networkDevice1
        sgaDevicePassword: samplePwd
      deviceConfigurationDeployment:
        enableModePassword: samplePwd
        execModePassword: samplePwd
        execModeUsername: aaa
        includeWhenDeployingSGTUpdates: true
      pushIdSupport: 'false'
      sgaNotificationAndUpdates:
        coaSourceHost: IseNodeName
        downlaodEnvironmentDataEveryXSeconds: 86400
        downlaodPeerAuthorizationPolicyEveryXSeconds: 86400
        downloadSGACLListsEveryXSeconds: 86400
        otherSGADevicesToTrustThisDevice: false
        reAuthenticationEveryXSeconds: 86400
        sendConfigurationToDevice: false
        sendConfigurationToDeviceUsing: ENABLE_USING_COA
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
