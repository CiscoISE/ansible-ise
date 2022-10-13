#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: px_grid_node_approve
short_description: Resource module for Px Grid Node Approve
description:
- Manage operation update of the resource Px Grid Node Approve.
- This API allows the client to approve a pxGrid node.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  name:
    description: Name path parameter.
    type: str
requirements:
- ciscoisesdk >= 2.0.5
- python >= 3.5
notes:
  - SDK Method used are
    px_grid_node.PxGridNode.approve_px_grid_node,

  - Paths used are
    put /ers/config/pxgridnode/name/{name}/approve,

"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.px_grid_node_approve:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
