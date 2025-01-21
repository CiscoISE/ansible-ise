#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: user_equipment_subscriber_info
short_description: Information module for User Equipment Subscriber Info
description:
  - Get User Equipment Subscriber Info by id.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  subscriberId:
    description:
      - SubscriberId path parameter. Unique ID for a subscriber object.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    user_equipment.UserEquipment.get_user_equipments_by_subscriber_id,
  - Paths used are
    get /api/v1/fiveg/user-equipment/subscriber/{subscriberId},
"""

EXAMPLES = r"""
- name: Get User Equipment Subscriber Info by id
  cisco.ise.user_equipment_subscriber_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    subscriberId: 7c9484cf-0ebc-47ad-a9ef-bc12729ed73d
  register: result
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
        "description": "string",
        "deviceGroup": "string",
        "imei": "string",
        "createTime": "string",
        "updateTime": "string",
        "id": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""
