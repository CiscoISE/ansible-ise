#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: supportbundle
short_description: Resource module for Supportbundle
description:
- Manage operation create of the resource Supportbundle.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description.
    type: str
  hostName:
    description: This parameter is hostName only, xxxx of xxxx.yyy.zz.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  supportBundleIncludeOptions:
    description: Supportbundle's supportBundleIncludeOptions.
    suboptions:
      IncludeConfigDB:
        description: Set to include Config DB in Support Bundle.
        type: bool
      fromDate:
        description: Date from where support bundle should include the logs.
        type: dict
      includeCoreFiles:
        description: Set to include Core files in Support Bundle.
        type: bool
      includeDebugLogs:
        description: Set to include Debug logs in Support Bundle.
        type: bool
      includeLocalLogs:
        description: Set to include Local logs in Support Bundle.
        type: bool
      includeSystemLogs:
        description: Set to include System logs in Support Bundle.
        type: bool
      mntLogs:
        description: Set to include Monitoring and troublshooting logs in Support Bundle.
        type: bool
      policyXml:
        description: Set to include Policy XML in Support Bundle.
        type: bool
      toDate:
        description: Date upto where support bundle should include the logs.
        type: dict
    type: dict
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    supportbundle.Supportbundle.create_supportbundle,

  - Paths used are
    post /supportbundle/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.supportbundle:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    description: Support Bundle Generation
    hostName: sampleHost
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    name: supportBundle
    supportBundleIncludeOptions:
      fromDate: 04/21/2019
      includeConfigDB: true
      includeCoreFiles: true
      includeDebugLogs: true
      includeLocalLogs: true
      includeSystemLogs: true
      mntLogs: true
      policyXml: true
      toDate: 04/22/2019

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
