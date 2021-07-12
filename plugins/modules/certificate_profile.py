#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: certificate_profile
short_description: Resource module for Certificate Profile
description:
- Manage operations create and update of the resource Certificate Profile.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  allowedAsUserName:
    description: AllowedAsUserName flag.
    type: bool
  certificateAttributeName:
    description: Certificate Profile's certificateAttributeName.
    type: str
  description:
    description: Certificate Profile's description.
    type: str
  externalIdentityStoreName:
    description: Certificate Profile's externalIdentityStoreName.
    type: str
  id:
    description: Certificate Profile's id.
    type: str
  matchMode:
    description: Certificate Profile's matchMode.
    type: str
  name:
    description: Certificate Profile's name.
    type: str
  usernameFrom:
    description: Certificate Profile's usernameFrom.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.certificate_profile
# Reference by Internet resource
- name: Certificate Profile reference
  description: Complete reference of the Certificate Profile object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.certificate_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowedAsUserName: false
    certificateAttributeName: SUBJECT_COMMON_NAME
    description: Precreated Certificate Authorization Profile.
    externalIdentityStoreName: '[not applicable]'
    id: 925b6d20-8c01-11e6-996c-525400b48521
    matchMode: NEVER
    name: Preloaded_Certificate_Profile
    usernameFrom: CERTIFICATE

- name: Update by id
  cisco.ise.certificate_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowedAsUserName: false
    certificateAttributeName: SUBJECT_COMMON_NAME
    description: Precreated Certificate Authorization Profile.
    externalIdentityStoreName: '[not applicable]'
    id: 925b6d20-8c01-11e6-996c-525400b48521
    matchMode: NEVER
    name: Preloaded_Certificate_Profile
    usernameFrom: CERTIFICATE

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
