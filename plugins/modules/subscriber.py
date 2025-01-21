#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: subscriber
short_description: Resource module for Subscriber
description:
  - Manage operations create, update and delete of the resource Subscriber.
version_added: '2.8.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  enabled:
    description: Subscriber is enabled or not.
    type: bool
  friendlyName:
    description: Friendly name for the subscriber.
    type: str
  identityGroups:
    description: Identity Group(s). With more than one idGroups it needs to be comma seperated.
    type: str
  imeis:
    description: IMEI to be attached to the subscriber.
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
  subscriberId:
    description: SubscriberId path parameter. Unique id for a subscriber object.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    subscriber.Subscriber.create_subscriber,
    subscriber.Subscriber.delete_subscriber,
    subscriber.Subscriber.update_subscriber,
  - Paths used are
    post /api/v1/fiveg/subscriber,
    delete /api/v1/fiveg/subscriber/{subscriberId},
    put /api/v1/fiveg/subscriber/{subscriberId},
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.subscriber:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    enabled: true
    friendlyName: string
    identityGroups: string
    imeis: string
    imsi: string
    ki: string
    opc: string
- name: Update by id
  cisco.ise.subscriber:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    enabled: true
    friendlyName: string
    identityGroups: string
    imeis: string
    ki: string
    opc: string
    subscriberId: string
- name: Delete by id
  cisco.ise.subscriber:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    subscriberId: string
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
ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
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
      },
      "version": "string"
    }
"""
