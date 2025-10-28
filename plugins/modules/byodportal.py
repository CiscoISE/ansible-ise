#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: byodportal
short_description: Resource module for BYODportal
description:
  - Manage operation create of the resource BYODportal.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  customizations:
    description: BYODportal's customizations.
    suboptions:
      globalCustomizations:
        description: BYODportal's globalCustomizations.
        suboptions:
          backgroundImage:
            description: BYODportal's backgroundImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerImage:
            description: BYODportal's bannerImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerTitle:
            description: BYODportal's bannerTitle.
            type: str
          contactText:
            description: BYODportal's contactText.
            type: str
          footerElement:
            description: BYODportal's footerElement.
            type: str
          mobileLogoImage:
            description: BYODportal's mobileLogoImage.
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
        description: BYODportal's pageCustomizations.
        suboptions:
          data:
            description: The Dictionary will be exposed here as key value pair.
            elements: dict
            type: list
        type: dict
      portalTheme:
        description: BYODportal's portalTheme.
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
        description: BYODportal's portalTweakSettings.
        suboptions:
          banneColor:
            description: BYODportal's banneColor.
            type: str
          bannerTextColor:
            description: BYODportal's bannerTextColor.
            type: str
          pageBackgroundColor:
            description: BYODportal's pageBackgroundColor.
            type: str
          pageLabelAndTextColor:
            description: BYODportal's pageLabelAndTextColor.
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
    description: BYODportal's settings.
    suboptions:
      byodSettings:
        description: BYODportal's byodSettings.
        suboptions:
          byodRegistrationSettings:
            description: BYODportal's byodRegistrationSettings.
            suboptions:
              endPointIdentityGroupId:
                description: TIdentity group id for which endpoint belongs.
                type: str
              showDeviceID:
                description: Display Device ID field during registration.
                type: bool
            type: dict
          byodRegistrationSuccessSettings:
            description: BYODportal's byodRegistrationSuccessSettings.
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
            description: BYODportal's byodWelcomeSettings.
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
      portalSettings:
        description: BYODportal's portalSettings.
        suboptions:
          allowedInterfaces:
            description: Interfaces that the portal will be reachable on. Allowed
              values eth0, eth1, eth2, eth3, eth4, eth5, bond0, bond1 and bond2.
            type: str
          alwaysUsedLanguage:
            description: Used when displayLang = alwaysUse.
            type: str
          certificateGroupTag:
            description: Logical name of the x.509 server certificate that will be
              used for the portal.
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
      supportInfoSettings:
        description: BYODportal's supportInfoSettings.
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
    byodportal.Byodportal.create_byodportal,
  - Paths used are
    post /byodportal/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.byodportal:
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
