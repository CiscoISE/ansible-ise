#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: self_registered_portal
short_description: Resource module for Self Registered Portal
description:
- Manage operations create, update and delete of the resource Self Registered Portal.
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
    customizations:
      globalCustomizations:
        bannerTitle: Guest Portal
        contactText: Contact Support
        footerElement: ''
      language:
        viewLanguage: English
      pageCustomizations:
        data:
        - key: ui_contact_ip_address_label
          value: SVAgQWRkcmVzczo=
        - key: ui_self_reg_results_sms_error
          value: U01TIHdhcyBub3Qgc2VudC4=
        - key: ui_self_reg_results_email_attempts_left_instruction_message
          value: RW1haWwgTWUgYXR0ZW1wdHMgbGVmdDo=
        - key: ui_error_content_label
          value: RXJyb3I=
        - key: ui_self_reg_registration_code_label
          value: UmVnaXN0cmF0aW9uIENvZGU=
        - key: ui_error_retry_button
          value: UmV0cnk=
        - key: ui_device_reg_skip_button
          value: Tm8sIHNraXAgcmVnaXN0cmF0aW9uLg==
        - key: ui_byod_install_ios_button
          value: TGF1bmNoIEFwcGxlIFByb2ZpbGUgYW5kIENlcnRpZmljYXRlIEluc3RhbGxlcnMgTm93
        - key: ui_byod_install_android_instruction_message
          value: VG8gY29uZmlndXJlIHlvdXIgZGV2aWNlIGZvciBzZWN1cmUgYWNjZXNzLCB5b3UgbmVlZCB0byBnbyB0byBHb29nbGUgUGxheSB...
        - key: ui_smtp_error
          value: WW91ciByZXF1ZXN0IGZvciBuZXR3b3JrIGFjY2VzcyBpcyBkZW5pZWQuIFBsZWFzZSBjb250YWN0IHlvdXIgaG9zdCBmb3IgbW9...
        - key: ui_self_reg_results_email_button
          value: RW1haWwgTWU=
        - key: ui_byod_reg_id_label
          value: RGV2aWNlIElEOg==
        - key: ui_success_optional_content_2
          value: ''
        - key: ui_success_optional_content_1
          value: ''
        - key: ui_client_provision_restricted_network_error
          value: WW91IGFyZSB1c2luZyByZXN0cmljdGVkIG5ldHdvcmsgYWNjZXNzIQ==
        - key: ui_post_access_optional_content_1
          value: ''
        - key: ui_post_access_optional_content_2
          value: ''
        - key: ui_contact_optional_content_1
          value: ''
        - key: ui_self_reg_email_deny
          value: RGVueQ==
        - key: ui_contact_optional_content_2
          value: ''
        - key: ui_byod_ios_provisioning_error
          value: RmFpbGVkIHRvIGNvbXBsZXRlIHByb3Zpc2lvbmluZyBvZiB5b3VyIGRldmljZS4gIFlvdSBjYW4gcnVuIHRoZSBwcm9jZXNzIGF...
        - key: ui_vlan_unsupported_error_message
          value: VG8gYWNjZXNzIHRoZSBuZXR3b3JrLCB5b3UgbXVzdCBtYW51YWxseSByZXNldCB0aGUgSVAgYWRkcmVzcyBvbiB5b3VyIGRldml...
        - key: ui_byod_reg_page_title
          value: RGV2aWNlIEluZm9ybWF0aW9u
        - key: ui_self_reg_results_password_label
          value: UGFzc3dvcmQ6
        - key: ui_login_sso_hyperlink_1
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_client_provision_instruction_message_temporal
          value: WW91ciBjb21wdXRlciByZXF1aXJlcyBzZWN1cml0eSBzb2Z0d2FyZSB0byBiZSBydW5uaW5nIGJlZm9yZSB5b3UgY2FuIGNvbm5...
        - key: ui_client_provision_agent_installation_message
          value: PG9sPiA8bGk+IDxzcGFuPiBZb3UgbXVzdCBpbnN0YWxsICR1aV9jbGllbnRfcHJvdmlzaW9uX2FnZW50X3R5cGUkIHRvIGNoZWN...
        - key: ui_login_sso_hyperlink_7
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_login_sso_hyperlink_6
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_login_sso_hyperlink_9
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_login_sso_hyperlink_8
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_login_aup_link
          value: UGxlYXNlIHJlYWQgdGhlIHRlcm1zIGFuZCBjb25kaXRpb25zLg==
        - key: ui_client_provision_agent_installed_instructions_without_java_message_temporal
          value: PG9sPiA8bGk+IDxzcGFuPiBTdGFydCAkdWlfY2xpZW50X3Byb3Zpc2lvbl9hZ2VudF90eXBlJCBzbyBpdCBjYW4gY2hlY2sgeW9...
        - key: ui_login_sso_hyperlink_3
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_login_sso_hyperlink_2
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_login_content_welcome_label
          value: V2VsY29tZQ==
        - key: ui_login_sso_hyperlink_5
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_login_sso_hyperlink_4
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_self_reg_content_label
          value: UmVnaXN0cmF0aW9u
        - key: ui_client_provision_page_title
          value: RGV2aWNlIFNlY3VyaXR5IENoZWNr
        - key: ui_client_provision_protected_mode_error
          value: VmVyaWZ5IHByb3RlY3RlZCBtb2RlIGlzIGVuYWJsZWQgZm9yIHRoaXMgc2VjdXJpdHkgem9uZS4gVG8gZW5hYmxlZCBpdCwgY2h...
        - key: ui_byod_welcome_os_selection_message
          value: U2VsZWN0IHlvdXIgRGV2aWNl
        - key: ui_invalid_password_policy_error
          value: SW52YWxpZCBQYXNzd29yZCBQb2xpY3ku
        - key: ui_grace_access_expire_page_instruction_message
          value: ''
        - key: ui_device_reg_delete_button
          value: RGVsZXRl
        - key: ui_self_reg_results_print_button
          value: UHJpbnQ=
        - key: ui_contact_sessioninfo_title
          value: U2Vzc2lvbiBJbmZvcm1hdGlvbg==
        - key: ui_login_sso_hyperlink_14
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_login_facebook_signon_button
          value: TG9nIGluIFdpdGggRmFjZWJvb2s=
        - key: ui_login_sso_hyperlink_13
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_byod_welcome_aup_agreement_label
          value: SSBhZ3JlZSB0byB0aGUgdGVybXMgYW5kIGNvbmRpdGlvbnM=
        - key: ui_login_sso_hyperlink_15
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_byod_reg_optional_content_1
          value: ''
        - key: ui_login_sso_hyperlink_10
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_client_provision_agent_installed_button_message_temporal
          value: KyBUaGlzIGlzIHdoYXQgdG8gZG8gbmV4dA==
        - key: ui_aup_accept_button
          value: QWNjZXB0
        - key: ui_client_provision_unsupported_browser_error
          value: VGhpcyBicm93c2VyIGlzIG5vdCBzdXBwb3J0ZWQuIENsb3NlIHRoaXMgd2luZG93LCBzd2l0Y2ggdG8gYSBzdXBwb3J0ZWQgd2V...
        - key: ui_login_sso_hyperlink_12
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_device_reg_register_label
          value: WWVzLCByZWdpc3RlciBkZXZpY2VzLg==
        - key: ui_login_sso_hyperlink_11
          value: QWx0ZXJuYXRpdmUgTG9naW4gUG9ydGFs
        - key: ui_invalid_email_error
          value: SW52YWxpZCBlbWFpbCBhZGRyZXNzIGZvcm1hdC4=
        - key: ui_self_reg_results_email_sms_limit_instruction_message
          value: WW91IGNhbiBvbmx5IGNsaWNrIHRoZSBidXR0b24gNSB0aW1lcy4=
        - key: ui_grace_access_expire_page_title
          value: V2UgYXJlIHNvcnJ5IHRoYXQgeW91IGFyZSBzdGlsbCB3YWl0aW5nIQ==
        - key: ui_client_provision_agent_status_message
          value: c3RhdHVz
        - key: ui_changepwd_values_match_error
          value: WW91IG11c3QgZW50ZXIgdGhlIHNhbWUgcGFzc3dvcmQgaW4gdGhlIE5ldyBQYXNzd29yZCBhbmQgQ29uZmlybSBQYXNzd29yZCB...
        - key: ui_confirm_popup_yes_button
          value: WWVz
        - key: ui_error_optional_content_2
          value: ''
        - key: ui_changepwd_confirmpwd_label
          value: Q29uZmlybSBwYXNzd29yZDo=
        - key: ui_error_optional_content_1
          value: ''
        - key: ui_byod_welcome_renew_cert_message
          value: WW91ciBkZXZpY2UgcmVnaXN0cmF0aW9uIG11c3QgYmUgcmVuZXdlZCB0byBjb250aW51ZSB1c2luZyB0aGUgc2VjdXJlIG5ldHd...
        - key: ui_login_page_title
          value: U2lnbiBPbg==
        - key: ui_client_provision_java_or_activex_not_present_error
          value: VG8gY29udGludWUsIGluc3RhbGwgYW5kIGVuYWJsZSB0aGUgbGF0ZXN0IEphdmEgdmVyc2lvbiwgYW5kIG1ha2Ugc3VyZSB0aGU...
        - key: ui_notification_success_message
          value: eW91ciBlbWFpbCBvciBTTVMgd2FzIHNlbnQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_client_provision_running_agent_message
          value: UnVubmluZyBDaXNjbyBBZ2VudC4uLnBsZWFzZSB3YWl0Lg==
        - key: ui_self_reg_aup_agreement_label
          value: SSBhZ3JlZSB0byB0aGUgdGVybXMgYW5kIGNvbmRpdGlvbnM=
        - key: ui_device_reg_optional_content_2
          value: ''
        - key: ui_changepwd_content_label
          value: Q2hhbmdlIFBhc3N3b3Jk
        - key: ui_step_viewer_registration_tab_label
          value: UmVnaXN0cmF0aW9u
        - key: ui_device_reg_optional_content_1
          value: ''
        - key: ui_footer_label
          value: ''
        - key: ui_client_provision_installation_timer_message_temporal
          value: WW91IGhhdmUgJHVpX2NsaWVudF9wcm92aXNpb25faW5zdGFsbF9hZ2VudF9taW5zJCBtaW51dGVzIHRvIHJ1biBhbmQgZm9yIHR...
        - key: ui_login_instruction_message
          value: U2lnbiBvbiBmb3IgZ3Vlc3QgYWNjZXNzLg==
        - key: ui_post_access_page_title
          value: UG9zdC1Mb2dpbiBCYW5uZXI=
        - key: ui_byod_success_optional_content_2
          value: ''
        - key: ui_byod_success_optional_content_1
          value: ''
        - key: ui_grace_access_success_page_instruction_message
          value: ''
        - key: ui_contact_page_title
          value: U3VwcG9ydCBJbmZvcm1hdGlvbg==
        - key: ui_byod_reg_content_message
          value: RW50ZXIgdGhlIERldmljZSBOYW1lIGFuZCBvcHRpb25hbCBkZXNjcmlwdGlvbiBmb3IgdGhpcyBkZXZpY2Ugc28geW91IGNhbiB...
        - key: ui_changepwd_values_unique_error
          value: WW91IGNhbm5vdCBlbnRlciB0aGUgc2FtZSBwYXNzd29yZCBpbiB0aGUgQ3VycmVudCBQYXNzd29yZCBhbmQgTmV3IFBhc3N3b3J...
        - key: ui_client_provision_agent_run_applet_error
          value: RXJyb3Igd2hlbiBydW5uaW5nIEphdmEgQXBwbGV0IGZvciBDaXNjbyBBZ2VudA==
        - key: ui_step_viewer_denied_tab_label
          value: RGVuaWVk
        - key: ui_byod_reg_continue_button
          value: Q29udGludWU=
        - key: ui_byod_success_instruction_message
          value: WW91IGNhbiBjbG9zZSB5b3VyIGJyb3dzZXIgbm93Lg==
        - key: ui_contact_instruction_message
          value: U2hhcmUgdGhlc2UgZGV0YWlscyB3aXRoIHRoZSBoZWxwIGRlc2sgd2hlbiB0cm91Ymxlc2hvb3RpbmcgaXNzdWVzIHdpdGggdGh...
        - key: ui_login_aup_agreement_label
          value: SSBhZ3JlZSB0byB0aGUgdGVybXMgYW5kIGNvbmRpdGlvbnM=
        - key: ui_session_timeout_error
          value: WW91ciBzZXNzaW9uIGhhcyB0aW1lZCBvdXQuIENsaWNrIFJldHJ5IHRvIHRyeSBhZ2Fpbi4=
        - key: ui_byod_success_unsupported_device_message
          value: WW91ciBkZXZpY2UgaXMgdW5zdXBwb3J0ZWQuICBIb3dldmVyLCB5b3UgYXJlIG5vdyBjb25uZWN0ZWQgdG8gdGhlIHNlY3VyZSB...
        - key: ui_self_reg_instruction_message
          value: UGxlYXNlIGNvbXBsZXRlIHRoaXMgcmVnaXN0cmF0aW9uIGZvcm06
        - key: ui_contact_helpdesk_text
          value: Q29udGFjdCB0aGUgaGVscCBkZXNrIGF0ICh4eHgpIHh4eC14eHh4Lg==
        - key: ui_login_change_password_button
          value: Q2hhbmdlIFBhc3N3b3Jk
        - key: ui_byod_reg_limit_message
          value: WW91IGhhdmUgcmVhY2hlZCB0aGUgbWF4aW11bSBudW1iZXIgb2YgZGV2aWNlcyBhbGxvd2VkIHRvIHJlZ2lzdGVyLiBTZWxlY3Q...
        - key: ui_grace_access_success_page_description_html
          value: WW91ciBhY2NvdW50IGlzIGFwcHJvdmVkIGFuZCB5b3UgbWF5IG5vdyBhY2Nlc3MgdGhlIGludGVybmV0Ljxici8+V2Ugc2VudCB...
        - key: ui_client_provision_posture_check_compliant_message
          value: WW91ciBkZXZpY2UgY29tcGxpZXMgd2l0aCB0aGUgbmV0d29yaydzIHNlY3VyaXR5IGd1aWRlbGluZXMsIGFuZCB5b3Ugc2hvdWx...
        - key: ui_login_content_label
          value: V2VsY29tZQ==
        - key: ui_client_provision_installation_timer_message
          value: WW91IGhhdmUgJHVpX2NsaWVudF9wcm92aXNpb25faW5zdGFsbF9hZ2VudF9taW5zJCBtaW51dGVzIHRvIGluc3RhbGwgYW5kIGZ...
        - key: ui_vlan_execute_message
          value: UmVsZWFzaW5nIGFuZCByZW5ld2luZyB5b3VyIElQIGFkZHJlc3Mu
        - key: ui_login_self_service_button
          value: T3IgcmVnaXN0ZXIgZm9yIGd1ZXN0IGFjY2Vzcw==
        - key: ui_username_mismatch_policy_error
          value: VXNlcm5hbWUgZGlkIG5vdCBtYXRjaCBVc2VybmFtZSBQb2xpY3ku
        - key: ui_aup_guest_text
          value: UGxlYXNlIGFjY2VwdCB0aGUgcG9saWN5OllvdSBhcmUgcmVzcG9uc2libGUgZm9yIG1haW50YWluaW5nIHRoZSBjb25maWRlbnR...
        - key: ui_byod_reg_optional_content_2
          value: ''
        - key: ui_vlan_execute_error_message
          value: VW5hYmxlIHRvIHJlbmV3IHRoZSBJUCBhZGRyZXNzLiBZb3UgbWlnaHQgbmVlZCB0byBkaXNhYmxlIG9yIHJlZHVjZSB0aGUgc2V...
        - key: ui_contact_link
          value: Q29udGFjdCBTdXBwb3J0
        - key: ui_aup_page_title
          value: QWNjZXB0YWJsZSBVc2UgUG9saWN5
        - key: ui_self_reg_results_social_login_approval
          value: V2hlbiBhY2Nlc3MgaGFzIGJlZW4gYXBwcm92ZWQgeW91IHdpbGwgcmVjZWl2ZSBhbiBlbWFpbCBvciB0ZXh0IG1lc3NhZ2Uu
        - key: ui_self_reg_results_optional_content_2
          value: ''
        - key: ui_device_reg_max_reached_message
          value: WW91IGhhdmUgcmVhY2hlZCB0aGUgbWF4aW11bSBhbW91bnQgb2YgZGV2aWNlcyB0aGF0IGNhbiBiZSByZWdpc3RlcmVkLiBJZiB...
        - key: ui_client_provision_agentless_page_button
          value: QWJvcnQ=
        - key: ui_self_reg_results_optional_content_1
          value: ''
        - key: ui_byod_install_android_after_install_message
          value: QWZ0ZXIgaW5zdGFsbGluZywgcnVuIHRoZSBTZXR1cCBBc3Npc3RhbnQgYW5kIHlvdSB3aWxsIGF1dG9tYXRpY2FsbHkgYmUgcmV...
        - key: ui_changepwd_policy_help_label
          value: UGFzc3dvcmRzIG11c3QgYmUgOCBjaGFyYWN0ZXJzIGFuZCBoYXZlIGEgbGV0dGVyIGFuZCBudW1iZXIu
        - key: ui_device_reg_manage_label
          value: TWFuYWdlIERldmljZXM=
        - key: ui_invalid_mac_format_error
          value: SW52YWxpZCBNQUMgYWRkcmVzcyBmb3JtYXQu
        - key: ui_client_provision_agent_aup_error
          value: WW91IG11c3QgYWNjZXB0IHRoZSBhZ3JlZW1lbnQgdG8gZ2V0IG5ldHdvcmsgYWNjZXNzIQ==
        - key: ui_client_provision_agent_installed_message
          value: Q2lzY28gQWdlbnQgd2FzIHN1Y2Nlc3NmdWxseSBpbnN0YWxsZWQh
        - key: ui_contact_user_agent_label
          value: VXNlciBBZ2VudDo=
        - key: ui_byod_success_content_label
          value: U3VjY2Vzcw==
        - key: ui_self_reg_results_phone_label
          value: TW9iaWxlIG51bWJlcjo=
        - key: ui_client_provision_agentless_content_label
          value: QWdlbnRsZXNzIFBvcnRhbA==
        - key: ui_aup_employee_text
          value: UGxlYXNlIGFjY2VwdCB0aGUgcG9saWN5OllvdSBhcmUgcmVzcG9uc2libGUgZm9yIG1haW50YWluaW5nIHRoZSBjb25maWRlbnR...
        - key: ui_aup_optional_content_2
          value: ''
        - key: ui_vlan_install_message
          value: WW91ciB3ZWIgYnJvd3NlciBpcyBhdHRlbXB0aW5nIHRvIGRvd25sb2FkIGFuIGFwcGxpY2F0aW9uLCB3aGljaCB3aWxsIGF1dG9...
        - key: ui_contact_mac_address_label
          value: TUFDIEFkZHJlc3M6
        - key: ui_aup_optional_content_1
          value: ''
        - key: ui_changepwd_page_title
          value: Q2hhbmdlIFBhc3N3b3Jk
        - key: ui_error_instruction_message
          value: ''
        - key: ui_client_provision_start_button
          value: U3RhcnQ=
        - key: ui_contact_title_label
          value: U3VwcG9ydCBJbmZvcm1hdGlvbg==
        - key: ui_contact_username_label
          value: VXNlcm5hbWU6
        - key: ui_client_provision_agent_run_error
          value: RXJyb3Igd2hlbiBydW5uaW5nIENpc2NvIEFnZW50
        - key: ui_client_provision_agent_download_error
          value: RmFpbGVkIHRvIGRvd25sb2FkIENpc2NvIEFnZW50
        - key: ui_self_reg_results_aup_text
          value: UGxlYXNlIGFjY2VwdCB0aGUgcG9saWN5OllvdSBhcmUgcmVzcG9uc2libGUgZm9yIG1haW50YWluaW5nIHRoZSBjb25maWRlbnR...
        - key: ui_max_devices_continue_button
          value: Q29udGludWU=
        - key: ui_client_provision_optional_content_1
          value: ''
        - key: ui_client_provision_downloading_agent_message
          value: RG93bmxvYWRpbmcgQ2lzY28gQWdlbnQuLi5wbGVhc2Ugd2FpdC4=
        - key: ui_changepwd_instruction_message
          value: WW91IGFyZSByZXF1aXJlZCB0byBjaGFuZ2UgeW91ciBwYXNzd29yZCBub3cuIFBsZWFzZSBlbnRlciBhIG5ldyBwYXNzd29yZC4=
        - key: ui_user_last_login_ipaddr_label
          value: RnJvbTo=
        - key: ui_client_provision_optional_content_2
          value: ''
        - key: ui_grace_access_waiting_page_optional_content_1
          value: ''
        - key: ui_grace_access_waiting_page_optional_content_2
          value: ''
        - key: ui_client_provision_cookies_not_present_error
          value: WW91IG5lZWQgdG8gZW5hYmxlIGJyb3dzZXIgY29va2llcyB0byB1c2UgdGhpcyBzaXRlLg==
        - key: ui_grace_access_success_page_timer
          value: WW91IHdpbGwgYmUgcmVkaXJlY3RlZCBpbg==
        - key: ui_byod_reg_next_button
          value: TmV4dA==
        - key: ui_client_provision_posture_agent_check_message
          value: RGV0ZWN0aW5nIGlmICR1aV9jbGllbnRfcHJvdmlzaW9uX2FnZW50X3R5cGUkIGlzIGluc3RhbGxlZCBhbmQgcnVubmluZy4uLg==
        - key: ui_grace_access_expire_page_optional_content_1
          value: ''
        - key: ui_invalid_first_name_error
          value: SW52YWxpZCBGaXJzdCBuYW1lLg==
        - key: ui_byod_install_winmac_instruction_message
          value: UGxlYXNlIHdhaXQgd2hpbGUgd2UgZG93bmxvYWQgdGhlIENpc2NvIE5ldHdvcmsgU2V0dXAgQXNzaXN0YW50LiBZb3Ugd2lsbCB...
        - key: ui_grace_access_expire_page_optional_content_2
          value: ''
        - key: ui_byod_install_ios_instruction_message
          value: VG8gY29uZmlndXJlIHlvdXIgZGV2aWNlLCBjbGljayB0aGUgPGI+TGF1bmNoIEFwcGxlIFByb2ZpbGUgYW5kIENlcnRpZmljYXR...
        - key: ui_self_reg_aup_link
          value: UGxlYXNlIHJlYWQgdGhlIHRlcm1zIGFuZCBjb25kaXRpb25z
        - key: ui_byod_welcome_optional_content_1
          value: ''
        - key: ui_device_reg_desc_label
          value: RGV2aWNlIERlc2NyaXB0aW9u
        - key: ui_login_username_label
          value: VXNlcm5hbWU6
        - key: ui_byod_welcome_optional_content_2
          value: ''
        - key: ui_aup_decline_error
          value: WW91IGNob3NlIHRvIHJlamVjdCB0aGUgQWNjZXB0YWJsZSBVc2UgUG9saWN5LiBXZSBjYW5ub3QgYWxsb3cgYWNjZXNzIHRvIHR...
        - key: ui_invalid_last_name_error
          value: SW52YWxpZCBMYXN0IG5hbWUu
        - key: ui_self_reg_results_auto_email_require_approval_error
          value: WW91ciByZXF1ZXN0IGZvciBuZXR3b3JrIGFjY2VzcyBpcyBkZW5pZWQuIFBsZWFzZSBjb250YWN0IHlvdXIgaG9zdCBmb3IgbW9...
        - key: ui_client_provision_os_not_supported_error
          value: VGhlIE9TIHlvdSBhcmUgdXNpbmcgaXMgbm90IHN1cHBvcnRlZC4=
        - key: ui_self_reg_results_location_label
          value: TG9jYXRpb246
        - key: ui_vlan_optional_content_2
          value: ''
        - key: ui_vlan_optional_content_1
          value: ''
        - key: ui_aup_agreement_label
          value: SSBhZ3JlZSB0byB0aGUgdGVybXMgYW5kIGNvbmRpdGlvbnMu
        - key: ui_grace_access_success_page_optional_content_2
          value: ''
        - key: ui_self_reg_results_page_title
          value: QWNjb3VudCBDcmVhdGVk
        - key: ui_byod_welcome_guest_access_button
          value: SSB3YW50IGd1ZXN0IGFjY2VzcyBvbmx5
        - key: ui_self_reg_results_username_label
          value: VXNlcm5hbWU6
        - key: ui_invalid_username_policy_error
          value: SW52YWxpZCBVc2VybmFtZSBQb2xpY3ku
        - key: ui_grace_access_success_page_optional_content_1
          value: ''
        - key: ui_client_provision_try_install_message
          value: VHJ5aW5nIHRvIGluc3RhbGw=
        - key: ui_field_required_error
          value: VGhpcyBmaWVsZCBpcyByZXF1aXJlZC4=
        - key: ui_client_provision_install_button
          value: SW5zdGFsbCBhZ2VudA==
        - key: ui_grace_access_waiting_page_description_html
          value: V2hpbGUgeW91IGFyZSB3YWl0aW5nIGZvciB5b3VyIGFjY291bnQsIHlvdSBoYXZlIHRlbXBvcmFyeSBhY2Nlc3MgdG8gdGhlIGl...
        - key: ui_self_reg_email_approve
          value: QXBwcm92ZQ==
        - key: ui_grace_access_waiting_page_timer
          value: VGVtcG9yYXJ5IGFjY2VzcyBleHBpcmVzIGlu
        - key: ui_self_reg_results_email_success
          value: RW1haWwgd2FzIHNlbnQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_self_reg_results_aup_agreement_label
          value: SSBhZ3JlZSB0byB0aGUgdGVybXMgYW5kIGNvbmRpdGlvbnM=
        - key: ui_byod_success_message
          value: RmluaXNoZWQgaW5zdGFsbGluZyBhbmQgY29uZmlndXJpbmcgeW91ciBkZXZpY2UuICBZb3UgYXJlIG5vdyBjb25uZWN0ZWQgdG8...
        - key: ui_grace_access_deny_page_instruction_message
          value: ''
        - key: ui_self_reg_results_continue_button
          value: U2lnbiBPbg==
        - key: ui_aup_instruction_message
          value: UGxlYXNlIHJlYWQgdGhlIEFjY2VwdGFibGUgVXNlIFBvbGljeQ==
        - key: ui_byod_welcome_content_label
          value: QllPRCBXZWxjb21l
        - key: ui_invalid_username_error
          value: SW52YWxpZCB1c2VybmFtZS4=
        - key: ui_self_reg_results_access_code_label
          value: QWNjZXNzIGNvZGU6
        - key: ui_device_reg_delete_confirmation_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGRlbGV0ZSB5b3VyIGRldmljZT8=
        - key: ui_lastname_mismatch_policy_error
          value: TGFzdE5hbWUgZGlkIG5vdCBtYXRjaCBVc2VybmFtZSBQb2xpY3k=
        - key: ui_changepwd_policy_error_message
          value: WW91ciBwYXNzd29yZCBkb2VzIG5vdCBtZWV0IHRoZSBwYXNzd29yZCBwb2xpY3kgcmVxdWlyZW1lbnRzLiBQbGVhc2UgY29udGF...
        - key: ui_max_devices_message
          value: WW91IGhhdmUgYWRkZWQgdGhlIG1heGltdW0gbnVtYmVyIG9mIHN1cHBvcnRlZCBkZXZpY2VzLiBUaGUgZmlyc3QgZGV2aWNlIHl...
        - key: ui_byod_welcome_aup_text
          value: UGxlYXNlIGFjY2VwdCB0aGUgcG9saWN5OllvdSBhcmUgcmVzcG9uc2libGUgZm9yIG1haW50YWluaW5nIHRoZSBjb25maWRlbnR...
        - key: ui_byod_install_winmac_button
          value: RG93bmxvYWQgYW5kIEluc3RhbGwu
        - key: ui_client_provision_agent_installation_message_temporal
          value: PG9sPiA8bGk+IDxzcGFuPiA8YSBocmVmPSIkdWlfY2xpZW50X3Byb3Zpc2lvbl9hZ2VudF91cmwkIiB0YXJnZXQ9Il9ibGFuayI...
        - key: ui_invalid_date_dmy_error
          value: SW52YWxpZCBkYXRlIGZvcm1hdCBkZC9tbS95eS4=
        - key: ui_byod_reg_install_button
          value: RG93bmxvYWQgYW5kIEluc3RhbGw=
        - key: ui_grace_access_expire_page_description_html
          value: WW91ciByZXF1ZXN0IGZvciBuZXR3b3JrIGFjY2VzcyBoYXMgZXhwaXJlZC4gUGxlYXNlIGNoZWNrIGlmIHlvdXIgaG9zdCBoYXM...
        - key: ui_back_to_login_page_button
          value: QmFjayB0byBMb2cgSW4=
        - key: ui_device_reg_content_label
          value: RGV2aWNlIFJlZ2lzdHJhdGlvbg==
        - key: ui_byod_install_page_title
          value: SW5zdGFsbA==
        - key: ui_success_message
          value: WW91IG5vdyBoYXZlIEludGVybmV0IGFjY2VzcyB0aHJvdWdoIHRoaXMgbmV0d29yay4=
        - key: ui_client_provision_no_policy_error
          value: SVNFIGlzIG5vdCBhYmxlIHRvIGFwcGx5IGFuIGFjY2VzcyBwb2xpY3kgdG8geW91ciBsb2ctaW4gc2Vzc2lvbiBhdCB0aGlzIHR...
        - key: ui_client_provision_generic_system_error
          value: QSBzeXN0ZW0gZXJyb3Igb2NjdXJyZWQsIHBsZWFzZSBjb250YWN0IHlvdXIgbmV0d29yayBhZG1pbmlzdHJhdG9yLg==
        - key: ui_changepwd_submit_button
          value: U3VibWl0
        - key: ui_user_last_login_pass_time_label
          value: TGFzdCBMb2dpbjo=
        - key: ui_post_access_content_label
          value: V2VsY29tZSBNZXNzYWdl
        - key: ui_byod_success_redirecting_message
          value: UmVjb25uZWN0aW5nIGFuZCByZWRpcmVjdGluZy4uLg==
        - key: ui_client_provision_agent_not_installed_button_message
          value: KyBUaGlzIGlzIG15IGZpcnN0IHRpbWUgaGVyZQ==
        - key: ui_login_forgot_password_button
          value: UmVzZXQgUGFzc3dvcmQ=
        - key: ui_grace_access_deny_page_title
          value: WW91ciByZXF1ZXN0IGlzIGRlbmllZA==
        - key: ui_login_signon_button
          value: U2lnbiBPbg==
        - key: ui_client_provision_content_label
          value: RGV2aWNlIFNlY3VyaXR5IENoZWNr
        - key: ui_byod_reg_instruction_message
          value: ''
        - key: ui_success_returning_message
          value: ''
        - key: ui_byod_success_manual_reconnect_message
          value: SW5zdGFsbGF0aW9uIGFuZCBDb25maWd1cmF0aW9uIG9mIHlvdXIgZGV2aWNlIGlzIG5vdyBmaW5pc2hlZC4gIFlvdSBtdXN0IG5...
        - key: ui_error_page_title
          value: RXJyb3I=
        - key: ui_invalid_phone_error
          value: SW52YWxpZCBtb2JpbGUgbnVtYmVyIGZvcm1hdC4=
        - key: ui_client_provision_cp_disabled_error
          value: Q2xpZW50IHByb3Zpc2lvbmluZyBpcyBkaXNhYmxlZC4=
        - key: ui_vlan_instruction_message
          value: ''
        - key: ui_self_reg_results_email_error
          value: RW1haWwgd2FzIG5vdCBzZW50Lg==
        - key: ui_byod_install_android_button
          value: R2V0IENpc2NvIE5ldHdvcmsgU2V0dXAgQXNzaXN0YW50IE5vdw==
        - key: ui_contact_sessioninfo_text
          value: VGhpcyBpbmZvcm1hdGlvbiBwcm92aWRlcyBkZXRhaWxzIHRoYXQgdGhlIGhlbHAgZGVzayBtaWdodCBuZWVkIHRvIHJlc29sdmU...
        - key: ui_contact_content_label
          value: Q29udGVudA==
        - key: ui_device_reg_already_registered_message
          value: VGhlIGRldmljZSBoYXMgYWxyZWFkeSBiZWVuIHJlZ2lzdGVyZWQu
        - key: ui_byod_success_page_title
          value: U3VjY2Vzcw==
        - key: ui_self_reg_submit_button
          value: UmVnaXN0ZXI=
        - key: ui_login_failed_error
          value: QXV0aGVudGljYXRpb24gZmFpbGVkLg==
        - key: ui_byod_install_content_label
          value: SW5zdGFsbA==
        - key: ui_self_reg_results_reason_visit_label
          value: UmVhc29uIGJlaW5nIHZpc2l0ZWQ6
        - key: ui_device_reg_add_button
          value: QWRk
        - key: ui_portal_internal_error
          value: QW4gdW5leHBlY3RlZCBlcnJvciBvY2N1cnJlZC4gUGxlYXNlIGNvbnRhY3QgdGhlIGhlbHAgZGVzayBmb3IgYXNzaXN0YW5jZS4=
        - key: ui_byod_reg_delete_confirmation_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGRlbGV0ZSB0aGlzIGRldmljZT8gIFlvdSB3b24ndCBiZSBhYmxlIHRvIHVzZSBpdCB...
        - key: ui_vlan_install_error_message
          value: SW5zdGFsbGF0aW9uIG9mIHRoZSBhcHBsaWNhdGlvbiBmYWlsZWQuIEZvbGxvdyB0aGUgaW5zdHJ1Y3Rpb25zIGJlbG93IHRvIGN...
        - key: ui_byod_welcome_page_title
          value: QllPRCBXZWxjb21l
        - key: ui_login_alternative_login_msg
          value: WW91IGNhbiBhbHNvIGxvZ2luIHdpdGg=
        - key: ui_grace_access_deny_page_description_html
          value: WW91ciByZXF1ZXN0IGZvciBuZXR3b3JrIGFjY2VzcyBpcyBkZW5pZWQuIFBsZWFzZSBjb250YWN0IHlvdXIgaG9zdCBmb3IgbW9...
        - key: ui_client_provision_posture_check_non_compliant_message
          value: WW91ciBkZXZpY2UgZG9lcyBub3QgY29tcGx5IHdpdGggdGhlIG5ldHdvcmsncyBzZWN1cml0eSBndWlkZWxpbmVzLCBhbmQgaGF...
        - key: ui_byod_install_optional_content_2
          value: ''
        - key: ui_changepwd_cancel_button
          value: U2tpcA==
        - key: ui_byod_reg_desc_label
          value: RGVzY3JpcHRpb246
        - key: ui_byod_install_optional_content_1
          value: ''
        - key: ui_post_access_instruction_message
          value: Q2xpY2sgPGI+Q29udGludWU8L2I+IHRvIGNvbm5lY3QgdG8gdGhlIG5ldHdvcmsu
        - key: ui_client_provision_login_fail_error
          value: WW91ciBsb2dpbiBzZXNzaW9uIGZhaWxlZCE=
        - key: ui_changepwd_currentpwd_label
          value: Q3VycmVudCBwYXNzd29yZDo=
        - key: ui_aup_content_label
          value: QWNjZXB0YWJsZSBVc2UgUG9saWN5
        - key: ui_max_devices_content_label
          value: TWF4aW11bSBEZXZpY2VzIFJlYWNoZWQ=
        - key: ui_byod_install_ios_after_install_message
          value: QWZ0ZXIgY29uZmlndXJhdGlvbiBvZiB5b3VyIGRldmljZSwgeW91IHdpbGwgYmUgYWJsZSB0byBjb25uZWN0IHRvIHRoZSBuZXR...
        - key: ui_grace_access_deny_page_optional_content_1
          value: ''
        - key: ui_login_passcode_label
          value: UGFzc2NvZGU6
        - key: ui_self_reg_results_email_label
          value: RW1haWw6
        - key: ui_grace_access_deny_page_optional_content_2
          value: ''
        - key: ui_empty_phone_error
          value: TW9iaWxlIG51bWJlciBpcyByZXF1aXJlZC4=
        - key: ui_login_aup_text
          value: UGxlYXNlIGFjY2VwdCB0aGUgcG9saWN5OiBZb3UgYXJlIHJlc3BvbnNpYmxlIGZvciBtYWludGFpbmluZyB0aGUgY29uZmlkZW5...
        - key: ui_changepwd_optional_content_2
          value: ''
        - key: ui_self_reg_page_title
          value: U2VsZiBSZWdpc3RyYXRpb24=
        - key: ui_changepwd_optional_content_1
          value: ''
        - key: ui_client_provision_login_timeout_error
          value: WW91ciBsb2dpbiBzZXNzaW9uIHRpbWVkIG91dCE=
        - key: ui_vlan_page_title
          value: Q29ubmVjdGluZyB0byBOZXR3b3Jr
        - key: ui_byod_welcome_renew_button
          value: UmVuZXc=
        - key: ui_vlan_coa_error_message
          value: VW5hYmxlIHRvIGNvbW11bmljYXRlIHdpdGggc2VydmVyIHRvIHBlcmZvcm0gQ29BLiBDb250YWN0IHlvdXIgc3lzdGVtIGFkbWl...
        - key: ui_self_reg_results_sms_provider_label
          value: U01TIHByb3ZpZGVyOg==
        - key: ui_client_provision_refresh_ipaddress_error
          value: WW91IG5lZWQgdG8gcmVmcmVzaCBJUCBhZGRyZXNzIG1hbnVhbGx5IHRvIGdldCBuZXR3b3JrIGFjY2VzcyE=
        - key: ui_self_reg_optional_content_2
          value: ''
        - key: ui_byod_install_instruction_message
          value: ''
        - key: ui_self_reg_results_sms_attempts_left_instruction_message
          value: VGV4dCBNZSBhdHRlbXB0cyBsZWZ0Og==
        - key: ui_self_reg_results_sms_button
          value: VGV4dCBNZQ==
        - key: ui_self_reg_results_person_visited_label
          value: UGVyc29uIGJlaW5nIHZpc2l0ZWQgKGVtYWlsKTo=
        - key: ui_device_reg_instruction_message
          value: RG8geW91IHdhbnQgdG8gcmVnaXN0ZXIgYW55IGRldmljZXMgYXQgdGhpcyB0aW1lPyBUaGlzIGlzIHVzZWZ1bCBmb3IgcmVnaXN...
        - key: ui_contact_failure_code_label
          value: RmFpbHVyZSBDb2RlOg==
        - key: ui_success_instruction_message
          value: ''
        - key: ui_client_provision_agent_installed_instructions_without_java_message
          value: PG9sPiA8bGk+IDxzcGFuPiBJZiAkdWlfY2xpZW50X3Byb3Zpc2lvbl9hZ2VudF90eXBlJCBpcyBhbHJlYWR5IGluc3RhbGxlZCw...
        - key: ui_self_reg_optional_content_1
          value: ''
        - key: ui_byod_welcome_config_device_message
          value: QWNjZXNzIHRvIHRoaXMgbmV0d29yayByZXF1aXJlcyB5b3VyIGRldmljZSB0byBiZSBjb25maWd1cmVkIGZvciBlbmhhbmNlZCB...
        - key: ui_self_reg_aup_text
          value: UGxlYXNlIGFjY2VwdCB0aGUgcG9saWN5OllvdSBhcmUgcmVzcG9uc2libGUgZm9yIG1haW50YWluaW5nIHRoZSBjb25maWRlbnR...
        - key: ui_changepwd_newpwd_label
          value: TmV3IHBhc3N3b3JkOg==
        - key: ui_vlan_content_label
          value: Q29ubmVjdGluZyB0byBOZXR3b3Jr
        - key: ui_self_reg_cancel_button
          value: Q2FuY2Vs
        - key: ui_device_reg_cancel_button
          value: Q2FuY2VsLCBDb250aW51ZQ==
        - key: ui_client_provision_agent_installation_cancel_error
          value: Q2lzY28gTkFDIEFnZW50IGluc3RhbGxhdGlvbiB3YXMgY2FuY2VsbGVkLiBUbyB0cnkgYWdhaW4sIG9wZW4gYSBuZXcgYnJvd3N...
        - key: ui_self_reg_results_last_name_label
          value: TGFzdCBuYW1lOg==
        - key: ui_device_reg_page_title
          value: RGV2aWNlIFJlZ2lzdHJhdGlvbg==
        - key: ui_client_provision_agent_installation_instructions_with_no_java_message
          value: VG8gY29udGludWUsIGluc3RhbGwgYW5kIGVuYWJsZSB0aGUgbGF0ZXN0IEphdmEgdmVyc2lvbiwgYW5kIG1ha2Ugc3VyZSB0aGU...
        - key: ui_client_provision_posture_agent_scan_message
          value: U2Nhbm5pbmcgeW91ciBkZXZpY2UuIE9wZW4gJHVpX2NsaWVudF9wcm92aXNpb25fYWdlbnRfdHlwZSQgdG8gY2hlY2sgdGhlIGN...
        - key: ui_self_reg_results_content_label
          value: QWNjb3VudCBDcmVhdGVk
        - key: ui_auto_device_reg_content_label
          value: QXV0b21hdGljIEd1ZXN0IERldmljZSBSZWdpc3RyYXRpb24=
        - key: ui_step_viewer_approval_tab_label
          value: QXBwcm92YWw=
        - key: ui_self_reg_results_first_name_label
          value: Rmlyc3QgbmFtZTo=
        - key: ui_success_content_label
          value: U3VjY2Vzcw==
        - key: ui_login_or_for_buttons
          value: T1I=
        - key: ui_client_provision_unable_to_detect_message
          value: VW5hYmxlIHRvIGRldGVjdCAkdWlfY2xpZW50X3Byb3Zpc2lvbl9hZ2VudF90eXBlJCBQb3N0dXJlIEFnZW50
        - key: ui_client_provision_login_fail_hint_message
          value: WW91IHdpbGwgaGF2ZSBsaW1pdGVkIG5ldHdvcmsgY29ubmVjdGl2aXR5LiBQbGVhc2UgdHJ5IGRpc2Nvbm5lY3RpbmcgYW5kIHJ...
        - key: ui_byod_reg_confirmation_yes_button
          value: WWVz
        - key: ui_vlan_java_disabled_error_message
          value: VG8gY29udGludWUsIGluc3RhbGwgYW5kIGVuYWJsZSB0aGUgbGF0ZXN0IEphdmEgdmVyc2lvbiwgYW5kIG1ha2Ugc3VyZSB0aGU...
        - key: ui_step_viewer_waiting_tab_label
          value: V2FpdGluZyBmb3IgYXBwcm92YWw=
        - key: ui_byod_reg_name_label
          value: RGV2aWNlIE5hbWU6
        - key: ui_self_reg_results_instruction_message
          value: Q2hvb3NlIGhvdyB0byByZWNlaXZlIHlvdXIgbG9naW4gaW5mb3JtYXRpb24sIGJ5IHRleHQgb3IgZW1haWwu
        - key: ui_post_access_continue_button
          value: Q29udGludWU=
        - key: ui_javascript_disabled_message
          value: WW91IG11c3QgdHVybiBvbiBKYXZhU2NyaXB0IHRvIHVzZSB0aGlzIHdlYiBzaXRlLg==
        - key: ui_client_provision_posture_agent_message
          value: UG9zdHVyZSBBZ2VudC4=
        - key: ui_max_devices_page_title
          value: QXV0b21hdGljIEd1ZXN0IERldmljZSBSZWdpc3RyYXRpb24=
        - key: ui_byod_welcome_instruction_message
          value: V2VsY29tZSB0byB0aGUgQllPRCBwb3J0YWwu
        - key: ui_contact_policy_server_label
          value: UG9saWN5IFNlcnZlcjo=
        - key: ui_max_devices_optional_content_2
          value: ''
        - key: ui_max_devices_optional_content_1
          value: ''
        - key: ui_login_notification_instruction_message
          value: QW4gZW1haWwgb3IgYW4gU01TIG1lc3NhZ2UgaGFzIGJlZW4gc2VudCB0byB5b3UgY29udGFpbmluZyB5b3VyIHNpZ24gb24gY3J...
        - key: ui_grace_access_waiting_page_instruction_message
          value: ''
        - key: ui_byod_time_skew_error
          value: VGltZSBza2V3IGV4aXN0cyBiZXR3ZWVuIHlvdXIgZGV2aWNlIGFuZCBJU0UuICBQbGVhc2UgY29ycmVjdCB5b3VyIGRldmljZSd...
        - key: ui_grace_access_waiting_page_title
          value: ''
        - key: ui_confirm_popup_no_button
          value: Tm8=
        - key: ui_success_page_title
          value: U3VjY2Vzcw==
        - key: ui_invalid_date_mdy_error
          value: SW52YWxpZCBkYXRlIGZvcm1hdCBtbS9kZC95eS4=
        - key: ui_byod_reg_confirmation_no_button
          value: Tm8=
        - key: ui_contact_helpdesk_title
          value: U3VwcG9ydCBJbmZvcm1hdGlvbg==
        - key: ui_byod_welcome_start_button
          value: U3RhcnQ=
        - key: ui_login_optional_content_1
          value: ''
        - key: ui_login_optional_content_2
          value: ''
        - key: ui_byod_welcome_os_detection_confirmation_message
          value: V2FzIHlvdXIgZGV2aWNlIGRldGVjdGVkIGluY29ycmVjdGx5Pw==
        - key: ui_aup_decline_button
          value: RGVjbGluZQ==
        - key: ui_changepwd_username_label
          value: VXNlcm5hbWU6
        - key: ui_max_devices_instruction_message
          value: ''
        - key: ui_device_reg_id_label
          value: RGV2aWNlIElE
        - key: ui_client_provision_another_login_running_error
          value: WW91IGhhdmUgYW5vdGhlciBsb2dpbiBzZXNzaW9uIHJ1bm5pbmch
        - key: ui_client_provision_agent_installed_button_message
          value: KyBSZW1pbmQgbWUgd2hhdCB0byBkbyBuZXh0
        - key: ui_byod_welcome_os_detected_message
          value: VGhlIGZvbGxvd2luZyBzeXN0ZW0gd2FzIGRldGVjdGVk
        - key: ui_session_timeout_retry_button
          value: UmV0cnk=
        - key: ui_post_access_message
          value: WW91J3JlIHZlcnkgY2xvc2UgdG8gZ2FpbmluZyBuZXR3b3JrIGFjY2Vzcy4=
        - key: ui_client_provision_agent_non_compliant_message
          value: WW91ciBzeXN0ZW0gaXMgbm90IGNvbXBsaWFudCBhbmQgd2lsbCBoYXZlIGxpbWl0ZWQgbmV0d29yayBjb25uZWN0aXZpdHkuIFB...
        - key: ui_step_viewer_expired_tab_label
          value: RXhwaXJlZA==
        - key: ui_self_reg_results_company_label
          value: Q29tcGFueTo=
        - key: ui_client_provision_instruction_message
          value: WW91ciBjb21wdXRlciByZXF1aXJlcyBzZWN1cml0eSBzb2Z0d2FyZSB0byBiZSBpbnN0YWxsZWQgYmVmb3JlIHlvdSBjYW4gY29...
        - key: ui_self_reg_results_aup_link
          value: VGVybXMgYW5kIENvbmRpdGlvbnM=
        - key: ui_contact_message
          value: U3VwcG9ydCBJbmZvcm1hdGlvbg==
        - key: ui_login_password_label
          value: UGFzc3dvcmQ6
        - key: ui_device_reg_register_message
          value: WW91IGNhbiBhZGQgYSBtYXhpbXVtIG9mICR1aV9tYXhfcmVnX2RldmljZXMkIGRldmljZXMuIEVudGVyIGEgZGV2aWNlIElEIGF...
        - key: ui_client_provision_agentless_instruction_message
          value: WW91ciBjb21wdXRlciBpcyBkb2luZyBzZWN1cml0eSBjaGVjayBiZWZvcmUgeW91IGNhbiBjb25uZWN0IHRvIHRoZSBuZXR3b3J...
        - key: ui_client_provision_agent_check_complete_message
          value: Q2lzY28gQWdlbnQgZmluaXNoZWQgY2hlY2tpbmcgeW91ciBzeXN0ZW0u
        - key: ui_self_reg_results_sms_success
          value: U01TIHdhcyBzZW50IHN1Y2Nlc3NmdWxseS4=
        - key: ui_byod_reg_content_label
          value: RGV2aWNlIEluZm9ybWF0aW9u
        - key: ui_device_reg_save_button
          value: U2F2ZSwgQ29udGludWU=
        - key: ui_byod_reg_delete_button
          value: RGVsZXRl
        - key: ui_banner_label
          value: R3Vlc3QgUG9ydGFs
        - key: ui_byod_welcome_aup_link
          value: UGxlYXNlIHJlYWQgdGhlIHRlcm1zIGFuZCBjb25kaXRpb25zLg==
        - key: ui_firstname_mismatch_policy_error
          value: Rmlyc3ROYW1lIGRpZCBub3QgbWF0Y2ggVXNlcm5hbWUgUG9saWN5
        - key: ui_grace_access_success_page_title
          value: U3VjY2Vzc2Z1bCE=
      portalTheme:
        id: 9eb421c0-8c01-11e6-996c-525400b48521
        name: Default Blue theme
      portalTweakSettings: {}
    description: My description
    name: My Self-Registered Guest Portal
    portalType: SELFREGGUEST
    settings:
      aupSettings:
        displayFrequency: FIRSTLOGIN
        includeAup: true
        requireScrolling: false
      authSuccessSettings:
        successRedirect: AUTHSUCCESSPAGE
      byodSettings:
        byodRegistrationSettings:
          endPointIdentityGroupId: aa13bb40-8bff-11e6-996c-525400b48521
          showDeviceID: false
        byodRegistrationSuccessSettings:
          successRedirect: AUTHSUCCESSPAGE
        byodWelcomeSettings:
          aupDisplay: ONPAGE
          enableBYOD: false
          enableGuestAccess: false
          includeAup: false
          requireAupAcceptance: false
          requireMDM: false
          requireScrolling: false
      guestChangePasswordSettings:
        allowChangePasswdAtFirstLogin: true
      guestDeviceRegistrationSettings:
        allowGuestsToRegisterDevices: false
        autoRegisterGuestDevices: true
      loginPageSettings:
        allowAlternateGuestPortal: false
        allowForgotPassword: true
        allowGuestToChangePassword: false
        allowGuestToCreateAccounts: true
        includeAup: false
        maxFailedAttemptsBeforeRateLimit: 5
        requireAccessCode: false
        socialConfigs:
        - socialMediaType: ''
          socialMediaValue: ''
        timeBetweenLoginsDuringRateLimit: 2
      portalSettings:
        allowedInterfaces:
        - eth0
        - bond0
        alwaysUsedLanguage: English
        assignedGuestTypeForEmployee: Contractor (default)
        authenticationMethod: 92e50f80-8c01-11e6-996c-525400b48521
        certificateGroupTag: Default Portal Certificate Group
        displayLang: USEBROWSERLOCALE
        fallbackLanguage: English
        httpsPort: 8443
      postLoginBannerSettings:
        includePostAccessBanner: true
      selfRegPageSettings:
        accountValidityDuration: 1
        allowGraceAccess: false
        approveDenyLinksTimeUnits: DAYS
        assignGuestsToGuestType: Daily (default)
        authenticateSponsorsUsingPortalList: false
        autoLoginSelfWait: false
        autoLoginTimePeriod: 5
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
        fieldPersonBeingVisited:
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
        guestEmailBlacklistDomains: []
        guestEmailWhitelistDomains: []
        includeAup: false
        postRegistrationRedirect: SELFREGISTRATIONSUCCESS
        requireAupAcceptance: false
        requireGuestApproval: false
        requireRegistrationCode: false
        selectableLocations:
        - San Jose
        selectableSmsProviders:
        - Global Default
        sponsorPortalList: []
      selfRegSuccessSettings:
        allowGuestLoginFromSelfregSuccessPage: false
        allowGuestSendSelfUsingEmail: false
        allowGuestSendSelfUsingPrint: false
        allowGuestSendSelfUsingSms: false
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
