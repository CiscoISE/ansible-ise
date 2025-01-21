#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: subscriber_info
short_description: Information module for Subscriber
description:
  - Get all Subscriber.
  - Get Subscriber by id.
version_added: '2.8.0'
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
  subscriberId:
    description:
      - SubscriberId path parameter. Unique id for a subscriber object.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    subscriber.Subscriber.get_all_subscribers_generator,
    subscriber.Subscriber.get_subscriber_by_id,
  - Paths used are
    get /api/v1/fiveg/subscriber,
    get /api/v1/fiveg/subscriber/{subscriberId},
"""

EXAMPLES = r"""
- name: Get all Subscriber
  cisco.ise.subscriber_info:
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
- name: Get Subscriber by id
  cisco.ise.subscriber_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    subscriberId: string
  register: result
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
ise_responses:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
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
    ]
"""
