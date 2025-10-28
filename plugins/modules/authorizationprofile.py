#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: authorizationprofile
short_description: Resource module for Authorizationprofile
description:
- Manage operation create of the resource Authorizationprofile.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  accessType:
    description: Allowed Values ACCESS_ACCEPT, ACCESS_REJECT.
    type: str
  acl:
    description: Authorizationprofile's acl.
    type: str
  advancedAttributes:
    description: Authorizationprofile's advancedAttributes.
    suboptions:
      leftHandSideDictionaryAttribue:
        description: Authorizationprofile's leftHandSideDictionaryAttribue.
        suboptions:
          attributeName:
            description: Attribute name.
            type: str
          dictionaryName:
            description: Dictionary name.
            type: str
        type: dict
      rightHandSideAttribueValue:
        description: Attribute value can be of type AttributeValue or AdvancedDictionaryAttribute.
          For AttributeValue the value is String, For AdvancedDictionaryAttribute the
          value is dictionaryName and attributeName properties, for RADIUS Dictionary
          with attribute name starting with 'Tunnel-' there is also tagID property which
          is a number between 0-31.
        type: dict
    type: dict
  agentlessPosture:
    description: Authorizationprofile's agentlessPosture.
    type: dict
  airespaceACL:
    description: Authorizationprofile's airespaceACL.
    type: str
  airespaceIPv6ACL:
    description: Authorizationprofile's airespaceIPv6ACL.
    type: str
  asaVpn:
    description: Authorizationprofile's asaVpn.
    type: str
  authzProfileType:
    description: Allowed Values SWITCH, TRUSTSEC, TACACS. SWITCH is used for Standard
      Authorization Profiles. Only SWITCH is supported.
    type: str
  autoSmartPort:
    description: Authorizationprofile's autoSmartPort.
    type: str
  avcProfile:
    description: Authorizationprofile's avcProfile.
    type: str
  daclName:
    description: Authorizationprofile's daclName.
    type: str
  description:
    description: Description.
    type: str
  easywiredSessionCandidate:
    description: Authorizationprofile's easywiredSessionCandidate.
    type: dict
  id:
    description: Id.
    type: str
  interfaceTemplate:
    description: Authorizationprofile's interfaceTemplate.
    type: str
  ipv6ACLFilter:
    description: Authorizationprofile's ipv6ACLFilter.
    type: str
  ipv6DaclName:
    description: Authorizationprofile's ipv6DaclName.
    type: str
  macSecPolicy:
    description: Allowed Values MUST_SECURE, MUST_NOT_SECURE, SHOULD_SECURE.
    type: str
  name:
    description: Name.
    type: str
  neat:
    description: Authorizationprofile's neat.
    type: dict
  profileName:
    description: Value needs to be an existing Network Device Profile.
    type: str
  reauth:
    description: Authorizationprofile's reauth.
    suboptions:
      attributeName:
        description: The name of the attribute within the dictionary containing the
          value. Value should be date based in ISO 8601 form with timezone offset. For
          example, 2035-12-31T23 59 59-08 00.
        type: str
      connectivity:
        description: Allowed Values DEFAULT, RADIUS_REQUEST.
        type: str
      dictionaryName:
        description: The name of the dictionary containing the attribute.
        type: str
      reauthType:
        description: Allowed Values TIMER, EXPIRATION_DATE. Specifies the type of reauthentication.
          TIMER is used for time-based reauthentication, while EXPIRATION_DATE is used
          for dynamic date-based reauthentication.
        type: str
      timer:
        description: Specifies the reauthentication timer in seconds. Valid range is
          1-1073741823.
        type: dict
    type: dict
  serviceTemplate:
    description: Authorizationprofile's serviceTemplate.
    type: dict
  trackMovement:
    description: Authorizationprofile's trackMovement.
    type: dict
  uniqueIdentifier:
    description: Authorizationprofile's uniqueIdentifier.
    type: str
  vlan:
    description: Authorizationprofile's vlan.
    suboptions:
      nameID:
        description: Authorizationprofile's nameID.
        type: str
      tagID:
        description: Valid range is 0-31.
        type: float
    type: dict
  voiceDomainPermission:
    description: Authorizationprofile's voiceDomainPermission.
    type: dict
  webAuth:
    description: Authorizationprofile's webAuth.
    type: dict
  webRedirection:
    description: Authorizationprofile's webRedirection.
    suboptions:
      ACL:
        description: Authorizationprofile's ACL.
        type: str
      WebRedirectionType:
        description: Value MUST be one of the following CentralizedWebAuth, HotSpot,
          NativeSupplicanProvisioning, ClientProvisioning. The WebRedirectionType must
          fit the portalName.
        type: str
      displayCertificatesRenewalMessages:
        description: The displayCertificatesRenewalMessages is mandatory when 'WebRedirectionType'
          value is 'CentralizedWebAuth'. For all other 'WebRedirectionType' values the
          field must be ignored.
        type: bool
      portalName:
        description: A portal that exist in the DB and fits the WebRedirectionType.
        type: str
      staticIPHostNameFQDN:
        description: Authorizationprofile's staticIPHostNameFQDN.
        type: str
    type: dict
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    authorizationprofile.Authorizationprofile.create_authorizationprofile,

  - Paths used are
    post /authorizationprofile/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.authorizationprofile:
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
    agentlessPosture: false
    airespaceACL: ACL
    airespaceIPv6ACL: ACL6
    asaVpn: Cisco:cisco-call-type
    authzProfileType: SWITCH
    autoSmartPort: autoSmartPort
    avcProfile: avcProfile
    daclName: PERMIT_ALL_IPV4_TRAFFIC
    description: description
    easywiredSessionCandidate: false
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    interfaceTemplate: interfaceTemplate
    ipv6ACLFilter: ipv6ACLFilter
    ipv6DaclName: PERMIT_ALL_IPV6_TRAFFIC
    macSecPolicy: MUST_SECURE
    name: name
    neat: false
    profileName: Cisco
    reauth:
      connectivity: RADIUS_REQUEST
      reauthType: TIMER
      timer: 1800
    serviceTemplate: false
    trackMovement: false
    uniqueIdentifier: CERTIFICATE:Subject Alternative Name - URI
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
