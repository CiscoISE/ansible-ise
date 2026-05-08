#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_secondary_to_primary
short_description: Resource module for Node Secondary To Primary
description:
  - Promote a secondary PAN node to primary PAN.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
  - ciscoisesdk >= 2.2.1
  - python >= 3.5
notes:
  - SDK Method used are
    node_deployment.NodeDeployment.promote_node,
  - Paths used are
    post /api/v1/deployment/promote,
"""

EXAMPLES = r"""
---
- name: Promote secondary PAN to primary
  cisco.ise.node_secondary_to_primary:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
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
