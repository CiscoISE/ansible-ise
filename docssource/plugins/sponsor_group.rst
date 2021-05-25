.. _sponsor_group:

=============
sponsor_group
=============

Documentation
=============

Resource module for Sponsor Group

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Sponsor Group.


Options
-------
::

  options:
    autoNotification:
      description: AutoNotification flag.
      type: bool
    createPermissions:
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
      elements:
        type: str
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
      elements:
        type: str
      type: list
    managePermission:
      description: Sponsor Group's managePermission.
      type: str
    memberGroups:
      description: Sponsor Group's memberGroups.
      elements:
        type: str
      type: list
    name:
      description: Sponsor Group's name.
      type: str
    otherPermissions:
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
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.sponsor_group
  - description: Complete reference of the Sponsor Group object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Sponsor Group reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.sponsor_group:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      autoNotification: true
      createPermissions:
        canCreateRandomAccounts: true
        canImportMultipleAccounts: true
        canSetFutureStartDate: true
        canSpecifyUsernamePrefix: true
        defaultUsernamePrefix: string
        importBatchSizeLimit: 0
        randomBatchSizeLimit: 0
        startDateFutureLimitDays: 0
      description: string
      guestTypes:
      - string
      id: string
      isDefaultGroup: true
      isEnabled: true
      locations:
      - string
      managePermission: string
      memberGroups:
      - string
      name: string
      otherPermissions:
        canAccessViaRest: true
        canApproveSelfregGuests: true
        canDeleteGuestAccounts: true
        canExtendGuestAccounts: true
        canReinstateSuspendedAccounts: true
        canResetGuestPasswords: true
        canSendSmsNotifications: true
        canSuspendGuestAccounts: true
        canUpdateGuestContactInfo: true
        canViewGuestPasswords: true
        limitApprovalToSponsorsGuests: true
        requireSuspensionReason: true

  - name: Update by id
    cisco.ise.sponsor_group:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      autoNotification: true
      createPermissions:
        canCreateRandomAccounts: true
        canImportMultipleAccounts: true
        canSetFutureStartDate: true
        canSpecifyUsernamePrefix: true
        defaultUsernamePrefix: string
        importBatchSizeLimit: 0
        randomBatchSizeLimit: 0
        startDateFutureLimitDays: 0
      description: string
      guestTypes:
      - string
      id: string
      isDefaultGroup: true
      isEnabled: true
      locations:
      - string
      managePermission: string
      memberGroups:
      - string
      name: string
      otherPermissions:
        canAccessViaRest: true
        canApproveSelfregGuests: true
        canDeleteGuestAccounts: true
        canExtendGuestAccounts: true
        canReinstateSuspendedAccounts: true
        canResetGuestPasswords: true
        canSendSmsNotifications: true
        canSuspendGuestAccounts: true
        canUpdateGuestContactInfo: true
        canViewGuestPasswords: true
        limitApprovalToSponsorsGuests: true
        requireSuspensionReason: true

  - name: Delete by id
    cisco.ise.sponsor_group:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: absent
      id: string



Return
=======

ise_response
------------

- **Description**: A dictionary or list with the response returned by the Cisco ISE Python SDK
- **Returned**: always
- **Type**: complex

**Samples**

Sample 1:

.. code-block:: json

    {}

Sample 2:

.. code-block:: json

    {}

Sample 3:

.. code-block:: json

    {}
