.. _guest_ssid:

==========
guest_ssid
==========

Documentation
=============

Resource module for Guest Ssid

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Guest Ssid.


Options
-------
::

  options:
    id:
      description: Guest Ssid's id.
      type: str
    name:
      description: Guest Ssid's name.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.guest_ssid
  - description: Complete reference of the Guest Ssid object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Guest Ssid reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.guest_ssid:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      id: id
      name: ssid value

  - name: Update by id
    cisco.ise.guest_ssid:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      id: id
      name: ssid value

  - name: Delete by id
    cisco.ise.guest_ssid:
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
