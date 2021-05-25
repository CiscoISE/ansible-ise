.. _sponsored_guest_portal_info:

===========================
sponsored_guest_portal_info
===========================

Documentation
=============

Information module for Sponsored Guest Portal

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Sponsored Guest Portal.
- Get Sponsored Guest Portal by id.


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
  - module: cisco.ise.plugins.module_utils.definitions.sponsored_guest_portal
  - description: Complete reference of the Sponsored Guest Portal object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Sponsored Guest Portal reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Sponsored Guest Portal
    cisco.ise.sponsored_guest_portal_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
      filter: []
      filterType: AND
      sortasc: asc
      sortdec: string
    register: result

  - name: Get Sponsored Guest Portal by id
    cisco.ise.sponsored_guest_portal_info
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
      "SponsoredGuestPortal": {
        "id": "string",
        "name": "string",
        "description": "string",
        "portalType": "string",
        "settings": {
          "portalSettings": {
            "httpsPort": 0,
            "allowedInterfaces": [
              "string"
            ],
            "certificateGroupTag": "string",
            "authenticationMethod": "string",
            "assignedGuestTypeForEmployee": "string",
            "displayLang": "string",
            "fallbackLanguage": "string",
            "alwaysUsedLanguage": "string",
            "availableSsids": []
          },
          "loginPageSettings": {
            "requireAccessCode": true,
            "accessCode": "string",
            "maxFailedAttemptsBeforeRateLimit": 0,
            "timeBetweenLoginsDuringRateLimit": 0,
            "includeAup": true,
            "aupDisplay": "string",
            "requireAupAcceptance": true,
            "requireAupScrolling": true,
            "allowGuestToCreateAccounts": true,
            "allowGuestToChangePassword": true,
            "allowAlternateGuestPortal": true,
            "allowGuestToUseSocialAccounts": true,
            "allowShowGuestForm": true,
            "socialConfigs": []
          },
          "aupSettings": {
            "includeAup": true,
            "useDiffAupForEmployees": true,
            "skipAupForEmployees": true,
            "requireAccessCode": true,
            "requireScrolling": true,
            "displayFrequency": "string"
          },
          "guestChangePasswordSettings": {
            "allowChangePasswdAtFirstLogin": true
          },
          "guestDeviceRegistrationSettings": {
            "autoRegisterGuestDevices": true,
            "allowGuestsToRegisterDevices": true
          },
          "postLoginBannerSettings": {
            "includePostAccessBanner": true
          },
          "authSuccessSettings": {
            "successRedirect": "string",
            "redirectUrl": "string"
          },
          "supportInfoSettings": {
            "includeSupportInfoPage": true,
            "includeMacAddr": true,
            "includeIpAddress": true,
            "includeBrowserUserAgent": true,
            "includePolicyServer": true,
            "includeFailureCode": true,
            "emptyFieldDisplay": "string"
          }
        },
        "customizations": {
          "portalTheme": {
            "id": "string",
            "name": "string",
            "themeData": "string"
          },
          "portalTweakSettings": {
            "bannerColor": "string",
            "bannerTextColor": "string",
            "pageBackgroundColor": "string",
            "pageLabelAndTextColor": "string"
          },
          "language": {
            "viewLanguage": "string"
          },
          "globalCustomizations": {
            "mobileLogoImage": {
              "data": "string"
            },
            "desktopLogoImage": {
              "data": "string"
            },
            "bannerImage": {
              "data": "string"
            },
            "bannerTitle": "string",
            "contactText": "string",
            "footerElement": "string"
          },
          "pageCustomizations": {
            "data": [
              {
                "key": "string",
                "value": "string"
              }
            ]
          }
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
        ]
      }
    }
