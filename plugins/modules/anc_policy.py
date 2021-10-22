#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: anc_policy
short_description: Resource module for Anc Policy
description:
- Manage operations create, update and delete of the resource Anc Policy.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  actions:
    description: '- QUARANTINE Allows you to use Exception policies (authorization policies)
      to limit or deny an endpoint access to the network. - PORTBOUNCE Resets the port
      on the network device to which the endpoint is connected. - SHUTDOWN Shuts down
      the port on the network device to which the endpoint is connected. - RE_AUTHENTICATE
      Re-authenticates the session from the endpoint.'
    elements: str
    type: list
  id:
    description: Anc Policy's id.
    type: str
  name:
    description: Anc Policy's name.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Anc Policy reference
  description: Complete reference of the Anc Policy object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.anc_policy:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    actions:
    - string
    id: string
    name: string

- name: Delete by id
  cisco.ise.anc_policy:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.anc_policy:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    actions:
    - string
    name: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "actions": [
        "string"
      ],
      "link": {
        "rel": "string",
        "href": "string",
        "type": "string"
      }
    }

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
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
