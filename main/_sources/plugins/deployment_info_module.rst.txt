.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.cisco.ise.deployment_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

cisco.ise.deployment_info -- Information module for Deployment
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `cisco.ise collection <https://galaxy.ansible.com/cisco/ise>`_ (version 1.0.2).

    To install it use: :code:`ansible-galaxy collection install cisco.ise`.

    To use it in a playbook, specify: :code:`cisco.ise.deployment_info`.

.. version_added

.. versionadded:: 1.0.0 of cisco.ise

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Get all Deployment.

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
                    <div class="ansibleOptionAnchor" id="parameter-timeout"></div>
                    <b>timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>How long to wait for the server to send data before giving up.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso

See Also
--------

.. seealso::

   `Deployment reference <https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary>`_
       Complete reference of the Deployment object model.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get all Deployment
      cisco.ise.deployment_info:
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
      &quot;networkAccessInfo&quot;: {
        &quot;deploymentID&quot;: &quot;string&quot;,
        &quot;isCsnEnabled&quot;: true,
        &quot;nodeList&quot;: {
          &quot;nodeAndScope&quot;: [
            {}
          ]
        },
        &quot;sdaVNs&quot;: [],
        &quot;trustSecControl&quot;: &quot;string&quot;,
        &quot;radius3RdParty&quot;: []
      },
      &quot;profilerInfo&quot;: {
        &quot;deploymentID&quot;: &quot;string&quot;,
        &quot;nodeList&quot;: {
          &quot;node&quot;: [
            {
              &quot;onlineSubscriptionEnabled&quot;: true,
              &quot;lastAppliedFeedDateTime&quot;: &quot;string&quot;,
              &quot;scope&quot;: &quot;string&quot;,
              &quot;profiles&quot;: [
                {
                  &quot;profile&quot;: [],
                  &quot;customProfilesCount&quot;: 0,
                  &quot;endpointTypes&quot;: &quot;string&quot;,
                  &quot;totalProfilesCount&quot;: 0,
                  &quot;uniqueEndpointsCount&quot;: 0,
                  &quot;unknownEndpointsCount&quot;: 0,
                  &quot;totalEndpointsCount&quot;: 0,
                  &quot;unknownEndpointsPercentage&quot;: 0
                }
              ]
            }
          ]
        }
      },
      &quot;deploymentInfo&quot;: {
        &quot;deploymentID&quot;: &quot;string&quot;,
        &quot;versionHistoryInfo&quot;: [
          {
            &quot;opType&quot;: &quot;string&quot;,
            &quot;mainVersion&quot;: &quot;string&quot;,
            &quot;epochTime&quot;: 0
          }
        ],
        &quot;nodeList&quot;: {
          &quot;nodeAndNodeCountAndCountInfo&quot;: [
            {
              &quot;name&quot;: &quot;string&quot;,
              &quot;value&quot;: &quot;string&quot;,
              &quot;declaredType&quot;: &quot;string&quot;,
              &quot;scope&quot;: &quot;string&quot;,
              &quot;nil&quot;: true,
              &quot;globalScope&quot;: true,
              &quot;typeSubstituted&quot;: true
            }
          ]
        },
        &quot;fipsstatus&quot;: &quot;string&quot;
      },
      &quot;nadInfo&quot;: {
        &quot;nodeList&quot;: {
          &quot;nodeAndScope&quot;: [
            {}
          ]
        },
        &quot;nadcountInfo&quot;: {
          &quot;totalActiveNADCount&quot;: 0
        }
      },
      &quot;mdmInfo&quot;: {
        &quot;activeMdmServersCount&quot;: 0,
        &quot;activeDesktopMdmServersCount&quot;: 0,
        &quot;activeMobileMdmServersCount&quot;: 0,
        &quot;deploymentID&quot;: &quot;string&quot;,
        &quot;nodeList&quot;: {
          &quot;nodeAndScope&quot;: [
            {}
          ]
        }
      },
      &quot;licensesInfo&quot;: {
        &quot;deploymentID&quot;: &quot;string&quot;,
        &quot;nodeList&quot;: {
          &quot;node&quot;: [
            {}
          ]
        }
      },
      &quot;postureInfo&quot;: {
        &quot;content&quot;: [
          {
            &quot;name&quot;: &quot;string&quot;,
            &quot;value&quot;: &quot;string&quot;,
            &quot;declaredType&quot;: &quot;string&quot;,
            &quot;scope&quot;: &quot;string&quot;,
            &quot;nil&quot;: true,
            &quot;globalScope&quot;: true,
            &quot;typeSubstituted&quot;: true
          }
        ]
      },
      &quot;kongInfo&quot;: {
        &quot;deploymentID&quot;: &quot;string&quot;,
        &quot;nodeList&quot;: {
          &quot;node&quot;: [
            {
              &quot;sn&quot;: &quot;string&quot;,
              &quot;service&quot;: [
                {
                  &quot;serviceName&quot;: &quot;string&quot;,
                  &quot;route&quot;: [
                    {
                      &quot;routeName&quot;: &quot;string&quot;,
                      &quot;httpCount&quot;: {},
                      &quot;latencyCount&quot;: {},
                      &quot;latencySum&quot;: {}
                    }
                  ]
                }
              ]
            }
          ]
        }
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

