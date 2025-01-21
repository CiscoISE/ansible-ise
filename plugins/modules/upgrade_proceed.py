#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: upgrade_proceed
short_description: Resource module for Upgrade Proceed
description:
  - Manage operation create of the resource Upgrade Proceed.
  - API's purpose would be to orchestrate upgrade execution on PPAN.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  hostnames:
    description: Upgrade Proceed's hostnames.
    elements: str
    type: list
  preCheckReportID:
    description: Upgrade Proceed's preCheckReportID.
    type: str
  upgradeType:
    description: Upgrade Proceed's upgradeType.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    fullupgrade.Fullupgrade.initiate_upgrade_on_p_p_a_n,
  - Paths used are
    post /api/v1/upgrade/proceed/initiate-upgrade,
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.upgrade_proceed:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    hostnames:
      - string
    preCheckReportID: string
    upgradeType: string
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "message": "string",
        "preCheckReportID": "string"
      },
      "version": "string"
    }
"""
