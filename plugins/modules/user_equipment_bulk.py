#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: user_equipment_bulk
short_description: Resource module for User Equipment Bulk
description:
  - Manage operation create of the resource User Equipment Bulk.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  ItemList:
    description: User Equipment Bulk's ItemList.
    elements: dict
    suboptions:
      description:
        description: User Equipment Bulk's description.
        type: str
      deviceGroup:
        description: Device or Endpoint Group.
        type: str
      id:
        description: User Equipment Bulk's id.
        type: str
      imei:
        description: User Equipment Bulk's imei.
        type: str
    type: list
  operation:
    description: User Equipment Bulk's operation.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    user_equipment.UserEquipment.bulk_user_equipment_operation,
  - Paths used are
    post /api/v1/fiveg/user-equipment/bulk,
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.user_equipment_bulk:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    ItemList:
      - description: string
        deviceGroup: string
        id: string
        imei: string
    operation: string
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string"
    }
"""
