#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: certificateprofile
short_description: Resource module for Certificateprofile
description:
- Manage operation create of the resource Certificateprofile.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  allowedAsUserName:
    description: To be set true or false.
    type: bool
  certificateAttributeName:
    description: Attribute name of the Certificate Profile - used only when CERTIFICATE
      is chosen in usernameFrom. Allowed values SUBJECT_COMMON_NAME, SUBJECT_ALTERNATIVE_NAME,
      SUBJECT_SERIAL_NUMBER, SUBJECT, SUBJECT_ALTERNATIVE_NAME_OTHER_NAME, SUBJECT_ALTERNATIVE_NAME_EMAIL,
      SUBJECT_ALTERNATIVE_NAME_DNS. Additional internal value ALL_SUBJECT_AND_ALTERNATIVE_NAMES
      is used automatically when usernameFrom=UPN.
    type: dict
  description:
    description: Description.
    type: str
  externalIdentityStoreName:
    description: Referred IDStore name for the Certificate Profile or not applicable
      in case no identity store is chosen.
    type: str
  id:
    description: Id.
    type: str
  matchMode:
    description: Match mode of the Certificate Profile. Allowed values NEVER, RESOLVE_IDENTITY_AMBIGUITY,
      BINARY_COMPARISON.
    type: dict
  name:
    description: Name.
    type: str
  usernameFrom:
    description: The attribute in the certificate where the user name should be taken
      from. Allowed values CERTIFICATE (for a specific attribute as defined in certificateAttributeName),
      UPN (for using any Subject or Alternative Name Attributes in the Certificate -
      an option only in AD).
    type: dict
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    certificateprofile.Certificateprofile.create_certificateprofile,

  - Paths used are
    post /certificateprofile/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.certificateprofile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowedAsUserName: false
    certificateAttributeName: SUBJECT_COMMON_NAME
    description: descp
    externalIdentityStoreName: '[not applicable]'
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    matchMode: NEVER
    name: name
    usernameFrom: CERTIFICATE

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
