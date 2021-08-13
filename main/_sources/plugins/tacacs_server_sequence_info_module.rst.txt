.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.ise.tacacs_server_sequence_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.ise.tacacs_server_sequence_info -- Information module for Tacacs Server Sequence
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.ise collection <https://galaxy.ansible.com/cisco/ise>`_ (version 1.0.2).

    To install it use: :code:`ansible-galaxy collection install cisco.ise`.

    To use it in a playbook, specify: :code:`cisco.ise.tacacs_server_sequence_info`.

.. version_added

.. versionadded:: 1.0.0 of cisco.ise

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Get all Tacacs Server Sequence.
- Get Tacacs Server Sequence by id.
- Get Tacacs Server Sequence by name.

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
                                            <div>Name path parameter.</div>
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
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   `Tacacs Server Sequence reference <https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary>`_
       Complete reference of the Tacacs Server Sequence object model.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get all Tacacs Server Sequence
      cisco.ise.tacacs_server_sequence_info:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
        page: 1
        size: 20
      register: result

    - name: Get Tacacs Server Sequence by id
      cisco.ise.tacacs_server_sequence_info:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
        id: string
      register: result

    - name: Get Tacacs Server Sequence by name
      cisco.ise.tacacs_server_sequence_info:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
        name: string
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
      &quot;serverList&quot;: &quot;string&quot;,
      &quot;localAccounting&quot;: true,
      &quot;remoteAccounting&quot;: true,
      &quot;prefixStrip&quot;: true,
      &quot;prefixDelimiter&quot;: &quot;string&quot;,
      &quot;suffixStrip&quot;: true,
      &quot;suffixDelimiter&quot;: &quot;string&quot;,
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

