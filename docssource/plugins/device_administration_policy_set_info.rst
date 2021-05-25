.. _device_administration_policy_set_info:

=====================================
device_administration_policy_set_info
=====================================

Documentation
=============

Information module for Device Administration Policy Set

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Device Administration Policy Set.
- Get Device Administration Policy Set by id.


Options
-------
::

  options:
    id:
      description:
      - Id path parameter. Policy id.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.device_administration_policy_set
  - description: Complete reference of the Device Administration Policy Set object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Device Administration Policy Set reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Device Administration Policy Set
    cisco.ise.device_administration_policy_set_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
    register: result

  - name: Get Device Administration Policy Set by id
    cisco.ise.device_administration_policy_set_info
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
      "id": "string",
      "name": "string",
      "description": "string",
      "hitCounts": 0,
      "rank": 0,
      "state": "string",
      "default": true,
      "condition": {
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
      },
      "serviceName": "string",
      "isProxy": true
    }

Sample 2:

.. code-block:: json

    [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "hitCounts": 0,
        "rank": 0,
        "state": "string",
        "default": true,
        "condition": {
          "conditionType": "string",
          "isNegate": true
        },
        "serviceName": "string",
        "isProxy": true
      }
    ]
