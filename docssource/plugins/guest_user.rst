.. _guest_user:

==========
guest_user
==========

Documentation
=============

Resource module for Guest User

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Guest User.


Options
-------
::

  options:
    guestAccessInfo:
      suboptions:
        fromDate:
          description: Guest User's fromDate.
          type: str
        location:
          description: Guest User's location.
          type: str
        toDate:
          description: Guest User's toDate.
          type: str
        validDays:
          description: Guest User's validDays.
          type: int
      type: dict
    guestInfo:
      suboptions:
        emailAddress:
          description: Guest User's emailAddress.
          type: str
        enabled:
          description: Guest User's enabled.
          type: str
        firstName:
          description: Guest User's firstName.
          type: str
        lastName:
          description: Guest User's lastName.
          type: str
        password:
          description: Guest User's password.
          type: str
        userName:
          description: Guest User's userName.
          type: str
      type: dict
    guestType:
      description: Guest User's guestType.
      type: str
    id:
      description: Guest User's id.
      type: str
    name:
      description: Name path parameter.
      type: string
    portalId:
      description: Guest User's portalId.
      type: str
    reasonForVisit:
      description: Guest User's reasonForVisit.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.guest_user
  - description: Complete reference of the Guest User object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Guest User reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.guest_user:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      guestAccessInfo:
        fromDate: 04/27/2021 17:40
        location: San Jose
        toDate: 04/28/2021 17:40
        validDays: 1
      guestInfo:
        emailAddress: thomas@cisco.com
        enabled: 'true'
        firstName: Thomas
        lastName: Howard
        password: C1sco12345
        userName: 1homas
      guestType: Daily (default)
      portalId: bd48c1a1-9477-4746-8e40-e43d20c9f429
      reasonForVisit: ISE Guest Services

  - name: Update by id
    cisco.ise.guest_user:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      guestInfo:
        enabled: true
      guestType: Daily (default)
      id: 4cea2c31-605c-42d2-92d1-1e999b61aad0
      portalId: bd48c1a1-9477-4746-8e40-e43d20c9f429

  - name: Delete by id
    cisco.ise.guest_user:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: absent
      id: string

  - name: Update by name
    cisco.ise.guest_user:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      guestInfo:
        enabled: true
      guestType: Daily (default)
      id: 4cea2c31-605c-42d2-92d1-1e999b61aad0
      name: string
      portalId: bd48c1a1-9477-4746-8e40-e43d20c9f429

  - name: Delete by name
    cisco.ise.guest_user:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: absent
      name: string



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

Sample 4:

.. code-block:: json

    {}

Sample 5:

.. code-block:: json

    {}
