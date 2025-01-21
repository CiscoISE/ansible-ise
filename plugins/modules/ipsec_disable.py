#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: ipsec_disable
short_description: Resource module for Ipsec Disable
description:
  - Manage operation update of the resource Ipsec Disable.
  - Disables an enabled IPsec node connection.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  hostName:
    description: HostName path parameter. Hostname of the deployed node.
    type: str
  nadIp:
    description: NadIp path parameter. IP address of the NAD.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    native_ipsec.NativeIpsec.disable_ipsec_connection,
  - Paths used are
    put /api/v1/ipsec/disable/{hostName}/{nadIp},
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.ipsec_disable:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    hostName: string
    nadIp: string
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
ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: dict
  sample: >
    {
      "message": "string"
    }
"""
