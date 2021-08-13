.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.ise.aci_settings_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.ise.aci_settings_info -- Information module for Aci Settings
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.ise collection <https://galaxy.ansible.com/cisco/ise>`_ (version 1.0.2).

    To install it use: :code:`ansible-galaxy collection install cisco.ise`.

    To use it in a playbook, specify: :code:`cisco.ise.aci_settings_info`.

.. version_added

.. versionadded:: 1.0.0 of cisco.ise

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Get all Aci Settings.

.. note::
    This module has a corresponding :ref:`action plugin <action_plugins>`.

.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- ciscoisesdk


.. Options


.. Notes


.. Seealso

See Also
--------

.. seealso::

   `Aci Settings reference <https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary>`_
       Complete reference of the Aci Settings object model.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get all Aci Settings
      cisco.ise.aci_settings_info:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"
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
      &quot;enableAci&quot;: true,
      &quot;ipAddressHostName&quot;: &quot;string&quot;,
      &quot;adminName&quot;: &quot;string&quot;,
      &quot;adminPassword&quot;: &quot;string&quot;,
      &quot;aciipaddress&quot;: &quot;string&quot;,
      &quot;aciuserName&quot;: &quot;string&quot;,
      &quot;acipassword&quot;: &quot;string&quot;,
      &quot;tenantName&quot;: &quot;string&quot;,
      &quot;l3RouteNetwork&quot;: &quot;string&quot;,
      &quot;suffixToEpg&quot;: &quot;string&quot;,
      &quot;suffixToSgt&quot;: &quot;string&quot;,
      &quot;allSxpDomain&quot;: true,
      &quot;specificSxpDomain&quot;: true,
      &quot;specifixSxpDomainList&quot;: [
        &quot;string&quot;
      ],
      &quot;enableDataPlane&quot;: true,
      &quot;untaggedPacketIepgName&quot;: &quot;string&quot;,
      &quot;defaultSgtName&quot;: &quot;string&quot;,
      &quot;enableElementsLimit&quot;: true,
      &quot;maxNumIepgFromAci&quot;: 0,
      &quot;maxNumSgtToAci&quot;: 0,
      &quot;aci50&quot;: true,
      &quot;aci51&quot;: true
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

