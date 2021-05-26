#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: self_registered_portal
short_description: Resource module for Self Registered Portal
description:
- Manage operations create, update, delete of the resource Self Registered Portal.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    customizations:
      description: Self Registered Portal's customizations.
      suboptions:
        globalCustomizations:
          description: Self Registered Portal's globalCustomizations.
          suboptions:
            bannerImage:
              description: Self Registered Portal's bannerImage.
              suboptions:
                data:
                  description: Self Registered Portal's data.
                  type: str
              type: dict
            bannerTitle:
              description: Self Registered Portal's bannerTitle.
              type: str
            contactText:
              description: Self Registered Portal's contactText.
              type: str
            desktopLogoImage:
              description: Self Registered Portal's desktopLogoImage.
              suboptions:
                data:
                  description: Self Registered Portal's data.
                  type: str
              type: dict
            footerElement:
              description: Self Registered Portal's footerElement.
              type: str
            mobileLogoImage:
              description: Self Registered Portal's mobileLogoImage.
              suboptions:
                data:
                  description: Self Registered Portal's data.
                  type: str
              type: dict
          type: dict
        language:
          description: Self Registered Portal's language.
          suboptions:
            viewLanguage:
              description: Self Registered Portal's viewLanguage.
              type: str
          type: dict
        pageCustomizations:
          description: Self Registered Portal's pageCustomizations.
          suboptions:
            data:
              description: Self Registered Portal's data.
              suboptions:
                key:
                  description: Self Registered Portal's key.
                  type: str
                value:
                  description: Self Registered Portal's value.
                  type: str
              type: list
          type: dict
        portalTheme:
          description: Self Registered Portal's portalTheme.
          suboptions:
            id:
              description: Self Registered Portal's id.
              type: str
            name:
              description: Self Registered Portal's name.
              type: str
            themeData:
              description: Self Registered Portal's themeData.
              type: str
          type: dict
        portalTweakSettings:
          description: Self Registered Portal's portalTweakSettings.
          suboptions:
            bannerColor:
              description: Self Registered Portal's bannerColor.
              type: str
            bannerTextColor:
              description: Self Registered Portal's bannerTextColor.
              type: str
            pageBackgroundColor:
              description: Self Registered Portal's pageBackgroundColor.
              type: str
            pageLabelAndTextColor:
              description: Self Registered Portal's pageLabelAndTextColor.
              type: str
          type: dict
      type: dict
    description:
      description: Self Registered Portal's description.
      type: str
    id:
      description: Self Registered Portal's id.
      type: str
    name:
      description: Self Registered Portal's name.
      type: str
    portalType:
      description: Self Registered Portal's portalType.
      type: str
    settings:
      description: Self Registered Portal's settings.
      suboptions:
        aupSettings:
          description: Self Registered Portal's aupSettings.
          suboptions:
            displayFrequency:
              description: Self Registered Portal's displayFrequency.
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
          description: Self Registered Portal's authSuccessSettings.
          suboptions:
            redirectUrl:
              description: Self Registered Portal's redirectUrl.
              type: str
            successRedirect:
              description: Self Registered Portal's successRedirect.
              type: str
          type: dict
        guestChangePasswordSettings:
          description: Self Registered Portal's guestChangePasswordSettings.
          suboptions:
            allowChangePasswdAtFirstLogin:
              description: AllowChangePasswdAtFirstLogin flag.
              type: bool
          type: dict
        guestDeviceRegistrationSettings:
          description: Self Registered Portal's guestDeviceRegistrationSettings.
          suboptions:
            allowGuestsToRegisterDevices:
              description: AllowGuestsToRegisterDevices flag.
              type: bool
            autoRegisterGuestDevices:
              description: AutoRegisterGuestDevices flag.
              type: bool
          type: dict
        loginPageSettings:
          description: Self Registered Portal's loginPageSettings.
          suboptions:
            accessCode:
              description: Self Registered Portal's accessCode.
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
              description: Self Registered Portal's aupDisplay.
              type: str
            includeAup:
              description: IncludeAup flag.
              type: bool
            maxFailedAttemptsBeforeRateLimit:
              description: Self Registered Portal's maxFailedAttemptsBeforeRateLimit.
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
              description: Self Registered Portal's socialConfigs.
              type: list
            timeBetweenLoginsDuringRateLimit:
              description: Self Registered Portal's timeBetweenLoginsDuringRateLimit.
              type: int
          type: dict
        portalSettings:
          description: Self Registered Portal's portalSettings.
          suboptions:
            allowedInterfaces:
              description: Self Registered Portal's allowedInterfaces.
              elements: str
              type: list
            alwaysUsedLanguage:
              description: Self Registered Portal's alwaysUsedLanguage.
              type: str
            assignedGuestTypeForEmployee:
              description: Self Registered Portal's assignedGuestTypeForEmployee.
              type: str
            authenticationMethod:
              description: Self Registered Portal's authenticationMethod.
              type: str
            availableSsids:
              description: Self Registered Portal's availableSsids.
              type: list
            certificateGroupTag:
              description: Self Registered Portal's certificateGroupTag.
              type: str
            displayLang:
              description: Self Registered Portal's displayLang.
              type: str
            endpointIdentityGroup:
              description: Self Registered Portal's endpointIdentityGroup.
              type: str
            fallbackLanguage:
              description: Self Registered Portal's fallbackLanguage.
              type: str
            httpsPort:
              description: Self Registered Portal's httpsPort.
              type: int
          type: dict
        postLoginBannerSettings:
          description: Self Registered Portal's postLoginBannerSettings.
          suboptions:
            includePostAccessBanner:
              description: IncludePostAccessBanner flag.
              type: bool
          type: dict
        selfRegPageSettings:
          description: Self Registered Portal's selfRegPageSettings.
          suboptions:
            accountValidityDuration:
              description: Self Registered Portal's accountValidityDuration.
              type: int
            accountValidityTimeUnits:
              description: Self Registered Portal's accountValidityTimeUnits.
              type: str
            approveDenyLinksTimeUnits:
              description: Self Registered Portal's approveDenyLinksTimeUnits.
              type: str
            assignGuestsToGuestType:
              description: Self Registered Portal's assignGuestsToGuestType.
              type: str
            aupDisplay:
              description: Self Registered Portal's aupDisplay.
              type: str
            authenticateSponsorsUsingPortalList:
              description: AuthenticateSponsorsUsingPortalList flag.
              type: bool
            credentialNotificationUsingEmail:
              description: CredentialNotificationUsingEmail flag.
              type: bool
            credentialNotificationUsingSms:
              description: CredentialNotificationUsingSms flag.
              type: bool
            enableGuestEmailBlacklist:
              description: EnableGuestEmailBlacklist flag.
              type: bool
            enableGuestEmailWhitelist:
              description: EnableGuestEmailWhitelist flag.
              type: bool
            fieldCompany:
              description: Self Registered Portal's fieldCompany.
              suboptions:
                include:
                  description: Include flag.
                  type: bool
                require:
                  description: Require flag.
                  type: bool
              type: dict
            fieldEmailAddr:
              description: Self Registered Portal's fieldEmailAddr.
              suboptions:
                include:
                  description: Include flag.
                  type: bool
                require:
                  description: Require flag.
                  type: bool
              type: dict
            fieldFirstName:
              description: Self Registered Portal's fieldFirstName.
              suboptions:
                include:
                  description: Include flag.
                  type: bool
                require:
                  description: Require flag.
                  type: bool
              type: dict
            fieldLastName:
              description: Self Registered Portal's fieldLastName.
              suboptions:
                include:
                  description: Include flag.
                  type: bool
                require:
                  description: Require flag.
                  type: bool
              type: dict
            fieldLocation:
              description: Self Registered Portal's fieldLocation.
              suboptions:
                include:
                  description: Include flag.
                  type: bool
                require:
                  description: Require flag.
                  type: bool
              type: dict
            fieldPhoneNo:
              description: Self Registered Portal's fieldPhoneNo.
              suboptions:
                include:
                  description: Include flag.
                  type: bool
                require:
                  description: Require flag.
                  type: bool
              type: dict
            fieldReasonForVisit:
              description: Self Registered Portal's fieldReasonForVisit.
              suboptions:
                include:
                  description: Include flag.
                  type: bool
                require:
                  description: Require flag.
                  type: bool
              type: dict
            fieldSmsProvider:
              description: Self Registered Portal's fieldSmsProvider.
              suboptions:
                include:
                  description: Include flag.
                  type: bool
                require:
                  description: Require flag.
                  type: bool
              type: dict
            fieldUserName:
              description: Self Registered Portal's fieldUserName.
              suboptions:
                include:
                  description: Include flag.
                  type: bool
                require:
                  description: Require flag.
                  type: bool
              type: dict
            guestEmailBlacklistDomains:
              description: Self Registered Portal's guestEmailBlacklistDomains.
              elements: str
              type: list
            guestEmailWhitelistDomains:
              description: Self Registered Portal's guestEmailWhitelistDomains.
              elements: str
              type: list
            includeAup:
              description: IncludeAup flag.
              type: bool
            postRegistrationRedirect:
              description: Self Registered Portal's postRegistrationRedirect.
              type: str
            registrationCode:
              description: Self Registered Portal's registrationCode.
              type: str
            requireAupAcceptance:
              description: RequireAupAcceptance flag.
              type: bool
            requireGuestApproval:
              description: RequireGuestApproval flag.
              type: bool
            requireRegistrationCode:
              description: RequireRegistrationCode flag.
              type: bool
            selectableLocations:
              description: Self Registered Portal's selectableLocations.
              elements: str
              type: list
            selectableSmsProviders:
              description: Self Registered Portal's selectableSmsProviders.
              elements: str
              type: list
            sendApprovalRequestTo:
              description: Self Registered Portal's sendApprovalRequestTo.
              type: str
            sponsorPortalList:
              description: Self Registered Portal's sponsorPortalList.
              type: list
          type: dict
        selfRegSuccessSettings:
          description: Self Registered Portal's selfRegSuccessSettings.
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
            allowGuestSendSelfUsingSms:
              description: AllowGuestSendSelfUsingSms flag.
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
            includeSmsProvider:
              description: IncludeSmsProvider flag.
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
          description: Self Registered Portal's supportInfoSettings.
          suboptions:
            emptyFieldDisplay:
              description: Self Registered Portal's emptyFieldDisplay.
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
- module: cisco.ise.plugins.module_utils.definitions.self_registered_portal
# Reference by Internet resource
- name: Self Registered Portal reference
  description: Complete reference of the Self Registered Portal object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.self_registered_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present

- name: Update by id
  cisco.ise.self_registered_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: My SelfRegPortal
    id: 28771952-4a11-47da-8a12-e14569a0ac77
    name: My Self-Registered Guest Portal

- name: Delete by id
  cisco.ise.self_registered_portal:
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
    {
      "UpdatedFieldsList": {
        "updatedField": [
          "string"
        ]
      }
    }
"""
