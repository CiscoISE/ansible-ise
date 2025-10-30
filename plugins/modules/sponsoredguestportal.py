#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sponsoredguestportal
short_description: Resource module for Sponsoredguestportal
description:
  - Manage operation create of the resource Sponsoredguestportal.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  customizations:
    description: Sponsoredguestportal's customizations.
    suboptions:
      globalCustomizations:
        description: Sponsoredguestportal's globalCustomizations.
        suboptions:
          backgroundImage:
            description: Sponsoredguestportal's backgroundImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerImage:
            description: Sponsoredguestportal's bannerImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerTitle:
            description: Sponsoredguestportal's bannerTitle.
            type: str
          contactText:
            description: Sponsoredguestportal's contactText.
            type: str
          footerElement:
            description: Sponsoredguestportal's footerElement.
            type: str
          mobileLogoImage:
            description: Sponsoredguestportal's mobileLogoImage.
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
        description: Sponsoredguestportal's pageCustomizations.
        suboptions:
          data:
            description: The Dictionary will be exposed here as key value pair.
            elements: dict
            type: list
        type: dict
      portalTheme:
        description: Sponsoredguestportal's portalTheme.
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
        description: Sponsoredguestportal's portalTweakSettings.
        suboptions:
          banneColor:
            description: Sponsoredguestportal's banneColor.
            type: str
          bannerTextColor:
            description: Sponsoredguestportal's bannerTextColor.
            type: str
          pageBackgroundColor:
            description: Sponsoredguestportal's pageBackgroundColor.
            type: str
          pageLabelAndTextColor:
            description: Sponsoredguestportal's pageLabelAndTextColor.
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
    description: Sponsoredguestportal's settings.
    suboptions:
      aupSettings:
        description: Sponsoredguestportal's aupSettings.
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
            description: Require the portal user to scroll to the end of the AUP.
              Only valid if requireAupAcceptance = true.
            type: bool
          skipAupForEmployees:
            description: Only valid if requireAupAcceptance = true.
            type: bool
          useDiffAupForEmployees:
            description: Only valid if requireAupAcceptance = true.
            type: bool
        type: dict
      authSuccessSettings:
        description: Sponsoredguestportal's authSuccessSettings.
        suboptions:
          redirectUrl:
            description: Target URL for redirection, used when successRedirect = url.
            type: str
          successRedirect:
            description: After an Authentication Success where should user be redirected.
              Allowed Values authSuccessPage, originatingURL and url.
            type: str
        type: dict
      byodSettings:
        description: Sponsoredguestportal's byodSettings.
        suboptions:
          byodRegistrationSettings:
            description: Sponsoredguestportal's byodRegistrationSettings.
            suboptions:
              endPointIdentityGroupId:
                description: TIdentity group id for which endpoint belongs.
                type: str
              showDeviceID:
                description: Display Device ID field during registration.
                type: bool
            type: dict
          byodRegistrationSuccessSettings:
            description: Sponsoredguestportal's byodRegistrationSuccessSettings.
            suboptions:
              redirectUrl:
                description: Target URL for redirection, used when successRedirect
                  = url.
                type: str
              successRedirect:
                description: After an Authentication Success where should device be
                  redirected, allowedValues authSuccessPage, originatingURL and url.
                type: str
            type: dict
          byodWelcomeSettings:
            description: Sponsoredguestportal's byodWelcomeSettings.
            suboptions:
              aupDisplay:
                description: How the AUP should be displayed, either on page or as
                  a link. Only valid if includeAup = true. AllowedValues onPage, asLink.
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
                description: Require BYOD devices to scroll down to the bottom of
                  the AUP, Only valid if includeAup = true.
                type: bool
            type: dict
        type: dict
      guestChangePasswordSettings:
        description: Sponsoredguestportal's guestChangePasswordSettings.
        suboptions:
          allowChangePasswdAtFirstLogin:
            description: Allow guest to change their own passwords.
            type: bool
        type: dict
      guestDeviceRegistrationSettings:
        description: Sponsoredguestportal's guestDeviceRegistrationSettings.
        suboptions:
          allowGuestsToRegisterDevices:
            description: Allow guests to register devices.
            type: bool
          autoRegisterGuestDevices:
            description: Automatically register guest devices.
            type: bool
        type: dict
      loginPageSettings:
        description: Sponsoredguestportal's loginPageSettings.
        suboptions:
          accessCode:
            description: Access code that must be entered by the portal user (only
              valid if requireAccessCode = true).
            type: str
          allowGuestToChangePassword:
            description: Require the portal user to enter an access code.
            type: bool
          allowGuestToCreateAccounts:
            description: AllowGuestToCreateAccounts flag.
            type: bool
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
          requireAccessCode:
            description: Require the portal user to enter an access code.
            type: bool
          requireAupAcceptance:
            description: Require the portal user to accept the AUP. Only valid if
              includeAup = true.
            type: bool
          timeBetweenLoginsDuringRateLimit:
            description: Time between login attempts when rate limiting.
            type: float
        type: dict
      portalSettings:
        description: Sponsoredguestportal's portalSettings.
        suboptions:
          allowedInterfaces:
            description: Interfaces that the portal will be reachable on. Allowed
              values eth0, eth1, eth2, eth3, eth4, eth5, bond0, bond1 and bond2.
            type: str
          alwaysUsedLanguage:
            description: Used when displayLang = alwaysUse.
            type: str
          assignedGuestTypeForEmployee:
            description: Unique Id of a guest type. Employees using this portal as
              a guest inherit login options from the guest type.
            type: str
          authenticationMethod:
            description: Unique Id of the identity source sequence .
            type: str
          certificateGroupTag:
            description: Logical name of the x.509 server certificate that will be
              used for the portal.
            type: str
          displayLang:
            description: Allowed values useBrowserLocale and alwaysUse.
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
        description: Sponsoredguestportal's postLoginBannerSettings.
        suboptions:
          includePostAccessBanner:
            description: Include a Post-Login Banner page.
            type: bool
        type: dict
      supportInfoSettings:
        description: Sponsoredguestportal's supportInfoSettings.
        suboptions:
          defaultEmptyFieldValue:
            description: The default value displayed for an empty field Only valid
              when emptyFieldDisplay = displayWithDefaultValue.
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
    sponsoredguestportal.Sponsoredguestportal.create_sponsoredguestportal,
  - Paths used are
    post /sponsoredguestportal/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.sponsoredguestportal:
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
        allowForgotPassword: false
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
