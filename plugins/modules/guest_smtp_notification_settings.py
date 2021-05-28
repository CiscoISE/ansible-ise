#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: guest_smtp_notification_settings
short_description: Resource module for Guest Smtp Notification Settings
description:
- Manage operations create and update of the resource Guest Smtp Notification Settings.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  connectionTimeout:
    description: Guest Smtp Notification Settings's connectionTimeout.
    type: str
  defaultFromAddress:
    description: Guest Smtp Notification Settings's defaultFromAddress.
    type: str
  notificationEnabled:
    description: NotificationEnabled flag.
    type: bool
  password:
    description: Guest Smtp Notification Settings's password.
    type: str
  smtpPort:
    description: Guest Smtp Notification Settings's smtpPort.
    type: str
  smtpServer:
    description: Guest Smtp Notification Settings's smtpServer.
    type: str
  useDefaultFromAddress:
    description: UseDefaultFromAddress flag.
    type: bool
  usePasswordAuthentication:
    description: UsePasswordAuthentication flag.
    type: bool
  useTLSorSSLEncryption:
    description: UseTLSorSSLEncryption flag.
    type: bool
  userName:
    description: Guest Smtp Notification Settings's userName.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.guest_smtp_notification_settings
# Reference by Internet resource
- name: Guest Smtp Notification Settings reference
  description: Complete reference of the Guest Smtp Notification Settings object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.guest_smtp_notification_settings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    connectionTimeout: '60'
    defaultFromAddress: admin@ise.example.com
    notificationEnabled: true
    password: C1sco12345
    smtpPort: '465'
    smtpServer: smtp.example.com
    useDefaultFromAddress: false
    usePasswordAuthentication: true
    useTLSorSSLEncryption: true
    userName: smtp@example.com

- name: Update by id
  cisco.ise.guest_smtp_notification_settings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    connectionTimeout: '60'
    defaultFromAddress: admin@ise.example.com
    id: string
    notificationEnabled: true
    password: C1sco12345
    smtpPort: '465'
    smtpServer: smtp.example.com
    useDefaultFromAddress: false
    usePasswordAuthentication: true
    useTLSorSSLEncryption: true
    userName: smtp@example.com

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
