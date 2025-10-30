#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sgmapping
short_description: Resource module for SGmapping
description:
  - Manage operation create of the resource SGmapping.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  deployTo:
    description: SGmapping's deployTo.
    type: dict
  deployType:
    description: Allowed values ALL,ND,NDG.
    type: str
  description:
    description: Description.
    type: str
  hostIp:
    description: SGmapping's hostIp.
    type: str
  hostName:
    description: SGmapping's hostName.
    type: str
  id:
    description: Id.
    type: str
  mappingGroup:
    description: SGmapping's mappingGroup.
    type: dict
  name:
    description: Name.
    type: str
  sgt:
    description: SGmapping's sgt.
    type: dict
  sgtDomain:
    description: SGmapping's sgtDomain.
    type: str
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    sgmapping.Sgmapping.create_sgmapping,
  - Paths used are
    post /sgmapping/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.sgmapping:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    deployTo: network_device_id
    deployType: ND
    hostName: server1.cisco.com
    name: server1.cisco.com
    sgt: sgt_id
    sgtDomain:
      - sgt_domain
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
