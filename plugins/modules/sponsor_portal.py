#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: sponsor_portal
short_description: Resource module for Sponsor Portal
description:
- Manage operations create, update, delete of the resource Sponsor Portal.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    customizations:
      suboptions:
        globalCustomizations:
          suboptions:
            bannerImage:
              suboptions:
                data:
                  description: Sponsor Portal's data.
                  type: str
              type: dict
            bannerTitle:
              description: Sponsor Portal's bannerTitle.
              type: str
            contactText:
              description: Sponsor Portal's contactText.
              type: str
            desktopLogoImage:
              suboptions:
                data:
                  description: Sponsor Portal's data.
                  type: str
              type: dict
            footerElement:
              description: Sponsor Portal's footerElement.
              type: str
            mobileLogoImage:
              suboptions:
                data:
                  description: Sponsor Portal's data.
                  type: str
              type: dict
          type: dict
        language:
          suboptions:
            viewLanguage:
              description: Sponsor Portal's viewLanguage.
              type: str
          type: dict
        pageCustomizations:
          suboptions:
            data:
              description: Sponsor Portal's data.
              suboptions:
              - suboptions:
                  key:
                    description: Sponsor Portal's key.
                    type: str
                  value:
                    description: Sponsor Portal's value.
                    type: str
                type: dict
              type: list
          type: dict
        portalTheme:
          suboptions:
            id:
              description: Sponsor Portal's id.
              type: str
            name:
              description: Sponsor Portal's name.
              type: str
            themeData:
              description: Sponsor Portal's themeData.
              type: str
          type: dict
        portalTweakSettings:
          suboptions:
            bannerColor:
              description: Sponsor Portal's bannerColor.
              type: str
            bannerTextColor:
              description: Sponsor Portal's bannerTextColor.
              type: str
            pageBackgroundColor:
              description: Sponsor Portal's pageBackgroundColor.
              type: str
            pageLabelAndTextColor:
              description: Sponsor Portal's pageLabelAndTextColor.
              type: str
          type: dict
      type: dict
    description:
      description: Sponsor Portal's description.
      type: str
    id:
      description: Sponsor Portal's id.
      type: str
    name:
      description: Sponsor Portal's name.
      type: str
    portalType:
      description: Sponsor Portal's portalType.
      type: str
    settings:
      suboptions:
        aupSettings:
          suboptions:
            displayFrequency:
              description: Sponsor Portal's displayFrequency.
              type: str
            includeAup:
              description: IncludeAup flag.
              type: bool
            requireAccessCode:
              description: RequireAccessCode flag.
              type: bool
            requireScrolling:
              description: RequireScrolling flag.
              type: bool
            skipAupForEmployees:
              description: SkipAupForEmployees flag.
              type: bool
            useDiffAupForEmployees:
              description: UseDiffAupForEmployees flag.
              type: bool
          type: dict
        loginPageSettings:
          suboptions:
            allowAlternateGuestPortal:
              description: AllowAlternateGuestPortal flag.
              type: bool
            allowGuestToChangePassword:
              description: AllowGuestToChangePassword flag.
              type: bool
            allowGuestToCreateAccounts:
              description: AllowGuestToCreateAccounts flag.
              type: bool
            allowGuestToUseSocialAccounts:
              description: AllowGuestToUseSocialAccounts flag.
              type: bool
            allowShowGuestForm:
              description: AllowShowGuestForm flag.
              type: bool
            aupDisplay:
              description: Sponsor Portal's aupDisplay.
              type: str
            includeAup:
              description: IncludeAup flag.
              type: bool
            maxFailedAttemptsBeforeRateLimit:
              description: Sponsor Portal's maxFailedAttemptsBeforeRateLimit.
              type: int
            requireAccessCode:
              description: RequireAccessCode flag.
              type: bool
            requireAupAcceptance:
              description: RequireAupAcceptance flag.
              type: bool
            requireAupScrolling:
              description: RequireAupScrolling flag.
              type: bool
            socialConfigs:
              description: Sponsor Portal's socialConfigs.
              type: list
            timeBetweenLoginsDuringRateLimit:
              description: Sponsor Portal's timeBetweenLoginsDuringRateLimit.
              type: int
          type: dict
        portalSettings:
          suboptions:
            allowedInterfaces:
              description: Sponsor Portal's allowedInterfaces.
              elements:
                type: str
              type: list
            alwaysUsedLanguage:
              description: Sponsor Portal's alwaysUsedLanguage.
              type: str
            authenticationMethod:
              description: Sponsor Portal's authenticationMethod.
              type: str
            availableSsids:
              description: Sponsor Portal's availableSsids.
              elements:
                type: str
              type: list
            certificateGroupTag:
              description: Sponsor Portal's certificateGroupTag.
              type: str
            displayLang:
              description: Sponsor Portal's displayLang.
              type: str
            fallbackLanguage:
              description: Sponsor Portal's fallbackLanguage.
              type: str
            fqdn:
              description: Sponsor Portal's fqdn.
              type: str
            httpsPort:
              description: Sponsor Portal's httpsPort.
              type: int
            idleTimeout:
              description: Sponsor Portal's idleTimeout.
              type: int
          type: dict
        postLoginBannerSettings:
          suboptions:
            includePostAccessBanner:
              description: IncludePostAccessBanner flag.
              type: bool
          type: dict
        sponsorChangePasswordSettings:
          suboptions:
            allowSponsorToChangePwd:
              description: AllowSponsorToChangePwd flag.
              type: bool
          type: dict
        supportInfoSettings:
          suboptions:
            emptyFieldDisplay:
              description: Sponsor Portal's emptyFieldDisplay.
              type: str
            includeBrowserUserAgent:
              description: IncludeBrowserUserAgent flag.
              type: bool
            includeFailureCode:
              description: IncludeFailureCode flag.
              type: bool
            includeIpAddress:
              description: IncludeIpAddress flag.
              type: bool
            includeMacAddr:
              description: IncludeMacAddr flag.
              type: bool
            includePolicyServer:
              description: IncludePolicyServer flag.
              type: bool
            includeSupportInfoPage:
              description: IncludeSupportInfoPage flag.
              type: bool
          type: dict
      type: dict
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
- name: Create
  cisco.ise.sponsor_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customizations:
      globalCustomizations:
        bannerImage:
          data: string
        bannerTitle: string
        contactText: string
        desktopLogoImage:
          data: string
        footerElement: string
        mobileLogoImage:
          data: string
      language:
        viewLanguage: string
      pageCustomizations:
        data:
        - key: string
          value: string
      portalTheme:
        id: string
        name: string
        themeData: string
      portalTweakSettings:
        bannerColor: string
        bannerTextColor: string
        pageBackgroundColor: string
        pageLabelAndTextColor: string
    description: string
    id: string
    name: string
    portalType: string
    settings:
      aupSettings:
        displayFrequency: string
        includeAup: true
        requireAccessCode: true
        requireScrolling: true
        skipAupForEmployees: true
        useDiffAupForEmployees: true
      loginPageSettings:
        allowAlternateGuestPortal: true
        allowGuestToChangePassword: true
        allowGuestToCreateAccounts: true
        allowGuestToUseSocialAccounts: true
        allowShowGuestForm: true
        aupDisplay: string
        includeAup: true
        maxFailedAttemptsBeforeRateLimit: 0
        requireAccessCode: true
        requireAupAcceptance: true
        requireAupScrolling: true
        socialConfigs: []
        timeBetweenLoginsDuringRateLimit: 0
      portalSettings:
        allowedInterfaces:
        - string
        alwaysUsedLanguage: string
        authenticationMethod: string
        availableSsids:
        - string
        certificateGroupTag: string
        displayLang: string
        fallbackLanguage: string
        fqdn: string
        httpsPort: 0
        idleTimeout: 0
      postLoginBannerSettings:
        includePostAccessBanner: true
      sponsorChangePasswordSettings:
        allowSponsorToChangePwd: true
      supportInfoSettings:
        emptyFieldDisplay: string
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: true

