#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: active_directory_join_domain
short_description: Resource module for Active Directory Join Domain
description:
- Manage operation update of the resource Active Directory Join Domain.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    additionalData:
      description: Active Directory Join Domain's additionalData.
      suboptions:
        name:
          description: Active Directory Join Domain's name.
          type: str
        value:
          description: Active Directory Join Domain's value.
          type: str
      type: list
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.active_directory_join_domain
# Reference by Internet resource
- name: Active Directory Join Domain reference
  description: Complete reference of the Active Directory Join Domain object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.active_directory_join_domain:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    additionalData:
    - name: username
      value: '{{ad_admin_username}}'
    - name: password
      value: '{{ad_admin_password}}'
    - name: node
      value: '{{node_name}}'
    - name: orgunit
      value: '{{org_unit}}'
    id: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "ERSResponse": {
        "operation": "string",
        "messages": [
          {
            "title": "string",
            "type": "string",
            "code": "string"
          }
        ],
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    }
"""
