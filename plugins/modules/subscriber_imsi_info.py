#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: subscriber_imsi_info
short_description: Information module for Subscriber Imsi Info
description:
  - Get Subscriber Imsi Info by id.
version_added: '2.8.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  imsi:
    description:
      - Imsi path parameter. IMSI parameter.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    subscriber.Subscriber.get_subscriber_by_i_m_s_i,
  - Paths used are
    get /api/v1/fiveg/subscriber/imsi/{imsi},
"""

EXAMPLES = r"""
- name: Get Subscriber Imsi Info by id
  cisco.ise.subscriber_imsi_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    imsi: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "createTime": "string",
      "enabled": true,
      "friendlyName": "string",
      "id": "string",
      "identityGroups": "string",
      "imeis": "string",
      "imsi": "string",
      "ki": "string",
      "link": {
        "href": "string",
        "rel": "string",
        "type": "string"
      },
      "opc": "string",
      "updateTime": "string"
    }
"""
