#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: guesttype
short_description: Resource module for Guesttype
description:
- Manage operation create of the resource Guesttype.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  accessTime:
    description: Guesttype's accessTime.
    suboptions:
      allowAccessOnSpecificDaysTimes:
        description: Enable Specific Day Time Limits.
        type: bool
      dayTimeLimits:
        description: List of Time Ranges for account access.
        elements: dict
        type: list
      defaultDuration:
        description: Guesttype's defaultDuration.
        type: float
      durationTimeUnit:
        description: Allowed values are Days or Hours or Minutes.
        type: str
      fromFirstLogin:
        description: When Account Duration starts from first login or specified date.
        type: bool
      maxAccountDuration:
        description: Maximum value of Account Duration.
        type: float
    type: dict
  allowDynamicIdentityGroups:
    description: Enable the DynamicGroups Option.
    type: bool
  description:
    description: Description.
    type: str
  dynamicGroups:
    description: List of Dynamic Groups.
    elements: dict
    type: list
  expirationNotification:
    description: Guesttype's expirationNotification.
    suboptions:
      advanceNotificationDuration:
        description: Send Account Expiration Notification Duration before ( Days, Hours,
          Minutes ).
        type: float
      advanceNotificationUnits:
        description: Allowed values are Days, Hours, Minutes.
        type: str
      enableNotification:
        description: Enable Notification settings.
        type: bool
      sendEmailNotification:
        description: Enable Email Notification.
        type: bool
      sendSMSNotification:
        description: Maximum devices guests can register.
        type: float
    type: dict
  id:
    description: Id.
    type: str
  loginOptions:
    description: Guesttype's loginOptions.
    suboptions:
      allowGuestPortalBypass:
        description: AllowGuestPortalBypass flag.
        type: bool
      failureAction:
        description: When Guest Exceeds limit this action will be invoked, Allowed values
          are Disconnect_Oldest_Connection or Disconnect_Newest_Connection.
        type: str
      identityGroupId:
        description: ID of Guest Identity Group.
        type: str
      limitSimultaneousLogins:
        description: Enable Simultaneous Logins.
        type: bool
      maxRegisteredDevices:
        description: Maximum devices guests can register.
        type: float
      maxSimultaneousLogins:
        description: Number of Simultaneous Logins.
        type: float
    type: dict
  name:
    description: Name.
    type: str
  sponsorGroups:
    description: List of Sponsor Groups.
    elements: str
    type: list
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    guesttype.Guesttype.create_guesttype,

  - Paths used are
    post /guesttype/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.guesttype:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accessTime:
      allowAccessOnSpecificDaysTimes: false
      dayTimeLimits:
      - days:
        - Sunday
        - Tuesday
        endTime: '16:00'
        startTime: '12:00'
      defaultDuration: 90
      durationTimeUnit: DAYS
      fromFirstLogin: true
      maxAccountDuration: 365
    allowDynamicIdentityGroups: true
    description: Description
    dynamicGroups:
    - endpointIdentityGroupId: generatedID
      externalGroupName: ExternalServerName:GroupName
    expirationNotification:
      advanceNotificationDuration: 3
      advanceNotificationUnits: DAYS
      emailText: EmailText
      enableNotification: false
      sendEmailNotification: false
      sendSmsNotification: false
      smsText: SMS Text
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    loginOptions:
      allowGuestPortalBypass: false
      failureAction: Disconnect_Oldest_Connection
      identityGroupId: generatedID
      limitSimultaneousLogins: true
      maxRegisteredDevices: 5
      maxSimultaneousLogins: 3
    name: Name
    sponsorGroups:
    - Group1
    - Group2

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
