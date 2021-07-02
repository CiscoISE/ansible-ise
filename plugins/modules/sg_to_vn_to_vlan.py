#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sg_to_vn_to_vlan
short_description: Resource module for Sg To Vn To Vlan
description:
- Manage operations create, update and delete of the resource Sg To Vn To Vlan.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  description:
    description: Sg To Vn To Vlan's description.
    type: str
  id:
    description: Sg To Vn To Vlan's id.
    type: str
  name:
    description: Sg To Vn To Vlan's name.
    type: str
  sgtId:
    description: Sg To Vn To Vlan's sgtId.
    type: str
  virtualnetworklist:
    description: Sg To Vn To Vlan's virtualnetworklist.
    suboptions:
      defaultVirtualNetwork:
        description: DefaultVirtualNetwork flag.
        type: bool
      description:
        description: Sg To Vn To Vlan's description.
        type: str
      id:
        description: Sg To Vn To Vlan's id.
        type: str
      name:
        description: Sg To Vn To Vlan's name.
        type: str
      vlans:
        description: Sg To Vn To Vlan's vlans.
        suboptions:
          data:
            description: Data flag.
            type: bool
          defaultVlan:
            description: DefaultVlan flag.
            type: bool
          description:
            description: Sg To Vn To Vlan's description.
            type: str
          id:
            description: Sg To Vn To Vlan's id.
            type: str
          maxValue:
            description: Sg To Vn To Vlan's maxValue.
            type: int
          name:
            description: Sg To Vn To Vlan's name.
            type: str
        type: list
    type: list
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sg_to_vn_to_vlan
# Reference by Internet resource
- name: Sg To Vn To Vlan reference
  description: Complete reference of the Sg To Vn To Vlan object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sg_to_vn_to_vlan:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: description
    id: id
    name: name
    sgtId: sgt_id
    virtualnetworklist:
    - defaultVirtualNetwork: false
      description: description
      id: id
      name: virtual1
      vlans:
      - data: true
        defaultVlan: true
        description: description1
        id: '1'
        maxValue: 909386796
        name: vlan1
      - data: false
        defaultVlan: false
        description: description
        id: id
        maxValue: 1964790221
        name: vlan2
      - data: true
        defaultVlan: false
        description: description
        id: id
        maxValue: 0
        name: vlan3
    - defaultVirtualNetwork: true
      description: description
      id: id
      name: virtual2
      vlans:
      - data: false
        defaultVlan: false
        maxValue: 1368125387
        name: vlan4

- name: Update by id
  cisco.ise.sg_to_vn_to_vlan:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: description
    id: id
    name: name
    sgtId: sgt_id
    virtualnetworklist:
    - defaultVirtualNetwork: false
      description: description
      id: id
      name: virtual1
      vlans:
      - data: true
        defaultVlan: true
        description: description1
        id: '1'
        maxValue: 909386796
        name: vlan1
      - data: false
        defaultVlan: false
        description: description
        id: id
        maxValue: 1964790221
        name: vlan2
      - data: true
        defaultVlan: false
        description: description
        id: id
        maxValue: 0
        name: vlan3
    - defaultVirtualNetwork: true
      description: description
      id: id
      name: virtual2
      vlans:
      - data: false
        defaultVlan: false
        maxValue: 1368125387
        name: vlan4

- name: Delete by id
  cisco.ise.sg_to_vn_to_vlan:
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
