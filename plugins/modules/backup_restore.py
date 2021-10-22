#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: backup_restore
short_description: Resource module for Backup Restore
description:
- Manage operation create of the resource Backup Restore.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  backupEncryptionKey:
    description: The encryption key which was provided at the time of taking backup.
    type: str
  repositoryName:
    description: Name of the configred repository where the backup file exists.
    type: str
  restoreFile:
    description: Name of the backup file to be restored on ISE node.
    type: str
  restoreIncludeAdeos:
    description: Determines whether the ADE-OS configure is restored. Possible values
      true, false.
    type: str
requirements:
- ciscoisesdk >= 1.1.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Backup Restore reference
  description: Complete reference of the Backup Restore object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.backup_restore:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    backupEncryptionKey: string
    repositoryName: string
    restoreFile: string
    restoreIncludeAdeos: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "message": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      },
      "version": "string"
    }
"""
