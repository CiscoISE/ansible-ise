#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: guestsmtpnotificationsettings
short_description: Resource module for Guestsmtpnotificationsettings
description:
  - Manage operation create of the resource Guestsmtpnotificationsettings.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  connectionTimeout:
    description: Interval in seconds for all the SMTP client connections.
    type: str
  defaultFromAddress:
    description: The default From email address to be used to send emails from.
    type: str
  description:
    description: Description.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  notificationEnabled:
    description: Indicates if the email notification service is to be enabled.
    type: bool
  password:
    description: Password of Secure SMTP server.
    type: str
  smtpPort:
    description: Port at which SMTP Secure Server is listening.
    type: str
  smtpServer:
    description: The SMTP server ip address or fqdn such as outbound.mycompany.com.
    type: str
  useDefaultFromAddress:
    description: If the default from address should be used rather than using a sponsor
      user email address.
    type: bool
  usePasswordAuthentication:
    description: If configured to true, SMTP server authentication will happen using
      username/password.
    type: bool
  useTLSorSSLEncryption:
    description: If configured to true, SMTP server authentication will happen using
      TLS/SSL.
    type: bool
  userName:
    description: Username of Secure SMTP server.
    type: str
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    guestsmtpnotificationsettings.Guestsmtpnotificationsettings.create_guestsmtpnotificationsettings,
  - Paths used are
    post /guestsmtpnotificationsettings/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.guestsmtpnotificationsettings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    connectionTimeout: '60'
    defaultFromAddress: donotreply@example.com
    notificationEnabled: true
    password: ''
    smtpPort: '25'
    smtpServer: ''
    useDefaultFromAddress: false
    usePasswordAuthentication: false
    useTLSorSSLEncryption: false
    userName: ''
"""
RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""
