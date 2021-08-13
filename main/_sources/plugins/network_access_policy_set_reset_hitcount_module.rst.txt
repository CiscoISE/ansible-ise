.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.ise.network_access_policy_set_reset_hitcount_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.ise.network_access_policy_set_reset_hitcount -- Resource module for Network Access Policy Set Reset Hitcount
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.ise collection <https://galaxy.ansible.com/cisco/ise>`_ (version 1.0.2).

    To install it use: :code:`ansible-galaxy collection install cisco.ise`.

    To use it in a playbook, specify: :code:`cisco.ise.network_access_policy_set_reset_hitcount`.

.. version_added

.. versionadded:: 1.0.0 of cisco.ise

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Manage operation create of the resource Network Access Policy Set Reset Hitcount.

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

   `Network Access Policy Set Reset Hitcount reference <https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary>`_
       Complete reference of the Network Access Policy Set Reset Hitcount object model.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create
      cisco.ise.network_access_policy_set_reset_hitcount:
        ise_hostname: "{{ise_hostname}}"
        ise_username: "{{ise_username}}"
        ise_password: "{{ise_password}}"
        ise_verify: "{{ise_verify}}"





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
      &quot;message&quot;: &quot;string&quot;
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

