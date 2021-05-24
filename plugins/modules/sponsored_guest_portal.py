#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: sponsored_guest_portal
short_description: Resource module for Sponsored Guest Portal
description:
- Manage operations create, update, delete of the resource Sponsored Guest Portal.
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
                  description: Sponsored Guest Portal's data.
                  type: str
              type: dict
            bannerTitle:
              description: Sponsored Guest Portal's bannerTitle.
              type: str
            contactText:
              description: Sponsored Guest Portal's contactText.
              type: str
            desktopLogoImage:
              suboptions:
                data:
                  description: Sponsored Guest Portal's data.
                  type: str
              type: dict
            footerElement:
              description: Sponsored Guest Portal's footerElement.
              type: str
            mobileLogoImage:
              suboptions:
                data:
                  description: Sponsored Guest Portal's data.
                  type: str
              type: dict
          type: dict
        language:
          suboptions:
            viewLanguage:
              description: Sponsored Guest Portal's viewLanguage.
              type: str
          type: dict
        pageCustomizations:
          suboptions:
            data:
              description: Sponsored Guest Portal's data.
              suboptions:
              - suboptions:
                  key:
                    description: Sponsored Guest Portal's key.
                    type: str
                  value:
                    description: Sponsored Guest Portal's value.
                    type: str
                type: dict
              type: list
          type: dict
        portalTheme:
          suboptions:
            id:
              description: Sponsored Guest Portal's id.
              type: str
            name:
              description: Sponsored Guest Portal's name.
              type: str
            themeData:
              description: Sponsored Guest Portal's themeData.
              type: str
          type: dict
        portalTweakSettings:
          suboptions:
            bannerColor:
              description: Sponsored Guest Portal's bannerColor.
              type: str
            bannerTextColor:
              description: Sponsored Guest Portal's bannerTextColor.
              type: str
            pageBackgroundColor:
              description: Sponsored Guest Portal's pageBackgroundColor.
              type: str
            pageLabelAndTextColor:
              description: Sponsored Guest Portal's pageLabelAndTextColor.
              type: str
          type: dict
      type: dict
    description:
      description: Sponsored Guest Portal's description.
      type: str
    id:
      description: Sponsored Guest Portal's id.
      type: str
    name:
      description: Sponsored Guest Portal's name.
      type: str
    portalType:
      description: Sponsored Guest Portal's portalType.
      type: str
    settings:
      suboptions:
        aupSettings:
          suboptions:
            displayFrequency:
              description: Sponsored Guest Portal's displayFrequency.
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
        authSuccessSettings:
          suboptions:
            redirectUrl:
              description: Sponsored Guest Portal's redirectUrl.
              type: str
            successRedirect:
              description: Sponsored Guest Portal's successRedirect.
              type: str
          type: dict
        guestChangePasswordSettings:
          suboptions:
            allowChangePasswdAtFirstLogin:
              description: AllowChangePasswdAtFirstLogin flag.
              type: bool
          type: dict
        guestDeviceRegistrationSettings:
          suboptions:
            allowGuestsToRegisterDevices:
              description: AllowGuestsToRegisterDevices flag.
              type: bool
            autoRegisterGuestDevices:
              description: AutoRegisterGuestDevices flag.
              type: bool
          type: dict
        loginPageSettings:
          suboptions:
            accessCode:
              description: Sponsored Guest Portal's accessCode.
              type: str
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
              description: Sponsored Guest Portal's aupDisplay.
              type: str
            includeAup:
              description: IncludeAup flag.
              type: bool
            maxFailedAttemptsBeforeRateLimit:
              description: Sponsored Guest Portal's maxFailedAttemptsBeforeRateLimit.
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
              description: Sponsored Guest Portal's socialConfigs.
              type: list
            timeBetweenLoginsDuringRateLimit:
              description: Sponsored Guest Portal's timeBetweenLoginsDuringRateLimit.
              type: int
          type: dict
        portalSettings:
          suboptions:
            allowedInterfaces:
              description: Sponsored Guest Portal's allowedInterfaces.
              elements:
                type: str
              type: list
            alwaysUsedLanguage:
              description: Sponsored Guest Portal's alwaysUsedLanguage.
              type: str
            assignedGuestTypeForEmployee:
              description: Sponsored Guest Portal's assignedGuestTypeForEmployee.
              type: str
            authenticationMethod:
              description: Sponsored Guest Portal's authenticationMethod.
              type: str
            availableSsids:
              description: Sponsored Guest Portal's availableSsids.
              type: list
            certificateGroupTag:
              description: Sponsored Guest Portal's certificateGroupTag.
              type: str
            displayLang:
              description: Sponsored Guest Portal's displayLang.
              type: str
            fallbackLanguage:
              description: Sponsored Guest Portal's fallbackLanguage.
              type: str
            httpsPort:
              description: Sponsored Guest Portal's httpsPort.
              type: int
          type: dict
        postLoginBannerSettings:
          suboptions:
            includePostAccessBanner:
              description: IncludePostAccessBanner flag.
              type: bool
          type: dict
        supportInfoSettings:
          suboptions:
            emptyFieldDisplay:
              description: Sponsored Guest Portal's emptyFieldDisplay.
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
- module: cisco.ise.plugins.module_utils.definitions.sponsored_guest_portal
# Reference by Internet resource
- name: Sponsored Guest Portal reference
  description: Complete reference of the Sponsored Guest Portal object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sponsored_guest_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customizations:
      globalCustomizations:
        bannerImage:
          data: base 64 encoded value of image
        bannerTitle: Banner Title
        contactText: 'Contact Information '
        desktopLogoImage:
          data: base 64 encoded value of image
        footerElement: Footer Element
        mobileLogoImage:
          data: base 64 encoded value of image
      language:
        viewLanguage: English
      pageCustomizations:
        data:
        - key: ui_contact_link
          value: Contact Support
      portalTheme:
        id: themeId
        name: ThemeName
        themeData: Base 64 encoded string of Theme CSS file
      portalTweakSettings:
        bannerColor: Banner Color from GUI
        bannerTextColor: Banner Text color code from GUI
        pageBackgroundColor: Color code from GUI
        pageLabelAndTextColor: Label and Text color from GUI
    description: description
    id: id
    name: name
    portalType: SPONSOREDGUEST
    settings:
      aupSettings:
        displayFrequency: FIRSTLOGIN
        includeAup: false
        requireAccessCode: false
        requireScrolling: false
        skipAupForEmployees: false
        useDiffAupForEmployees: false
      authSuccessSettings:
        redirectUrl: www.cisco.com
        successRedirect: AUTHSUCCESSPAGE
      guestChangePasswordSettings:
        allowChangePasswdAtFirstLogin: false
      guestDeviceRegistrationSettings:
        allowGuestsToRegisterDevices: true
        autoRegisterGuestDevices: false
      loginPageSettings:
        accessCode: Access code
        allowAlternateGuestPortal: false
        allowGuestToChangePassword: false
        allowGuestToCreateAccounts: false
        allowGuestToUseSocialAccounts: false
        allowShowGuestForm: false
        aupDisplay: ASLINK
        includeAup: false
        maxFailedAttemptsBeforeRateLimit: 5
        requireAccessCode: false
        requireAupAcceptance: false
        requireAupScrolling: false
        socialConfigs: []
        timeBetweenLoginsDuringRateLimit: 2
      portalSettings:
        allowedInterfaces:
        - eth0
        - bond0
        alwaysUsedLanguage: English
        assignedGuestTypeForEmployee: Guest Type
        authenticationMethod: Identity Source
        availableSsids: []
        certificateGroupTag: Default Portal Certificate Group
        displayLang: USEBROWSERLOCALE
        fallbackLanguage: English
        httpsPort: 8443
      postLoginBannerSettings:
        includePostAccessBanner: true
      supportInfoSettings:
        emptyFieldDisplay: HIDE
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: false

