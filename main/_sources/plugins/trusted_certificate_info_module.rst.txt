.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.ise.trusted_certificate_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.ise.trusted_certificate_info -- Information module for Trusted Certificate
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.ise collection <https://galaxy.ansible.com/cisco/ise>`_ (version 1.0.2).

    To install it use: :code:`ansible-galaxy collection install cisco.ise`.

    To use it in a playbook, specify: :code:`cisco.ise.trusted_certificate_info`.

.. version_added

.. versionadded:: 1.0.0 of cisco.ise

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Get all Trusted Certificate.
- Get Trusted Certificate by id.

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
                                            <div>Filter query parameter. &lt;div&gt; &lt;style type=&quot;text/css&quot; scoped&gt; .apiServiceTable td, .apiServiceTable th { padding 5px 10px !important; text-align left; } &lt;/style&gt; &lt;span&gt; &lt;b&gt;Simple filtering&lt;/b&gt; should be available through the filter query string parameter. The structure of a filter is a triplet of field operator and value separated with dots. More than one filter can be sent. The logical operator common to ALL filter criteria will be by default AND, and can be changed by using the &lt;i&gt;&quot;filterType=or&quot;&lt;/i&gt; query string parameter. Each resource Data model description should specify if an attribute is a filtered field. &lt;/span&gt; &lt;br /&gt; &lt;table class=&quot;apiServiceTable&quot;&gt; &lt;thead&gt; &lt;tr&gt; &lt;th&gt;OPERATOR&lt;/th&gt; &lt;th&gt;DESCRIPTION&lt;/th&gt; &lt;/tr&gt; &lt;/thead&gt; &lt;tbody&gt; &lt;tr&gt; &lt;td&gt;EQ&lt;/td&gt; &lt;td&gt;Equals&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;NEQ&lt;/td&gt; &lt;td&gt;Not Equals&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;GT&lt;/td&gt; &lt;td&gt;Greater Than&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;LT&lt;/td&gt; &lt;td&gt;Less Then&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;STARTSW&lt;/td&gt; &lt;td&gt;Starts With&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;NSTARTSW&lt;/td&gt; &lt;td&gt;Not Starts With&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;ENDSW&lt;/td&gt; &lt;td&gt;Ends With&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;NENDSW&lt;/td&gt; &lt;td&gt;Not Ends With&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;CONTAINS&lt;/td&gt; &lt;td&gt;Contains&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;NCONTAINS&lt;/td&gt; &lt;td&gt;Not Contains&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt; &lt;/div&gt;.</div>
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
                                            <div>Id path parameter. The id of the trust certificate.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-sort"></div>
                    <b>sort</b>
                    <a class="ansibleOptionLink" href="#parameter-sort" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Sort query parameter. Sort type - asc or desc.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sortBy"></div>
                    <b>sortBy</b>
                    <a class="ansibleOptionLink" href="#parameter-sortBy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SortBy query parameter. Sort column by which objects needs to be sorted.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   `Trusted Certificate reference <https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary>`_
       Complete reference of the Trusted Certificate object model.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get all Trusted Certificate
      cisco.ise.trusted_certificate_info:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
        page: 1
        size: 20
        sort: asc
        sortBy: string
        filter: []
        filterType: AND
      register: result

    - name: Get Trusted Certificate by id
      cisco.ise.trusted_certificate_info:
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
      &quot;response&quot;: {
        &quot;authenticateBeforeCRLReceived&quot;: &quot;string&quot;,
        &quot;automaticCRLUpdate&quot;: &quot;string&quot;,
        &quot;automaticCRLUpdatePeriod&quot;: &quot;string&quot;,
        &quot;automaticCRLUpdateUnits&quot;: &quot;string&quot;,
        &quot;crlDistributionUrl&quot;: &quot;string&quot;,
        &quot;crlDownloadFailureRetries&quot;: &quot;string&quot;,
        &quot;crlDownloadFailureRetriesUnits&quot;: &quot;string&quot;,
        &quot;description&quot;: &quot;string&quot;,
        &quot;downloadCRL&quot;: &quot;string&quot;,
        &quot;enableOCSPValidation&quot;: &quot;string&quot;,
        &quot;enableServerIdentityCheck&quot;: &quot;string&quot;,
        &quot;expirationDate&quot;: &quot;string&quot;,
        &quot;friendlyName&quot;: &quot;string&quot;,
        &quot;id&quot;: &quot;string&quot;,
        &quot;ignoreCRLExpiration&quot;: &quot;string&quot;,
        &quot;internalCA&quot;: true,
        &quot;isReferredInPolicy&quot;: true,
        &quot;issuedBy&quot;: &quot;string&quot;,
        &quot;issuedTo&quot;: &quot;string&quot;,
        &quot;keySize&quot;: &quot;string&quot;,
        &quot;link&quot;: {
          &quot;href&quot;: &quot;string&quot;,
          &quot;rel&quot;: &quot;string&quot;,
          &quot;type&quot;: &quot;string&quot;
        },
        &quot;nonAutomaticCRLUpdatePeriod&quot;: &quot;string&quot;,
        &quot;nonAutomaticCRLUpdateUnits&quot;: &quot;string&quot;,
        &quot;rejectIfNoStatusFromOCSP&quot;: &quot;string&quot;,
        &quot;rejectIfUnreachableFromOCSP&quot;: &quot;string&quot;,
        &quot;selectedOCSPService&quot;: &quot;string&quot;,
        &quot;serialNumberDecimalFormat&quot;: &quot;string&quot;,
        &quot;sha256Fingerprint&quot;: &quot;string&quot;,
        &quot;signatureAlgorithm&quot;: &quot;string&quot;,
        &quot;status&quot;: &quot;string&quot;,
        &quot;subject&quot;: &quot;string&quot;,
        &quot;trustedFor&quot;: &quot;string&quot;,
        &quot;validFrom&quot;: &quot;string&quot;
      },
      &quot;version&quot;: &quot;string&quot;
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

