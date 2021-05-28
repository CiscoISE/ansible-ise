#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: rest_id_store
short_description: Resource module for Rest Id Store
description:
- Manage operations create, update and delete of the resource Rest Id Store.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  description:
    description: Rest Id Store's description.
    type: str
  ersRestIDStoreAttributes:
    description: Rest Id Store's ersRestIDStoreAttributes.
    suboptions:
      headers:
        description: Rest Id Store's headers.
        suboptions:
          key:
            description: Rest Id Store's key.
            type: str
          value:
            description: Rest Id Store's value.
            type: str
        type: list
      predefined:
        description: Rest Id Store's predefined.
        type: str
      rootUrl:
        description: Rest Id Store's rootUrl.
        type: str
      usernameSuffix:
        description: Rest Id Store's usernameSuffix.
        type: str
    type: dict
  id:
    description: Id path parameter.
    type: str
  name:
    description: Rest Id Store's name.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.rest_id_store
# Reference by Internet resource
- name: Rest Id Store reference
  description: Complete reference of the Rest Id Store object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.rest_id_store:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: '{{description}}'
    ersRestIDStoreAttributes:
      headers:
      - key: clientID
        value: '{{clientID}}'
      - key: clientSecret
        value: '{{clientSecret}}'
      - key: tenantID
        value: '{{tenantID}}'
      predefined: Azure
      rootUrl: http://169.254.6.2:9601/azure
      usernameSuffix: '{{usernameSuffix}}'
    name: '{{name}}'

- name: Update by id
  cisco.ise.rest_id_store:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: my new description
    id: '{{id}}'
    name: ISE_AzureAD_ROPC

- name: Delete by id
  cisco.ise.rest_id_store:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Update by name
  cisco.ise.rest_id_store:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: my new description
    name: string

- name: Delete by name
  cisco.ise.rest_id_store:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    name: string

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
