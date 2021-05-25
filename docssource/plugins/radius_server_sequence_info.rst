.. _radius_server_sequence_info:

===========================
radius_server_sequence_info
===========================

Documentation
=============

Information module for Radius Server Sequence

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Radius Server Sequence.
- Get Radius Server Sequence by id.


Options
-------
::

  options:
    id:
      description:
      - Id path parameter.
      type: str
    page:
      description:
      - Page query parameter. Page number.
      type: int
    size:
      description:
      - Size query parameter. Number of objects returned per page.
      type: int
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.radius_server_sequence
  - description: Complete reference of the Radius Server Sequence object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Radius Server Sequence reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Radius Server Sequence
    cisco.ise.radius_server_sequence_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
    register: result

  - name: Get Radius Server Sequence by id
    cisco.ise.radius_server_sequence_info
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
      "RadiusServerSequence": {
        "id": "string",
        "name": "string",
        "description": "string",
        "stripPrefix": true,
        "stripSuffix": true,
        "prefixSeparator": "string",
        "suffixSeparator": "string",
        "remoteAccounting": true,
        "localAccounting": true,
        "useAttrSetOnRequest": true,
        "useAttrSetBeforeAcc": true,
        "continueAuthorzPolicy": true,
        "RadiusServerList": [
          "string"
        ],
        "OnRequestAttrManipulatorList": [
          {
            "action": "string",
            "dictionaryName": "string",
            "attributeName": "string",
            "value": "string",
            "changedVal": "string"
          }
        ],
        "BeforeAcceptAttrManipulatorsList": [
          {
            "action": "string",
            "dictionaryName": "string",
            "attributeName": "string",
            "value": "string",
            "changedVal": "string"
          }
        ]
      }
    }

Sample 2:

.. code-block:: json

    {
      "SearchResult": {
        "total": 0,
        "resources": [
          {
            "id": "string",
            "name": "string",
            "description": "string",
            "link": {
              "rel": "string",
              "href": "string",
              "type": "string"
            }
          }
        ],
        "nextPage": {
          "rel": "string",
          "href": "string",
          "type": "string"
        },
        "previousPage": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    }
