.. _network_access_time_date_conditions:

===================================
network_access_time_date_conditions
===================================

Documentation
=============

Resource module for Network Access Time Date Conditions

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Network Access Time Date Conditions.


Options
-------
::

  options:
    attributeId:
      description: Network Access Time Date Conditions's attributeId.
      type: str
    attributeName:
      description: Network Access Time Date Conditions's attributeName.
      type: str
    attributeValue:
      description: Network Access Time Date Conditions's attributeValue.
      type: str
    children:
      description: Network Access Time Date Conditions's children.
      suboptions:
      - suboptions:
          conditionType:
            description: Network Access Time Date Conditions's conditionType.
            type: str
          isNegate:
            description: IsNegate flag.
            type: bool
        type: dict
      type: list
    conditionType:
      description: Network Access Time Date Conditions's conditionType.
      type: str
    datesRange:
      suboptions:
        endDate:
          description: Network Access Time Date Conditions's endDate.
          type: str
        startDate:
          description: Network Access Time Date Conditions's startDate.
          type: str
      type: dict
    datesRangeException:
      suboptions:
        endDate:
          description: Network Access Time Date Conditions's endDate.
          type: str
        startDate:
          description: Network Access Time Date Conditions's startDate.
          type: str
      type: dict
    description:
      description: Condition description.
      type: str
    dictionaryName:
      description: Network Access Time Date Conditions's dictionaryName.
      type: str
    dictionaryValue:
      description: Network Access Time Date Conditions's dictionaryValue.
      type: str
    hoursRange:
      suboptions:
        endTime:
          description: Network Access Time Date Conditions's endTime.
          type: str
        startTime:
          description: Network Access Time Date Conditions's startTime.
          type: str
      type: dict
    hoursRangeException:
      suboptions:
        endTime:
          description: Network Access Time Date Conditions's endTime.
          type: str
        startTime:
          description: Network Access Time Date Conditions's startTime.
          type: str
      type: dict
    id:
      description: Network Access Time Date Conditions's id.
      type: str
    isNegate:
      description: IsNegate flag.
      type: bool
    name:
      description: Condition name.
      type: str
    operator:
      description: Network Access Time Date Conditions's operator.
      type: str
    weekDays:
      description: <p>Defines for which days this condition will be matched<br> Days
        format - Arrays of WeekDay enums <br> Default - List of All week days</p>.
      elements:
        type: str
      type: list
    weekDaysException:
      description: <p>Defines for which days this condition will NOT be matched<br>
        Days format - Arrays of WeekDay enums <br> Default - Not enabled</p>.
      elements:
        type: str
      type: list
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.network_access_time_date_conditions
  - description: Complete reference of the Network Access Time Date Conditions object
      model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Access Time Date Conditions reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.network_access_time_date_conditions:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      {}

  - name: Update by id
    cisco.ise.network_access_time_date_conditions:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
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

  - name: Delete by id
    cisco.ise.network_access_time_date_conditions:
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

Sample 3:

.. code-block:: json

    {
      "id": "string"
    }
