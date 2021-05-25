.. _tacacs_server_sequence_info:

===========================
tacacs_server_sequence_info
===========================

Documentation
=============

Information module for Tacacs Server Sequence

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Tacacs Server Sequence.
- Get Tacacs Server Sequence by id.
- Get Tacacs Server Sequence by name.


Options
-------
::

  options:
    id:
      description:
      - Id path parameter.
      type: str
    name:
      description:
      - Name path parameter.
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
  - module: cisco.ise.plugins.module_utils.definitions.tacacs_server_sequence
  - description: Complete reference of the Tacacs Server Sequence object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Tacacs Server Sequence reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Tacacs Server Sequence
    cisco.ise.tacacs_server_sequence_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
    register: result

  - name: Get Tacacs Server Sequence by id
    cisco.ise.tacacs_server_sequence_info
      id: string
    register: result

  - name: Get Tacacs Server Sequence by name
    cisco.ise.tacacs_server_sequence_info
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
      "TacacsServerSequence": {
        "name": "string",
        "serverList": "string",
        "localAccounting": true,
        "remoteAccounting": true,
        "prefixStrip": true,
        "prefixDelimiter": "string",
        "suffixStrip": true,
        "suffixDelimiter": "string"
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
