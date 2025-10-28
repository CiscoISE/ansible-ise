#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: supportbundledownload
short_description: Resource module for Supportbundledownload
description:
- Manage operation update of the resource Supportbundledownload.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description.
    type: str
  fileName:
    description: File name along with path from where file needs to be downloaded.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    supportbundledownload.Supportbundledownload.update_supportbundledownload,

  - Paths used are
    put /supportbundledownload/,

"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.supportbundledownload:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    fileName: Support bundle file name to be picked for download

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "UpdatedFieldsList": {
        "updatedField": [
          {
            "field": "string",
            "oldValue": "string",
            "newValue": "string"
          }
        ]
      }
    }
"""
