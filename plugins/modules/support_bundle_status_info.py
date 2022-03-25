#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: support_bundle_status_info
short_description: Information module for Support Bundle Status
description:
- Get all Support Bundle Status.
- Get Support Bundle Status by id.
- This API allows the client to get a support bundle status by ID.
- This API allows the client to get all the support bundle status.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter.
    type: str
  page:
    description:
    - Page query parameter. Page number.
    type: int
  size:
    description:
    - Size query parameter. Number of objects returned per page.
    type: int
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    support_bundle_status.SupportBundleStatus.get_support_bundle_status_by_id,
    support_bundle_status.SupportBundleStatus.get_support_bundle_status_generator,

  - Paths used are
    get /ers/config/supportbundlestatus,
    get /ers/config/supportbundlestatus/{id},

"""

EXAMPLES = r"""
- name: Get all Support Bundle Status
  cisco.ise.support_bundle_status_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result

- name: Get Support Bundle Status by id
  cisco.ise.support_bundle_status_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "fileName": "string",
      "fileSize": 0,
      "hostName": "string",
      "message": "string",
      "startTime": "string",
      "status": "string",
      "link": {
        "rel": "string",
        "href": "string",
        "type": "string"
      }
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
        "id": "string",
        "name": "string",
        "description": "string",
        "fileName": "string",
        "fileSize": 0,
        "hostName": "string",
        "message": "string",
        "startTime": "string",
        "status": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""
