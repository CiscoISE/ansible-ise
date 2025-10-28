#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: hotspotportal
short_description: Resource module for Hotspotportal
description:
- Manage operation create of the resource Hotspotportal.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  customizations:
    description: Hotspotportal's customizations.
    suboptions:
      globalCustomizations:
        description: Hotspotportal's globalCustomizations.
        suboptions:
          backgroundImage:
            description: Hotspotportal's backgroundImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerImage:
            description: Hotspotportal's bannerImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerTitle:
            description: Hotspotportal's bannerTitle.
            type: str
          contactText:
            description: Hotspotportal's contactText.
            type: str
          footerElement:
            description: Hotspotportal's footerElement.
            type: str
          mobileLogoImage:
            description: Hotspotportal's mobileLogoImage.
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
        description: Hotspotportal's pageCustomizations.
        suboptions:
          data:
            description: The Dictionary will be exposed here as key value pair.
            elements: dict
            type: list
        type: dict
      portalTheme:
        description: Hotspotportal's portalTheme.
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
        description: Hotspotportal's portalTweakSettings.
        suboptions:
          banneColor:
            description: Hotspotportal's banneColor.
            type: str
          bannerTextColor:
            description: Hotspotportal's bannerTextColor.
            type: str
          pageBackgroundColor:
            description: Hotspotportal's pageBackgroundColor.
            type: str
          pageLabelAndTextColor:
            description: Hotspotportal's pageLabelAndTextColor.
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
    description: Hotspotportal's settings.
    suboptions:
      aupSettings:
        description: Hotspotportal's aupSettings.
        suboptions:
          accessCode:
            description: Access code that must be entered by the portal user (only valid
              if requireAccessCode = true).
            type: str
          includeAup:
            description: Require the portal user to read and accept an AUP.
            type: bool
          requireAccessCode:
            description: Require the portal user to enter an access code. Only used
              in Hotspot portal.
            type: bool
          requireAupScrolling:
            description: Require the portal user to scroll to the end of the AUP. Only
              valid if requireAupAcceptance = true.
            type: bool
        type: dict
      authSuccessSettings:
        description: Hotspotportal's authSuccessSettings.
        suboptions:
          redirectUrl:
            description: Target URL for redirection, used when successRedirect = url.
            type: str
          successRedirect:
            description: After an Authentication Success where should user be redirected.
              Allowed Values authSuccessPage, originatingURL and url.
            type: str
        type: dict
      portalSettings:
        description: Hotspotportal's portalSettings.
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
          coaType:
            description: Allowed Values coaReauthenticate and coaTerminate.
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
        description: Hotspotportal's postLoginBannerSettings.
        suboptions:
          includePostAccessBanner:
            description: Include a Post-Login Banner page.
            type: bool
        type: dict
      supportInfoSettings:
        description: Hotspotportal's supportInfoSettings.
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
    hotspotportal.Hotspotportal.create_hotspotportal,

  - Paths used are
    post /hotspotportal/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.hotspotportal:
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
    portalType: HOTSPOTGUEST
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
      portalSettings:
        allowedInterfaces:
        - eth0
        - bond0
        alwaysUsedLanguage: English
        availableSsids: []
        certificateGroupTag: Default Portal Certificate Group
        coaType: COAREAUTHENTICATE
        displayLang: USEBROWSERLOCALE
        endpointIdentityGroup: f14227b0-6e5c-11e6-8f6a-005056873bd0
        fallbackLanguage: English
        httpsPort: 8443
      postAccessBannerSettings:
        includePostAccessBanner: false
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
