#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: sponsor_portal_info
short_description: Information module for Sponsor Portal
description:
- Get all Sponsor Portal.
- Get Sponsor Portal by id.
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
  id:
    description:
    - Id path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sponsor_portal
# Reference by Internet resource
- name: Sponsor Portal reference
  description: Complete reference of the Sponsor Portal object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
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

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'SponsorPortal': {'id': 'string', 'name': 'string', 'description': 'string', 'portalType': 'string', 'settings': {'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'fqdn': 'string', 'authenticationMethod': 'string', 'idleTimeout': 0, 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string', 'availableSsids': ['string']}, 'loginPageSettings': {'requireAccessCode': True, 'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireAupScrolling': True, 'allowGuestToCreateAccounts': True, 'allowGuestToChangePassword': True, 'allowAlternateGuestPortal': True, 'allowGuestToUseSocialAccounts': True, 'allowShowGuestForm': True, 'socialConfigs': []}, 'aupSettings': {'includeAup': True, 'useDiffAupForEmployees': True, 'skipAupForEmployees': True, 'requireAccessCode': True, 'requireScrolling': True, 'displayFrequency': 'string'}, 'sponsorChangePasswordSettings': {'allowSponsorToChangePwd': True}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string'}}, 'customizations': {'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}}}}
  - {'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': {'rel': 'string', 'href': 'string', 'type': 'string'}, 'previousPage': {'rel': 'string', 'href': 'string', 'type': 'string'}}}
"""
