.. _authorization_profile_info:

==========================
authorization_profile_info
==========================

Documentation
=============

Information module for Authorization Profile

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Authorization Profile.
- Get Authorization Profile by id.
- Get Authorization Profile by name.


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
  - module: cisco.ise.plugins.module_utils.definitions.authorization_profile
  - description: Complete reference of the Authorization Profile object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Authorization Profile reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Authorization Profile
    cisco.ise.authorization_profile_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
    register: result

  - name: Get Authorization Profile by id
    cisco.ise.authorization_profile_info
      id: string
    register: result

  - name: Get Authorization Profile by name
    cisco.ise.authorization_profile_info
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
      "AuthorizationProfile": {
        "id": "string",
        "name": "string",
        "description": "string",
        "advancedAttributes": [
          {
            "leftHandSideDictionaryAttribue": {
              "AdvancedAttributeValueType": "string",
              "dictionaryName": "string",
              "attributeName": "string"
            },
            "rightHandSideAttribueValue": {
              "AdvancedAttributeValueType": "string",
              "value": "string"
            }
          }
        ],
        "accessType": "string",
        "authzProfileType": "string",
        "vlan": {
          "nameID": "string",
          "tagID": 0
        },
        "reauth": {
          "timer": 0,
          "connectivity": "string"
        },
        "airespaceACL": "string",
        "airespaceIPv6ACL": "string",
        "webRedirection": {
          "WebRedirectionType": "string",
          "acl": "string",
          "portalName": "string",
          "staticIPHostNameFQDN": "string",
          "displayCertificatesRenewalMessages": true
        },
        "acl": "string",
        "trackMovement": true,
        "serviceTemplate": true,
        "easywiredSessionCandidate": true,
        "daclName": "string",
        "voiceDomainPermission": true,
        "neat": true,
        "webAuth": true,
        "autoSmartPort": "string",
        "interfaceTemplate": "string",
        "ipv6ACLFilter": "string",
        "avcProfile": "string",
        "macSecPolicy": "string",
        "asaVpn": "string",
        "profileName": "string",
        "ipv6DaclName": "string"
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
