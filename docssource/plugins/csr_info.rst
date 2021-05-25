.. _csr_info:

========
csr_info
========

Documentation
=============

Information module for Csr

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Csr.
- Get Csr by id.


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
    hostName:
      description:
      - HostName path parameter. Name of the host of which CSR's should be returned.
      type: str
    id:
      description:
      - Id path parameter. The ID of the Certificate Signing Request returned.
      type: str
    page:
      description:
      - Page query parameter. Page number.
      type: int
    size:
      description:
      - Size query parameter. Number of objects returned per page.
      type: int
    sort:
      description:
      - Sort query parameter. Sort type - asc or desc.
      type: str
    sortBy:
      description:
      - SortBy query parameter. Sort column by which objects needs to be sorted.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.csr
  - description: Complete reference of the Csr object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Csr reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Csr
    cisco.ise.csr_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
      sort: asc
      sortBy: string
      filter: []
      filterType: AND
    register: result

  - name: Get Csr by id
    cisco.ise.csr_info
      hostName: string
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
      "response": {},
      "version": "string"
    }

Sample 2:

.. code-block:: json

    {
      "response": [
        {
          "id": "string",
          "hostName": "string",
          "subject": "string",
          "keySize": "string",
          "timeStamp": "string",
          "friendlyName": "string",
          "usedFor": "string",
          "groupTag": "string",
          "signatureAlgorithm": "string",
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
      },
      "version": "string"
    }
