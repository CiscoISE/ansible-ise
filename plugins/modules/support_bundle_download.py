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
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  dirPath:
    description: Directory absolute path. Defaults to the current working directory.
    type: str
  fileName:
    description: Support Bundle Download's fileName.
    type: str
  saveFile:
    description: Enable or disable automatic file creation of raw response.
    type: bool
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
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
    dirPath: /tmp/downloads/
    fileName: string
    saveFile: true

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
