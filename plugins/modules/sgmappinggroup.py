#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sgmappinggroup
short_description: Resource module for SGmappinggroup
description:
- Manage operation create of the resource SGmappinggroup.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  deployTo:
    description: SGmappinggroup's deployTo.
    type: dict
  deployType:
    description: Allowed values ALL,ND,NDG.
    type: str
  description:
    description: Description.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  sgt:
    description: SGmappinggroup's sgt.
    type: dict
  sgtDomain:
    description: SGmappinggroup's sgtDomain.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    sgmappinggroup.Sgmappinggroup.create_sgmappinggroup,

  - Paths used are
    post /sgmappinggroup/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sgmappinggroup:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    deployTo: network_device_id
    deployType: ND
    name: groupA
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
