#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_deployment_info
short_description: Information module for Node Deployment
description:
  - Get all Node Deployment.
  - Get Node Deployment by hostname.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  hostname:
    description:
      - Hostname path parameter.
    type: str
  filter:
    description:
      - Filter query parameter.
    type: str
  filterType:
    description:
      - FilterType query parameter.
    type: str
requirements:
  - ciscoisesdk >= 2.2.1
  - python >= 3.5
notes:
  - SDK Method used are
    node_deployment.NodeDeployment.get_node_details,
    node_deployment.NodeDeployment.get_deployment_nodes,
  - Paths used are
    get /api/v1/deployment/node/{hostname},
    get /api/v1/deployment/node,
"""

EXAMPLES = r"""
---
- name: Get all Node Deployment
  cisco.ise.node_deployment_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result

- name: Get Node Deployment by hostname
  cisco.ise.node_deployment_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    hostname: isenode.example.com
  register: result
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
"""
