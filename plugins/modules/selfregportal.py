#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: selfregportal
short_description: Resource module for Selfregportal
description:
  - Manage operation create of the resource Selfregportal.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  customizations:
    description: Selfregportal's customizations.
    suboptions:
      globalCustomizations:
        description: Selfregportal's globalCustomizations.
        suboptions:
          backgroundImage:
            description: Selfregportal's backgroundImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerImage:
            description: Selfregportal's bannerImage.
            suboptions:
              data:
                description: Represented as base 64 encoded string of the image byte
                  array.
                type: str
            type: dict
          bannerTitle:
            description: Selfregportal's bannerTitle.
            type: str
          contactText:
            description: Selfregportal's contactText.
            type: str
          footerElement:
            description: Selfregportal's footerElement.
            type: str
          mobileLogoImage:
            description: Selfregportal's mobileLogoImage.
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
        description: Selfregportal's pageCustomizations.
        suboptions:
          data:
            description: The Dictionary will be exposed here as key value pair.
            elements: dict
            type: list
        type: dict
      portalTheme:
        description: Selfregportal's portalTheme.
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
        description: Selfregportal's portalTweakSettings.
        suboptions:
          banneColor:
            description: Selfregportal's banneColor.
            type: str
          bannerTextColor:
            description: Selfregportal's bannerTextColor.
            type: str
          pageBackgroundColor:
            description: Selfregportal's pageBackgroundColor.
            type: str
          pageLabelAndTextColor:
            description: Selfregportal's pageLabelAndTextColor.
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
    description: Selfregportal's settings.
    suboptions:
      aupSettings:
        description: Selfregportal's aupSettings.
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
        description: Selfregportal's authSuccessSettings.
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
        description: Selfregportal's byodSettings.
        suboptions:
          byodRegistrationSettings:
            description: Selfregportal's byodRegistrationSettings.
            suboptions:
              endPointIdentityGroupId:
                description: TIdentity group id for which endpoint belongs.
                type: str
              showDeviceID:
                description: Display Device ID field during registration.
                type: bool
            type: dict
          byodRegistrationSuccessSettings:
            description: Selfregportal's byodRegistrationSuccessSettings.
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
            description: Selfregportal's byodWelcomeSettings.
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
        description: Selfregportal's guestChangePasswordSettings.
        suboptions:
          allowChangePasswdAtFirstLogin:
            description: Allow guest to change their own passwords.
            type: bool
        type: dict
      guestDeviceRegistrationSettings:
        description: Selfregportal's guestDeviceRegistrationSettings.
        suboptions:
          allowGuestsToRegisterDevices:
            description: Allow guests to register devices.
            type: bool
          autoRegisterGuestDevices:
            description: Automatically register guest devices.
            type: bool
        type: dict
      loginPageSettings:
        description: Selfregportal's loginPageSettings.
        suboptions:
          accessCode:
            description: Access code that must be entered by the portal user (only
              valid if requireAccessCode = true).
            type: str
          allowAlternateGuestPortal:
            description: AllowAlternateGuestPortal flag.
            type: bool
          allowGuestToChangePassword:
            description: Require the portal user to enter an access code.
            type: bool
          allowGuestToCreateAccounts:
            description: AllowGuestToCreateAccounts flag.
            type: bool
          alternateGuestPortal:
            description: Selfregportal's alternateGuestPortal.
            type: str
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
        description: Selfregportal's portalSettings.
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
        description: Selfregportal's postLoginBannerSettings.
        suboptions:
          includePostAccessBanner:
            description: Include a Post-Login Banner page.
            type: bool
        type: dict
      selfRegPageSettings:
        description: Selfregportal's selfRegPageSettings.
        suboptions:
          accountValidityDuration:
            description: Self-registered guest account is valid for this many account_validity_time_units.
            type: float
          accountValidityTimeUnits:
            description: Time units for account_validity_duration. Allowed Values
              days, hours and minutes.
            type: str
          approvalEmailAddresses:
            description: Only valid if requireGuestApproval = true and sendApprovalRequestTo
              = selectedEmailAddresses.
            type: str
          approveDenyLinksTimeUnits:
            description: This attribute, along with approveDenyLinksValidFor, specifies
              how long the link can be used. Only valid if requireGuestApproval =
              true. Allowed Values days, hours and minutes.
            type: str
          approveDenyLinksValidFor:
            description: This attribute, along with approveDenyLinksTimeUnits, specifies
              how long the link can be used. Only valid if requireGuestApproval =
              true.
            type: float
          assignGuestsToGuestType:
            description: Guests are assigned to this guest type.
            type: str
          aupDisplay:
            description: How the AUP should be displayed, either on page or as a link.
              Only valid if includeAup = true. Allowed Values onPage and asLink.
            type: str
          autoLoginSelfWait:
            description: Allow guests to login automatically from self-registration
              after sponsor's approval. No need to provide the credentials by guest
              to login.
            type: bool
          autoLoginTimePeriod:
            description: Waiting period for auto login until sponsor's approval. If
              time exceeds, guest has to login manually by providing the credentials.
              Default value is 5 minutes.
            type: dict
          credentialNotificationUsingEmail:
            description: If true, send credential notification upon approval using
              email. Only valid if requireGuestApproval = true.
            type: bool
          credentialNotificationUsingSMS:
            description: If true, send credential notification upon approval using
              SMS. Only valid if requireGuestApproval = true.
            type: bool
          enableGuestEmailAllowlist:
            description: Allow guests with an e-mail address from selected domains.
            type: bool
          enableGuestEmailBlocklist:
            description: Disallow guests with an e-mail address from selected domains.
            type: bool
          fieldCompany:
            description: Selfregportal's fieldCompany.
            suboptions:
              displayFrequency:
                description: Only applicable if include = true.
                type: bool
              include:
                description: Include flag.
                type: bool
            type: dict
          fieldEmailAddr:
            description: Selfregportal's fieldEmailAddr.
            suboptions:
              displayFrequency:
                description: Only applicable if include = true.
                type: bool
              include:
                description: Include flag.
                type: bool
            type: dict
          fieldFirstName:
            description: Selfregportal's fieldFirstName.
            suboptions:
              displayFrequency:
                description: Only applicable if include = true.
                type: bool
              include:
                description: Include flag.
                type: bool
            type: dict
          fieldLastName:
            description: Selfregportal's fieldLastName.
            suboptions:
              displayFrequency:
                description: Only applicable if include = true.
                type: bool
              include:
                description: Include flag.
                type: bool
            type: dict
          fieldLocation:
            description: Selfregportal's fieldLocation.
            suboptions:
              displayFrequency:
                description: Only applicable if include = true.
                type: bool
              include:
                description: Include flag.
                type: bool
            type: dict
          fieldPersonBeingVisited:
            description: Selfregportal's fieldPersonBeingVisited.
            suboptions:
              displayFrequency:
                description: Only applicable if include = true.
                type: bool
              include:
                description: Include flag.
                type: bool
            type: dict
          fieldPhoneNo:
            description: Selfregportal's fieldPhoneNo.
            suboptions:
              displayFrequency:
                description: Only applicable if include = true.
                type: bool
              include:
                description: Include flag.
                type: bool
            type: dict
          fieldReasonForVisit:
            description: Selfregportal's fieldReasonForVisit.
            suboptions:
              displayFrequency:
                description: Only applicable if include = true.
                type: bool
              include:
                description: Include flag.
                type: bool
            type: dict
          fieldSMSProvider:
            description: Selfregportal's fieldSMSProvider.
            suboptions:
              displayFrequency:
                description: Only applicable if include = true.
                type: bool
              include:
                description: Include flag.
                type: bool
            type: dict
          fieldUserName:
            description: Selfregportal's fieldUserName.
            suboptions:
              displayFrequency:
                description: Only applicable if include = true.
                type: bool
              include:
                description: Include flag.
                type: bool
            type: dict
          guestEmailAllowlistDomains:
            description: Self-registered guests whose e-mail address is in one of
              these domains will be allowed. Only valid if enableGuestEmailWhitelist
              = true.
            elements: str
            type: list
          guestEmailBlocklistDomains:
            description: Self-registered guests whose e-mail address is in one of
              these domains will be disallowed. Only valid if enableGuestEmailBlacklist
              = true.
            elements: str
            type: list
          includeAup:
            description: Include an Acceptable Use Policy (AUP) that should be displayed
              during login.
            type: bool
          postRegistrationRedirect:
            description: After the registration submission direct the guest user to
              one of the following pages. Only valid if requireGuestApproval = true.
              Allowed Values selfRegistrationSuccess, loginPageWithInstructions and
              url.
            type: str
          postRegistrationRedirectUrl:
            description: URL where guest user is redirected after registration. Only
              valid if requireGuestApproval = true and postRegistrationRedirect =
              url.
            type: str
          registrationCode:
            description: The registration code that the guest user must enter.
            type: str
          requireApproverToAuthenticate:
            description: When self-registered guests require approval, an approval
              request is e-mailed to one or more sponsor users. If the ISE Administrator
              chooses to include an approval link in the e-mail, a sponsor user who
              clicks the link will be required to enter their username and password
              if this attribute is true. Only valid if requireGuestApproval = true.
            type: bool
          requireAupAcceptance:
            description: Require the portal user to accept the AUP. Only valid if
              includeAup = true.
            type: bool
          requireGuestApproval:
            description: Require self-registered guests to be approved if true.
            type: bool
          requireRegistrationCode:
            description: Self-registered guests are required to enter a registration
              code.
            type: bool
          selectableLocations:
            description: Guests can choose from these locations to set their time
              zone.
            elements: str
            type: list
          selectableSMSProviders:
            description: This attribute is an array of SMS provider names.
            elements: str
            type: list
          sendApprovalRequestTo:
            description: Specifies where approval requests are sent. Only valid if
              requireGuestApproval = true. Allowed Values selectedEmailAddresses and
              personBeingVisited.
            type: str
          sponsorPortalList:
            description: When self-registered guests require approval, an approval
              request is e-mailed to one or more sponsor users. If the ISE Administrator
              chooses to include an approval link in the e-mail, a sponsor user who
              clicks the link will be authenticated against the selected sponsor portals
              in the order specified. Only valid if requireGuestApproval = true. The
              array should contain the names of the selected portals.
            elements: str
            type: list
        type: dict
      selfRegSuccessSettings:
        description: Selfregportal's selfRegSuccessSettings.
        suboptions:
          allowGuestLoginFromSelfregSuccessPage:
            description: AllowGuestLoginFromSelfregSuccessPage flag.
            type: bool
          allowGuestSendSelfUsingEmail:
            description: AllowGuestSendSelfUsingEmail flag.
            type: bool
          allowGuestSendSelfUsingPrint:
            description: AllowGuestSendSelfUsingPrint flag.
            type: bool
          allowGuestSendSelfUsingSMS:
            description: AllowGuestSendSelfUsingSMS flag.
            type: bool
          aupOnPage:
            description: AupOnPage flag.
            type: bool
          includeAup:
            description: IncludeAup flag.
            type: bool
          includeCompany:
            description: IncludeCompany flag.
            type: bool
          includeEmailAddr:
            description: IncludeEmailAddr flag.
            type: bool
          includeFirstName:
            description: IncludeFirstName flag.
            type: bool
          includeLastName:
            description: IncludeLastName flag.
            type: bool
          includeLocation:
            description: IncludeLocation flag.
            type: bool
          includePassword:
            description: IncludePassword flag.
            type: bool
          includePersonBeingVisited:
            description: IncludePersonBeingVisited flag.
            type: bool
          includePhoneNo:
            description: IncludePhoneNo flag.
            type: bool
          includeReasonForVisit:
            description: IncludeReasonForVisit flag.
            type: bool
          includeSMSProvider:
            description: IncludeSMSProvider flag.
            type: bool
          includeUserName:
            description: IncludeUserName flag.
            type: bool
          requireAupAcceptance:
            description: RequireAupAcceptance flag.
            type: bool
          requireAupScrolling:
            description: RequireAupScrolling flag.
            type: bool
        type: dict
      supportInfoSettings:
        description: Selfregportal's supportInfoSettings.
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
    selfregportal.Selfregportal.create_selfregportal,
  - Paths used are
    post /selfregportal/,
