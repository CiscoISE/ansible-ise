.. _network_access_authorization_global_exception_rules:

===================================================
network_access_authorization_global_exception_rules
===================================================

Documentation
=============

Resource module for Network Access Authorization Global Exception Rules

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Network Access Authorization Global Exception Rules.


Options
-------
::

  options:
    id:
      description: Id path parameter. Rule id.
      type: string
    profile:
      description: The authorization profile/s.
      elements:
        type: str
      type: list
    rule:
      suboptions:
        condition:
          suboptions:
            attributeId:
              description: Network Access Authorization Global Exception Rules's attributeId.
              type: str
            attributeName:
              description: Network Access Authorization Global Exception Rules's attributeName.
              type: str
            attributeValue:
              description: Network Access Authorization Global Exception Rules's attributeValue.
              type: str
            children:
              description: Network Access Authorization Global Exception Rules's children.
              suboptions:
              - suboptions:
                  conditionType:
                    description: Network Access Authorization Global Exception Rules's
                      conditionType.
                    type: str
                  isNegate:
                    description: IsNegate flag.
                    type: bool
                type: dict
              type: list
            conditionType:
              description: Network Access Authorization Global Exception Rules's conditionType.
              type: str
            datesRange:
              suboptions:
                endDate:
                  description: Network Access Authorization Global Exception Rules's
                    endDate.
                  type: str
                startDate:
                  description: Network Access Authorization Global Exception Rules's
                    startDate.
                  type: str
              type: dict
            datesRangeException:
              suboptions:
                endDate:
                  description: Network Access Authorization Global Exception Rules's
                    endDate.
                  type: str
                startDate:
                  description: Network Access Authorization Global Exception Rules's
                    startDate.
                  type: str
              type: dict
            description:
              description: Network Access Authorization Global Exception Rules's description.
              type: str
            dictionaryName:
              description: Network Access Authorization Global Exception Rules's dictionaryName.
              type: str
            dictionaryValue:
              description: Network Access Authorization Global Exception Rules's dictionaryValue.
              type: str
            hoursRange:
              suboptions:
                endTime:
                  description: Network Access Authorization Global Exception Rules's
                    endTime.
                  type: str
                startTime:
                  description: Network Access Authorization Global Exception Rules's
                    startTime.
                  type: str
              type: dict
            hoursRangeException:
              suboptions:
                endTime:
                  description: Network Access Authorization Global Exception Rules's
                    endTime.
                  type: str
                startTime:
                  description: Network Access Authorization Global Exception Rules's
                    startTime.
                  type: str
              type: dict
            id:
              description: Network Access Authorization Global Exception Rules's id.
              type: str
            isNegate:
              description: IsNegate flag.
              type: bool
            name:
              description: Network Access Authorization Global Exception Rules's name.
              type: str
            operator:
              description: Network Access Authorization Global Exception Rules's operator.
              type: str
            weekDays:
              description: Network Access Authorization Global Exception Rules's weekDays.
              elements:
                type: str
              type: list
            weekDaysException:
              description: Network Access Authorization Global Exception Rules's weekDaysException.
              elements:
                type: str
              type: list
          type: dict
        default:
          description: Indicates if this rule is the default one.
          type: bool
        description:
          description: The description of the rule.
          type: str
        hitCounts:
          description: The amount of times the rule was matched.
          type: int
        id:
          description: The identifier of the rule.
          type: str
        name:
          description: Rule name, Valid characters are alphanumerics, underscore, hyphen,
            space, period, parentheses.
          type: str
        rank:
          description: The rank(priority) in relation to other rules. Lower rank is
            higher priority.
          type: int
        state:
          description: The state that the rule is in. A disabled rule cannot be matched.
          type: str
      type: dict
    securityGroup:
      description: Security group used in authorization policies.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.network_access_authorization_global_exception_rules
  - description: Complete reference of the Network Access Authorization Global Exception
      Rules object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Access Authorization Global Exception Rules reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.network_access_authorization_global_exception_rules:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      profile:
      - string
      rule:
        condition:
          attributeId: string
          attributeName: string
          attributeValue: string
          children:
          - conditionType: string
            isNegate: true
          conditionType: string
          datesRange:
            endDate: string
            startDate: string
          datesRangeException:
            endDate: string
            startDate: string
          description: string
          dictionaryName: string
          dictionaryValue: string
          hoursRange:
            endTime: string
            startTime: string
          hoursRangeException:
            endTime: string
            startTime: string
          id: string
          isNegate: true
          name: string
          operator: string
          weekDays:
          - string
          weekDaysException:
          - string
        default: true
        description: string
        hitCounts: 0
        id: string
        name: string
        rank: 0
        state: string
      securityGroup: string

  - name: Update by id
    cisco.ise.network_access_authorization_global_exception_rules:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      id: string
      profile:
      - string
      rule:
        condition:
          attributeId: string
          attributeName: string
          attributeValue: string
          children:
          - conditionType: string
            isNegate: true
          conditionType: string
          datesRange:
            endDate: string
            startDate: string
          datesRangeException:
            endDate: string
            startDate: string
          description: string
          dictionaryName: string
          dictionaryValue: string
          hoursRange:
            endTime: string
            startTime: string
          hoursRangeException:
            endTime: string
            startTime: string
          id: string
          isNegate: true
          name: string
          operator: string
          weekDays:
          - string
          weekDaysException:
          - string
        default: true
        description: string
        hitCounts: 0
        id: string
        name: string
        rank: 0
        state: string
      securityGroup: string

  - name: Delete by id
    cisco.ise.network_access_authorization_global_exception_rules:
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
      "profile": [
        "string"
      ],
      "securityGroup": "string"
    }

Sample 2:

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
      "profile": [
        "string"
      ],
      "securityGroup": "string"
    }

Sample 3:

.. code-block:: json

    {
      "id": "string"
    }
