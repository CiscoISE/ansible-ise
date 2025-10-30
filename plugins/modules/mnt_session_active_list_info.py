#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: mnt_session_active_list_info
short_description: Information module for MNT Session Active List
description:
  - Get all MNT Session Active List.
  - Returns a list of active sessions.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    misc.Misc.get_active_session_list,
  - Paths used are
    get /Session/ActiveList,
"""
EXAMPLES = r"""
---
- name: Get all MNT Session Active List
  cisco.ise.mnt_session_active_list_info:
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
      "activeSession": [
        {
          "user_name": "string",
          "calling_station_id": "string",
          "orig_calling_station_id": "string",
          "nas_ip_address": "string",
          "nas_ipv6_address": "string",
          "acct_session_id": "string",
          "audit_session_id": "string",
          "cpmsession_id": "string",
          "server": "string",
          "framed_ip_address": "string",
          "device_ip_address": "string",
          "framed_ipv6_address": {
            "ipv6_address": [
              "string"
            ]
          }
        }
      ],
      "noOfActiveSession": 0
    }
"""
