#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: aci_settings
short_description: Resource module for Aci Settings
description:
- Manage operation update of the resource Aci Settings.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  aci50:
    description: Aci50 flag.
    type: bool
  aci51:
    description: Aci51 flag.
    type: bool
  aciipaddress:
    description: Aci Settings's aciipaddress.
    type: str
  acipassword:
    description: Aci Settings's acipassword.
    type: str
  aciuserName:
    description: Aci Settings's aciuserName.
    type: str
  adminName:
    description: Aci Settings's adminName.
    type: str
  adminPassword:
    description: Aci Settings's adminPassword.
    type: str
  allSxpDomain:
    description: AllSxpDomain flag.
    type: bool
  defaultSgtName:
    description: Aci Settings's defaultSgtName.
    type: str
  enableAci:
    description: EnableAci flag.
    type: bool
  enableDataPlane:
    description: EnableDataPlane flag.
    type: bool
  enableElementsLimit:
    description: EnableElementsLimit flag.
    type: bool
  id:
    description: Aci Settings's id.
    type: str
  ipAddressHostName:
    description: Aci Settings's ipAddressHostName.
    type: str
  l3RouteNetwork:
    description: Aci Settings's l3RouteNetwork.
    type: str
  maxNumIepgFromAci:
    description: Aci Settings's maxNumIepgFromAci.
    type: int
  maxNumSgtToAci:
    description: Aci Settings's maxNumSgtToAci.
    type: int
  specificSxpDomain:
    description: SpecificSxpDomain flag.
    type: bool
  specifixSxpDomainList:
    description: Aci Settings's specifixSxpDomainList.
    elements: str
    type: list
  suffixToEpg:
    description: Aci Settings's suffixToEpg.
    type: str
  suffixToSgt:
    description: Aci Settings's suffixToSgt.
    type: str
  tenantName:
    description: Aci Settings's tenantName.
    type: str
  untaggedPacketIepgName:
    description: Aci Settings's untaggedPacketIepgName.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.aci_settings
# Reference by Internet resource
- name: Aci Settings reference
  description: Complete reference of the Aci Settings object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.aci_settings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    aci50: false
    aci51: false
    adminName: admin name
    allSxpDomain: false
    defaultSgtName: Unknown
    enableAci: false
    enableDataPlane: false
    enableElementsLimit: true
    id: 872c4e3f-8b3f-4462-98ba-00519a033cce
    ipAddressHostName: 10.0.0.1
    l3RouteNetwork: L3_ROUTE
    maxNumIepgFromAci: 1000
    maxNumSgtToAci: 500
    specificSxpDomain: true
    specifixSxpDomainList:
    - default
    suffixToEpg: SGT
    suffixToSgt: EPG
    tenantName: ISE
    untaggedPacketIepgName: Untagged

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
