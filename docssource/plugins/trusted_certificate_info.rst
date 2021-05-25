.. _trusted_certificate_info:

========================
trusted_certificate_info
========================

Documentation
=============

Information module for Trusted Certificate

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Trusted Certificate.
- Get Trusted Certificate by id.


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
      - Id path parameter. The id of the trust certificate.
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
  - module: cisco.ise.plugins.module_utils.definitions.trusted_certificate
  - description: Complete reference of the Trusted Certificate object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Trusted Certificate reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Trusted Certificate
    cisco.ise.trusted_certificate_info:
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

  - name: Get Trusted Certificate by id
    cisco.ise.trusted_certificate_info
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
      "response": {
        "id": "string",
        "friendlyName": "string",
        "subject": "string",
        "issuedTo": "string",
        "issuedBy": "string",
        "keySize": "string",
        "signatureAlgorithm": "string",
        "validFrom": "string",
        "expirationDate": "string",
        "serialNumberDecimalFormat": "string",
        "description": "string",
        "status": "string",
        "trustedFor": "string",
        "internalCA": true,
        "isReferredInPolicy": true,
        "downloadCRL": "string",
        "crlDistributionUrl": "string",
        "automaticCRLUpdate": "string",
        "automaticCRLUpdatePeriod": "string",
        "automaticCRLUpdateUnits": "string",
        "nonAutomaticCRLUpdatePeriod": "string",
        "nonAutomaticCRLUpdateUnits": "string",
        "crlDownloadFailureRetries": "string",
        "crlDownloadFailureRetriesUnits": "string",
        "authenticateBeforeCRLReceived": "string",
        "ignoreCRLExpiration": "string",
        "enableServerIdentityCheck": "string",
        "enableOCSPValidation": "string",
        "selectedOCSPService": "string",
        "rejectIfNoStatusFromOCSP": "string",
        "rejectIfUnreachableFromOCSP": "string",
        "sha256Fingerprint": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      },
      "version": "string"
    }

Sample 2:

.. code-block:: json

    {
      "response": [
        {
          "id": "string",
          "friendlyName": "string",
          "subject": "string",
          "issuedTo": "string",
          "issuedBy": "string",
          "keySize": "string",
          "signatureAlgorithm": "string",
          "validFrom": "string",
          "expirationDate": "string",
          "serialNumberDecimalFormat": "string",
          "description": "string",
          "status": "string",
          "trustedFor": "string",
          "internalCA": true,
          "isReferredInPolicy": true,
          "downloadCRL": "string",
          "crlDistributionUrl": "string",
          "automaticCRLUpdate": "string",
          "automaticCRLUpdatePeriod": "string",
          "automaticCRLUpdateUnits": "string",
          "nonAutomaticCRLUpdatePeriod": "string",
          "nonAutomaticCRLUpdateUnits": "string",
          "crlDownloadFailureRetries": "string",
          "crlDownloadFailureRetriesUnits": "string",
          "authenticateBeforeCRLReceived": "string",
          "ignoreCRLExpiration": "string",
          "enableServerIdentityCheck": "string",
          "enableOCSPValidation": "string",
          "selectedOCSPService": "string",
          "rejectIfNoStatusFromOCSP": "string",
          "rejectIfUnreachableFromOCSP": "string",
          "sha256Fingerprint": "string",
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
