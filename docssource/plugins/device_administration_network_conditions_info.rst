.. _device_administration_network_conditions_info:

=============================================
device_administration_network_conditions_info
=============================================

Documentation
=============

Information module for Device Administration Network Conditions

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Device Administration Network Conditions.
- Get Device Administration Network Conditions by id.


Options
-------
::

  options:
    id:
      description:
      - Id path parameter. Condition id.
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

  - name: Get all Device Administration Network Conditions
    cisco.ise.device_administration_network_conditions_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
    register: result

  - name: Get Device Administration Network Conditions by id
    cisco.ise.device_administration_network_conditions_info
      id: string
    register: result



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

    [
      {
        "name": "string",
        "id": "string",
        "description": "string",
        "conditionType": "string"
      }
    ]
