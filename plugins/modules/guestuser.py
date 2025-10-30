#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: guestuser
short_description: Resource module for Guestuser
description:
  - Manage operation create of the resource Guestuser.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  customFields:
    description: Key value map.
    type: dict
  description:
    description: Description.
    type: str
  guestAccessInfo:
    description: Guestuser's guestAccessInfo.
    suboptions:
      fromDate:
        description: Guestuser's fromDate.
        type: str
      groupTag:
        description: Guestuser's groupTag.
        type: str
      location:
        description: Guestuser's location.
        type: str
      ssid:
        description: Guestuser's ssid.
        type: str
      toDate:
        description: Guestuser's toDate.
        type: str
      validDays:
        description: Number of days guest user is valid. To validate validDays property,
          ISE consider only date(not time) between fromDate and toDate properites.
        type: dict
    type: dict
  guestInfo:
    description: Guestuser's guestInfo.
    suboptions:
      company:
        description: Guestuser's company.
        type: str
      creationTime:
        description: Guestuser's creationTime.
        type: str
      emailAddress:
        description: Guestuser's emailAddress.
        type: str
      enabled:
        description: This field is only for Get operation not applicable for Create,
          Update operations.
        type: bool
      firstName:
        description: Guestuser's firstName.
        type: str
      lastName:
        description: Guestuser's lastName.
        type: str
      notificationLanguage:
        description: Guestuser's notificationLanguage.
        type: str
      password:
        description: Guestuser's password.
        type: str
      phoneNumber:
        description: Phone number should be E.164 format.
        type: str
      smsServiceProvider:
        description: Guestuser's smsServiceProvider.
        type: str
      userName:
        description: This field is applicable for Get and Create operations not applicable
          for Update operation.If account needs be created with mobile number, please
          provide mobile number here.
        type: str
    type: dict
  guestType:
    description: Guestuser's guestType.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  personBeingVisited:
    description: Guestuser's personBeingVisited.
    type: str
  portalId:
    description: This field is applicable only for Create and Update operations not
      applicable for Get operation.Portal ID will be used to fetch configuration from
      Portal if missing from the Payload. For example Notification Language will be
      fetched from Portal if missing.
    type: str
  reasonForVisit:
    description: Guestuser's reasonForVisit.
    type: str
  sponsorUserId:
    description: This field is applicable only for Get operation not applicable for
      Create and Update operations.
    type: str
  sponsorUserName:
    description: This field is applicable for Get and Create operations not applicable
      for Update operation.
    type: str
  status:
    description: This field is applicable only for Get operation not applicable for
      Create and Update operations.
    type: str
  statusReason:
    description: Guestuser's statusReason.
    type: str
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    guestuser.Guestuser.create_guestuser,
  - Paths used are
    post /guestuser/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.guestuser:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customFields:
      another key: and its value
      some key: some value
    description: 'ERS Example user '
    guestAccessInfo:
      fromDate: 07/29/2014 14:44
      location: San Jose
      toDate: 10/29/2014 17:30
      validDays: 90
    guestInfo:
      emailAddress: email@some.uri.com
      enabled: true
      password: asdlkj324ew
      phoneNumber: '+13211239034'
      smsServiceProvider: GLobal Default
      userName: DS3ewdsa34wWE
    guestType: Contractor
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    name: guestUser
    portalId: '23423432523'
    sponsorUserName: Mr Spons
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
