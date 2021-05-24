#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: network_access_network_condition_info
short_description: Information module for Network Access Network Condition
description:
- Get all Network Access Network Condition.
- Get Network Access Network Condition by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter. Condition id.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_network_condition
# Reference by Internet resource
- name: Network Access Network Condition reference
  description: Complete reference of the Network Access Network Condition object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Network Access Network Condition
  cisco.ise.network_access_network_condition_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result

- name: Get Network Access Network Condition by id
  cisco.ise.network_access_network_condition_info
    id: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'name': 'string', 'id': 'string', 'description': 'string', 'conditionType': 'string', 'ipAddrList': ['string'], 'macAddrList': ['string'], 'cliDnisList': ['string'], 'deviceList': ['string'], 'deviceGroupList': ['string']}
  - [{'name': 'string', 'id': 'string', 'description': 'string', 'conditionType': 'string'}]
"""
