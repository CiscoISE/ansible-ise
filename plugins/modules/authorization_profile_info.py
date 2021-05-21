#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: authorization_profile_info
short_description: Information module for Authorization Profile
description:
- Get all Authorization Profile.
- Get Authorization Profile by id.
- Get Authorization Profile by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  page:
    description:
    - Page query parameter. Page number.
    type: int
  size:
    description:
    - Size query parameter. Number of objects returned per page.
    type: int
  id:
    description:
    - Id path parameter.
    type: str
  name:
    description:
    - Name path parameter.
    type: str
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
- name: Get all Authorization Profile
  cisco.ise.authorization_profile_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result
- name: Get Authorization Profile by id
  cisco.ise.authorization_profile_info
    id: string
  register: result
- name: Get Authorization Profile by name
  cisco.ise.authorization_profile_info
    name: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'AuthorizationProfile': {'id': 'string', 'name': 'string', 'description': 'string', 'advancedAttributes': [{'leftHandSideDictionaryAttribue': {'AdvancedAttributeValueType': 'string', 'dictionaryName': 'string', 'attributeName': 'string'}, 'rightHandSideAttribueValue': {'AdvancedAttributeValueType': 'string', 'value': 'string'}}], 'accessType': 'string', 'authzProfileType': 'string', 'vlan': {'nameID': 'string', 'tagID': 0}, 'reauth': {'timer': 0, 'connectivity': 'string'}, 'airespaceACL': 'string', 'airespaceIPv6ACL': 'string', 'webRedirection': {'WebRedirectionType': 'string', 'acl': 'string', 'portalName': 'string', 'staticIPHostNameFQDN': 'string', 'displayCertificatesRenewalMessages': True}, 'acl': 'string', 'trackMovement': True, 'serviceTemplate': True, 'easywiredSessionCandidate': True, 'daclName': 'string', 'voiceDomainPermission': True, 'neat': True, 'webAuth': True, 'autoSmartPort': 'string', 'interfaceTemplate': 'string', 'ipv6ACLFilter': 'string', 'avcProfile': 'string', 'macSecPolicy': 'string', 'asaVpn': 'string', 'profileName': 'string', 'ipv6DaclName': 'string'}}
  - {'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': {'rel': 'string', 'href': 'string', 'type': 'string'}, 'previousPage': {'rel': 'string', 'href': 'string', 'type': 'string'}}}
"""
