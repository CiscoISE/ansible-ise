#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sponsorportal
short_description: Resource module for Sponsorportal
description:
  - Manage operation create of the resource Sponsorportal.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  customizations:
    description: Sponsorportal's customizations.
    suboptions:
      globalCustomizations:
        description: Sponsorportal's globalCustomizations.
        suboptions:
          backgroundImage:
            description: Sponsorportal's backgroundImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerImage:
            description: Sponsorportal's bannerImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerTitle:
            description: Sponsorportal's bannerTitle.
            type: str
          contactText:
            description: Sponsorportal's contactText.
            type: str
          footerElement:
            description: Sponsorportal's footerElement.
            type: str
          mobileLogoImage:
            description: Sponsorportal's mobileLogoImage.
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
        description: Sponsorportal's pageCustomizations.
        suboptions:
          data:
            description: The Dictionary will be exposed here as key value pair.
            elements: dict
            type: list
        type: dict
      portalTheme:
        description: Sponsorportal's portalTheme.
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
        description: Sponsorportal's portalTweakSettings.
        suboptions:
          banneColor:
            description: Sponsorportal's banneColor.
            type: str
          bannerTextColor:
            description: Sponsorportal's bannerTextColor.
            type: str
          pageBackgroundColor:
            description: Sponsorportal's pageBackgroundColor.
            type: str
          pageLabelAndTextColor:
            description: Sponsorportal's pageLabelAndTextColor.
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
    description: Sponsorportal's settings.
    suboptions:
      aupSettings:
        description: Sponsorportal's aupSettings.
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
        type: dict
      loginPageSettings:
        description: Sponsorportal's loginPageSettings.
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
            description: Require the portal user to accept the AUP. Only valid if
              includeAup = true.
            type: bool
          timeBetweenLoginsDuringRateLimit:
            description: Time between login attempts when rate limiting.
            type: float
        type: dict
      portalSettings:
        description: Sponsorportal's portalSettings.
        suboptions:
          allowedInterfaces:
            description: Interfaces that the portal will be reachable on. Allowed
              values eth0, eth1, eth2, eth3, eth4, eth5, bond0, bond1 and bond2.
            type: str
          alwaysUsedLanguage:
            description: Used when displayLang = alwaysUse.
            type: str
          authenticationMethod:
            description: Unique Id of the identity source sequence .
            type: str
          availableSSIDs:
            description: Names of the SSIDs available for assignment to guest users
              by sponsors.
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
          fqdn:
            description: The fully-qualified domain name (FQDN) that end-users will
              use to access this portal. Used only in Sponsor portal.
            type: str
          httpsPort:
            description: The port number that the allowed interfaces will listen on.
              Range from 8000 to 8999.
            type: float
          idleTimeout:
            description: Sponsorportal's idleTimeout.
            type: float
        type: dict
      postLoginBannerSettings:
        description: Sponsorportal's postLoginBannerSettings.
        suboptions:
          includePostAccessBanner:
            description: Include a Post-Login Banner page.
            type: bool
        type: dict
      sponsorChangePasswordSettings:
        description: Sponsorportal's sponsorChangePasswordSettings.
        suboptions:
          allowSponsorToChangePwd:
            description: Allow sponsors to change their own passwords.
            type: bool
        type: dict
      supportInfoSettings:
        description: Sponsorportal's supportInfoSettings.
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
    sponsorportal.Sponsorportal.create_sponsorportal,
  - Paths used are
    post /sponsorportal/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.sponsorportal:
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
    portalType: SPONSOR
    settings:
      aupSettings:
        displayFrequency: FIRSTLOGIN
        includeAup: false
        requireAccessCode: false
        requireScrolling: true
        skipAupForEmployees: false
        useDiffAupForEmployees: false
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
        availableSsids:
          - ssid1
          - ssid2
        certificateGroupTag: Default Portal Certificate Group
        displayLang: USEBROWSERLOCALE
        fallbackLanguage: English
        fqdn: Fully Qualified Domain Name
        httpsPort: 8443
        idleTimeout: 10
      postLoginBannerSettings:
        includePostAccessBanner: true
      sponsorChangePasswordSettings:
        allowSponsorToChangePwd: false
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
