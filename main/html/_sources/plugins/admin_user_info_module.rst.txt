.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.ise.admin_user_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.ise.admin_user_info -- Information module for Admin User
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.ise collection <https://galaxy.ansible.com/cisco/ise>`_ (version 1.0.2).

    To install it use: :code:`ansible-galaxy collection install cisco.ise`.

    To use it in a playbook, specify: :code:`cisco.ise.admin_user_info`.

.. version_added

.. versionadded:: 1.0.0 of cisco.ise

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Get all Admin User.
- Get Admin User by id.

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

   `Admin User reference <https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary>`_
       Complete reference of the Admin User object model.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get all Admin User
      cisco.ise.admin_user_info:
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

    - name: Get Admin User by id
      cisco.ise.admin_user_info:
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
      &quot;name&quot;: &quot;string&quot;,
      &quot;id&quot;: &quot;string&quot;,
      &quot;description&quot;: &quot;string&quot;,
      &quot;enabled&quot;: true,
      &quot;password&quot;: &quot;string&quot;,
      &quot;changePassword&quot;: true,
      &quot;includeSystemAlarmsInEmail&quot;: true,
      &quot;externalUser&quot;: true,
      &quot;inactiveAccountNeverDisabled&quot;: true,
      &quot;adminGroups&quot;: &quot;string&quot;,
      &quot;customAttributes&quot;: {},
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

