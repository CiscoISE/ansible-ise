.. _device_administration_authentication_rules_info:

===============================================
device_administration_authentication_rules_info
===============================================

Documentation
=============

Information module for Device Administration Authentication Rules

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Device Administration Authentication Rules.
- Get Device Administration Authentication Rules by id.


Options
-------
::

  options:
    id:
      description:
      - Id path parameter. Rule id.
      type: str
    policyId:
      description:
      - PolicyId path parameter. Policy id.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.device_administration_authentication_rules
  - description: Complete reference of the Device Administration Authentication Rules
      object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Device Administration Authentication Rules reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Device Administration Authentication Rules
    cisco.ise.device_administration_authentication_rules_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      policyId: string
    register: result

  - name: Get Device Administration Authentication Rules by id
    cisco.ise.device_administration_authentication_rules_info
      policyId: string
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
      "rule": {
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
        }
      },
      "identitySourceId": "string",
      "ifAuthFail": "string",
      "ifUserNotFound": "string",
      "ifProcessFail": "string"
    }

Sample 2:

.. code-block:: json

    [
      {
        "rule": {
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
          }
        },
        "identitySourceId": "string",
        "ifAuthFail": "string",
        "ifUserNotFound": "string",
        "ifProcessFail": "string"
      }
    ]
