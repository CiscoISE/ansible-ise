#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint_certificate
short_description: Resource module for Endpoint Certificate
description:
- Manage operation create of the resource Endpoint Certificate.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  certTemplateName:
    description: Endpoint Certificate's certTemplateName.
    type: str
  certificateRequest:
    description: Endpoint Certificate's certificateRequest.
    suboptions:
      cn:
        description: Endpoint Certificate's cn.
        type: str
      san:
        description: Endpoint Certificate's san.
        type: str
    type: dict
  format:
    description: Endpoint Certificate's format.
    type: str
  password:
    description: Endpoint Certificate's password.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.endpoint_certificate
# Reference by Internet resource
- name: Endpoint Certificate reference
  description: Complete reference of the Endpoint Certificate object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.endpoint_certificate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    certTemplateName: Certificate_Template_Name
    certificateRequest:
      cn: userName [or] machineName
      san: 11-22-33-44-55-66
    format: PKCS8 [or] PKCS8_CHAIN [or] PKCS12 [or] PKCS12_CHAIN
    password: password

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
