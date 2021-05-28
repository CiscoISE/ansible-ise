#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: active_directory
short_description: Resource module for Active Directory
description:
- Manage operations create and delete of the resource Active Directory.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  adAttributes:
    description: Active Directory's adAttributes.
    suboptions:
      attributes:
        description: Active Directory's attributes.
        suboptions:
          defaultValue:
            description: Active Directory's defaultValue.
            type: str
          internalName:
            description: Active Directory's internalName.
            type: str
          name:
            description: Active Directory's name.
            type: str
          type:
            description: Active Directory's type.
            type: str
        type: list
    type: dict
  adScopesNames:
    description: Active Directory's adScopesNames.
    type: str
  adgroups:
    description: Active Directory's adgroups.
    suboptions:
      groups:
        description: Active Directory's groups.
        suboptions:
          name:
            description: Active Directory's name.
            type: str
          sid:
            description: Active Directory's sid.
            type: str
          type:
            description: Active Directory's type.
            type: str
        type: list
    type: dict
  advancedSettings:
    description: Active Directory's advancedSettings.
    suboptions:
      agingTime:
        description: Active Directory's agingTime.
        type: int
      country:
        description: Active Directory's country.
        type: str
      department:
        description: Active Directory's department.
        type: str
      email:
        description: Active Directory's email.
        type: str
      enableCallbackForDialinClient:
        description: EnableCallbackForDialinClient flag.
        type: bool
      enableDialinPermissionCheck:
        description: EnableDialinPermissionCheck flag.
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
      firstName:
        description: Active Directory's firstName.
        type: str
      identityNotInAdBehaviour:
        description: Active Directory's identityNotInAdBehaviour.
        type: str
      jobTitle:
        description: Active Directory's jobTitle.
        type: str
      lastName:
        description: Active Directory's lastName.
        type: str
      locality:
        description: Active Directory's locality.
        type: str
      organizationalUnit:
        description: Active Directory's organizationalUnit.
        type: str
      plaintextAuth:
        description: PlaintextAuth flag.
        type: bool
      rewriteRules:
        description: Active Directory's rewriteRules.
        suboptions:
          rewriteMatch:
            description: Active Directory's rewriteMatch.
            type: str
          rewriteResult:
            description: Active Directory's rewriteResult.
            type: str
          rowId:
            description: Active Directory's rowId.
            type: int
        type: list
      schema:
        description: Active Directory's schema.
        type: str
      stateOrProvince:
        description: Active Directory's stateOrProvince.
        type: str
      streetAddress:
        description: Active Directory's streetAddress.
        type: str
      telephone:
        description: Active Directory's telephone.
        type: str
      unreachableDomainsBehaviour:
        description: Active Directory's unreachableDomainsBehaviour.
        type: str
    type: dict
  description:
    description: Active Directory's description.
    type: str
  domain:
    description: Active Directory's domain.
    type: str
  id:
    description: Id path parameter.
    type: str
  name:
    description: Active Directory's name.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.active_directory
# Reference by Internet resource
- name: Active Directory reference
  description: Complete reference of the Active Directory object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.active_directory:
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
    adScopesNames: Default_Scope
    adgroups:
      groups:
      - name: cisco.com/operators
        sid: S-1-5-32-548
        type: GLOBAL
    advancedSettings:
      agingTime: 5
      country: co
      department: department
      email: mail
      enableCallbackForDialinClient: false
      enableDialinPermissionCheck: false
      enableMachineAccess: true
      enableMachineAuth: true
      enablePassChange: true
      enableRewrites: false
      firstName: givenName
      identityNotInAdBehaviour: SEARCH_JOINED_FOREST
      jobTitle: title
      lastName: sn
      locality: l
      organizationalUnit: company
      plaintextAuth: false
      rewriteRules:
      - rewriteMatch: host/[HOSTNAME].[DOMAIN]
        rewriteResult: host/[HOSTNAME].[DOMAIN]
        rowId: 0
      - rewriteMatch: host/[HOSTNAME]
        rewriteResult: host/[HOSTNAME]
        rowId: 1
      - rewriteMatch: '[DOMAIN]\[IDENTITY]'
        rewriteResult: '[DOMAIN]\[IDENTITY]'
        rowId: 2
      - rewriteMatch: '[IDENTITY]@[DOMAIN]'
        rewriteResult: '[IDENTITY]@[DOMAIN]'
        rowId: 3
      - rewriteMatch: '[IDENTITY]'
        rewriteResult: '[IDENTITY]'
        rowId: 4
      schema: ACTIVE_DIRECTORY
      stateOrProvince: st
      streetAddress: streetAddress
      telephone: telephoneNumber
      unreachableDomainsBehaviour: PROCEED
    description: ''
    domain: cisco.com
    name: cisco.com

- name: Delete by id
  cisco.ise.active_directory:
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
