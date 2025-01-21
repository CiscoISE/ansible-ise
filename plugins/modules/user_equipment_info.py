#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: user_equipment_info
short_description: Information module for User Equipment Info
description:
  - Get all User Equipment Info.
  - Get User Equipment Info by id.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  page:
    description:
      - Page query parameter. Page number.
    type: int
  size:
    description:
      - Size query parameter. Number of objects returned per page.
    type: int
  filter:
    description:
      - >
        Filter query parameter. .. Container **Simple filtering** should be available through the filter query string parameter. The structure
        of a filter is a triplet of field operator and value separated with dots. More than one filter can be sent. The logical operator common
        to ALL filter criteria will be by default AND, and can be changed by using the *"filterType=or"* query string parameter.
      - Each resource Data model description should specify if an attribute is a filtered field.
      - The 'EQ' operator describes 'Equals'.
      - The 'NEQ' operator describes 'Not Equals'.
      - The 'GT' operator describes 'Greater Than'.
      - The 'LT' operator describes 'Less Than'.
      - The 'STARTSW' operator describes 'Starts With'.
      - The 'NSTARTSW' operator describes 'Not Starts With'.
      - The 'ENDSW' operator describes 'Ends With'.
      - The 'NENDSW' operator describes 'Not Ends With'.
      - The 'CONTAINS' operator describes 'Contains'.
      - The 'NCONTAINS' operator describes 'Not Contains'.
    type: str
  filterType:
    description:
      - >
        FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and can be changed by using the
        parameter.
    type: str
  sort:
    description:
      - Sort query parameter. Sort type - asc or desc.
    type: str
  sortBy:
    description:
      - SortBy query parameter. Sort column by which objects needs to be sorted.
    type: str
  userEquipmentId:
    description:
      - UserEquipmentId path parameter. Unique ID for a user equipment object.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    user_equipment.UserEquipment.get_user_equipment_by_id,
    user_equipment.UserEquipment.get_user_equipments_generator,
  - Paths used are
    get /api/v1/fiveg/user-equipment,
    get /api/v1/fiveg/user-equipment/{userEquipmentId},
"""

EXAMPLES = r"""
- name: Get all User Equipment Info
  cisco.ise.user_equipment_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 0
    size: 0
    filter: string
    filterType: string
    sort: string
    sortBy: string
  register: result
- name: Get User Equipment Info by id
  cisco.ise.user_equipment_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    userEquipmentId: 7c9484cf-0ebc-47ad-a9ef-bc12729ed73b
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
ise_responses:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: list
  elements: dict
  sample: >
    [
      {}
    ]
"""
