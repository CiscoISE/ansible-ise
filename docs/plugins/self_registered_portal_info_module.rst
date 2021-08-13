.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.ise.self_registered_portal_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.ise.self_registered_portal_info -- Information module for Self Registered Portal
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.ise collection <https://galaxy.ansible.com/cisco/ise>`_ (version 1.0.2).

    To install it use: :code:`ansible-galaxy collection install cisco.ise`.

    To use it in a playbook, specify: :code:`cisco.ise.self_registered_portal_info`.

.. version_added

.. versionadded:: 1.0.0 of cisco.ise

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Get all Self Registered Portal.
- Get Self Registered Portal by id.

.. note::
    This module has a corresponding :ref:`action plugin <action_plugins>`.

.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- ciscoisesdk


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-filter"></div>
                    <b>filter</b>
                    <a class="ansibleOptionLink" href="#parameter-filter" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Filter query parameter. &lt;br/&gt; **Simple filtering** should be available through the filter query string parameter. The structure of a filter is a triplet of field operator and value separated with dots. More than one filter can be sent. The logical operator common to ALL filter criteria will be by default AND, and can be changed by using the &quot;filterType=or&quot; query string parameter. Each resource Data model description should specify if an attribute is a filtered field. &lt;br/&gt; Operator | Description &lt;br/&gt; ------------|----------------- &lt;br/&gt; EQ | Equals &lt;br/&gt; NEQ | Not Equals &lt;br/&gt; GT | Greater Than &lt;br/&gt; LT | Less Then &lt;br/&gt; STARTSW | Starts With &lt;br/&gt; NSTARTSW | Not Starts With &lt;br/&gt; ENDSW | Ends With &lt;br/&gt; NENDSW | Not Ends With &lt;br/&gt; CONTAINS | Contains &lt;br/&gt; NCONTAINS | Not Contains &lt;br/&gt;.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-filterType"></div>
                    <b>filterType</b>
                    <a class="ansibleOptionLink" href="#parameter-filterType" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and can be changed by using the parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Id path parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-page"></div>
                    <b>page</b>
                    <a class="ansibleOptionLink" href="#parameter-page" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Page query parameter. Page number.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-size"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-size" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Size query parameter. Number of objects returned per page.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sortasc"></div>
                    <b>sortasc</b>
                    <a class="ansibleOptionLink" href="#parameter-sortasc" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Sortasc query parameter. Sort asc.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sortdsc"></div>
                    <b>sortdsc</b>
                    <a class="ansibleOptionLink" href="#parameter-sortdsc" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Sortdsc query parameter. Sort desc.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   `Self Registered Portal reference <https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary>`_
       Complete reference of the Self Registered Portal object model.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get all Self Registered Portal
      cisco.ise.self_registered_portal_info:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
        page: 1
        size: 20
        sortasc: string
        sortdsc: string
        filter: []
        filterType: AND
      register: result

    - name: Get Self Registered Portal by id
      cisco.ise.self_registered_portal_info:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
        id: string
      register: result





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ise_response"></div>
                    <b>ise_response</b>
                    <a class="ansibleOptionLink" href="#return-ise_response" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>A dictionary or list with the response returned by the Cisco ISE Python SDK</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{
      &quot;id&quot;: &quot;string&quot;,
      &quot;name&quot;: &quot;string&quot;,
      &quot;description&quot;: &quot;string&quot;,
      &quot;portalType&quot;: &quot;string&quot;,
      &quot;portalTestUrl&quot;: &quot;string&quot;,
      &quot;settings&quot;: {
        &quot;portalSettings&quot;: {
          &quot;httpsPort&quot;: 0,
          &quot;allowedInterfaces&quot;: &quot;string&quot;,
          &quot;certificateGroupTag&quot;: &quot;string&quot;,
          &quot;authenticationMethod&quot;: &quot;string&quot;,
          &quot;assignedGuestTypeForEmployee&quot;: &quot;string&quot;,
          &quot;displayLang&quot;: &quot;string&quot;,
          &quot;fallbackLanguage&quot;: &quot;string&quot;,
          &quot;alwaysUsedLanguage&quot;: &quot;string&quot;
        },
        &quot;loginPageSettings&quot;: {
          &quot;requireAccessCode&quot;: true,
          &quot;maxFailedAttemptsBeforeRateLimit&quot;: 0,
          &quot;timeBetweenLoginsDuringRateLimit&quot;: 0,
          &quot;includeAup&quot;: true,
          &quot;aupDisplay&quot;: &quot;string&quot;,
          &quot;requireAupAcceptance&quot;: true,
          &quot;accessCode&quot;: &quot;string&quot;,
          &quot;allowGuestToCreateAccounts&quot;: true,
          &quot;allowForgotPassword&quot;: true,
          &quot;allowGuestToChangePassword&quot;: true,
          &quot;allowAlternateGuestPortal&quot;: true,
          &quot;alternateGuestPortal&quot;: &quot;string&quot;,
          &quot;allowGuestToUseSocialAccounts&quot;: true,
          &quot;allowShowGuestForm&quot;: true,
          &quot;socialConfigs&quot;: [
            {
              &quot;socialMediaType&quot;: &quot;string&quot;,
              &quot;socialMediaValue&quot;: &quot;string&quot;
            }
          ]
        },
        &quot;selfRegPageSettings&quot;: {
          &quot;assignGuestsToGuestType&quot;: &quot;string&quot;,
          &quot;accountValidityDuration&quot;: 0,
          &quot;accountValidityTimeUnits&quot;: &quot;string&quot;,
          &quot;requireRegistrationCode&quot;: true,
          &quot;registrationCode&quot;: &quot;string&quot;,
          &quot;fieldUserName&quot;: {
            &quot;include&quot;: true,
            &quot;require&quot;: true
          },
          &quot;fieldFirstName&quot;: {
            &quot;include&quot;: true,
            &quot;require&quot;: true
          },
          &quot;fieldLastName&quot;: {
            &quot;include&quot;: true,
            &quot;require&quot;: true
          },
          &quot;fieldEmailAddr&quot;: {
            &quot;include&quot;: true,
            &quot;require&quot;: true
          },
          &quot;fieldPhoneNo&quot;: {
            &quot;include&quot;: true,
            &quot;require&quot;: true
          },
          &quot;fieldCompany&quot;: {
            &quot;include&quot;: true,
            &quot;require&quot;: true
          },
          &quot;fieldLocation&quot;: {
            &quot;include&quot;: true,
            &quot;require&quot;: true
          },
          &quot;selectableLocations&quot;: [
            &quot;string&quot;
          ],
          &quot;fieldSmsProvider&quot;: {
            &quot;include&quot;: true,
            &quot;require&quot;: true
          },
          &quot;selectableSmsProviders&quot;: [
            &quot;string&quot;
          ],
          &quot;fieldPersonBeingVisited&quot;: {
            &quot;include&quot;: true,
            &quot;require&quot;: true
          },
          &quot;fieldReasonForVisit&quot;: {
            &quot;include&quot;: true,
            &quot;require&quot;: true
          },
          &quot;includeAup&quot;: true,
          &quot;aupDisplay&quot;: &quot;string&quot;,
          &quot;requireAupAcceptance&quot;: true,
          &quot;enableGuestEmailWhitelist&quot;: true,
          &quot;guestEmailWhitelistDomains&quot;: &quot;string&quot;,
          &quot;enableGuestEmailBlacklist&quot;: true,
          &quot;guestEmailBlacklistDomains&quot;: &quot;string&quot;,
          &quot;requireGuestApproval&quot;: true,
          &quot;autoLoginSelfWait&quot;: true,
          &quot;autoLoginTimePeriod&quot;: 0,
          &quot;allowGraceAccess&quot;: true,
          &quot;graceAccessExpireInterval&quot;: 0,
          &quot;graceAccessSendAccountExpiration&quot;: true,
          &quot;sendApprovalRequestTo&quot;: &quot;string&quot;,
          &quot;approvalEmailAddresses&quot;: &quot;string&quot;,
          &quot;postRegistrationRedirect&quot;: &quot;string&quot;,
          &quot;postRegistrationRedirectUrl&quot;: &quot;string&quot;,
          &quot;credentialNotificationUsingEmail&quot;: true,
          &quot;credentialNotificationUsingSms&quot;: true,
          &quot;approveDenyLinksValidFor&quot;: 0,
          &quot;approveDenyLinksTimeUnits&quot;: &quot;string&quot;,
          &quot;requireApproverToAuthenticate&quot;: true,
          &quot;authenticateSponsorsUsingPortalList&quot;: &quot;string&quot;,
          &quot;sponsorPortalList&quot;: []
        },
        &quot;selfRegSuccessSettings&quot;: {
          &quot;includeUserName&quot;: true,
          &quot;includePassword&quot;: true,
          &quot;includeFirstName&quot;: true,
          &quot;includeLastName&quot;: true,
          &quot;includeEmailAddr&quot;: true,
          &quot;includePhoneNo&quot;: true,
          &quot;includeCompany&quot;: true,
          &quot;includeLocation&quot;: true,
          &quot;includeSmsProvider&quot;: true,
          &quot;includePersonBeingVisited&quot;: true,
          &quot;includeReasonForVisit&quot;: true,
          &quot;allowGuestSendSelfUsingPrint&quot;: true,
          &quot;allowGuestSendSelfUsingEmail&quot;: true,
          &quot;allowGuestSendSelfUsingSms&quot;: true,
          &quot;includeAup&quot;: true,
          &quot;aupOnPage&quot;: true,
          &quot;requireAupAcceptance&quot;: true,
          &quot;requireAupScrolling&quot;: true,
          &quot;allowGuestLoginFromSelfregSuccessPage&quot;: true
        },
        &quot;aupSettings&quot;: {
          &quot;includeAup&quot;: true,
          &quot;useDiffAupForEmployees&quot;: true,
          &quot;skipAupForEmployees&quot;: true,
          &quot;requireScrolling&quot;: true,
          &quot;requireAupScrolling&quot;: true,
          &quot;displayFrequency&quot;: &quot;string&quot;,
          &quot;displayFrequencyIntervalDays&quot;: 0
        },
        &quot;guestChangePasswordSettings&quot;: {
          &quot;allowChangePasswdAtFirstLogin&quot;: true
        },
        &quot;guestDeviceRegistrationSettings&quot;: {
          &quot;autoRegisterGuestDevices&quot;: true,
          &quot;allowGuestsToRegisterDevices&quot;: true
        },
        &quot;byodSettings&quot;: {
          &quot;byodWelcomeSettings&quot;: {
            &quot;enableBYOD&quot;: true,
            &quot;enableGuestAccess&quot;: true,
            &quot;requireMDM&quot;: true,
            &quot;includeAup&quot;: true,
            &quot;aupDisplay&quot;: &quot;string&quot;,
            &quot;requireAupAcceptance&quot;: true,
            &quot;requireScrolling&quot;: true
          },
          &quot;byodRegistrationSettings&quot;: {
            &quot;showDeviceID&quot;: true,
            &quot;endPointIdentityGroupId&quot;: &quot;string&quot;
          },
          &quot;byodRegistrationSuccessSettings&quot;: {
            &quot;successRedirect&quot;: &quot;string&quot;,
            &quot;redirectUrl&quot;: &quot;string&quot;
          }
        },
        &quot;postLoginBannerSettings&quot;: {
          &quot;includePostAccessBanner&quot;: true
        },
        &quot;postAccessBannerSettings&quot;: {
          &quot;includePostAccessBanner&quot;: true
        },
        &quot;authSuccessSettings&quot;: {
          &quot;successRedirect&quot;: &quot;string&quot;,
          &quot;redirectUrl&quot;: &quot;string&quot;
        },
        &quot;supportInfoSettings&quot;: {
          &quot;includeSupportInfoPage&quot;: true,
          &quot;includeMacAddr&quot;: true,
          &quot;includeIpAddress&quot;: true,
          &quot;includeBrowserUserAgent&quot;: true,
          &quot;includePolicyServer&quot;: true,
          &quot;includeFailureCode&quot;: true,
          &quot;emptyFieldDisplay&quot;: &quot;string&quot;,
          &quot;defaultEmptyFieldValue&quot;: &quot;string&quot;
        }
      },
      &quot;customizations&quot;: {
        &quot;portalTheme&quot;: {
          &quot;id&quot;: &quot;string&quot;,
          &quot;name&quot;: &quot;string&quot;,
          &quot;themeData&quot;: &quot;string&quot;
        },
        &quot;portalTweakSettings&quot;: {
          &quot;bannerColor&quot;: &quot;string&quot;,
          &quot;bannerTextColor&quot;: &quot;string&quot;,
          &quot;pageBackgroundColor&quot;: &quot;string&quot;,
          &quot;pageLabelAndTextColor&quot;: &quot;string&quot;
        },
        &quot;language&quot;: {
          &quot;viewLanguage&quot;: &quot;string&quot;
        },
        &quot;globalCustomizations&quot;: {
          &quot;mobileLogoImage&quot;: {
            &quot;data&quot;: &quot;string&quot;
          },
          &quot;desktopLogoImage&quot;: {
            &quot;data&quot;: &quot;string&quot;
          },
          &quot;bannerImage&quot;: {
            &quot;data&quot;: &quot;string&quot;
          },
          &quot;backgroundImage&quot;: {
            &quot;data&quot;: &quot;string&quot;
          },
          &quot;bannerTitle&quot;: &quot;string&quot;,
          &quot;contactText&quot;: &quot;string&quot;,
          &quot;footerElement&quot;: &quot;string&quot;
        },
        &quot;pageCustomizations&quot;: {
          &quot;data&quot;: [
            {
              &quot;key&quot;: &quot;string&quot;,
              &quot;value&quot;: &quot;string&quot;
            }
          ]
        }
      },
      &quot;link&quot;: {
        &quot;rel&quot;: &quot;string&quot;,
        &quot;href&quot;: &quot;string&quot;,
        &quot;type&quot;: &quot;string&quot;
      }
    }</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Rafael Campos (@racampos)



.. Parsing errors

