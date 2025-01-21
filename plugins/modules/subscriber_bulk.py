#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: subscriber_bulk
short_description: Resource module for Subscriber Bulk
description:
  - Manage operation create of the resource Subscriber Bulk.
version_added: '2.8.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  ItemList:
    description: Subscriber Bulk's ItemList.
    elements: dict
    suboptions:
      enabled:
        description: Subscriber is enabled or not.
        type: bool
      friendlyName:
        description: Friendly name for the subscriber.
        type: str
      id:
        description: Subscriber Bulk's id.
        type: str
      identityGroups:
        description: Identity Group(s). With more than one idGroups it needs to be comma seperated.
        type: str
      imeis:
        description: Comma separated IMEIs to be attached to the subscriber.
        type: str
      imsi:
        description: IMSI for Subscriber.
        type: str
      ki:
        description: KI.
        type: str
      opc:
        description: OPC.
        type: str
    type: list
  operation:
    description: Subscriber Bulk's operation.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    subscriber.Subscriber.bulk_subscriber_operation,
  - Paths used are
    post /api/v1/fiveg/subscriber/bulk,
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.subscriber_bulk:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    ItemList:
      - enabled: true
        friendlyName: string
        id: string
        identityGroups: string
        imeis: string
        imsi: string
        ki: string
        opc: string
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
