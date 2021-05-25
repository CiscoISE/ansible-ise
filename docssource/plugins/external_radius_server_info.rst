.. _external_radius_server_info:

===========================
external_radius_server_info
===========================

Documentation
=============

Information module for External Radius Server

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all External Radius Server.
- Get External Radius Server by id.
- Get External Radius Server by name.


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
  - module: cisco.ise.plugins.module_utils.definitions.external_radius_server
  - description: Complete reference of the External Radius Server object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: External Radius Server reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all External Radius Server
    cisco.ise.external_radius_server_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
    register: result

  - name: Get External Radius Server by id
    cisco.ise.external_radius_server_info
      id: string
    register: result

  - name: Get External Radius Server by name
    cisco.ise.external_radius_server_info
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
      "ExternalRadiusServer": {
        "id": "string",
        "name": "string",
        "description": "string",
        "hostIP": "string",
        "sharedSecret": "string",
        "enableKeyWrap": true,
        "encryptionKey": "string",
        "authenticatorKey": "string",
        "keyInputFormat": "string",
        "authenticationPort": 0,
        "accountingPort": 0,
        "timeout": 0,
        "retries": 0,
        "proxyTimeout": 0
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
