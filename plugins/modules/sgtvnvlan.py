#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sgtvnvlan
short_description: Resource module for SGtvnvlan
description:
  - Manage operation create of the resource SGtvnvlan.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  sgtId:
    description: SGtId.
    type: str
  virtualnetworklist:
    description: List of VirtualNetwork.
    elements: dict
    type: list
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    sgtvnvlan.Sgtvnvlan.create_sgtvnvlan,
  - Paths used are
    post /sgtvnvlan/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.sgtvnvlan:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: description
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    name: name
    sgtId: sgt_id
    virtualnetworklist:
      - defaultVirtualNetwork: false
        description: description
        id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
        name: virtual1
        vlans:
          - data: true
            defaultVlan: true
            description: description1
            id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
            maxValue: 279060040
            name: vlan1
      - data: false
        defaultVlan: false
        description: description
        id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
        maxValue: 536930244
        name: vlan2
      - data: true
        defaultVlan: false
        description: description
        id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
        maxValue: 0
        name: vlan3
      - defaultVirtualNetwork: true
        description: description
        id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
        name: virtual2
        vlans:
          - data: false
            defaultVlan: false
            maxValue: 1453775043
            name: vlan4
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
