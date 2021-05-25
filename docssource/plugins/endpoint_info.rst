.. _endpoint_info:

=============
endpoint_info
=============

Documentation
=============

Information module for Endpoint

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Endpoint.
- Get Endpoint by id.
- Get Endpoint by name.


Options
-------
::

  options:
    filter:
      description:
      - Filter query parameter. <br/> **Simple filtering** should be available through
        the filter query string parameter. The structure of a filter is a triplet of
        field operator and value separated with dots. More than one filter can be sent.
        The logical operator common to ALL filter criteria will be by default AND, and
        can be changed by using the "filterType=or" query string parameter. Each resource
        Data model description should specify if an attribute is a filtered field. <br/>
        Operator | Description <br/> ------------|----------------- <br/> EQ | Equals
        <br/> NEQ | Not Equals <br/> GT | Greater Than <br/> LT | Less Then <br/> STARTSW
        | Starts With <br/> NSTARTSW | Not Starts With <br/> ENDSW | Ends With <br/>
        NENDSW | Not Ends With <br/> CONTAINS | Contains <br/> NCONTAINS | Not Contains
        <br/>.
      type: list
    filterType:
      description:
      - FilterType query parameter. The logical operator common to ALL filter criteria
        will be by default AND, and can be changed by using the parameter.
      type: str
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
    sortasc:
      description:
      - Sortasc query parameter. Sort asc.
      type: str
    sortdec:
      description:
      - Sortdec query parameter. Sort desc.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.endpoint
  - description: Complete reference of the Endpoint object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Endpoint reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Endpoint
    cisco.ise.endpoint_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
      sortasc: asc
      sortdec: string
      filter: []
      filterType: AND
    register: result

  - name: Get Endpoint by id
    cisco.ise.endpoint_info
      id: string
    register: result

  - name: Get Endpoint by name
    cisco.ise.endpoint_info
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
      "ERSEndPoint": {
        "id": "string",
        "name": "string",
        "description": "string",
        "mac": "string",
        "profileId": "string",
        "staticProfileAssignment": true,
        "groupId": "string",
        "staticGroupAssignment": true,
        "portalUser": "string",
        "identityStore": "string",
        "identityStoreId": "string",
        "customAttributes": {
          "customAttributes": {
            "key1": "string",
            "key2": "string"
          }
        },
        "mdmAttributes": {
          "mdmServerName": "string",
          "mdmReachable": true,
          "mdmEnrolled": true,
          "mdmComplianceStatus": true,
          "mdmOS": "string",
          "mdmManufacturer": "string",
          "mdmModel": "string",
          "mdmSerial": "string",
          "mdmEncrypted": true,
          "mdmPinlock": true,
          "mdmJailBroken": true,
          "mdmIMEI": "string",
          "mdmPhoneNumber": "string"
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
