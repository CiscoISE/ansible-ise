#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: hotspot_portal
short_description: Resource module for Hotspot Portal
description:
- Manage operations create, update, delete of the resource Hotspot Portal.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    customizations:
      suboptions:
        globalCustomizations:
          suboptions:
            bannerTitle:
              description: Hotspot Portal's bannerTitle.
              type: str
            contactText:
              description: Hotspot Portal's contactText.
              type: str
            footerElement:
              description: Hotspot Portal's footerElement.
              type: str
          type: dict
        language:
          suboptions:
            viewLanguage:
              description: Hotspot Portal's viewLanguage.
              type: str
          type: dict
        pageCustomizations:
          suboptions:
            data:
              description: Hotspot Portal's data.
              suboptions:
              - suboptions:
                  key:
                    description: Hotspot Portal's key.
                    type: str
                  value:
                    description: Hotspot Portal's value.
                    type: str
                type: dict
              type: list
          type: dict
        portalTheme:
          suboptions:
            id:
              description: Hotspot Portal's id.
              type: str
            name:
              description: Hotspot Portal's name.
              type: str
          type: dict
      type: dict
    description:
      description: Hotspot Portal's description.
      type: str
    id:
      description: Hotspot Portal's id.
      type: str
    name:
      description: Hotspot Portal's name.
      type: str
    portalType:
      description: Hotspot Portal's portalType.
      type: str
    settings:
      suboptions:
        aupSettings:
          suboptions:
            includeAup:
              description: IncludeAup flag.
              type: bool
            requireScrolling:
              description: RequireScrolling flag.
              type: bool
          type: dict
        authSuccessSettings:
          suboptions:
            successRedirect:
              description: Hotspot Portal's successRedirect.
              type: str
          type: dict
        portalSettings:
          suboptions:
            allowedInterfaces:
              description: Hotspot Portal's allowedInterfaces.
              elements:
                type: str
              type: list
            alwaysUsedLanguage:
              description: Hotspot Portal's alwaysUsedLanguage.
              type: str
            certificateGroupTag:
              description: Hotspot Portal's certificateGroupTag.
              type: str
            coaType:
              description: Hotspot Portal's coaType.
              type: str
            displayLang:
              description: Hotspot Portal's displayLang.
              type: str
            endpointIdentityGroup:
              description: Hotspot Portal's endpointIdentityGroup.
              type: str
            fallbackLanguage:
              description: Hotspot Portal's fallbackLanguage.
              type: str
            httpsPort:
              description: Hotspot Portal's httpsPort.
              type: int
          type: dict
        postAccessBannerSettings:
          suboptions:
            includePostAccessBanner:
              description: IncludePostAccessBanner flag.
              type: bool
          type: dict
        supportInfoSettings:
          suboptions:
            emptyFieldDisplay:
              description: Hotspot Portal's emptyFieldDisplay.
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
- module: cisco.ise.plugins.module_utils.definitions.hotspot_portal
# Reference by Internet resource
- name: Hotspot Portal reference
  description: Complete reference of the Hotspot Portal object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.hotspot_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customizations:
      globalCustomizations:
        bannerTitle: Hotspot Portal
        contactText: Contact Support
        footerElement: ''
      language:
        viewLanguage: English
      pageCustomizations:
        data:
        - key: ui_contact_ip_address_label
          value: SVAgYWRkcmVzczo=
        - key: ui_error_content_label
          value: RXJyb3I=
        - key: ui_success_optional_content_2
          value: ''
        - key: ui_success_optional_content_1
          value: ''
        - key: ui_post_access_optional_content_1
          value: ''
        - key: ui_post_access_optional_content_2
          value: ''
        - key: ui_success_message
          value: WW91IGhhdmUgc3VjY2Vzc2Z1bGx5IGNvbm5lY3RlZCB0byB0aGUgbmV0d29yay4=
        - key: ui_contact_optional_content_1
          value: ''
        - key: ui_contact_optional_content_2
          value: ''
        - key: ui_vlan_unsupported_error_message
          value: VG8gYWNjZXNzIHRoZSBuZXR3b3JrLCB5b3UgbXVzdCBtYW51YWxseSByZXNldCB0aGUgSVAgYWRkcmVzcyBvbiB5b3VyIGRldmljZS4gQ29udGFjdCB5b3VyIEhlbHAgRGVzayBpZiB5b3UgbmVlZCBhc3Npc3RhbmNlLg==
        - key: ui_user_last_login_pass_time_label
          value: TGFzdCBMb2dpbjo=
        - key: ui_post_access_content_label
          value: V2VsY29tZSBNZXNzYWdl
        - key: ui_success_returning_message
          value: ''
        - key: ui_error_page_title
          value: RXJyb3I=
        - key: ui_vlan_instruction_message
          value: ''
        - key: ui_contact_sessioninfo_text
          value: VGhpcyBpbmZvcm1hdGlvbiBwcm92aWRlcyBkZXRhaWxzIHRoYXQgdGhlIGhlbHAgZGVzayBtaWdodCBuZWVkIHRvIHJlc29sdmUgYW55IGlzc3VlcyB5b3UgYXJlIGV4cGVyaWVuY2luZy4=
        - key: ui_contact_content_label
          value: U3VwcG9ydCBJbmZvcm1hdGlvbg==
        - key: ui_contact_sessioninfo_title
          value: U2Vzc2lvbiBJbmZvcm1hdGlvbg==
        - key: ui_aup_accept_button
          value: QWNjZXB0
        - key: ui_error_optional_content_2
          value: ''
        - key: ui_error_optional_content_1
          value: ''
        - key: ui_vlan_install_error_message
          value: SW5zdGFsbGF0aW9uIG9mIHRoZSBhcHBsaWNhdGlvbiBmYWlsZWQuIEZvbGxvdyB0aGUgaW5zdHJ1Y3Rpb25zIGJlbG93IHRvIGNvbmZpZ3VyZSB5b3VyIGJyb3dzZXIgYW5kIHJlY29ubmVjdCB0byBuZXR3b3JrLg==
        - key: ui_footer_label
          value: ''
        - key: ui_post_access_instruction_message
          value: ''
        - key: ui_post_access_page_title
          value: UG9zdC1BY2Nlc3MgQmFubmVy
        - key: ui_aup_content_label
          value: QWNjZXB0YWJsZSBVc2UgUG9saWN5
        - key: ui_contact_page_title
          value: U3VwcG9ydCBJbmZvcm1hdGlvbg==
        - key: ui_contact_instruction_message
          value: U2hhcmUgdGhlc2UgZGV0YWlscyB3aXRoIHRoZSBoZWxwIGRlc2sgd2hlbiB0cm91Ymxlc2hvb3RpbmcgaXNzdWVzIHdpdGggdGhpcyBwb3J0YWwu
        - key: ui_session_timeout_error
          value: WW91ciBzZXNzaW9uIGhhcyB0aW1lZCBvdXQuIENsaWNrIFJldHJ5IHRvIHRyeSBhZ2Fpbi4=
        - key: ui_vlan_page_title
          value: Q29ubmVjdGluZyB0byBOZXR3b3Jr
        - key: ui_contact_helpdesk_text
          value: Q29udGFjdCB0aGUgaGVscCBkZXNrIGF0ICh4eHgpIHh4eC14eHh4Lg==
        - key: ui_aup_registration_code_label
          value: QWNjZXNzIGNvZGU6
        - key: ui_vlan_coa_error_message
          value: VW5hYmxlIHRvIGNvbW11bmljYXRlIHdpdGggc2VydmVyIHRvIHBlcmZvcm0gdGhlIGNoYW5nZSBvZiBhdXRob3JpemF0aW9uIChDb0EpLiBDb250YWN0IHRoZSBoZWxwIGRlc2sgZm9yIGFzc2lzdGFuY2Uu
        - key: ui_vlan_execute_message
          value: UmVsZWFzaW5nIGFuZCByZW5ld2luZyB5b3VyIElQIGFkZHJlc3Mu
        - key: ui_vlan_execute_error_message
          value: VW5hYmxlIHRvIHJlbmV3IHRoZSBJUCBhZGRyZXNzLiBZb3UgbWlnaHQgbmVlZCB0byBkaXNhYmxlIG9yIHJlZHVjZSB0aGUgc2VjdXJpdHkgbGV2ZWwgaW4gdGhlIFVzZXIgQWNjZXNzIENvbnRyb2wgKFVBQykuIFRvIG9wZW4gVUFDLCBjaG9vc2UgU3RhcnQgPiBDb250cm9sIFBhbmVsLiBJbiB0aGUgc2VhcmNoIGJveCwgdHlwZSB1YWMsIGFuZCB0aGVuIGNsaWNrIENoYW5nZSBVc2VyIEFjY291bnQgQ29udHJvbCBzZXR0aW5ncy4gIElmIHlvdSBhcmUgdXNpbmcgTWljcm9zb2Z0IEludGVybmV0IEV4cGxvcmVyLCB0aGUgc2l0ZSBuYW1lIHRoYXQgYXBwZWFycyBpbiB0aGUgVVJMIGFkZHJlc3MgZmllbGQgbXVzdCBiZSBhZGRlZCB0byB0aGUgdHJ1c3RlZCBzaXRlcy4gIFRvIGFkZCBpdCBhcyBhIHRydXN0ZWQgc2l0ZSwgY2hvb3NlIFRvb2xzID4gSW50ZXJuZXQgT3B0aW9ucyA+IFNlY3VyaXR5ID4gVHJ1c3RlZCBTaXRlcyku
        - key: ui_contact_failure_code_label
          value: RmFpbHVyZSBjb2RlOg==
        - key: ui_contact_link
          value: Q29udGFjdCBTdXBwb3J0
        - key: ui_success_instruction_message
          value: ''
        - key: ui_aup_page_title
          value: QWNjZXB0YWJsZSBVc2UgUG9saWN5
        - key: ui_contact_user_agent_label
          value: VXNlciBhZ2VudDo=
        - key: ui_aup_hotspot_text
          value: UGxlYXNlIGFjY2VwdCB0aGUgcG9saWN5OllvdSBhcmUgcmVzcG9uc2libGUgZm9yIG1haW50YWluaW5nIHRoZSBjb25maWRlbnRpYWxpdHkgb2YgdGhlIHBhc3N3b3JkIGFuZCBhbGwgYWN0aXZpdGllcyB0aGF0IG9jY3VyIHVuZGVyIHlvdXIgdXNlcm5hbWUgYW5kIHBhc3N3b3JkLkNpc2NvIFN5c3RlbXMgb2ZmZXJzIHRoZSAgU2VydmljZSBmb3IgYWN0aXZpdGllcyAgc3VjaCBhcyB0aGUgYWN0aXZlIHVzZSBvZiBlLW1haWwsIGluc3RhbnQgbWVzc2FnaW5nLCBicm93c2luZyB0aGUgV29ybGQgV2lkZSBXZWIgYW5kIGFjY2Vzc2luZyBjb3Jwb3JhdGUgaW50cmFuZXRzLiBIaWdoIHZvbHVtZSBkYXRhIHRyYW5zZmVycywgZXNwZWNpYWxseSBzdXN0YWluZWQgaGlnaCB2b2x1bWUgZGF0YSB0cmFuc2ZlcnMsIGFyZSBub3QgcGVybWl0dGVkLiBIb3N0aW5nIGEgd2ViIHNlcnZlciBvciBhbnkgb3RoZXIgc2VydmVyIGJ5IHVzZSBvZiBvdXIgU2VydmljZSBpcyBwcm9oaWJpdGVkLiBUcnlpbmcgdG8gYWNjZXNzIHNvbWVvbmUgZWxzZSdzIGFjY291bnQsIHNlbmRpbmcgdW5zb2xpY2l0ZWQgYnVsayBlLW1haWwsIGNvbGxlY3Rpb24gb2Ygb3RoZXIgcGVvcGxlJ3MgcGVyc29uYWwgZGF0YSB3aXRob3V0IHRoZWlyIGtub3dsZWRnZSBhbmQgaW50ZXJmZXJlbmNlIHdpdGggb3RoZXIgbmV0d29yayB1c2VycyBhcmUgYWxsIHByb2hpYml0ZWQuQ2lzY28gU3lzdGVtcyByZXNlcnZlcyB0aGUgcmlnaHQgdG8gc3VzcGVuZCB0aGUgU2VydmljZSBpZkNpc2NvIFN5c3RlbXMgcmVhc29uYWJseSBiZWxpZXZlcyB0aGF0IHlvdXIgdXNlIG9mIHRoZSBTZXJ2aWNlIGlzIHVucmVhc29uYWJseSBleGNlc3NpdmUgb3IgeW91IGFyZSB1c2luZyB0aGUgU2VydmljZSBmb3IgY3JpbWluYWwgb3IgaWxsZWdhbCBhY3Rpdml0aWVzLiBZb3UgZG8gbm90IGhhdmUgdGhlIHJpZ2h0IHRvIHJlc2VsbCB0aGlzIFNlcnZpY2UgdG8gYSB0aGlyZCBwYXJ0eS5DaXNjbyBTeXN0ZW1zIHJlc2VydmVzIHRoZSByaWdodCB0byByZXZpc2UsIGFtZW5kIG9yIG1vZGlmeSB0aGVzZSBUZXJtcyAmIENvbmRpdGlvbnMsIG91ciBvdGhlciBwb2xpY2llcyBhbmQgYWdyZWVtZW50cywgYW5kIGFzcGVjdHMgb2YgdGhlIFNlcnZpY2UgaXRzZWxmLiBOb3RpY2Ugb2YgYW55IHJldmlzaW9uLCBhbWVuZG1lbnQsIG9yIG1vZGlmaWNhdGlvbiB3aWxsIGJlIHBvc3RlZCBvbiBDaXNjbyBTeXN0ZW0ncyB3ZWJzaXRlIGFuZCB3aWxsIGJlIGVmZmVjdGl2ZSBhcyB0byBleGlzdGluZyB1c2VycyAzMCBkYXlzIGFmdGVyIHBvc3Rpbmcu
        - key: ui_vlan_content_label
          value: Q29ubmVjdGluZyB0byBOZXR3b3Jr
        - key: ui_aup_optional_content_2
          value: ''
        - key: ui_vlan_install_message
          value: WW91ciB3ZWIgYnJvd3NlciBpcyBhdHRlbXB0aW5nIHRvIGRvd25sb2FkIGFuIGFwcGxpY2F0aW9uLCB3aGljaCB3aWxsIGF1dG9tYXRpY2FsbHkgcmVuZXcgeW91ciBJUCBhZGRyZXNzIHNvIHlvdSBjYW4gYWNjZXNzIHRoZSBuZXR3b3JrLiBUaGlzIGRvd25sb2FkIHByb2Nlc3MgbWlnaHQgdGFrZSBzZXZlcmFsIG1pbnV0ZXMsIGRlcGVuZGluZyBvbiB5b3VyIGNvbm5lY3Rpb24gc3BlZWQuIEFmdGVyIHRoZSBkb3dubG9hZCBmaW5pc2hlcywgeW91IG11c3QgaGF2ZSBhZG1pbmlzdHJhdG9yIHByaXZpbGVnZXMgb24gdGhpcyBzeXN0ZW0gdG8gaW5zdGFsbCB0aGUgYXBwbGljYXRpb24uIEluIEZpcmVmb3gsIG1ha2Ugc3VyZSB0aGF0ICJBbGxvdyIgb3B0aW9uIGlzIHNlbGVjdGVkIGZvciBhbGwgSmF2YSBpdGVtcyBsaXN0ZWQgdW5kZXIgIkFjdGl2YXRlIFBsdWdpbnMiIHNlY3Rpb24gb2YgIlBlcm1pc3Npb25zIiB0YWIgaW4gIk1vcmUgSW5mb3JtYXRpb24iIGRpYWxvZy4gVGhlICJNb3JlIEluZm9ybWF0aW9uIiBkaWFsb2cgY2FuIGJlIGFjY2Vzc2VkIGJ5IGNsaWNraW5nIHRoZSBsb2NrIGljb24gb2YgdGhlIHNpdGUgVVJMIGFkZHJlc3MgZmllbGQuIElmIHlvdSBhcmUgdXNpbmcgTWljcm9zb2Z0IEludGVybmV0IEV4cGxvcmVyLCB5b3UgbXVzdCBhbHNvIHZlcmlmeSB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cjx1bD4KPGxpPlRoZSBzaXRlIG5hbWUgdGhhdCBhcHBlYXJzIGluIHRoZSBVUkwgYWRkcmVzcyBmaWVsZCBtdXN0IGJlIGFkZGVkIHRvIHRoZSB0cnVzdGVkIHNpdGVzLiAgVG8gYWRkIGl0IGFzIGEgdHJ1c3RlZCBzaXRlLCBjaG9vc2UgPGI+VG9vbHMgPiBJbnRlcm5ldCBPcHRpb25zID4gU2VjdXJpdHkgPiBUcnVzdGVkIFNpdGVzPC9iPikuPC9saT4KPGxpPllvdSBzaG91bGQgYWxzbyB0dXJuIG9mZiB0aGUgPGI+UHJvdGVjdGVkIE1vZGU8L2I+IG9wdGlvbiAodW5hdmFpbGFibGUgb24gV2luZG93cyBYUCkuPC9saT4KPGxpPkR1cmluZyB0aGUgZG93bmxvYWQgcHJvY2VzcywgeW91IG1pZ2h0IGJlIHByb21wdGVkIHRvIGFjY2VwdCBhIGRpZ2l0YWwgY2VydGlmaWNhdGUuIFZlcmlmeSB0aGUgdmFsaWRpdHkgb2YgdGhlIGNlcnRpZmljYXRlIGJlZm9yZSBhY2NlcHRpbmcgaXQuPC9saT4KPC91bD4=
        - key: ui_contact_mac_address_label
          value: TUFDIGFkZHJlc3M6
        - key: ui_aup_optional_content_1
          value: ''
        - key: ui_error_instruction_message
          value: ''
        - key: ui_success_content_label
          value: Q29ubmVjdGlvbiBTdWNjZXNzZnVs
        - key: ui_contact_title_label
          value: U3VwcG9ydCBJbmZvcm1hdGlvbg==
        - key: ui_vlan_java_disabled_error_message
          value: VG8gY29udGludWUsIGluc3RhbGwgYW5kIGVuYWJsZSB0aGUgbGF0ZXN0IEphdmEgdmVyc2lvbiwgYW5kIG1ha2Ugc3VyZSB0aGUgSmF2YSBwbHVnLWluIGlzIG5vdCBibG9ja2VkLiBZb3UgY2FuIGRvd25sb2FkIGFuZCBpbnN0YWxsIEphdmEgZnJvbSBodHRwOi8vd3d3LmphdmEuY29tL2VuL2Rvd25sb2FkLiBJZiB5b3UgYXJlIHVuYWJsZSB0byBkb3dubG9hZCBKYXZhLCBjb25uZWN0IHRvIGEgZGlmZmVyZW50IG5ldHdvcmsgYW5kIHRyeSBhZ2Fpbi4=
        - key: ui_post_access_continue_button
          value: Q29udGludWU=
        - key: ui_javascript_disabled_message
          value: WW91IG11c3QgdHVybiBvbiBKYXZhU2NyaXB0IHRvIHVzZSB0aGlzIHdlYiBzaXRlLg==
        - key: ui_contact_policy_server_label
          value: UG9saWN5IHNlcnZlcjo=
        - key: ui_user_last_login_ipaddr_label
          value: RnJvbTo=
        - key: ui_success_page_title
          value: Q29ubmVjdGlvbiBTdWNjZXNzZnVs
        - key: ui_contact_helpdesk_title
          value: U3VwcG9ydCBJbmZvcm1hdGlvbg==
        - key: ui_aup_decline_button
          value: RGVjbGluZQ==
        - key: ui_aup_decline_error
          value: WW91IGNob3NlIHRvIHJlamVjdCB0aGUgQWNjZXB0YWJsZSBVc2UgUG9saWN5LiBXZSBjYW5ub3QgYWxsb3cgYWNjZXNzIHRvIHRoaXMgbmV0d29yayB1bnRpbCB5b3UgYWNjZXB0IHRoZSBBY2NlcHRhYmxlIFVzZSBQb2xpY3ku
        - key: ui_session_timeout_retry_button
          value: UmV0cnk=
        - key: ui_post_access_message
          value: Q2xpY2sgPGI+Q29udGludWU8L2I+IHRvIGNvbm5lY3QgdG8gdGhlIG5ldHdvcmsu
        - key: ui_vlan_optional_content_2
          value: ''
        - key: ui_vlan_optional_content_1
          value: ''
        - key: ui_aup_agreement_label
          value: SSBhZ3JlZSB0byB0aGUgdGVybXMgYW5kIGNvbmRpdGlvbnM=
        - key: ui_contact_message
          value: Q29udGFjdCBJbmZvcm1hdGlvbg==
        - key: ui_field_required_error
          value: VGhpcyBmaWVsZCBpcyByZXF1aXJlZC4=
        - key: ui_banner_label
          value: SG90c3BvdCBQb3J0YWw=
        - key: ui_aup_instruction_message
          value: UGxlYXNlIHJlYWQgdGhlIEFjY2VwdGFibGUgVXNlIFBvbGljeS4=
      portalTheme:
        id: 9eb421c0-8c01-11e6-996c-525400b48521
        name: Default Blue theme
    description: Guests do not require username and password credentials to access the
      network, but you can optionally require an access code
    name: Hotspot Guest Portal (default)
    portalType: HOTSPOTGUEST
    settings:
      aupSettings:
        includeAup: true
        requireScrolling: false
      authSuccessSettings:
        successRedirect: AUTHSUCCESSPAGE
      portalSettings:
        allowedInterfaces:
        - eth0
        - bond0
        alwaysUsedLanguage: English
        certificateGroupTag: Default Portal Certificate Group
        coaType: COAREAUTHENTICATE
        displayLang: USEBROWSERLOCALE
        endpointIdentityGroup: aa178bd0-8bff-11e6-996c-525400b48521
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
- name: Update by id
  cisco.ise.hotspot_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: ''
    id: bd533907-bb9e-43d3-aef2-9a9f2a9dbb35
    name: My Hotspot Guest Portal
    settings:
      portalSettings:
        allowedInterfaces:
        - eth0
        - eth1
        - bond0
        httpsPort: 8443
- name: Delete by id
  cisco.ise.hotspot_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
- name: Ise request doc
  cisco.ise.hotspot_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
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
  - 
"""
