.. _network_device_group:

====================
network_device_group
====================

Documentation
=============

Resource module for Network Device Group

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Network Device Group.


Options
-------
::

  options:
    description:
      description: Network Device Group's description.
      type: str
    id:
      description: Id path parameter.
      type: string
    name:
      description: Network Device Group's name.
      type: str
    othername:
      description: Network Device Group's othername.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.network_device_group
  - description: Complete reference of the Network Device Group object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Device Group reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.network_device_group:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: '...'
      name: Device Type#All Device Types#SDWAN
      othername: Device Type

  - name: Update by id
    cisco.ise.network_device_group:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: SDWAN description
      id: string
      name: Device Type#All Device Types#SDWAN
      othername: Device Type

  - name: Delete by id
    cisco.ise.network_device_group:
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

    {
      "UpdatedFieldsList": {
        "updatedField": [
          {
            "field": "string",
            "oldValue": "string",
            "newValue": "string"
          }
        ]
      }
    }

Sample 3:

.. code-block:: json

    {}
