.. _network_access_authentication_rules_info:

========================================
network_access_authentication_rules_info
========================================

Documentation
=============

Information module for Network Access Authentication Rules

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Network Access Authentication Rules.
- Get Network Access Authentication Rules by id.


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
  - module: cisco.ise.plugins.module_utils.definitions.network_access_authentication_rules
  - description: Complete reference of the Network Access Authentication Rules object
      model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Access Authentication Rules reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Network Access Authentication Rules
    cisco.ise.network_access_authentication_rules_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      policyId: string
    register: result

  - name: Get Network Access Authentication Rules by id
    cisco.ise.network_access_authentication_rules_info
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
