#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_deployment
short_description: Resource module for Node Deployment
description:
- Manage operations create, update and delete of the resource Node Deployment.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  allowCertImport:
    description: Consent to import the self-signed certificate of the registering node.
    type: bool
  fqdn:
    description: Node Deployment's fqdn.
    type: str
  hostname:
    description: Hostname path parameter. Hostname of the deployed node.
    type: str
  password:
    description: Node Deployment's password.
    type: str
  roles:
    description: Roles can be empty or have many values for a node.
    elements: str
    type: list
  services:
    description: Services can be empty or have many values for a node.
    elements: str
    type: list
  userName:
    description: Node Deployment's userName.
    type: str
requirements:
- ciscoisesdk >= 1.3.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Node Deployment reference
  description: Complete reference of the Node Deployment object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowCertImport: true
    fqdn: string
    password: string
    roles:
    - string
    services:
    - string
    userName: string

- name: Update by name
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    hostname: string
    roles:
    - string
    services:
    - string

- name: Delete by name
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    hostname: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "fqdn": "string",
      "hostname": "string",
      "ipAddress": "string",
      "nodeStatus": "string",
      "roles": [
        "string"
      ],
      "services": [
        "string"
      ]
    }

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
"""
