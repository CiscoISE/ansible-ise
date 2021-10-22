#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_administration_network_conditions
short_description: Resource module for Device Administration Network Conditions
description:
- Manage operations create, update and delete of the resource Device Administration Network Conditions.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  conditionType:
    description: This field determines the content of the conditions field.
    type: str
  conditions:
    description: Device Administration Network Conditions's conditions.
    suboptions:
      cliDnisList:
        description: <p>This field should contain a Caller ID (CLI), comma, and Called
          ID (DNIS).<br> Line format - Caller ID (CLI), Called ID (DNIS)</p>.
        elements: str
        type: list
      deviceGroupList:
        description: <p>This field should contain a tuple with NDG Root, comma, and
          an NDG (that it under the root).<br> Line format - NDG Root Name, NDG, Port</p>.
        elements: str
        type: list
      deviceList:
        description: <p>This field should contain Device-Name,port-number. The device
          name must be the same as the name field in a Network Device object.<br> Line
          format - Device Name,Port</p>.
        elements: str
        type: list
      ipAddrList:
        description: <p>This field should contain IP-address-or-subnet,port number<br>
          IP address can be IPV4 format (n.n.n.n) or IPV6 format (n n n n n n n n).<br>
          IP subnet can be IPV4 format (n.n.n.n/m) or IPV6 format (n n n n n n n n/m).<br>
          Line format - IP Address or subnet,Port</p>.
        elements: str
        type: list
      macAddrList:
        description: <p>This field should contain Endstation MAC address, comma, and
          Destination MAC addresses.<br> Each Max address must include twelve hexadecimal
          digits using formats nn nn nn nn nn nn or nn-nn-nn-nn-nn-nn or nnnn.nnnn.nnnn
          or nnnnnnnnnnnn.<br> Line format - Endstation MAC,Destination MAC </p>.
        elements: str
        type: list
    type: list
  description:
    description: Device Administration Network Conditions's description.
    type: str
  id:
    description: Device Administration Network Conditions's id.
    type: str
  link:
    description: Device Administration Network Conditions's link.
    suboptions:
      href:
        description: Device Administration Network Conditions's href.
        type: str
      rel:
        description: Device Administration Network Conditions's rel.
        type: str
      type:
        description: Device Administration Network Conditions's type.
        type: str
    type: dict
  name:
    description: Network Condition name.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Device Administration Network Conditions reference
  description: Complete reference of the Device Administration Network Conditions object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.device_administration_network_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    conditionType: string
    conditions:
    - cliDnisList:
      - string
      deviceGroupList:
      - string
      deviceList:
      - string
      ipAddrList:
      - string
      macAddrList:
      - string
    description: string
    id: string
    link:
      href: string
      rel: string
      type: string
    name: string

- name: Update by id
  cisco.ise.device_administration_network_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    conditionType: string
    conditions:
    - cliDnisList:
      - string
      deviceGroupList:
      - string
      deviceList:
      - string
      ipAddrList:
      - string
      macAddrList:
      - string
    description: string
    id: string
    link:
      href: string
      rel: string
      type: string
    name: string

- name: Delete by id
  cisco.ise.device_administration_network_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "conditionType": "string",
      "description": "string",
      "id": "string",
      "link": {
        "href": "string",
        "rel": "string",
        "type": "string"
      },
      "name": "string",
      "conditions": [
        {
          "cliDnisList": [
            "string"
          ],
          "ipAddrList": [
            "string"
          ],
          "macAddrList": [
            "string"
          ],
          "deviceGroupList": [
            "string"
          ],
          "deviceList": [
            "string"
          ]
        }
      ]
    }

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
  type: dict
  sample: >
    {
      "response": {
        "conditionType": "string",
        "description": "string",
        "id": "string",
        "link": {
          "href": "string",
          "rel": "string",
          "type": "string"
        },
        "name": "string",
        "conditions": [
          {
            "cliDnisList": [
              "string"
            ],
            "ipAddrList": [
              "string"
            ],
            "macAddrList": [
              "string"
            ],
            "deviceGroupList": [
              "string"
            ],
            "deviceList": [
              "string"
            ]
          }
        ]
      },
      "version": "string"
    }
"""
