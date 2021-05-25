.. _tacacs_profile_info:

===================
tacacs_profile_info
===================

Documentation
=============

Information module for Tacacs Profile

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Tacacs Profile.
- Get Tacacs Profile by id.
- Get Tacacs Profile by name.


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
  - module: cisco.ise.plugins.module_utils.definitions.tacacs_profile
  - description: Complete reference of the Tacacs Profile object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Tacacs Profile reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Tacacs Profile
    cisco.ise.tacacs_profile_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
    register: result

  - name: Get Tacacs Profile by id
    cisco.ise.tacacs_profile_info
      id: string
    register: result

  - name: Get Tacacs Profile by name
    cisco.ise.tacacs_profile_info
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
      "TacacsProfile": {
        "id": "string",
        "name": "string",
        "description": "string",
        "sessionAttributes": {
          "sessionAttributeList": [
            {
              "type": "string",
              "name": "string",
              "value": "string"
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
