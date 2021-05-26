#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: authorization_profile
short_description: Resource module for Authorization Profile
description:
- Manage operations create, update, delete of the resource Authorization Profile.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    accessType:
      description: Authorization Profile's accessType.
      type: str
    acl:
      description: Authorization Profile's acl.
      type: str
    advancedAttributes:
      description: Authorization Profile's advancedAttributes.
      suboptions:
        leftHandSideDictionaryAttribue:
          description: Authorization Profile's leftHandSideDictionaryAttribue.
          suboptions:
            AdvancedAttributeValueType:
              description: Authorization Profile's AdvancedAttributeValueType.
              type: str
            attributeName:
              description: Authorization Profile's attributeName.
              type: str
            dictionaryName:
              description: Authorization Profile's dictionaryName.
              type: str
          type: dict
        rightHandSideAttribueValue:
          description: Authorization Profile's rightHandSideAttribueValue.
          suboptions:
            AdvancedAttributeValueType:
              description: Authorization Profile's AdvancedAttributeValueType.
              type: str
            value:
              description: Authorization Profile's value.
              type: str
          type: dict
      type: list
    airespaceACL:
      description: Authorization Profile's airespaceACL.
      type: str
    airespaceIPv6ACL:
      description: Authorization Profile's airespaceIPv6ACL.
      type: str
    asaVpn:
      description: Authorization Profile's asaVpn.
      type: str
    authzProfileType:
      description: Authorization Profile's authzProfileType.
      type: str
    autoSmartPort:
      description: Authorization Profile's autoSmartPort.
      type: str
    avcProfile:
      description: Authorization Profile's avcProfile.
      type: str
    daclName:
      description: Authorization Profile's daclName.
      type: str
    description:
      description: Authorization Profile's description.
      type: str
    easywiredSessionCandidate:
      description: EasywiredSessionCandidate flag.
      type: bool
    id:
      description: Authorization Profile's id.
      type: str
    interfaceTemplate:
      description: Authorization Profile's interfaceTemplate.
      type: str
    ipv6ACLFilter:
      description: Authorization Profile's ipv6ACLFilter.
      type: str
    ipv6DaclName:
      description: Authorization Profile's ipv6DaclName.
      type: str
    macSecPolicy:
      description: Authorization Profile's macSecPolicy.
      type: str
    name:
      description: Authorization Profile's name.
      type: str
    neat:
      description: Neat flag.
      type: bool
    profileName:
      description: Authorization Profile's profileName.
      type: str
    reauth:
      description: Authorization Profile's reauth.
      suboptions:
        connectivity:
          description: Authorization Profile's connectivity.
          type: str
        timer:
          description: Authorization Profile's timer.
          type: int
      type: dict
    serviceTemplate:
      description: ServiceTemplate flag.
      type: bool
    trackMovement:
      description: TrackMovement flag.
      type: bool
    vlan:
      description: Authorization Profile's vlan.
      suboptions:
        nameID:
          description: Authorization Profile's nameID.
          type: str
        tagID:
          description: Authorization Profile's tagID.
          type: int
      type: dict
    voiceDomainPermission:
      description: VoiceDomainPermission flag.
      type: bool
    webAuth:
      description: WebAuth flag.
      type: bool
    webRedirection:
      description: Authorization Profile's webRedirection.
      suboptions:
        WebRedirectionType:
          description: Authorization Profile's WebRedirectionType.
          type: str
        acl:
          description: Authorization Profile's acl.
          type: str
        displayCertificatesRenewalMessages:
          description: DisplayCertificatesRenewalMessages flag.
          type: bool
        portalName:
          description: Authorization Profile's portalName.
          type: str
        staticIPHostNameFQDN:
          description: Authorization Profile's staticIPHostNameFQDN.
          type: str
      type: dict
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.authorization_profile
# Reference by Internet resource
- name: Authorization Profile reference
  description: Complete reference of the Authorization Profile object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.authorization_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accessType: ACCESS_ACCEPT
    acl: aclfilter
    advancedAttributes:
    - leftHandSideDictionaryAttribue:
        AdvancedAttributeValueType: AdvancedDictionaryAttribute
        attributeName: cisco-call-filter
        dictionaryName: Cisco
      rightHandSideAttribueValue:
        AdvancedAttributeValueType: AttributeValue
        value: '23'
    airespaceACL: ACL
    airespaceIPv6ACL: ACL6
    asaVpn: Cisco:cisco-call-type
    authzProfileType: SWITCH
    autoSmartPort: autoSmartPort
    avcProfile: avcProfile
    daclName: PERMIT_ALL_IPV4_TRAFFIC
    description: description
    easywiredSessionCandidate: false
    id: id
    interfaceTemplate: interfaceTemplate
    ipv6ACLFilter: ipv6ACLFilter
    ipv6DaclName: PERMIT_ALL_IPV6_TRAFFIC
    macSecPolicy: MUST_SECURE
    name: name
    neat: false
    profileName: Cisco
    reauth:
      connectivity: RADIUS_REQUEST
      timer: 1800
    serviceTemplate: false
    trackMovement: false
    vlan:
      nameID: vlanName
      tagID: 1
    voiceDomainPermission: false
    webAuth: false
    webRedirection:
      WebRedirectionType: CentralizedWebAuth
      acl: acl
      displayCertificatesRenewalMessages: true
      portalName: Sponsored Guest Portal (default)
      staticIPHostNameFQDN: 10.56.54.200

- name: Update by id
  cisco.ise.authorization_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accessType: ACCESS_ACCEPT
    acl: aclfilter
    advancedAttributes:
    - leftHandSideDictionaryAttribue:
        AdvancedAttributeValueType: AdvancedDictionaryAttribute
        attributeName: cisco-call-filter
        dictionaryName: Cisco
      rightHandSideAttribueValue:
        AdvancedAttributeValueType: AttributeValue
        value: '23'
    airespaceACL: ACL
    airespaceIPv6ACL: ACL6
    asaVpn: Cisco:cisco-call-type
    authzProfileType: SWITCH
    autoSmartPort: autoSmartPort
    avcProfile: avcProfile
    daclName: PERMIT_ALL_IPV4_TRAFFIC
    description: description
    easywiredSessionCandidate: false
    id: id
    interfaceTemplate: interfaceTemplate
    ipv6ACLFilter: ipv6ACLFilter
    ipv6DaclName: PERMIT_ALL_IPV6_TRAFFIC
    macSecPolicy: MUST_SECURE
    name: name
    neat: false
    profileName: Cisco
    reauth:
      connectivity: RADIUS_REQUEST
      timer: 1800
    serviceTemplate: false
    trackMovement: false
    vlan:
      nameID: vlanName
      tagID: 1
    voiceDomainPermission: false
    webAuth: false
    webRedirection:
      WebRedirectionType: CentralizedWebAuth
      acl: acl
      displayCertificatesRenewalMessages: true
      portalName: Sponsored Guest Portal (default)
      staticIPHostNameFQDN: 10.56.54.200

- name: Delete by id
  cisco.ise.authorization_profile:
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
