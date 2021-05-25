.. _tacacs_command_sets_info:

========================
tacacs_command_sets_info
========================

Documentation
=============

Information module for Tacacs Command Sets

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Tacacs Command Sets.
- Get Tacacs Command Sets by id.
- Get Tacacs Command Sets by name.


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
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.tacacs_command_sets
  - description: Complete reference of the Tacacs Command Sets object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Tacacs Command Sets reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Tacacs Command Sets
    cisco.ise.tacacs_command_sets_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
    register: result

  - name: Get Tacacs Command Sets by id
    cisco.ise.tacacs_command_sets_info
      id: string
    register: result

  - name: Get Tacacs Command Sets by name
    cisco.ise.tacacs_command_sets_info
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
      "TacacsCommandSets": {
        "name": "string",
        "description": "string",
        "permitUnmatched": true,
        "commands": {
          "commandList": [
            {
              "grant": "string",
              "command": "string",
              "arguments": "string"
            }
          ]
        }
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
