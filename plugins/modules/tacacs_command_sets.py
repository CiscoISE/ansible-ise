#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tacacs_command_sets
short_description: Resource module for Tacacs Command Sets
description:
- Manage operations create, update and delete of the resource Tacacs Command Sets.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    commands:
      description: Tacacs Command Sets's commands.
      suboptions:
        commandList:
          description: Tacacs Command Sets's commandList.
          suboptions:
            arguments:
              description: Tacacs Command Sets's arguments.
              type: str
            command:
              description: Tacacs Command Sets's command.
              type: str
            grant:
              description: Tacacs Command Sets's grant.
              type: str
          type: list
      type: dict
    description:
      description: Tacacs Command Sets's description.
      type: str
    id:
      description: Id path parameter.
      type: str
    name:
      description: Tacacs Command Sets's name.
      type: str
    permitUnmatched:
      description: PermitUnmatched flag.
      type: bool
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.tacacs_command_sets
# Reference by Internet resource
- name: Tacacs Command Sets reference
  description: Complete reference of the Tacacs Command Sets object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.tacacs_command_sets:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    commands:
      commandList:
      - arguments: string
        command: string
        grant: string
    description: string
    name: string
    permitUnmatched: true

- name: Update by id
  cisco.ise.tacacs_command_sets:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    commands:
      commandList:
      - arguments: string
        command: string
        grant: string
    description: string
    id: string
    name: string
    permitUnmatched: true

- name: Delete by id
  cisco.ise.tacacs_command_sets:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
