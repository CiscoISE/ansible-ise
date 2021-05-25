.. _internal_user:

=============
internal_user
=============

Documentation
=============

Resource module for Internal User

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Internal User.


Options
-------
::

  options:
    changePassword:
      description: ChangePassword flag.
      type: bool
    customAttributes:
      suboptions:
        key1:
          description: Internal User's key1.
          type: str
        key2:
          description: Internal User's key2.
          type: str
      type: dict
    description:
      description: Internal User's description.
      type: str
    email:
      description: Internal User's email.
      type: str
    enablePassword:
      description: Internal User's enablePassword.
      type: str
    enabled:
      description: Enabled flag.
      type: bool
    expiryDate:
      description: Internal User's expiryDate.
      type: str
    expiryDateEnabled:
      description: ExpiryDateEnabled flag.
      type: bool
    firstName:
      description: Internal User's firstName.
      type: str
    id:
      description: Internal User's id.
      type: str
    identityGroups:
      description: Internal User's identityGroups.
      type: str
    lastName:
      description: Internal User's lastName.
      type: str
    name:
      description: Internal User's name.
      type: str
    password:
      description: Internal User's password.
      type: str
    passwordIDStore:
      description: Internal User's passwordIDStore.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.internal_user
  - description: Complete reference of the Internal User object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Internal User reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.internal_user:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: '{{description}}'
      name: '{{username}}'
      password: '{{password}}'

  - name: Update by id
    cisco.ise.internal_user:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: New description
      id: string

  - name: Delete by id
    cisco.ise.internal_user:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: absent
      id: string

  - name: Update by name
    cisco.ise.internal_user:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      name: string
      password: Ch@ngedP@55w0rd

  - name: Delete by name
    cisco.ise.internal_user:
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
