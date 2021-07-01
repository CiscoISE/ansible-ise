#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: support_bundle
short_description: Resource module for Support Bundle
description:
- Manage operation create of the resource Support Bundle.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  description:
    description: Support Bundle's description.
    type: str
  hostName:
    description: Support Bundle's hostName.
    type: str
  name:
    description: Support Bundle's name.
    type: str
  supportBundleIncludeOptions:
    description: Support Bundle's supportBundleIncludeOptions.
    suboptions:
      fromDate:
        description: Support Bundle's fromDate.
        type: str
      includeConfigDB:
        description: IncludeConfigDB flag.
        type: bool
      includeCoreFiles:
        description: IncludeCoreFiles flag.
        type: bool
      includeDebugLogs:
        description: IncludeDebugLogs flag.
        type: bool
      includeLocalLogs:
        description: IncludeLocalLogs flag.
        type: bool
      includeSystemLogs:
        description: IncludeSystemLogs flag.
        type: bool
      mntLogs:
        description: MntLogs flag.
        type: bool
      policyXml:
        description: PolicyXml flag.
        type: bool
      toDate:
        description: Support Bundle's toDate.
        type: str
    type: dict
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.support_bundle
# Reference by Internet resource
- name: Support Bundle reference
  description: Complete reference of the Support Bundle object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.support_bundle:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    description: Support Bundle Generation
    hostName: ise
    name: supportBundle
    supportBundleIncludeOptions:
      fromDate: 04/21/2021
      includeConfigDB: true
      includeCoreFiles: true
      includeDebugLogs: true
      includeLocalLogs: true
      includeSystemLogs: true
      mntLogs: true
      policyXml: true
      toDate: 04/22/2021

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
