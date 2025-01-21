#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: user_equipment_imei_info
short_description: Information module for User Equipment Imei Info
description:
  - Get User Equipment Imei Info by id.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  imei:
    description:
      - Imei path parameter. IMEI for the user equipment object.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    user_equipment.UserEquipment.get_user_equipment_by_i_m_e_i,
  - Paths used are
    get /api/v1/fiveg/user-equipment/imei/{imei},
"""

EXAMPLES = r"""
- name: Get User Equipment Imei Info by id
  cisco.ise.user_equipment_imei_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    imei: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
