#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sgacls
short_description: Resource module for SGacls
description:
- Manage operation create of the resource SGacls.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  limit:
    description: SGacls's limit.
    type: float
  max:
    description: SGacls's max.
    type: float
  names:
    description: SGacls's names.
    elements: str
    type: list
  offset:
    description: SGacls's offset.
    type: float
  policyVerId:
    description: SGacls's policyVerId.
    type: str
  pullId:
    description: SGacls's pullId.
    type: str
  pushId:
    description: Value range 2 to 65519 or -1 to auto-generate.
    type: str
  sgacls:
    description: SGacls's sgacls.
    suboptions:
      description:
        description: SGacls's description.
        type: str
      name:
        description: SGacls's name.
        type: str
      protocol:
        description: SGacls's protocol.
        type: str
      rule:
        description: SGacls's rule.
        type: str
      sgaclGenID:
        description: SGacls's sgaclGenID.
        type: str
    type: dict
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    sgacls.Sgacls.create_sgacls,

  - Paths used are
    post /sgacls/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sgacls:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    limit: 1
    max: 1
    names:
    - Permit_IP_Log
    offset: 0
    policyVerId: 12-0-1968919659f
    pushId: '1'

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "operation": "string",
      "messages": [
        {
          "title": "string",
          "type": "string",
          "code": "string"
        }
      ]
    }
"""
