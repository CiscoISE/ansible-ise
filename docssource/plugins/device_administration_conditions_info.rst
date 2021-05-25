.. _device_administration_conditions_info:

=====================================
device_administration_conditions_info
=====================================

Documentation
=============

Information module for Device Administration Conditions

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Device Administration Conditions.
- Get Device Administration Conditions by id.
- Get Device Administration Conditions by name.


Options
-------
::

  options:
    id:
      description:
      - Id path parameter. Condition id.
      type: str
    name:
      description:
      - Name path parameter. Condition name.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.device_administration_conditions
  - description: Complete reference of the Device Administration Conditions object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Device Administration Conditions reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Device Administration Conditions
    cisco.ise.device_administration_conditions_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
    register: result

  - name: Get Device Administration Conditions by id
    cisco.ise.device_administration_conditions_info
      id: string
    register: result

  - name: Get Device Administration Conditions by name
    cisco.ise.device_administration_conditions_info
      name: string
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
      "conditionType": "string",
      "isNegate": true,
      "name": "string",
      "id": "string",
      "description": "string",
      "dictionaryName": "string",
      "attributeName": "string",
      "attributeId": "string",
      "operator": "string",
      "dictionaryValue": "string",
      "attributeValue": "string",
      "children": [
        {
          "conditionType": "string",
          "isNegate": true
        }
      ],
      "hoursRange": {
        "startTime": "string",
        "endTime": "string"
      },
      "hoursRangeException": {
        "startTime": "string",
        "endTime": "string"
      },
      "weekDays": [
        "string"
      ],
      "weekDaysException": [
        "string"
      ],
      "datesRange": {
        "startDate": "string",
        "endDate": "string"
      },
      "datesRangeException": {
        "startDate": "string",
        "endDate": "string"
      }
    }

Sample 2:

.. code-block:: json

    [
      {
        "conditionType": "string",
        "isNegate": true
      }
    ]
