.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.ise.network_device_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.ise.network_device -- Resource module for Network Device
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.ise collection <https://galaxy.ansible.com/cisco/ise>`_ (version 1.0.2).

    To install it use: :code:`ansible-galaxy collection install cisco.ise`.

    To use it in a playbook, specify: :code:`cisco.ise.network_device`.

.. version_added

.. versionadded:: 1.0.0 of cisco.ise

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Manage operations create, update and delete of the resource Network Device.

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
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-authenticationSettings"></div>
                    <b>authenticationSettings</b>
                    <a class="ansibleOptionLink" href="#parameter-authenticationSettings" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s authenticationSettings.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-authenticationSettings/dtlsRequired"></div>
                    <b>dtlsRequired</b>
                    <a class="ansibleOptionLink" href="#parameter-authenticationSettings/dtlsRequired" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>This value enforces use of dtls.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-authenticationSettings/enabled"></div>
                    <b>enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-authenticationSettings/enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Enabled flag.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-authenticationSettings/enableKeyWrap"></div>
                    <b>enableKeyWrap</b>
                    <a class="ansibleOptionLink" href="#parameter-authenticationSettings/enableKeyWrap" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>EnableKeyWrap flag.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-authenticationSettings/enableMultiSecret"></div>
                    <b>enableMultiSecret</b>
                    <a class="ansibleOptionLink" href="#parameter-authenticationSettings/enableMultiSecret" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>EnableMultiSecret flag.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-authenticationSettings/keyEncryptionKey"></div>
                    <b>keyEncryptionKey</b>
                    <a class="ansibleOptionLink" href="#parameter-authenticationSettings/keyEncryptionKey" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s keyEncryptionKey.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-authenticationSettings/keyInputFormat"></div>
                    <b>keyInputFormat</b>
                    <a class="ansibleOptionLink" href="#parameter-authenticationSettings/keyInputFormat" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Allowed values - ASCII, - HEXADECIMAL.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-authenticationSettings/messageAuthenticatorCodeKey"></div>
                    <b>messageAuthenticatorCodeKey</b>
                    <a class="ansibleOptionLink" href="#parameter-authenticationSettings/messageAuthenticatorCodeKey" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s messageAuthenticatorCodeKey.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-authenticationSettings/networkProtocol"></div>
                    <b>networkProtocol</b>
                    <a class="ansibleOptionLink" href="#parameter-authenticationSettings/networkProtocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Allowed values - RADIUS, - TACACS_PLUS.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-authenticationSettings/radiusSharedSecret"></div>
                    <b>radiusSharedSecret</b>
                    <a class="ansibleOptionLink" href="#parameter-authenticationSettings/radiusSharedSecret" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s radiusSharedSecret.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-authenticationSettings/secondRadiusSharedSecret"></div>
                    <b>secondRadiusSharedSecret</b>
                    <a class="ansibleOptionLink" href="#parameter-authenticationSettings/secondRadiusSharedSecret" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s secondRadiusSharedSecret.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-coaPort"></div>
                    <b>coaPort</b>
                    <a class="ansibleOptionLink" href="#parameter-coaPort" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s coaPort.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s description.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-dtlsDnsName"></div>
                    <b>dtlsDnsName</b>
                    <a class="ansibleOptionLink" href="#parameter-dtlsDnsName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This value is used to verify the client identity contained in the X.509 RADIUS/DTLS client certificate.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                            <div>Network Device&#x27;s id.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-modelName"></div>
                    <b>modelName</b>
                    <a class="ansibleOptionLink" href="#parameter-modelName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s modelName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-NetworkDeviceGroupList"></div>
                    <b>NetworkDeviceGroupList</b>
                    <a class="ansibleOptionLink" href="#parameter-NetworkDeviceGroupList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of Network Device Group names for this node.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-NetworkDeviceIPList"></div>
                    <b>NetworkDeviceIPList</b>
                    <a class="ansibleOptionLink" href="#parameter-NetworkDeviceIPList" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of IP Subnets for this node.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-NetworkDeviceIPList/getIpaddressExclude"></div>
                    <b>getIpaddressExclude</b>
                    <a class="ansibleOptionLink" href="#parameter-NetworkDeviceIPList/getIpaddressExclude" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>It can be either single IP address or IP range address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-NetworkDeviceIPList/ipaddress"></div>
                    <b>ipaddress</b>
                    <a class="ansibleOptionLink" href="#parameter-NetworkDeviceIPList/ipaddress" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s ipaddress.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-NetworkDeviceIPList/mask"></div>
                    <b>mask</b>
                    <a class="ansibleOptionLink" href="#parameter-NetworkDeviceIPList/mask" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s mask.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-profileName"></div>
                    <b>profileName</b>
                    <a class="ansibleOptionLink" href="#parameter-profileName" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s profileName.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-snmpsettings"></div>
                    <b>snmpsettings</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpsettings" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s snmpsettings.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpsettings/linkTrapQuery"></div>
                    <b>linkTrapQuery</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpsettings/linkTrapQuery" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>LinkTrapQuery flag.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpsettings/macTrapQuery"></div>
                    <b>macTrapQuery</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpsettings/macTrapQuery" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>MacTrapQuery flag.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpsettings/originatingPolicyServicesNode"></div>
                    <b>originatingPolicyServicesNode</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpsettings/originatingPolicyServicesNode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s originatingPolicyServicesNode.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpsettings/pollingInterval"></div>
                    <b>pollingInterval</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpsettings/pollingInterval" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s pollingInterval.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpsettings/roCommunity"></div>
                    <b>roCommunity</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpsettings/roCommunity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s roCommunity.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snmpsettings/version"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-snmpsettings/version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s version.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-softwareVersion"></div>
                    <b>softwareVersion</b>
                    <a class="ansibleOptionLink" href="#parameter-softwareVersion" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s softwareVersion.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-tacacsSettings"></div>
                    <b>tacacsSettings</b>
                    <a class="ansibleOptionLink" href="#parameter-tacacsSettings" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s tacacsSettings.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-tacacsSettings/connectModeOptions"></div>
                    <b>connectModeOptions</b>
                    <a class="ansibleOptionLink" href="#parameter-tacacsSettings/connectModeOptions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Allowed values - OFF, - ON_LEGACY, - ON_DRAFT_COMPLIANT.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-tacacsSettings/sharedSecret"></div>
                    <b>sharedSecret</b>
                    <a class="ansibleOptionLink" href="#parameter-tacacsSettings/sharedSecret" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s sharedSecret.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings"></div>
                    <b>trustsecsettings</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s trustsecsettings.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/deviceAuthenticationSettings"></div>
                    <b>deviceAuthenticationSettings</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/deviceAuthenticationSettings" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s deviceAuthenticationSettings.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/deviceAuthenticationSettings/sgaDeviceId"></div>
                    <b>sgaDeviceId</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/deviceAuthenticationSettings/sgaDeviceId" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s sgaDeviceId.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/deviceAuthenticationSettings/sgaDevicePassword"></div>
                    <b>sgaDevicePassword</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/deviceAuthenticationSettings/sgaDevicePassword" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s sgaDevicePassword.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/deviceConfigurationDeployment"></div>
                    <b>deviceConfigurationDeployment</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/deviceConfigurationDeployment" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s deviceConfigurationDeployment.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/deviceConfigurationDeployment/enableModePassword"></div>
                    <b>enableModePassword</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/deviceConfigurationDeployment/enableModePassword" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s enableModePassword.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/deviceConfigurationDeployment/execModePassword"></div>
                    <b>execModePassword</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/deviceConfigurationDeployment/execModePassword" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s execModePassword.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/deviceConfigurationDeployment/execModeUsername"></div>
                    <b>execModeUsername</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/deviceConfigurationDeployment/execModeUsername" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s execModeUsername.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/deviceConfigurationDeployment/includeWhenDeployingSGTUpdates"></div>
                    <b>includeWhenDeployingSGTUpdates</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/deviceConfigurationDeployment/includeWhenDeployingSGTUpdates" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>IncludeWhenDeployingSGTUpdates flag.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/pushIdSupport"></div>
                    <b>pushIdSupport</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/pushIdSupport" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>PushIdSupport flag.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/sgaNotificationAndUpdates"></div>
                    <b>sgaNotificationAndUpdates</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/sgaNotificationAndUpdates" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s sgaNotificationAndUpdates.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/sgaNotificationAndUpdates/coaSourceHost"></div>
                    <b>coaSourceHost</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/sgaNotificationAndUpdates/coaSourceHost" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s coaSourceHost.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/sgaNotificationAndUpdates/downlaodEnvironmentDataEveryXSeconds"></div>
                    <b>downlaodEnvironmentDataEveryXSeconds</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/sgaNotificationAndUpdates/downlaodEnvironmentDataEveryXSeconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s downlaodEnvironmentDataEveryXSeconds.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/sgaNotificationAndUpdates/downlaodPeerAuthorizationPolicyEveryXSeconds"></div>
                    <b>downlaodPeerAuthorizationPolicyEveryXSeconds</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/sgaNotificationAndUpdates/downlaodPeerAuthorizationPolicyEveryXSeconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s downlaodPeerAuthorizationPolicyEveryXSeconds.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/sgaNotificationAndUpdates/downloadSGACLListsEveryXSeconds"></div>
                    <b>downloadSGACLListsEveryXSeconds</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/sgaNotificationAndUpdates/downloadSGACLListsEveryXSeconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s downloadSGACLListsEveryXSeconds.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/sgaNotificationAndUpdates/otherSGADevicesToTrustThisDevice"></div>
                    <b>otherSGADevicesToTrustThisDevice</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/sgaNotificationAndUpdates/otherSGADevicesToTrustThisDevice" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>OtherSGADevicesToTrustThisDevice flag.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/sgaNotificationAndUpdates/reAuthenticationEveryXSeconds"></div>
                    <b>reAuthenticationEveryXSeconds</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/sgaNotificationAndUpdates/reAuthenticationEveryXSeconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Device&#x27;s reAuthenticationEveryXSeconds.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/sgaNotificationAndUpdates/sendConfigurationToDevice"></div>
                    <b>sendConfigurationToDevice</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/sgaNotificationAndUpdates/sendConfigurationToDevice" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>SendConfigurationToDevice flag.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-trustsecsettings/sgaNotificationAndUpdates/sendConfigurationToDeviceUsing"></div>
                    <b>sendConfigurationToDeviceUsing</b>
                    <a class="ansibleOptionLink" href="#parameter-trustsecsettings/sgaNotificationAndUpdates/sendConfigurationToDeviceUsing" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Allowed values - ENABLE_USING_COA, - ENABLE_USING_CLI, - DISABLE_ALL.</div>
                                                        </td>
            </tr>
                    
                    
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   `Network Device reference <https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary>`_
       Complete reference of the Network Device object model.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Update by name
      cisco.ise.network_device:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
        state: present
        NetworkDeviceGroupList:
        - string
        NetworkDeviceIPList:
        - getIpaddressExclude: string
          ipaddress: string
          mask: 0
        authenticationSettings:
          dtlsRequired: true
          enableKeyWrap: true
          enableMultiSecret: true
          enabled: true
          keyEncryptionKey: string
          keyInputFormat: string
          messageAuthenticatorCodeKey: string
          networkProtocol: string
          radiusSharedSecret: string
          secondRadiusSharedSecret: string
        coaPort: 0
        description: string
        dtlsDnsName: string
        id: string
        modelName: string
        name: string
        profileName: string
        snmpsettings:
          linkTrapQuery: true
          macTrapQuery: true
          originatingPolicyServicesNode: string
          pollingInterval: 0
          roCommunity: string
          version: string
        softwareVersion: string
        tacacsSettings:
          connectModeOptions: string
          sharedSecret: string
        trustsecsettings:
          deviceAuthenticationSettings:
            sgaDeviceId: string
            sgaDevicePassword: string
          deviceConfigurationDeployment:
            enableModePassword: string
            execModePassword: string
            execModeUsername: string
            includeWhenDeployingSGTUpdates: true
          pushIdSupport: true
          sgaNotificationAndUpdates:
            coaSourceHost: string
            downlaodEnvironmentDataEveryXSeconds: 0
            downlaodPeerAuthorizationPolicyEveryXSeconds: 0
            downloadSGACLListsEveryXSeconds: 0
            otherSGADevicesToTrustThisDevice: true
            reAuthenticationEveryXSeconds: 0
            sendConfigurationToDevice: true
            sendConfigurationToDeviceUsing: string

    - name: Delete by name
      cisco.ise.network_device:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
        state: absent
        name: string

    - name: Update by id
      cisco.ise.network_device:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
        state: present
        NetworkDeviceGroupList:
        - string
        NetworkDeviceIPList:
        - getIpaddressExclude: string
          ipaddress: string
          mask: 0
        authenticationSettings:
          dtlsRequired: true
          enableKeyWrap: true
          enableMultiSecret: true
          enabled: true
          keyEncryptionKey: string
          keyInputFormat: string
          messageAuthenticatorCodeKey: string
          networkProtocol: string
          radiusSharedSecret: string
          secondRadiusSharedSecret: string
        coaPort: 0
        description: string
        dtlsDnsName: string
        id: string
        modelName: string
        name: string
        profileName: string
        snmpsettings:
          linkTrapQuery: true
          macTrapQuery: true
          originatingPolicyServicesNode: string
          pollingInterval: 0
          roCommunity: string
          version: string
        softwareVersion: string
        tacacsSettings:
          connectModeOptions: string
          sharedSecret: string
        trustsecsettings:
          deviceAuthenticationSettings:
            sgaDeviceId: string
            sgaDevicePassword: string
          deviceConfigurationDeployment:
            enableModePassword: string
            execModePassword: string
            execModeUsername: string
            includeWhenDeployingSGTUpdates: true
          pushIdSupport: true
          sgaNotificationAndUpdates:
            coaSourceHost: string
            downlaodEnvironmentDataEveryXSeconds: 0
            downlaodPeerAuthorizationPolicyEveryXSeconds: 0
            downloadSGACLListsEveryXSeconds: 0
            otherSGADevicesToTrustThisDevice: true
            reAuthenticationEveryXSeconds: 0
            sendConfigurationToDevice: true
            sendConfigurationToDeviceUsing: string

    - name: Delete by id
      cisco.ise.network_device:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
        state: absent
        id: string

    - name: Create
      cisco.ise.network_device:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
        state: present
        NetworkDeviceGroupList:
        - string
        NetworkDeviceIPList:
        - getIpaddressExclude: string
          ipaddress: string
          mask: 0
        authenticationSettings:
          dtlsRequired: true
          enableKeyWrap: true
          enableMultiSecret: true
          enabled: true
          keyEncryptionKey: string
          keyInputFormat: string
          messageAuthenticatorCodeKey: string
          networkProtocol: string
          radiusSharedSecret: string
          secondRadiusSharedSecret: string
        coaPort: 0
        description: string
        dtlsDnsName: string
        modelName: string
        name: string
        profileName: string
        snmpsettings:
          linkTrapQuery: true
          macTrapQuery: true
          originatingPolicyServicesNode: string
          pollingInterval: 0
          roCommunity: string
          version: string
        softwareVersion: string
        tacacsSettings:
          connectModeOptions: string
          sharedSecret: string
        trustsecsettings:
          deviceAuthenticationSettings:
            sgaDeviceId: string
            sgaDevicePassword: string
          deviceConfigurationDeployment:
            enableModePassword: string
            execModePassword: string
            execModeUsername: string
            includeWhenDeployingSGTUpdates: true
          pushIdSupport: true
          sgaNotificationAndUpdates:
            coaSourceHost: string
            downlaodEnvironmentDataEveryXSeconds: 0
            downlaodPeerAuthorizationPolicyEveryXSeconds: 0
            downloadSGACLListsEveryXSeconds: 0
            otherSGADevicesToTrustThisDevice: true
            reAuthenticationEveryXSeconds: 0
            sendConfigurationToDevice: true
            sendConfigurationToDeviceUsing: string





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
      &quot;UpdatedFieldsList&quot;: {
        &quot;updatedField&quot;: {
          &quot;field&quot;: &quot;string&quot;,
          &quot;oldValue&quot;: &quot;string&quot;,
          &quot;newValue&quot;: &quot;string&quot;
        },
        &quot;field&quot;: &quot;string&quot;,
        &quot;oldValue&quot;: &quot;string&quot;,
        &quot;newValue&quot;: &quot;string&quot;
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