- name: Update by id
  cisco.ise.sponsor_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customizations:
      globalCustomizations:
        bannerImage:
          data: string
        bannerTitle: string
        contactText: string
        desktopLogoImage:
          data: string
        footerElement: string
        mobileLogoImage:
          data: string
      language:
        viewLanguage: string
      pageCustomizations:
        data:
        - key: string
          value: string
      portalTheme:
        id: string
        name: string
        themeData: string
      portalTweakSettings:
        bannerColor: string
        bannerTextColor: string
        pageBackgroundColor: string
        pageLabelAndTextColor: string
    description: string
    id: string
    name: string
    portalType: string
    settings:
      aupSettings:
        displayFrequency: string
        includeAup: true
        requireAccessCode: true
        requireScrolling: true
        skipAupForEmployees: true
        useDiffAupForEmployees: true
      loginPageSettings:
        allowAlternateGuestPortal: true
        allowGuestToChangePassword: true
        allowGuestToCreateAccounts: true
        allowGuestToUseSocialAccounts: true
        allowShowGuestForm: true
        aupDisplay: string
        includeAup: true
        maxFailedAttemptsBeforeRateLimit: 0
        requireAccessCode: true
        requireAupAcceptance: true
        requireAupScrolling: true
        socialConfigs: []
        timeBetweenLoginsDuringRateLimit: 0
      portalSettings:
        allowedInterfaces:
        - string
        alwaysUsedLanguage: string
        authenticationMethod: string
        availableSsids:
        - string
        certificateGroupTag: string
        displayLang: string
        fallbackLanguage: string
        fqdn: string
        httpsPort: 0
        idleTimeout: 0
      postLoginBannerSettings:
        includePostAccessBanner: true
      sponsorChangePasswordSettings:
        allowSponsorToChangePwd: true
      supportInfoSettings:
        emptyFieldDisplay: string
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: true

- name: Delete by id
  cisco.ise.sponsor_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {}
  - {}
  - {}
"""
