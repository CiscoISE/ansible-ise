#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: support_bundle_download
short_description: Resource module for Support Bundle Download
description:
- Manage operation update of the resource Support Bundle Download.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  fileName:
    description: Support Bundle Download's fileName.
    type: str
  dirPath:
    description: Directory absolute path. Defaults to current working directory
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.support_bundle_download
# Reference by Internet resource
- name: Support Bundle Download reference
  description: Complete reference of the Support Bundle Download object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.support_bundle_download:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    fileName: Support bundle file name to be picked for download
    dirPath: '/tmp'

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
