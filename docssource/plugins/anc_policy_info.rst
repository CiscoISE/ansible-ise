.. _anc_policy_info:

===============
anc_policy_info
===============

Documentation
=============

Information module for Anc Policy

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Anc Policy.
- Get Anc Policy by id.
- Get Anc Policy by name.


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
  - module: cisco.ise.plugins.module_utils.definitions.anc_policy
  - description: Complete reference of the Anc Policy object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Anc Policy reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Anc Policy
    cisco.ise.anc_policy_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
    register: result

  - name: Get Anc Policy by id
    cisco.ise.anc_policy_info
      id: string
    register: result

  - name: Get Anc Policy by name
    cisco.ise.anc_policy_info
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
      "ErsAncPolicy": {
        "name": "string",
        "actions": [
          "string"
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
