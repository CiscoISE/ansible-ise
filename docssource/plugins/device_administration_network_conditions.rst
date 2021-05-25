.. _device_administration_network_conditions:

========================================
device_administration_network_conditions
========================================

Documentation
=============

Resource module for Device Administration Network Conditions

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Device Administration Network Conditions.


Options
-------
::

  options:
    cliDnisList:
      description: Device Administration Network Conditions's cliDnisList.
      elements:
        type: str
      type: list
    conditionType:
      description: Device Administration Network Conditions's conditionType.
      type: str
    description:
      description: Device Administration Network Conditions's description.
      type: str
    deviceGroupList:
      description: Device Administration Network Conditions's deviceGroupList.
      elements:
        type: str
      type: list
    deviceList:
      description: Device Administration Network Conditions's deviceList.
      elements:
        type: str
      type: list
    id:
      description: Device Administration Network Conditions's id.
      type: str
    ipAddrList:
      description: Device Administration Network Conditions's ipAddrList.
      elements:
        type: str
      type: list
    macAddrList:
      description: Device Administration Network Conditions's macAddrList.
      elements:
        type: str
      type: list
    name:
      description: Device Administration Network Conditions's name.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.device_administration_network_conditions
  - description: Complete reference of the Device Administration Network Conditions
      object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Device Administration Network Conditions reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.device_administration_network_conditions:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      {}

  - name: Update by id
    cisco.ise.device_administration_network_conditions:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      cliDnisList:
      - string
      conditionType: string
      description: string
      deviceGroupList:
      - string
      deviceList:
      - string
      id: string
      ipAddrList:
      - string
      macAddrList:
      - string
      name: string

  - name: Delete by id
    cisco.ise.device_administration_network_conditions:
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

    {
      "name": "string",
      "id": "string",
      "description": "string",
      "conditionType": "string",
      "ipAddrList": [
        "string"
      ],
      "macAddrList": [
        "string"
      ],
      "cliDnisList": [
        "string"
      ],
      "deviceList": [
        "string"
      ],
      "deviceGroupList": [
        "string"
      ]
    }

Sample 2:

.. code-block:: json

    {
      "name": "string",
      "id": "string",
      "description": "string",
      "conditionType": "string",
      "ipAddrList": [
        "string"
      ],
      "macAddrList": [
        "string"
      ],
      "cliDnisList": [
        "string"
      ],
      "deviceList": [
        "string"
      ],
      "deviceGroupList": [
        "string"
      ]
    }

Sample 3:

.. code-block:: json

    {
      "id": "string"
    }
