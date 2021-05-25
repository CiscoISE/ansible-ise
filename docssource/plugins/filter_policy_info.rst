.. _filter_policy_info:

==================
filter_policy_info
==================

Documentation
=============

Information module for Filter Policy

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Filter Policy.
- Get Filter Policy by id.


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
  - module: cisco.ise.plugins.module_utils.definitions.filter_policy
  - description: Complete reference of the Filter Policy object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Filter Policy reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Filter Policy
    cisco.ise.filter_policy_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
    register: result

  - name: Get Filter Policy by id
    cisco.ise.filter_policy_info
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
      "ERSFilterPolicy": {
        "subnet": "string",
        "domains": "string",
        "sgt": "string",
        "vn": "string"
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
