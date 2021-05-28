#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device
short_description: Resource module for Network Device
description:
- Manage operations create, update and delete of the resource Network Device.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  NetworkDeviceGroupList:
    description: Network Device's NetworkDeviceGroupList.
    elements: str
    type: list
  NetworkDeviceIPList:
    description: Network Device's NetworkDeviceIPList.
    suboptions:
      ipaddress:
        description: Network Device's ipaddress.
        type: str
      mask:
        description: Network Device's mask.
        type: int
    type: list
  authenticationSettings:
    description: Network Device's authenticationSettings.
    suboptions:
      dtlsRequired:
        description: DtlsRequired flag.
        type: bool
      enableKeyWrap:
        description: EnableKeyWrap flag.
        type: bool
      enableMultiSecret:
        description: Network Device's enableMultiSecret.
        type: str
      keyEncryptionKey:
        description: Network Device's keyEncryptionKey.
        type: str
      keyInputFormat:
        description: Network Device's keyInputFormat.
        type: str
      messageAuthenticatorCodeKey:
        description: Network Device's messageAuthenticatorCodeKey.
        type: str
      networkProtocol:
        description: Network Device's networkProtocol.
        type: str
      radiusSharedSecret:
        description: Network Device's radiusSharedSecret.
        type: str
    type: dict
  coaPort:
    description: Network Device's coaPort.
    type: int
  description:
    description: Network Device's description.
    type: str
  dtlsDnsName:
    description: Network Device's dtlsDnsName.
    type: str
  id:
    description: Id path parameter.
    type: str
  name:
    description: Network Device's name.
    type: str
  profileName:
    description: Network Device's profileName.
    type: str
  snmpsettings:
    description: Network Device's snmpsettings.
    suboptions:
      authPassowrd:
        description: Network Device's authPassowrd.
        type: str
      linkTrapQuery:
        description: LinkTrapQuery flag.
        type: bool
      macTrapQuery:
        description: MacTrapQuery flag.
        type: bool
      originatingPolicyServicesNode:
        description: Network Device's originatingPolicyServicesNode.
        type: str
      pollingInterval:
        description: Network Device's pollingInterval.
        type: int
      privacyPassowrd:
        description: Network Device's privacyPassowrd.
        type: str
      roCommunity:
        description: Network Device's roCommunity.
        type: str
      version:
        description: Network Device's version.
        type: str
    type: dict
  tacacsSettings:
    description: Network Device's tacacsSettings.
    suboptions:
      connectModeOptions:
        description: Network Device's connectModeOptions.
        type: str
      sharedSecret:
        description: Network Device's sharedSecret.
        type: str
    type: dict
  trustsecsettings:
    description: Network Device's trustsecsettings.
    suboptions:
      deviceAuthenticationSettings:
        description: Network Device's deviceAuthenticationSettings.
        suboptions:
          sgaDeviceId:
            description: Network Device's sgaDeviceId.
            type: str
          sgaDevicePassword:
            description: Network Device's sgaDevicePassword.
            type: str
        type: dict
      deviceConfigurationDeployment:
        description: Network Device's deviceConfigurationDeployment.
        suboptions:
          enableModePassword:
            description: Network Device's enableModePassword.
            type: str
          execModePassword:
            description: Network Device's execModePassword.
            type: str
          includeWhenDeployingSGTUpdates:
            description: IncludeWhenDeployingSGTUpdates flag.
            type: bool
        type: dict
      pushIdSupport:
        description: Network Device's pushIdSupport.
        type: str
      sgaNotificationAndUpdates:
        description: Network Device's sgaNotificationAndUpdates.
        suboptions:
          coaSourceHost:
            description: Network Device's coaSourceHost.
            type: str
          downlaodEnvironmentDataEveryXSeconds:
            description: Network Device's downlaodEnvironmentDataEveryXSeconds.
            type: int
          downlaodPeerAuthorizationPolicyEveryXSeconds:
            description: Network Device's downlaodPeerAuthorizationPolicyEveryXSeconds.
            type: int
          downloadSGACLListsEveryXSeconds:
            description: Network Device's downloadSGACLListsEveryXSeconds.
            type: int
          otherSGADevicesToTrustThisDevice:
            description: OtherSGADevicesToTrustThisDevice flag.
            type: bool
          reAuthenticationEveryXSeconds:
            description: Network Device's reAuthenticationEveryXSeconds.
            type: int
          sendConfigurationToDevice:
            description: SendConfigurationToDevice flag.
            type: bool
          sendConfigurationToDeviceUsing:
            description: Network Device's sendConfigurationToDeviceUsing.
            type: str
        type: dict
    type: dict
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_device
# Reference by Internet resource
- name: Network Device reference
  description: Complete reference of the Network Device object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.network_device:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    NetworkDeviceGroupList:
    - Location#All Locations
    - IPSEC#Is IPSEC Device#No
    - Device Type#All Device Types
    NetworkDeviceIPList:
    - ipaddress: 1.2.3.4
      mask: 32
    authenticationSettings:
      networkProtocol: RADIUS
      radiusSharedSecret: C1sco12345
    description: ''
    name: nad
    tacacsSettings:
      connectModeOptions: false
      sharedSecret: C1sco12345

- name: Update by id
  cisco.ise.network_device:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    NetworkDeviceGroupList:
    - Location#All Locations
    - IPSEC#Is IPSEC Device#No
    - Device Type#All Device Types
    NetworkDeviceIPList:
    - ipaddress: 1.2.3.4
      mask: 32
    authenticationSettings:
      networkProtocol: RADIUS
      radiusSharedSecret: C1sco12345
    description: ''
    id: string
    name: nad
    tacacsSettings:
      connectModeOptions: false
      sharedSecret: C1sco12345

- name: Delete by id
  cisco.ise.network_device:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Update by name
  cisco.ise.network_device:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    NetworkDeviceGroupList:
    - Location#All Locations
    - IPSEC#Is IPSEC Device#No
    - Device Type#All Device Types
    NetworkDeviceIPList:
    - ipaddress: 1.2.3.4
      mask: 32
    authenticationSettings:
      networkProtocol: RADIUS
      radiusSharedSecret: C1sco12345
    description: ''
    name: nad
    tacacsSettings:
      connectModeOptions: false
      sharedSecret: C1sco12345

- name: Delete by name
  cisco.ise.network_device:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    name: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
