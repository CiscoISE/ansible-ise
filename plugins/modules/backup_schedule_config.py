#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: backup_schedule_config
short_description: Resource module for Backup Schedule Config
description:
- Manage operation create of the resource Backup Schedule Config.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    backupDescription:
      description: Description of the backup.
      type: str
    backupEncryptionKey:
      description: The encyption key for the backed up file. Encryption key must satisfy
        the following criteria - Contains at least one uppercase letter A-Z, Contains
        at least one lowercase letter a-z, Contains at least one digit 0-9, Contain only
        A-Za-z0-9_#, Has at least 8 characters, Has not more than 15 characters, Must
        not contain 'CcIiSsCco', Must not begin with.
      type: str
    backupName:
      description: The backup file will get saved with this name.
      type: str
    endDate:
      description: End date of the scheduled backup job. Allowed format YYYY-MM-DD. End
        date is not required in case of ONE_TIME frequency.
      type: str
    frequency:
      description: Frequency with which the backup will get scheduled in the ISE node.
        Allowed values - ONE_TIME, DAILY, WEEKLY, MONTHLY.
      type: str
    repositoryName:
      description: Name of the repository where the generated backup file will get copied.
      type: str
    startDate:
      description: Start date for scheduling the backup job. Allowed format YYYY-MM-DD.
      type: str
    time:
      description: Time at which backup job get scheduled. Example- 12 00 AM.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.backup_schedule_config
# Reference by Internet resource
- name: Backup Schedule Config reference
  description: Complete reference of the Backup Schedule Config object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.backup_schedule_config:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    backupDescription: string
    backupEncryptionKey: string
    backupName: string
    endDate: string
    frequency: string
    repositoryName: string
    startDate: string
    time: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
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
