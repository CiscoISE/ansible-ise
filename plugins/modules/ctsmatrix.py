#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: ctsmatrix
short_description: Resource module for Ctsmatrix
description:
- Manage operation create of the resource Ctsmatrix.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  cells:
    description: Ctsmatrix's cells.
    suboptions:
      colCells:
        description: Ctsmatrix's colCells.
        suboptions:
          dstSGt:
            description: Ctsmatrix's dstSGt.
            type: str
          monitorMode:
            description: Ctsmatrix's monitorMode.
            type: str
          sgacls:
            description: Ctsmatrix's sgacls.
            suboptions:
              name:
                description: Ctsmatrix's name.
                type: str
              protocol:
                description: Ctsmatrix's protocol.
                type: str
              sgaclGenID:
                description: Ctsmatrix's sgaclGenID.
                type: str
            type: dict
          srcSGt:
            description: Ctsmatrix's srcSGt.
            type: str
        type: dict
      dstSGt:
        description: Ctsmatrix's dstSGt.
        type: str
      dstSGtGenID:
        description: Ctsmatrix's dstSGtGenID.
        type: str
      refreshTimer:
        description: Ctsmatrix's refreshTimer.
        type: str
      srcSGt:
        description: Ctsmatrix's srcSGt.
        type: str
      srcSGtGenID:
        description: Ctsmatrix's srcSGtGenID.
        type: str
    type: dict
  dstSGtArr:
    description: Ctsmatrix's dstSGtArr.
    elements: str
    type: list
  globalMonitorModeEnabled:
    description: GlobalMonitorModeEnabled flag.
    type: bool
  limit:
    description: Ctsmatrix's limit.
    type: float
  max:
    description: Ctsmatrix's max.
    type: float
  offset:
    description: Ctsmatrix's offset.
    type: float
  policyVerId:
    description: Ctsmatrix's policyVerId.
    type: str
  pushId:
    description: Value range 2 to 65519 or -1 to auto-generate.
    type: str
  srcSGtArr:
    description: Ctsmatrix's srcSGtArr.
    elements: str
    type: list
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    ctsmatrix.Ctsmatrix.create_ctsmatrix,

  - Paths used are
    post /ctsmatrix/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.ctsmatrix:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    dstSgtArr:
    - 0C
    limit: 500
    offset: 0
    pushId: '123456'
    srcSgtArr: []

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
