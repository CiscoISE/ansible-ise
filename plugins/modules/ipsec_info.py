#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: ipsec_info
short_description: Information module for Ipsec Info
description:
  - Get all Ipsec Info.
  - Get Ipsec Info by id.
  - Returns all the IPsec enabled nodes with configuration details.
  - Returns the IPsec configuration details of a given node with the hostname and the NAD IP.
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
      - >
        SortBy query parameter. Sort column - The IPsec enabled nodes are sorted based on the columns. This is applicable for the field - hostName.
    type: str
  hostName:
    description:
      - HostName path parameter. Hostname of the deployed node.
    type: str
  nadIp:
    description:
      - NadIp path parameter. IP address of the NAD.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    native_ipsec.NativeIpsec.get_ipsec_enabled_nodes_generator,
    native_ipsec.NativeIpsec.get_ipsec_node,
  - Paths used are
    get /api/v1/ipsec,
    get /api/v1/ipsec/{hostName}/{nadIp},
"""

EXAMPLES = r"""
- name: Get all Ipsec Info
  cisco.ise.ipsec_info:
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
- name: Get Ipsec Info by id
  cisco.ise.ipsec_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    hostName: string
    nadIp: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "authType": "string",
      "certId": "string",
      "configureVti": true,
      "createTime": "string",
      "espAhProtocol": "string",
      "hostName": "string",
      "id": "string",
      "iface": "string",
      "ikeReAuthTime": 0,
      "ikeVersion": "string",
      "link": {
        "href": "string",
        "rel": "string",
        "type": "string"
      },
      "localInternalIp": "string",
      "modeOption": "string",
      "nadIp": "string",
      "phaseOneDHGroup": "string",
      "phaseOneEncryptionAlgo": "string",
      "phaseOneHashAlgo": "string",
      "phaseOneLifeTime": 0,
      "phaseTwoDHGroup": "string",
      "phaseTwoEncryptionAlgo": "string",
      "phaseTwoHashAlgo": "string",
      "phaseTwoLifeTime": 0,
      "psk": "string",
      "remotePeerInternalIp": "string",
      "status": "string",
      "updateTime": "string"
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
        "authType": "string",
        "certId": "string",
        "configureVti": true,
        "createTime": "string",
        "espAhProtocol": "string",
        "hostName": "string",
        "id": "string",
        "iface": "string",
        "ikeReAuthTime": 0,
        "ikeVersion": "string",
        "link": {
          "href": "string",
          "rel": "string",
          "type": "string"
        },
        "localInternalIp": "string",
        "modeOption": "string",
        "nadIp": "string",
        "phaseOneDHGroup": "string",
        "phaseOneEncryptionAlgo": "string",
        "phaseOneHashAlgo": "string",
        "phaseOneLifeTime": 0,
        "phaseTwoDHGroup": "string",
        "phaseTwoEncryptionAlgo": "string",
        "phaseTwoHashAlgo": "string",
        "phaseTwoLifeTime": 0,
        "psk": "string",
        "remotePeerInternalIp": "string",
        "status": "string",
        "updateTime": "string"
      }
    ]
"""
