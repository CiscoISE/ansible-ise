#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_access_global_exception_rules_reset_hitcount
short_description: Resource module for Network Access Global Exception Rules Reset Hitcount
description:
- Manage operation create of the resource Network Access Global Exception Rules Reset Hitcount.
- Network Access - Reset HitCount for Global Exceptions.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk >= 2.0.8
- python >= 3.5
seealso:
- name: Cisco ISE documentation for Network Access - Authorization Global Exception Rules
  description: Complete reference of the Network Access - Authorization Global Exception Rules API.
  link: https://developer.cisco.com/docs/identity-services-engine/v1/#!policy-openapi
notes:
  - SDK Method used are
    network_access_authorization_global_exception_rules.NetworkAccessAuthorizationGlobalExceptionRules.reset_hit_counts_network_access_global_exceptions,

  - Paths used are
    post /network-access/policy-set/global-exception/reset-hitcount,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.network_access_global_exception_rules_reset_hitcount:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "message": "string"
    }
"""
