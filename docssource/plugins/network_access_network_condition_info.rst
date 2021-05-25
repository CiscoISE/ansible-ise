.. _network_access_network_condition_info:

=====================================
network_access_network_condition_info
=====================================

Documentation
=============

Information module for Network Access Network Condition

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Network Access Network Condition.
- Get Network Access Network Condition by id.


Options
-------
::

  options:
    id:
      description:
      - Id path parameter. Condition id.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.network_access_network_condition
  - description: Complete reference of the Network Access Network Condition object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Access Network Condition reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Network Access Network Condition
    cisco.ise.network_access_network_condition_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
    register: result

  - name: Get Network Access Network Condition by id
    cisco.ise.network_access_network_condition_info
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
