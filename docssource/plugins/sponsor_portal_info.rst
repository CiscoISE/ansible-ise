.. _sponsor_portal_info:

===================
sponsor_portal_info
===================

Documentation
=============

Information module for Sponsor Portal

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Sponsor Portal.
- Get Sponsor Portal by id.


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
  - module: cisco.ise.plugins.module_utils.definitions.sponsor_portal
  - description: Complete reference of the Sponsor Portal object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Sponsor Portal reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Sponsor Portal
    cisco.ise.sponsor_portal_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
    register: result

  - name: Get Sponsor Portal by id
    cisco.ise.sponsor_portal_info
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
      "SponsorPortal": {
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
            "fqdn": "string",
            "authenticationMethod": "string",
            "idleTimeout": 0,
            "displayLang": "string",
            "fallbackLanguage": "string",
            "alwaysUsedLanguage": "string",
            "availableSsids": [
              "string"
            ]
          },
          "loginPageSettings": {
            "requireAccessCode": true,
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
          "sponsorChangePasswordSettings": {
            "allowSponsorToChangePwd": true
          },
          "postLoginBannerSettings": {
            "includePostAccessBanner": true
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
