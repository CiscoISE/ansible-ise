#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: adresourcereservation_
short_description: Resource module for Adresourcereservation 
description:
- Manage operation update of the resource Adresourcereservation .
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description.
    type: str
  id:
    description: Id path parameter.
    type: str
  joinPointNames:
    description: Selected Join Points in PSN.
    type: str
  name:
    description: Name.
    type: str
  node:
    description: PSN name.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    adresourcereservation.Adresourcereservation.update_adresourcereservation_by_id,

  - Paths used are
    put /adresourcereservation/{id},

"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.adresourcereservation_:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    id: string
    joinPointNames: jp1,jp2,jp3
    node: node1.com

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "node": "string",
      "joinPointNames": "string",
      "name": "string",
      "id": "string",
      "description": "string",
      "link": {
        "rel": "string",
        "href": "string",
        "type": "string"
      }
    }

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: dict
  sample: >
    {
      "UpdatedFieldsList": {
        "updatedField": [
          {
            "field": "string",
            "oldValue": "string",
            "newValue": "string"
          }
        ]
      }
    }
"""
