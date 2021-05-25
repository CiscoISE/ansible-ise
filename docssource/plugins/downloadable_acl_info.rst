.. _downloadable_acl_info:

=====================
downloadable_acl_info
=====================

Documentation
=============

Information module for Downloadable Acl

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Downloadable Acl.
- Get Downloadable Acl by id.


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
  - module: cisco.ise.plugins.module_utils.definitions.downloadable_acl
  - description: Complete reference of the Downloadable Acl object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Downloadable Acl reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Downloadable Acl
    cisco.ise.downloadable_acl_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
    register: result

  - name: Get Downloadable Acl by id
    cisco.ise.downloadable_acl_info
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
      "DownloadableAcl": {
        "name": "string",
        "description": "string",
        "dacl": "string",
        "daclType": "string"
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
        ]
      }
    }
