#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: egressmatrixcell
short_description: Resource module for Egressmatrixcell
description:
  - Manage operation create of the resource Egressmatrixcell.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  defaultRule:
    description: Allowed values NONE,DENY_IP,PERMIT_IP.
    type: str
  description:
    description: Description.
    type: str
  destinationSGtId:
    description: Egressmatrixcell's destinationSGtId.
    type: str
  id:
    description: Id.
    type: str
  matrixCellStatus:
    description: Allowed values DISABLED,ENABLED,MONITOR.
    type: str
  matrixId:
    description: Default value is Production Matrix Id, when no value is provided
      during creation.To use it as filter, the values should be an UUID of a Matrix.
      The values are case sensitive.For example, 'ERSObjectURL?filter=matrixId.eq.ccf9a6ea-153b-4056-b8f4-0dc17eca4d30'.
    type: str
  name:
    description: Name.
    type: str
  sgacls:
    description: Egressmatrixcell's sgacls.
    type: list
  sourceSGtId:
    description: Egressmatrixcell's sourceSGtId.
    type: str
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    egressmatrixcell.Egressmatrixcell.create_egressmatrixcell,
  - Paths used are
    post /egressmatrixcell/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.egressmatrixcell:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultRule: PERMIT_IP
    destinationSgtId: 1ebbc200-7a26-11e4-bc43-000c29ed7428
    id: 3b12f244-7c2b-4b1e-9bc1-1a5d6e420b94
    matrixCellStatus: MONITOR
    matrixId: f47ac10b-58cc-4372-a567-0e02b2c3d479
    sgacls:
      - 1ebbc100-7a26-11e4-bc43-000c29ed7428
      - 2ebbc100-7a26-11e4-bc43-000c29ed7428
    sourceSgtId: 2ebbc200-7a26-11e4-bc43-000c29ed7428
"""
RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""
