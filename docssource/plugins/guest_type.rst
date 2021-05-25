.. _guest_type:

==========
guest_type
==========

Documentation
=============

Resource module for Guest Type

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Guest Type.


Options
-------
::

  options:
    accessTime:
      suboptions:
        allowAccessOnSpecificDaysTimes:
          description: AllowAccessOnSpecificDaysTimes flag.
          type: bool
        dayTimeLimits:
          description: Guest Type's dayTimeLimits.
          suboptions:
          - suboptions:
              days:
                description: Guest Type's days.
                elements:
                  type: str
                type: list
              endTime:
                description: Guest Type's endTime.
                type: str
              startTime:
                description: Guest Type's startTime.
                type: str
            type: dict
          type: list
        defaultDuration:
          description: Guest Type's defaultDuration.
          type: int
        durationTimeUnit:
          description: Guest Type's durationTimeUnit.
          type: str
        fromFirstLogin:
          description: FromFirstLogin flag.
          type: bool
        maxAccountDuration:
          description: Guest Type's maxAccountDuration.
          type: int
      type: dict
    description:
      description: Guest Type's description.
      type: str
    expirationNotification:
      suboptions:
        advanceNotificationDuration:
          description: Guest Type's advanceNotificationDuration.
          type: int
        advanceNotificationUnits:
          description: Guest Type's advanceNotificationUnits.
          type: str
        emailText:
          description: Guest Type's emailText.
          type: str
        enableNotification:
          description: EnableNotification flag.
          type: bool
        sendEmailNotification:
          description: SendEmailNotification flag.
          type: bool
        sendSmsNotification:
          description: SendSmsNotification flag.
          type: bool
        smsText:
          description: Guest Type's smsText.
          type: str
      type: dict
    id:
      description: Guest Type's id.
      type: str
    loginOptions:
      suboptions:
        allowGuestPortalBypass:
          description: AllowGuestPortalBypass flag.
          type: bool
        failureAction:
          description: Guest Type's failureAction.
          type: str
        identityGroupId:
          description: Guest Type's identityGroupId.
          type: str
        limitSimultaneousLogins:
          description: LimitSimultaneousLogins flag.
          type: bool
        maxRegisteredDevices:
          description: Guest Type's maxRegisteredDevices.
          type: int
        maxSimultaneousLogins:
          description: Guest Type's maxSimultaneousLogins.
          type: int
      type: dict
    name:
      description: Guest Type's name.
      type: str
    sponsorGroups:
      description: Guest Type's sponsorGroups.
      elements:
        type: str
      type: list
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.guest_type
  - description: Complete reference of the Guest Type object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Guest Type reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.guest_type:
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
      description: Description
      expirationNotification:
        advanceNotificationDuration: 3
        advanceNotificationUnits: DAYS
        emailText: EmailText
        enableNotification: false
        sendEmailNotification: false
        sendSmsNotification: false
        smsText: SMS Text
      id: id
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

  - name: Update by id
    cisco.ise.guest_type:
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
      description: Description
      expirationNotification:
        advanceNotificationDuration: 3
        advanceNotificationUnits: DAYS
        emailText: EmailText
        enableNotification: false
        sendEmailNotification: false
        sendSmsNotification: false
        smsText: SMS Text
      id: id
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

  - name: Delete by id
    cisco.ise.guest_type:
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

    {
      "GuestType": {
        "id": "string",
        "name": "string",
        "description": "string",
        "accessTime": {
          "fromFirstLogin": true,
          "maxAccountDuration": 0,
          "durationTimeUnit": "string",
          "defaultDuration": 0,
          "allowAccessOnSpecificDaysTimes": true,
          "dayTimeLimits": [
            {
              "startTime": "string",
              "endTime": "string",
              "days": [
                "string"
              ]
            }
          ]
        },
        "loginOptions": {
          "limitSimultaneousLogins": true,
          "maxSimultaneousLogins": 0,
          "failureAction": "string",
          "maxRegisteredDevices": 0,
          "identityGroupId": "string",
          "allowGuestPortalBypass": true
        },
        "expirationNotification": {
          "enableNotification": true,
          "advanceNotificationDuration": 0,
          "advanceNotificationUnits": "string",
          "sendEmailNotification": true,
          "emailText": "string",
          "sendSmsNotification": true,
          "smsText": "string"
        },
        "sponsorGroups": [
          "string"
        ]
      }
    }
