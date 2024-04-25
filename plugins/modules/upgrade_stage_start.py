#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: upgrade_stage_start
short_description: Resource module for Upgrade Stage Start
description:
- Manage operation create of the resource Upgrade Stage Start.
- API to initiate staging orcheastration from PPAN.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  hostnames:
    description: Upgrade Stage Start's hostnames.
    elements: str
    type: list
  preCheckReportID:
    description: Upgrade Stage Start's preCheckReportID.
    type: str
  reTrigger:
    description: ReTrigger flag.
    type: bool
  upgradeType:
    description: Upgrade Stage Start's upgradeType.
    type: str
requirements:
- ciscoisesdk >= 2.2.0
- python >= 3.5
notes:
  - SDK Method used are
    fullupgrade.Fullupgrade.initiate_staging_on_p_p_a_n,

  - Paths used are
    post /api/v1/upgrade/stage/start-stage,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.upgrade_stage_start:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    hostnames:
    - string
    preCheckReportID: string
    reTrigger: true
    upgradeType: string

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
        "dbStatus": "string",
        "message": "string",
        "node": "string",
        "percentage": 0,
        "progressMsg": "string",
        "status": "string"
      }
    ]
"""
