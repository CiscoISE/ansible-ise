#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_deployment_sync
short_description: Resource module for Node Deployment Sync
description:
  - Trigger configuration sync on a specific ISE node by hostname.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  hostname:
    description:
      - Hostname path parameter. FQDN of the ISE node to sync.
    type: str
    required: true
requirements:
  - ciscoisesdk >= 2.2.1
  - python >= 3.5
notes:
  - SDK Method used are
    node_deployment.NodeDeployment.sync_node,
  - Paths used are
    post /api/v1/deployment/sync-node/{hostname},
"""

EXAMPLES = r"""
---
- name: Sync Node Deployment
  cisco.ise.node_deployment_sync:
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
      "success": {
        "message": "string"
      },
      "version": "string"
    }
"""
