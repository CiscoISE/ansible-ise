#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: active_directory_add_groups
short_description: Resource module for Active Directory Add Groups
description:
- Manage operation update of the resource Active Directory Add Groups.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  description:
    description: Active Directory Add Groups's description.
    type: str
  domain:
    description: Active Directory Add Groups's domain.
    type: str
  id:
    description: Active Directory Add Groups's id.
    type: str
  name:
    description: Active Directory Add Groups's name.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.active_directory_add_groups
# Reference by Internet resource
- name: Active Directory Add Groups reference
  description: Complete reference of the Active Directory Add Groups object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.active_directory_add_groups:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: ''
    domain: '{{ad_domain_name}}'
    id: '{{id}}'
    name: '{{ad_domain_name}}'

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
