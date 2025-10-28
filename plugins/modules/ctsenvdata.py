#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: ctsenvdata
short_description: Resource module for Ctsenvdata
description:
- Manage operation create of the resource Ctsenvdata.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  capability:
    description: Allowed values ENV_DATA_BASIC, SG_TABLES, SGTAGS, SERVERS, SG_EPG_TRANSLATION.
    elements: str
    type: list
  deviceName:
    description: Ctsenvdata's deviceName.
    type: str
  deviceSGt:
    description: Ctsenvdata's deviceSGt.
    type: str
  policyVerId:
    description: Ctsenvdata's policyVerId.
    type: str
  refreshTimer:
    description: Ctsenvdata's refreshTimer.
    type: str
  servers:
    description: Ctsenvdata's servers.
    suboptions:
      certificate:
        description: Ctsenvdata's certificate.
        type: str
      hostName:
        description: Ctsenvdata's hostName.
        type: str
      ipv4:
        description: Ctsenvdata's ipv4.
        type: str
      port:
        description: Ctsenvdata's port.
        type: str
      serverName:
        description: Ctsenvdata's serverName.
        type: str
      serverType:
        description: Ctsenvdata's serverType.
        type: str
    type: dict
  sgts:
    description: Ctsenvdata's sgts.
    suboptions:
      genID:
        description: Ctsenvdata's genID.
        type: str
      securityGroupInfo:
        description: Ctsenvdata's securityGroupInfo.
        suboptions:
          genID:
            description: Ctsenvdata's genID.
            type: str
          sgtName:
            description: Ctsenvdata's sgtName.
            type: str
          sgtNumber:
            description: Ctsenvdata's sgtNumber.
            type: str
        type: dict
      securityGroupTable:
        description: Ctsenvdata's securityGroupTable.
        type: str
    type: dict
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    ctsenvdata.Ctsenvdata.create_ctsenvdata,

  - Paths used are
    post /ctsenvdata/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.ctsenvdata:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    capability:
    - SGTAGS
    - ENV_DATA_BASIC
    - SG_TABLES
    - SERVERS
    deviceName: tnad

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "operation": "string",
      "messages": [
        {
          "title": "string",
          "type": "string",
          "code": "string"
        }
      ]
    }
"""
