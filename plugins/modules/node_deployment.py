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
  - Register a new ISE node, update node roles/services, or deregister a node.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  state:
    description:
      - The state of the resource.
    type: str
    default: present
    choices: [present, absent]
  hostname:
    description:
      - Hostname of the ISE node. Used as primary identifier.
    type: str
  allowCertImport:
    description:
      - Allow the import of self-signed certificates from the node being registered.
    type: bool
  fqdn:
    description:
      - Fully qualified domain name of the node being registered.
    type: str
  password:
    description:
      - Password for the node admin account. Required on create.
    type: str
  roles:
    description:
      - ISE roles to assign to the node (e.g. PrimaryAdmin, SecondaryAdmin, PrimaryMonitoring).
    type: list
    elements: str
  services:
    description:
      - ISE services to enable on the node (e.g. Session, Profiler, DeviceAdmin).
    type: list
    elements: str
  userName:
    description:
      - Admin username for the node being registered. Required on create.
    type: str
requirements:
  - ciscoisesdk >= 2.2.1
  - python >= 3.5
notes:
  - SDK Method used are
    node_deployment.NodeDeployment.register_node,
    node_deployment.NodeDeployment.update_node,
    node_deployment.NodeDeployment.delete_node,
    node_deployment.NodeDeployment.get_node_details,
  - Paths used are
    post /api/v1/deployment/node,
    put /api/v1/deployment/node/{hostname},
    delete /api/v1/deployment/node/{hostname},
    get /api/v1/deployment/node/{hostname},
"""

EXAMPLES = r"""
---
- name: Register a new ISE node
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    fqdn: isenode.example.com
    hostname: isenode
    password: NodeAdminPass123
    userName: admin
    roles:
      - SecondaryAdmin
    services:
      - Session
      - Profiler
  register: result

- name: Update node roles
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    hostname: isenode
    roles:
      - SecondaryAdmin
      - SecondaryMonitoring
    services:
      - Session

- name: Deregister a node
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    hostname: isenode
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "hostname": "string",
      "fqdn": "string",
      "ipAddress": "string",
      "nodeServiceTypes": "string",
      "roles": ["string"],
      "services": ["string"]
    }
ise_update_response:
  description: A dictionary with the response returned by the Cisco ISE Python SDK
  returned: always, on update
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
ise_create_response:
  description: A dictionary with the response returned by the Cisco ISE Python SDK
  returned: always, on create
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
"""
