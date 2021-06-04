#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sponsor_group
short_description: Resource module for Sponsor Group
description:
- Manage operations create, update and delete of the resource Sponsor Group.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  autoNotification:
    description: AutoNotification flag.
    type: bool
  createPermissions:
    description: Sponsor Group's createPermissions.
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
        description: Sponsor Group's defaultUsernamePrefix.
        type: str
      importBatchSizeLimit:
        description: Sponsor Group's importBatchSizeLimit.
        type: int
      randomBatchSizeLimit:
        description: Sponsor Group's randomBatchSizeLimit.
        type: int
      startDateFutureLimitDays:
        description: Sponsor Group's startDateFutureLimitDays.
        type: int
    type: dict
  description:
    description: Sponsor Group's description.
    type: str
  guestTypes:
    description: Sponsor Group's guestTypes.
    elements: str
    type: list
  id:
    description: Sponsor Group's id.
    type: str
  isDefaultGroup:
    description: IsDefaultGroup flag.
    type: bool
  isEnabled:
    description: IsEnabled flag.
    type: bool
  locations:
    description: Sponsor Group's locations.
    elements: str
    type: list
  managePermission:
    description: Sponsor Group's managePermission.
    type: str
  memberGroups:
    description: Sponsor Group's memberGroups.
    elements: str
    type: list
  name:
    description: Sponsor Group's name.
    type: str
  otherPermissions:
    description: Sponsor Group's otherPermissions.
    suboptions:
      canAccessViaRest:
        description: CanAccessViaRest flag.
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
      canSendSmsNotifications:
        description: CanSendSmsNotifications flag.
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
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sponsor_group
# Reference by Internet resource
- name: Sponsor Group reference
  description: Complete reference of the Sponsor Group object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sponsor_group:
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
    id: id
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

- name: Update by id
  cisco.ise.sponsor_group:
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
    id: id
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

- name: Delete by id
  cisco.ise.sponsor_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
