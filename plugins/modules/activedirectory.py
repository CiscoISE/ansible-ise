#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: activedirectory
short_description: Resource module for Activedirectory
description:
- Manage operation create of the resource Activedirectory.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  ERSActiveDirectoryDomains:
    description: Activedirectory's ERSActiveDirectoryDomains.
    suboptions:
      domains:
        description: List of Domains.
        elements: dict
        type: list
    type: dict
  adAttributes:
    description: Activedirectory's adAttributes.
    suboptions:
      attributes:
        description: List of Attributes.
        elements: dict
        type: list
    type: dict
  adScopesNames:
    description: String that contains the names of the scopes that the active directory
      belongs to. Names are separated by comma.
    type: str
  adgroups:
    description: Activedirectory's adgroups.
    suboptions:
      groups:
        description: List of Groups.
        elements: dict
        type: list
    type: dict
  advancedSettings:
    description: Activedirectory's advancedSettings.
    suboptions:
      agingTime:
        description: Activedirectory's agingTime.
        type: float
      authProtectionType:
        description: Enable prevent AD account lockout for WIRELESS/WIRED/BOTH.
        type: str
      country:
        description: User info attribute.
        type: str
      department:
        description: User info attribute.
        type: str
      email:
        description: User info attribute.
        type: str
      enableCallbackForDialinClient:
        description: EnableCallbackForDialinClient flag.
        type: bool
      enableDialinPermissionCheck:
        description: EnableDialinPermissionCheck flag.
        type: bool
      enableFailedAuthProtection:
        description: Enable prevent AD account lockout due to too many bad password
          attempts.
        type: bool
      enableMachineAccess:
        description: EnableMachineAccess flag.
        type: bool
      enableMachineAuth:
        description: EnableMachineAuth flag.
        type: bool
      enablePassChange:
        description: EnablePassChange flag.
        type: bool
      enableRewrites:
        description: EnableRewrites flag.
        type: bool
      failedAuthThreshold:
        description: Number of bad password attempts.
        type: float
      firstName:
        description: User info attribute.
        type: str
      identityNotInAdBehaviour:
        description: Allowed values REJECT, SEARCH_JOINED_FOREST, SEARCH_ALL.
        type: dict
      jobTitle:
        description: User info attribute.
        type: str
      lastName:
        description: User info attribute.
        type: str
      locality:
        description: User info attribute.
        type: str
      organizationalUnit:
        description: User info attribute.
        type: str
      plaintextAuth:
        description: PlaintextAuth flag.
        type: bool
      rewriteRules:
        description: List of Rewrite rules.
        elements: dict
        type: list
      schema:
        description: Allowed values ACTIVE_DIRECTORY, CUSTOM.
        type: dict
      stateOrProvince:
        description: User info attribute.
        type: str
      streetAddress:
        description: User info attribute.
        type: str
      telephone:
        description: User info attribute.
        type: str
      unreachableDomainsBehaviour:
        description: Allowed values PROCEED, DROP.
        type: dict
    type: dict
  description:
    description: Description.
    type: str
  domain:
    description: The AD domain.
    type: str
  enableDomainAllowedList:
    description: EnableDomainAllowedList flag.
    type: bool
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    activedirectory.Activedirectory.create_activedirectory,

  - Paths used are
    post /activedirectory/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.activedirectory:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    adAttributes:
      attributes:
      - defaultValue: defaultString
        internalName: internalName1
        name: name1
        type: STRING
      - defaultValue: 1.1.1.1
        internalName: internalName2
        name: name2
        type: IP
      - defaultValue: 'true'
        internalName: internalName3
        name: name3
        type: BOOLEAN
      - defaultValue: '5'
        internalName: internalName4
        name: name4
        type: INT
      - defaultValue: defaultOctetString
        internalName: internalName5
        name: name5
        type: OCTET_STRING
    adScopesNames: Default_Scope
    adgroups:
      groups:
      - name: cisco.com/operators
        sid: S-1-5-32-548
        type: GLOBAL
      - name: cisco.com/office users
        sid: S-1-5-33-326
        type: DOMAIN LOCAL
    advancedSettings:
      agingTime: 5
      authProtectionType: WIRELESS
      country: co
      department: department
      email: mail
      enableAuthorizationFlow: false
      enableCallbackForDialinClient: false
      enableDialinPermissionCheck: false
      enableFailedAuthProtection: false
      enableMachineAccess: true
      enableMachineAuth: true
      enablePassChange: true
      enableRewrites: false
      enableSessionStitching: false
      failedAuthThreshold: 5
      firstName: givenName
      identityNotInAdBehaviour: SEARCH_JOINED_FOREST
      jobTitle: title
      lastName: sn
      locality: l
      organizationalUnit: company
      plaintextAuth: false
      rewriteRules:
      - rewriteMatch: exampleMatch0
        rewriteResult: exampleResult0
        rowId: 0
      - rewriteMatch: exampleMatch1
        rewriteResult: exampleResult1
        rowId: 1
      - rewriteMatch: exampleMatch2
        rewriteResult: exampleResult2
        rowId: 2
      - rewriteMatch: exampleMatch3
        rewriteResult: exampleResult3
        rowId: 3
      schema: ACTIVE_DIRECTORY
      stateOrProvince: st
      streetAddress: streetAddress
      telephone: telephoneNumber
      unreachableDomainsBehaviour: PROCEED
    description: Group of Active company users
    domain: cisco.com
    enableDomainAllowedList: true
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    name: Company_users

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
