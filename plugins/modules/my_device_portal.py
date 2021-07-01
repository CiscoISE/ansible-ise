#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: my_device_portal
short_description: Resource module for My Device Portal
description:
- Manage operations create and update of the resource My Device Portal.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  customizations:
    description: My Device Portal's customizations.
    suboptions:
      globalCustomizations:
        description: My Device Portal's globalCustomizations.
        suboptions:
          bannerImage:
            description: My Device Portal's bannerImage.
            suboptions:
              data:
                description: My Device Portal's data.
                type: str
            type: dict
          bannerTitle:
            description: My Device Portal's bannerTitle.
            type: str
          contactText:
            description: My Device Portal's contactText.
            type: str
          desktopLogoImage:
            description: My Device Portal's desktopLogoImage.
            suboptions:
              data:
                description: My Device Portal's data.
                type: str
            type: dict
          footerElement:
            description: My Device Portal's footerElement.
            type: str
          mobileLogoImage:
            description: My Device Portal's mobileLogoImage.
            suboptions:
              data:
                description: My Device Portal's data.
                type: str
            type: dict
        type: dict
      language:
        description: My Device Portal's language.
        suboptions:
          viewLanguage:
            description: My Device Portal's viewLanguage.
            type: str
        type: dict
      pageCustomizations:
        description: My Device Portal's pageCustomizations.
        suboptions:
          data:
            description: My Device Portal's data.
            suboptions:
              key:
                description: My Device Portal's key.
                type: str
              value:
                description: My Device Portal's value.
                type: str
            type: list
        type: dict
      portalTheme:
        description: My Device Portal's portalTheme.
        suboptions:
          id:
            description: My Device Portal's id.
            type: str
          name:
            description: My Device Portal's name.
            type: str
          themeData:
            description: My Device Portal's themeData.
            type: str
        type: dict
      portalTweakSettings:
        description: My Device Portal's portalTweakSettings.
        suboptions:
          bannerColor:
            description: My Device Portal's bannerColor.
            type: str
          bannerTextColor:
            description: My Device Portal's bannerTextColor.
            type: str
          pageBackgroundColor:
            description: My Device Portal's pageBackgroundColor.
            type: str
          pageLabelAndTextColor:
            description: My Device Portal's pageLabelAndTextColor.
            type: str
        type: dict
    type: dict
  description:
    description: My Device Portal's description.
    type: str
  id:
    description: My Device Portal's id.
    type: str
  name:
    description: My Device Portal's name.
    type: str
  portalType:
    description: My Device Portal's portalType.
    type: str
  settings:
    description: My Device Portal's settings.
    suboptions:
      aupSettings:
        description: My Device Portal's aupSettings.
        suboptions:
          displayFrequency:
            description: My Device Portal's displayFrequency.
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
      employeeChangePasswordSettings:
        description: My Device Portal's employeeChangePasswordSettings.
        suboptions:
          allowEmployeeToChangePwd:
            description: AllowEmployeeToChangePwd flag.
            type: bool
        type: dict
      loginPageSettings:
        description: My Device Portal's loginPageSettings.
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
            description: My Device Portal's aupDisplay.
            type: str
          includeAup:
            description: IncludeAup flag.
            type: bool
          maxFailedAttemptsBeforeRateLimit:
            description: My Device Portal's maxFailedAttemptsBeforeRateLimit.
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
            description: My Device Portal's socialConfigs.
            type: list
          timeBetweenLoginsDuringRateLimit:
            description: My Device Portal's timeBetweenLoginsDuringRateLimit.
            type: int
        type: dict
      portalSettings:
        description: My Device Portal's portalSettings.
        suboptions:
          allowedInterfaces:
            description: My Device Portal's allowedInterfaces.
            elements: str
            type: list
          alwaysUsedLanguage:
            description: My Device Portal's alwaysUsedLanguage.
            type: str
          authenticationMethod:
            description: My Device Portal's authenticationMethod.
            type: str
          availableSsids:
            description: My Device Portal's availableSsids.
            type: list
          certificateGroupTag:
            description: My Device Portal's certificateGroupTag.
            type: str
          displayLang:
            description: My Device Portal's displayLang.
            type: str
          endpointIdentityGroup:
            description: My Device Portal's endpointIdentityGroup.
            type: str
          fallbackLanguage:
            description: My Device Portal's fallbackLanguage.
            type: str
          fqdn:
            description: My Device Portal's fqdn.
            type: str
          httpsPort:
            description: My Device Portal's httpsPort.
            type: int
          idleTimeout:
            description: My Device Portal's idleTimeout.
            type: int
        type: dict
      postLoginBannerSettings:
        description: My Device Portal's postLoginBannerSettings.
        suboptions:
          includePostAccessBanner:
            description: IncludePostAccessBanner flag.
            type: bool
        type: dict
      supportInfoSettings:
        description: My Device Portal's supportInfoSettings.
        suboptions:
          emptyFieldDisplay:
            description: My Device Portal's emptyFieldDisplay.
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
- module: cisco.ise.plugins.module_utils.definitions.my_device_portal
# Reference by Internet resource
- name: My Device Portal reference
  description: Complete reference of the My Device Portal object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.my_device_portal:
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
      employeeChangePasswordSettings:
        allowEmployeeToChangePwd: true
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
        availableSsids: []
        certificateGroupTag: string
        displayLang: string
        endpointIdentityGroup: string
        fallbackLanguage: string
        fqdn: string
        httpsPort: 0
        idleTimeout: 0
      postLoginBannerSettings:
        includePostAccessBanner: true
      supportInfoSettings:
        emptyFieldDisplay: string
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: true

- name: Update by id
  cisco.ise.my_device_portal:
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
      employeeChangePasswordSettings:
        allowEmployeeToChangePwd: true
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
        availableSsids: []
        certificateGroupTag: string
        displayLang: string
        endpointIdentityGroup: string
        fallbackLanguage: string
        fqdn: string
        httpsPort: 0
        idleTimeout: 0
      postLoginBannerSettings:
        includePostAccessBanner: true
      supportInfoSettings:
        emptyFieldDisplay: string
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: true

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
