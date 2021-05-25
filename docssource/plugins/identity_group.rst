.. _identity_group:

==============
identity_group
==============

Documentation
=============

Resource module for Identity Group

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Identity Group.


Options
-------
::

  options:
    description:
      description: Identity Group's description.
      type: str
    id:
      description: Identity Group's id.
      type: str
    name:
      description: Identity Group's name.
      type: str
    systemDefined:
      description: SystemDefined flag.
      type: bool
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.identity_group
  - description: Complete reference of the Identity Group object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Identity Group reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.identity_group:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: 'Identity Group for Profile: Cisco-Meraki-Device'
      id: 1e2700a0-8c00-11e6-996c-525400b48521
      name: Cisco-Meraki-Device
      systemDefined: true

  - name: Update by id
    cisco.ise.identity_group:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: 'Identity Group for Profile: Cisco-Meraki-Device'
      id: 1e2700a0-8c00-11e6-996c-525400b48521
      name: Cisco-Meraki-Device
      systemDefined: true

  - name: Delete by id
    cisco.ise.identity_group:
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
