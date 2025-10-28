#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: internaluser
short_description: Resource module for Internaluser
description:
- Manage operation create of the resource Internaluser.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  accountNameAlias:
    description: The Account Name Alias will be used to send email notifications about
      password expiration.
    type: str
  changePassword:
    description: ChangePassword flag.
    type: bool
  customAttributes:
    description: Key value map.
    type: str
  dateCreated:
    description: The date of the user creation, formatted as 'YYYY-MM-DD'. Read-only.
    type: str
  dateModified:
    description: The date of the last user modification by admin, formatted as 'YYYY-MM-DD'.
      Read-only.
    type: str
  daysForPasswordExpiration:
    description: This field is for read only.
    type: float
  description:
    description: Description.
    type: str
  email:
    description: Internaluser's email.
    type: str
  enablePassword:
    description: EnablePassword field is added in ISE 2.0 to support T+.
    type: str
  enabled:
    description: Whether the user is enabled/disabled.To use it as filter, the values
      should be 'Enabled' or 'Disabled'. The values are case sensitive.For example,
      'ERSObjectURL?filter=enabled.EQ.Enabled'.
    type: bool
  expiryDate:
    description: To store the internal user's expiry date information. It's format is
      = 'YYYY-MM-DD'.
    type: str
  expiryDateEnabled:
    description: ExpiryDateEnabled flag.
    type: bool
  firstName:
    description: Internaluser's firstName.
    type: str
  id:
    description: Id.
    type: str
  identityGroups:
    description: CSV of identity group IDs.
    type: str
  lastName:
    description: Internaluser's lastName.
    type: str
  name:
    description: Name.
    type: str
  password:
    description: Internaluser's password.
    type: str
  passwordIDStore:
    description: The id store where the internal user's password is kept.
    type: str
  passwordNeverExpires:
    description: Set TRUE to indicate the user password never expires. This will not
      apply to Users who are also ISE Admins.
    type: bool
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    internaluser.Internaluser.create_internaluser,

  - Paths used are
    post /internaluser/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.internaluser:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accountNameAlias: accountNameAlias
    changePassword: true
    customAttributes:
      key1: value1
      key2: value3
    dateCreated: '2015-12-15'
    dateModified: '2015-12-20'
    daysForPasswordExpiration: 60
    description: description
    email: email@domain.com
    enablePassword: enablePassword
    enabled: true
    expiryDate: '2016-12-11'
    expiryDateEnabled: false
    firstName: firstName
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    identityGroups: CSV of identity groups IDs
    lastName: lastName
    name: name
    password: password
    passwordIDStore: Internal Users
    passwordNeverExpires: false

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
