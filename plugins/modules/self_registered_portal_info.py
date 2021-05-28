#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: self_registered_portal_info
short_description: Information module for Self Registered Portal
description:
- Get all Self Registered Portal.
- Get Self Registered Portal by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  page:
    description:
    - Page query parameter. Page number.
    type: int
  size:
    description:
    - Size query parameter. Number of objects returned per page.
    type: int
  filter:
    description:
    - >
      Filter query parameter. <br/> **Simple filtering** should be available through the filter query string
      parameter. The structure of a filter is a triplet of field operator and value separated with dots. More than
      one filter can be sent. The logical operator common to ALL filter criteria will be by default AND, and can
      be changed by using the "filterType=or" query string parameter. Each resource Data model description should
      specify if an attribute is a filtered field. <br/> Operator | Description <br/>
      ------------|----------------- <br/> EQ | Equals <br/> NEQ | Not Equals <br/> GT | Greater Than <br/> LT |
      Less Then <br/> STARTSW | Starts With <br/> NSTARTSW | Not Starts With <br/> ENDSW | Ends With <br/> NENDSW
      | Not Ends With <br/> CONTAINS | Contains <br/> NCONTAINS | Not Contains <br/>.
    type: list
  filterType:
    description:
    - >
      FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and
      can be changed by using the parameter.
    type: str
  sortasc:
    description:
    - Sortasc query parameter. Sort asc.
    type: str
  sortdec:
    description:
    - Sortdec query parameter. Sort desc.
    type: str
  id:
    description:
    - Id path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.self_registered_portal
# Reference by Internet resource
- name: Self Registered Portal reference
  description: Complete reference of the Self Registered Portal object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Self Registered Portal
  cisco.ise.self_registered_portal_info:
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

- name: Get Self Registered Portal by id
  cisco.ise.self_registered_portal_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "SelfRegPortal": {
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
            "endpointIdentityGroup": "string",
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
          "selfRegPageSettings": {
            "assignGuestsToGuestType": "string",
            "accountValidityDuration": 0,
            "accountValidityTimeUnits": "string",
            "requireRegistrationCode": true,
            "registrationCode": "string",
            "fieldUserName": {
              "include": true,
              "require": true
            },
            "fieldFirstName": {
              "include": true,
              "require": true
            },
            "fieldLastName": {
              "include": true,
              "require": true
            },
            "fieldEmailAddr": {
              "include": true,
              "require": true
            },
            "fieldPhoneNo": {
              "include": true,
              "require": true
            },
            "fieldCompany": {
              "include": true,
              "require": true
            },
            "fieldLocation": {
              "include": true,
              "require": true
            },
            "selectableLocations": [
              "string"
            ],
            "fieldSmsProvider": {
              "include": true,
              "require": true
            },
            "selectableSmsProviders": [
              "string"
            ],
            "fieldReasonForVisit": {
              "include": true,
              "require": true
            },
            "includeAup": true,
            "aupDisplay": "string",
            "requireAupAcceptance": true,
            "enableGuestEmailWhitelist": true,
            "guestEmailWhitelistDomains": [
              "string"
            ],
            "enableGuestEmailBlacklist": true,
            "guestEmailBlacklistDomains": [
              "string"
            ],
            "requireGuestApproval": true,
            "sendApprovalRequestTo": "string",
            "postRegistrationRedirect": "string",
            "credentialNotificationUsingEmail": true,
            "credentialNotificationUsingSms": true,
            "approveDenyLinksTimeUnits": "string",
            "authenticateSponsorsUsingPortalList": true,
            "sponsorPortalList": []
          },
          "selfRegSuccessSettings": {
            "includeUserName": true,
            "includePassword": true,
            "includeFirstName": true,
            "includeLastName": true,
            "includeEmailAddr": true,
            "includePhoneNo": true,
            "includeCompany": true,
            "includeLocation": true,
            "includeSmsProvider": true,
            "includePersonBeingVisited": true,
            "includeReasonForVisit": true,
            "allowGuestSendSelfUsingPrint": true,
            "allowGuestSendSelfUsingEmail": true,
            "allowGuestSendSelfUsingSms": true,
            "includeAup": true,
            "aupOnPage": true,
            "requireAupAcceptance": true,
            "requireAupScrolling": true,
            "allowGuestLoginFromSelfregSuccessPage": true
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
"""
