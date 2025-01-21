#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: reservation
short_description: Resource module for Reservation
description:
  - Manage operations create, update and delete of the resource Reservation.
  - Reserve given number of SGTs in a continuous range for the given Client.
  - Delete the reserved range of SGT for the given Client.
  - Update the reserved ranges of a specific Client by giving the custom start and end index.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  clientID:
    description: ClientID path parameter. Unique name for a Client.
    type: str
  clientName:
    description: Name of the given client.
    type: str
  endIndex:
    description: End index of the reserved range.
    type: int
  numberOfTags:
    description: Nummber of tags required to be reserved in ISE.
    type: int
  startIndex:
    description: Start index of the reserved range.
    type: int
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    sgt_range_reservation.SgtRangeReservation.delete_sgt_reserve_range,
    sgt_range_reservation.SgtRangeReservation.reserve_sgt_range,
    sgt_range_reservation.SgtRangeReservation.update_reserved_range,
  - Paths used are
    post /api/v1/sgt/reservation/reserveRange,
    delete /api/v1/sgt/reservation/{clientID},
    put /api/v1/sgt/reservation/{clientID},
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.reservation:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    clientName: string
    numberOfTags: 0
- name: Update by id
  cisco.ise.reservation:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    clientID: string
    endIndex: 0
    startIndex: 0
- name: Delete by id
  cisco.ise.reservation:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    clientID: string
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "clientID": "string",
      "clientName": "string",
      "endIndex": 0,
      "startIndex": 0
    }
ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
"""
