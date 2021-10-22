#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sxp_vpns
short_description: Resource module for Sxp Vpns
description:
- Manage operations create and delete of the resource Sxp Vpns.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter.
    type: str
  sxpVpnName:
    description: Sxp Vpns's sxpVpnName.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sxp Vpns reference
  description: Complete reference of the Sxp Vpns object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Delete by id
  cisco.ise.sxp_vpns:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sxp_vpns:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    sxpVpnName: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "sxpVpnName": "string",
      "link": {
        "rel": "string",
        "href": "string",
        "type": "string"
      }
    }
"""
