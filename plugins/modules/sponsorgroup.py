#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sponsorgroup
short_description: Resource module for Sponsorgroup
description:
  - Manage operation create of the resource Sponsorgroup.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  autoNotification:
    description: AutoNotification flag.
    type: bool
  createPermissions:
    description: Sponsorgroup's createPermissions.
    suboptions:
      canCreateRandomAccounts:
        description: CanCreateRandomAccounts flag.
        type: bool
      canImportMultipleAccounts:
        description: CanImportMultipleAccounts flag.
        type: bool
      canSetFutureStartDate:
        description: CanSetFutureStartDate flag.
        type: bool
      canSpecifyUsernamePrefix:
        description: CanSpecifyUsernamePrefix flag.
        type: bool
      defaultUsernamePrefix:
        description: Sponsorgroup's defaultUsernamePrefix.
        type: str
      importBatchSizeLimit:
        description: Sponsorgroup's importBatchSizeLimit.
        type: float
      randomBatchSizeLimit:
        description: Sponsorgroup's randomBatchSizeLimit.
        type: float
      startDateFutureLimitDays:
        description: Sponsorgroup's startDateFutureLimitDays.
        type: float
    type: dict
  description:
    description: Description.
    type: str
  guestTypes:
    description: Sponsorgroup's guestTypes.
    elements: str
    type: list
  id:
    description: Id.
    type: str
  isDefaultGroup:
    description: IsDefaultGroup flag.
    type: bool
  isEnabled:
    description: IsEnabled flag.
    type: bool
  locations:
    description: Sponsorgroup's locations.
    elements: str
    type: list
  managePermission:
    description: Allowed values allAccounts, groupAccounts, ownAccounts.
    type: dict
  memberGroups:
    description: Sponsorgroup's memberGroups.
    elements: str
    type: list
  name:
    description: Name.
    type: str
  otherPermissions:
    description: Sponsorgroup's otherPermissions.
    suboptions:
      canAccessViaREST:
        description: CanAccessViaREST flag.
        type: bool
      canApproveSelfregGuests:
        description: CanApproveSelfregGuests flag.
        type: bool
      canDeleteGuestAccounts:
        description: CanDeleteGuestAccounts flag.
        type: bool
      canExtendGuestAccounts:
        description: CanExtendGuestAccounts flag.
        type: bool
      canReinstateSuspendedAccounts:
        description: CanReinstateSuspendedAccounts flag.
        type: bool
      canResetGuestPasswords:
        description: CanResetGuestPasswords flag.
        type: bool
      canSendSMSNotifications:
        description: CanSendSMSNotifications flag.
        type: bool
      canSuspendGuestAccounts:
        description: CanSuspendGuestAccounts flag.
        type: bool
      canUpdateGuestContactInfo:
        description: CanUpdateGuestContactInfo flag.
        type: bool
      canViewGuestPasswords:
        description: CanViewGuestPasswords flag.
        type: bool
      limitApprovalToSponsorsGuests:
        description: LimitApprovalToSponsorsGuests flag.
        type: bool
      requireSuspensionReason:
        description: RequireSuspensionReason flag.
        type: bool
    type: dict
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    sponsorgroup.Sponsorgroup.create_sponsorgroup,
  - Paths used are
    post /sponsorgroup/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.sponsorgroup:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    autoNotification: false
    createPermissions:
      canCreateRandomAccounts: true
      canImportMultipleAccounts: true
      canSetFutureStartDate: false
      canSpecifyUsernamePrefix: false
      defaultUsernamePrefix: ''
      importBatchSizeLimit: 20
      randomBatchSizeLimit: 30
      startDateFutureLimitDays: 10
    description: description
    guestTypes:
      - Contractor (default)
      - Daily (default)
      - Weekly (default)
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    isDefaultGroup: false
    isEnabled: true
    locations:
      - San Jose
    managePermission: ALLACCOUNTS
    memberGroups:
      - ALL_ACCOUNTS (default)
    name: name
    otherPermissions:
      canAccessViaRest: false
      canApproveSelfregGuests: false
      canDeleteGuestAccounts: false
      canExtendGuestAccounts: false
      canReinstateSuspendedAccounts: false
      canResetGuestPasswords: false
      canSendSmsNotifications: false
      canSuspendGuestAccounts: false
      canUpdateGuestContactInfo: false
      canViewGuestPasswords: false
      limitApprovalToSponsorsGuests: false
      requireSuspensionReason: false
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
