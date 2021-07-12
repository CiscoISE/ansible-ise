#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: byod_portal
short_description: Resource module for Byod Portal
description:
- Manage operations create, update and delete of the resource Byod Portal.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  customizations:
    description: Byod Portal's customizations.
    suboptions:
      globalCustomizations:
        description: Byod Portal's globalCustomizations.
        suboptions:
          bannerImage:
            description: Byod Portal's bannerImage.
            suboptions:
              data:
                description: Byod Portal's data.
                type: str
            type: dict
          bannerTitle:
            description: Byod Portal's bannerTitle.
            type: str
          contactText:
            description: Byod Portal's contactText.
            type: str
          desktopLogoImage:
            description: Byod Portal's desktopLogoImage.
            suboptions:
              data:
                description: Byod Portal's data.
                type: str
            type: dict
          footerElement:
            description: Byod Portal's footerElement.
            type: str
          mobileLogoImage:
            description: Byod Portal's mobileLogoImage.
            suboptions:
              data:
                description: Byod Portal's data.
                type: str
            type: dict
        type: dict
      language:
        description: Byod Portal's language.
        suboptions:
          viewLanguage:
            description: Byod Portal's viewLanguage.
            type: str
        type: dict
      pageCustomizations:
        description: Byod Portal's pageCustomizations.
        suboptions:
          data:
            description: Byod Portal's data.
            suboptions:
              key:
                description: Byod Portal's key.
                type: str
              value:
                description: Byod Portal's value.
                type: str
            type: list
        type: dict
      portalTheme:
        description: Byod Portal's portalTheme.
        suboptions:
          id:
            description: Byod Portal's id.
            type: str
          name:
            description: Byod Portal's name.
            type: str
          themeData:
            description: Byod Portal's themeData.
            type: str
        type: dict
      portalTweakSettings:
        description: Byod Portal's portalTweakSettings.
        suboptions:
          bannerColor:
            description: Byod Portal's bannerColor.
            type: str
          bannerTextColor:
            description: Byod Portal's bannerTextColor.
            type: str
          pageBackgroundColor:
            description: Byod Portal's pageBackgroundColor.
            type: str
          pageLabelAndTextColor:
            description: Byod Portal's pageLabelAndTextColor.
            type: str
        type: dict
    type: dict
  description:
    description: Byod Portal's description.
    type: str
  id:
    description: Byod Portal's id.
    type: str
  name:
    description: Byod Portal's name.
    type: str
  portalType:
    description: Byod Portal's portalType.
    type: str
  settings:
    description: Byod Portal's settings.
    suboptions:
      byodSettings:
        description: Byod Portal's byodSettings.
        suboptions:
          byodRegistrationSettings:
            description: Byod Portal's byodRegistrationSettings.
            suboptions:
              endPointIdentityGroupId:
                description: Byod Portal's endPointIdentityGroupId.
                type: str
              showDeviceID:
                description: ShowDeviceID flag.
                type: bool
            type: dict
          byodRegistrationSuccessSettings:
            description: Byod Portal's byodRegistrationSuccessSettings.
            suboptions:
              redirectUrl:
                description: Byod Portal's redirectUrl.
                type: str
              successRedirect:
                description: Byod Portal's successRedirect.
                type: str
            type: dict
          byodWelcomeSettings:
            description: Byod Portal's byodWelcomeSettings.
            suboptions:
              aupDisplay:
                description: Byod Portal's aupDisplay.
                type: str
              enableBYOD:
                description: EnableBYOD flag.
                type: bool
              enableGuestAccess:
                description: EnableGuestAccess flag.
                type: bool
              includeAup:
                description: IncludeAup flag.
                type: bool
              requireAupAcceptance:
                description: RequireAupAcceptance flag.
                type: bool
              requireMDM:
                description: RequireMDM flag.
                type: bool
              requireScrolling:
                description: RequireScrolling flag.
                type: bool
            type: dict
        type: dict
      portalSettings:
        description: Byod Portal's portalSettings.
        suboptions:
          allowedInterfaces:
            description: Byod Portal's allowedInterfaces.
            elements: str
            type: list
          alwaysUsedLanguage:
            description: Byod Portal's alwaysUsedLanguage.
            type: str
          availableSsids:
            description: Byod Portal's availableSsids.
            type: list
          certificateGroupTag:
            description: Byod Portal's certificateGroupTag.
            type: str
          displayLang:
            description: Byod Portal's displayLang.
            type: str
          fallbackLanguage:
            description: Byod Portal's fallbackLanguage.
            type: str
          httpsPort:
            description: Byod Portal's httpsPort.
            type: int
        type: dict
      supportInfoSettings:
        description: Byod Portal's supportInfoSettings.
        suboptions:
          emptyFieldDisplay:
            description: Byod Portal's emptyFieldDisplay.
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
- module: cisco.ise.plugins.module_utils.definitions.byod_portal
# Reference by Internet resource
- name: Byod Portal reference
  description: Complete reference of the Byod Portal object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.byod_portal:
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
    portalType: BYOD
    settings:
      byodSettings:
        byodRegistrationSettings:
          endPointIdentityGroupId: End Identity Group ID
          showDeviceID: true
        byodRegistrationSuccessSettings:
          redirectUrl: Redirect URL
          successRedirect: AUTHSUCCESSPAGE
        byodWelcomeSettings:
          aupDisplay: ASLINK
          enableBYOD: true
          enableGuestAccess: false
          includeAup: true
          requireAupAcceptance: false
          requireMDM: false
          requireScrolling: false
      portalSettings:
        allowedInterfaces:
        - eth0
        - bond0
        alwaysUsedLanguage: English
        availableSsids: []
        certificateGroupTag: Default Portal Certificate Group
        displayLang: USEBROWSERLOCALE
        fallbackLanguage: English
        httpsPort: 8443
      supportInfoSettings:
        emptyFieldDisplay: HIDE
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: false

- name: Update by id
  cisco.ise.byod_portal:
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
    portalType: BYOD
    settings:
      byodSettings:
        byodRegistrationSettings:
          endPointIdentityGroupId: End Identity Group ID
          showDeviceID: true
        byodRegistrationSuccessSettings:
          redirectUrl: Redirect URL
          successRedirect: AUTHSUCCESSPAGE
        byodWelcomeSettings:
          aupDisplay: ASLINK
          enableBYOD: true
          enableGuestAccess: false
          includeAup: true
          requireAupAcceptance: false
          requireMDM: false
          requireScrolling: false
      portalSettings:
        allowedInterfaces:
        - eth0
        - bond0
        alwaysUsedLanguage: English
        availableSsids: []
        certificateGroupTag: Default Portal Certificate Group
        displayLang: USEBROWSERLOCALE
        fallbackLanguage: English
        httpsPort: 8443
      supportInfoSettings:
        emptyFieldDisplay: HIDE
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: false

- name: Delete by id
  cisco.ise.byod_portal:
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
  type: dict
  sample: >
    {}
"""
