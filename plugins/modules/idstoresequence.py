#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: idstoresequence
short_description: Resource module for Idstoresequence
description:
- Manage operation create of the resource Idstoresequence.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  breakOnStoreFail:
    description: Do not access other stores in the sequence If a selected identity store
      cannot be accessed for authentication.
    type: bool
  certificateAuthenticationProfile:
    description: Certificate Authentication Profile, empty if doesn't exist.
    type: str
  description:
    description: Description.
    type: str
  id:
    description: Id.
    type: str
  idSeqItem:
    description: List of id stores comprised of id store name and order.
    type: str
  name:
    description: Name.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    idstoresequence.Idstoresequence.create_idstoresequence,

  - Paths used are
    post /idstoresequence/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.idstoresequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    breakOnStoreFail: false
    certificateAuthenticationProfile: Preloaded_Certificate_Profile
    description: 'ERS Example Id sequence '
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    idSeqItem:
    - idstore: Internal Users
      order: 1
    - idstore: Guest Users
      order: 2
    name: idSeq1

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
        },
        "idSeqItem": {
          "idstore": "string",
          "order": "string"
        }
      }
    ]
"""
