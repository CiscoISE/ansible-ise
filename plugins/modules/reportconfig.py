#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: reportconfig
short_description: Resource module for Reportconfig
description:
  - Manage operation create of the resource Reportconfig.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  containsManualDefs:
    description: Reportconfig's containsManualDefs.
    type: str
  containsValues:
    description: Reportconfig's containsValues.
    type: str
  policyVerId:
    description: Reportconfig's policyVerId.
    type: str
  policyVerIdOnISE:
    description: Reportconfig's policyVerIdOnISE.
    type: str
  pullId:
    description: Reportconfig's pullId.
    type: str
  reportData:
    description: Reportconfig's reportData.
    suboptions:
      ctsMatrix:
        description: Reportconfig's ctsMatrix.
        type: str
    type: dict
  reportType:
    description: Allowed values DISABLED, DELTA_WITH_GEN_ID, DELTA_WITH_VALUES, FULL_WITH_GEN_ID,
      FULL_WITH_VALUES, FULL_INCLUDE_MANUAL_RULES, POLICY_VERSION_ID.
    type: str
  validationResult:
    description: Reportconfig's validationResult.
    type: str
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    reportconfig.Reportconfig.create_reportconfig,
  - Paths used are
    post /reportconfig/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.reportconfig:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    containsManualDefs: false
    containsValues: false
    policyVerId: 12-1-196a90e49e4
    pullId: '1729003030'
    reportData:
      ctsMatrix:
        policyType: steering
      sgtArr:
        - 0E
      sgts:
        - genID: '0'
          sgtNumber: '9'
    reportType: DELTA_WITH_GEN_ID
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
