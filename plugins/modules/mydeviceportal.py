#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: mydeviceportal
short_description: Resource module for Mydeviceportal
description:
- Manage operation create of the resource Mydeviceportal.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  customizations:
    description: Mydeviceportal's customizations.
    suboptions:
      globalCustomizations:
        description: Mydeviceportal's globalCustomizations.
        suboptions:
          backgroundImage:
            description: Mydeviceportal's backgroundImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerImage:
            description: Mydeviceportal's bannerImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerTitle:
            description: Mydeviceportal's bannerTitle.
            type: str
          contactText:
            description: Mydeviceportal's contactText.
            type: str
          footerElement:
            description: Mydeviceportal's footerElement.
            type: str
          mobileLogoImage:
            description: Mydeviceportal's mobileLogoImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
        type: dict
      language:
        description: This property is supported only for Read operation and it allows
          to show the customizations in English. Other languages are not supported.
        type: dict
      pageCustomizations:
        description: Mydeviceportal's pageCustomizations.
        suboptions:
          data:
            description: The Dictionary will be exposed here as key value pair.
            elements: dict
            type: list
        type: dict
      portalTheme:
        description: Mydeviceportal's portalTheme.
        suboptions:
          id:
            description: The unique internal identifier of the portal theme.
            type: str
          name:
            description: The system- or user-assigned name of the portal theme.
            type: str
          themeData:
            description: A CSS file, represented as a Base64-encoded byte array.
            type: str
        type: dict
      portalTweakSettings:
        description: Mydeviceportal's portalTweakSettings.
        suboptions:
          banneColor:
            description: Mydeviceportal's banneColor.
            type: str
          bannerTextColor:
            description: Mydeviceportal's bannerTextColor.
            type: str
          pageBackgroundColor:
            description: Mydeviceportal's pageBackgroundColor.
            type: str
          pageLabelAndTextColor:
            description: Mydeviceportal's pageLabelAndTextColor.
            type: str
        type: dict
    type: dict
  description:
    description: Description.
    type: str
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
  portalTestUrl:
    description: URL to bring up a test page for this portal.
    type: str
  portalType:
    description: Allowed values byod, hotspotGuest, mydevice, selfRegGuest, sponsor
      and sponsoredGuest.
    type: str
  settings:
    description: Mydeviceportal's settings.
    suboptions:
      aupSettings:
        description: Mydeviceportal's aupSettings.
        suboptions:
          displayFrequency:
            description: How the AUP should be displayed, either on page or as a link.
              Only valid if includeAup = true. Allowed Values firstLogin, everyLogin
              and recurring.
            type: str
          displayFrequencyIntervalDays:
            description: Number of days between AUP confirmations (when displayFrequency
              = recurring).
            type: float
          includeAup:
            description: Require the portal user to read and accept an AUP.
            type: bool
          requireAupScrolling:
            description: Require the portal user to scroll to the end of the AUP. Only
              valid if requireAupAcceptance = true.
            type: bool
        type: dict
      employeeChangePasswordSettings:
        description: Mydeviceportal's employeeChangePasswordSettings.
        suboptions:
          allowEmployeeToChangePwd:
            description: Allow employees to change their own passwords.
            type: bool
        type: dict
      loginPageSettings:
        description: Mydeviceportal's loginPageSettings.
        suboptions:
          aupDisplay:
            description: How the AUP should be displayed, either on page or as a link.
              Only valid if includeAup = true. Allowed Values onPage and asLink.
            type: str
          includeAup:
            description: Include an Acceptable Use Policy (AUP) that should be displayed
              during login.
            type: bool
          maxFailedAttemptsBeforeRateLimit:
            description: Maximum failed login attempts before rate limiting.
            type: float
          requireAupAcceptance:
            description: Require the portal user to accept the AUP. Only valid if includeAup
              = true.
            type: bool
          requireAupScrolling:
            description: Require the portal user to scroll to the end of the AUP. Only
              valid if requireAupAcceptance = true.
            type: bool
          timeBetweenLoginsDuringRateLimit:
            description: Mydeviceportal's timeBetweenLoginsDuringRateLimit.
            type: float
        type: dict
      portalSettings:
        description: Mydeviceportal's portalSettings.
        suboptions:
          allowedInterfaces:
            description: Interfaces that the portal will be reachable on. Allowed values
              eth0, eth1, eth2, eth3, eth4, eth5, bond0, bond1 and bond2.
            type: str
          alwaysUsedLanguage:
            description: Used when displayLang = alwaysUse.
            type: str
          certificateGroupTag:
            description: Logical name of the x.509 server certificate that will be used
              for the portal.
            type: str
          displayLang:
            description: Allowed values useBrowserLocale and alwaysUse.
            type: str
          endpointIdentityGroup:
            description: Unique Id of the endpoint identity group where user's devices
              will be added. Used only in Hotspot Portal.
            type: str
          fallbackLanguage:
            description: Used when displayLang = useBrowserLocale.
            type: str
          httpsPort:
            description: The port number that the allowed interfaces will listen on.
              Range from 8000 to 8999.
            type: float
        type: dict
      postLoginBannerSettings:
        description: Mydeviceportal's postLoginBannerSettings.
        suboptions:
          includePostAccessBanner:
            description: Include a Post-Login Banner page.
            type: bool
        type: dict
      supportInfoSettings:
        description: Mydeviceportal's supportInfoSettings.
        suboptions:
          defaultEmptyFieldValue:
            description: The default value displayed for an empty field Only valid when
              emptyFieldDisplay = displayWithDefaultValue.
            type: str
          emptyFieldDisplay:
            description: Specifies how empty fields are handled on the Support Information
              Page. AllowedValues hide, displayWithNoValue and displayWithDefaultValue.
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
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    mydeviceportal.Mydeviceportal.create_mydeviceportal,

  - Paths used are
    post /mydeviceportal/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.mydeviceportal:
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
    id: f75760e7-a4f9-40ef-93bb-88a97e9fb171
    name: name
    portalType: MYDEVICE
    settings:
      aupSettings:
        displayFrequency: FIRSTLOGIN
        includeAup: false
        requireAccessCode: false
        requireScrolling: true
        skipAupForEmployees: false
        useDiffAupForEmployees: false
      employeeChangePasswordSettings:
        allowEmployeeToChangePwd: false
      loginPageSettings:
        allowAlternateGuestPortal: false
        allowForgotPassword: true
        allowGuestToChangePassword: false
        allowGuestToCreateAccounts: true
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
        authenticationMethod: Identity Source
        availableSsids: []
        certificateGroupTag: Default Portal Certificate Group
        displayLang: USEBROWSERLOCALE
        endpointIdentityGroup: Identity Group
        fallbackLanguage: English
        fqdn: Fully Qualified Domain Name
        httpsPort: 8443
        idleTimeout: 10
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

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
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
"""
