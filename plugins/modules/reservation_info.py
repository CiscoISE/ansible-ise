#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: reservation_info
short_description: Information module for Reservation Info
description:
  - Get all Reservation Info.
  - Get Reservation Info by id.
  - Get all the reserved Security Group tag ranges in ISE.
  - Get the reserved range of SGT for the specific client which is passed in the URL.
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
  clientID:
    description:
      - ClientID path parameter. Unique name for a Client.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    sgt_range_reservation.SgtRangeReservation.get_sgt_reserved_range,
    sgt_range_reservation.SgtRangeReservation.get_sgt_reserved_ranges_generator,
  - Paths used are
    get /api/v1/sgt/reservation,
    get /api/v1/sgt/reservation/{clientID},
"""

EXAMPLES = r"""
- name: Get all Reservation Info
  cisco.ise.reservation_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 0
    size: 0
  register: result
- name: Get Reservation Info by id
  cisco.ise.reservation_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    clientID: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "clientId": "string",
      "clientName": "string",
      "endIndex": 0,
      "startIndex": 0
    }
ise_responses:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: list
  elements: dict
  sample: >
    [
      {
        "clientId": "string",
        "clientName": "string",
        "endIndex": 0,
        "startIndex": 0
      }
    ]
"""