"""
EXAMPLES = r"""
---
- name: Create
  cisco.ise.selfregportal:
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
    portalType: SELFREGGUEST
    settings:
      aupSettings:
        displayFrequency: FIRSTLOGIN
        includeAup: false
        requireAccessCode: false
        requireScrolling: true
        skipAupForEmployees: true
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
        accessCode: Access Code
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
        assignedGuestTypeForEmployee: Guest Type configured
        authenticationMethod: Identity Sequence
        availableSsids: []
        certificateGroupTag: Default Portal Certificate Group
        displayLang: USEBROWSERLOCALE
        endpointIdentityGroup: f14227b0-6e5c-11e6-8f6a-005056873bd0
        fallbackLanguage: English
        httpsPort: 8443
      postLoginBannerSettings:
        includePostAccessBanner: true
      selfRegPageSettings:
        accountValidityDuration: 1
        accountValidityTimeUnits: DAYS
        allowGraceAccess: false
        approveDenyLinksTimeUnits: DAYS
        assignGuestsToGuestType: Guest Type
        aupDisplay: ASLINK
        authenticateSponsorsUsingPortalList: false
        autoLoginSelfWait: false
        autoLoginTimePeriod: 1
        credentialNotificationUsingEmail: false
        credentialNotificationUsingSms: false
        enableGuestEmailBlacklist: false
        enableGuestEmailWhitelist: false
        fieldCompany:
          include: true
          require: false
        fieldEmailAddr:
          include: true
          require: false
        fieldFirstName:
          include: true
          require: false
        fieldLastName:
          include: true
          require: false
        fieldLocation:
          include: true
          require: false
        fieldPhoneNo:
          include: true
          require: false
        fieldReasonForVisit:
          include: true
          require: false
        fieldSmsProvider:
          include: true
          require: false
        fieldUserName:
          include: true
          require: false
        graceAccessExpireInterval: 10
        graceAccessSendAccountExpiration: false
        guestEmailBlacklistDomains:
          - test1@cisco.com
        guestEmailWhitelistDomains:
          - test@cisco.com
        includeAup: false
        postRegistrationRedirect: SELFREGISTRATIONSUCCESS
        registrationCode: Registration Code
        requireAupAcceptance: false
        requireGuestApproval: false
        requireRegistrationCode: false
        selectableLocations:
          - location1
          - location2
        selectableSmsProviders:
          - Sms1
        sendApprovalRequestTo: SELECTEDEMAILADDRESSES
        sponsorPortalList: []
      selfRegSuccessSettings:
        allowGuestLoginFromSelfregSuccessPage: true
        allowGuestSendSelfUsingEmail: true
        allowGuestSendSelfUsingPrint: true
        allowGuestSendSelfUsingSms: true
        aupOnPage: false
        includeAup: false
        includeCompany: true
        includeEmailAddr: true
        includeFirstName: true
        includeLastName: true
        includeLocation: true
        includePassword: true
        includePersonBeingVisited: true
        includePhoneNo: true
        includeReasonForVisit: true
        includeSmsProvider: true
        includeUserName: true
        requireAupAcceptance: false
        requireAupScrolling: false
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
