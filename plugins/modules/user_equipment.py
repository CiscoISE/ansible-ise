#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: user_equipment
short_description: Resource module for User Equipment
description:
  - Manage operations create, update and delete of the resource User Equipment.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description for User Equipment.
    type: str
  deviceGroup:
    description: Device or Endpoint Group.
    type: str
  imei:
    description: IMEI for User Equipment.
    type: str
  userEquipmentId:
    description: UserEquipmentId path parameter. Unique ID for a user equipment object.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    user_equipment.UserEquipment.create_user_equipment,
    user_equipment.UserEquipment.delete_user_equipment,
    user_equipment.UserEquipment.update_user_equipment,
  - Paths used are
    post /api/v1/fiveg/user-equipment,
    delete /api/v1/fiveg/user-equipment/{userEquipmentId},
    put /api/v1/fiveg/user-equipment/{userEquipmentId},
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.user_equipment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    deviceGroup: string
    imei: string
- name: Update by id
  cisco.ise.user_equipment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    deviceGroup: string
    userEquipmentId: 7c9484cf-0ebc-47ad-a9ef-bc12729ed73b
- name: Delete by id
  cisco.ise.user_equipment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    userEquipmentId: 7c9484cf-0ebc-47ad-a9ef-bc12729ed73b
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