- name: Update by id
  cisco.ise.sponsored_guest_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customizations:
      globalCustomizations:
        bannerImage:
          data: base 64 encoded value of image
        bannerTitle: Banner Title
        contactText: 'Contact Information '
        desktopLogoImage:
          data: base 64 encoded value of image
        footerElement: Footer Element
        mobileLogoImage:
          data: base 64 encoded value of image
      language:
        viewLanguage: English
      pageCustomizations:
        data:
        - key: ui_contact_link
          value: Contact Support
      portalTheme:
        id: themeId
        name: ThemeName
        themeData: Base 64 encoded string of Theme CSS file
      portalTweakSettings:
        bannerColor: Banner Color from GUI
        bannerTextColor: Banner Text color code from GUI
        pageBackgroundColor: Color code from GUI
        pageLabelAndTextColor: Label and Text color from GUI
    description: description
    id: id
    name: name
    portalType: SPONSOREDGUEST
    settings:
      aupSettings:
        displayFrequency: FIRSTLOGIN
        includeAup: false
        requireAccessCode: false
        requireScrolling: false
        skipAupForEmployees: false
        useDiffAupForEmployees: false
      authSuccessSettings:
        redirectUrl: www.cisco.com
        successRedirect: AUTHSUCCESSPAGE
      guestChangePasswordSettings:
        allowChangePasswdAtFirstLogin: false
      guestDeviceRegistrationSettings:
        allowGuestsToRegisterDevices: true
        autoRegisterGuestDevices: false
      loginPageSettings:
        accessCode: Access code
        allowAlternateGuestPortal: false
        allowGuestToChangePassword: false
        allowGuestToCreateAccounts: false
        allowGuestToUseSocialAccounts: false
        allowShowGuestForm: false
        aupDisplay: ASLINK
        includeAup: false
        maxFailedAttemptsBeforeRateLimit: 5
        requireAccessCode: false
        requireAupAcceptance: false
        requireAupScrolling: false
        socialConfigs: []
        timeBetweenLoginsDuringRateLimit: 2
      portalSettings:
        allowedInterfaces:
        - eth0
        - bond0
        alwaysUsedLanguage: English
        assignedGuestTypeForEmployee: Guest Type
        authenticationMethod: Identity Source
        availableSsids: []
        certificateGroupTag: Default Portal Certificate Group
        displayLang: USEBROWSERLOCALE
        fallbackLanguage: English
        httpsPort: 8443
      postLoginBannerSettings:
        includePostAccessBanner: true
      supportInfoSettings:
        emptyFieldDisplay: HIDE
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: false

- name: Delete by id
  cisco.ise.sponsored_guest_portal:
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
