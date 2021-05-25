.. _radius_server_sequence:

======================
radius_server_sequence
======================

Documentation
=============

Resource module for Radius Server Sequence

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Radius Server Sequence.


Options
-------
::

  options:
    BeforeAcceptAttrManipulatorsList:
      description: Radius Server Sequence's BeforeAcceptAttrManipulatorsList.
      suboptions:
      - suboptions:
          action:
            description: Radius Server Sequence's action.
            type: str
          attributeName:
            description: Radius Server Sequence's attributeName.
            type: str
          changedVal:
            description: Radius Server Sequence's changedVal.
            type: str
          dictionaryName:
            description: Radius Server Sequence's dictionaryName.
            type: str
          value:
            description: Radius Server Sequence's value.
            type: str
        type: dict
      type: list
    OnRequestAttrManipulatorList:
      description: Radius Server Sequence's OnRequestAttrManipulatorList.
      suboptions:
      - suboptions:
          action:
            description: Radius Server Sequence's action.
            type: str
          attributeName:
            description: Radius Server Sequence's attributeName.
            type: str
          changedVal:
            description: Radius Server Sequence's changedVal.
            type: str
          dictionaryName:
            description: Radius Server Sequence's dictionaryName.
            type: str
          value:
            description: Radius Server Sequence's value.
            type: str
        type: dict
      type: list
    RadiusServerList:
      description: Radius Server Sequence's RadiusServerList.
      elements:
        type: str
      type: list
    continueAuthorzPolicy:
      description: ContinueAuthorzPolicy flag.
      type: bool
    description:
      description: Radius Server Sequence's description.
      type: str
    id:
      description: Radius Server Sequence's id.
      type: str
    localAccounting:
      description: LocalAccounting flag.
      type: bool
    name:
      description: Radius Server Sequence's name.
      type: str
    prefixSeparator:
      description: Radius Server Sequence's prefixSeparator.
      type: str
    remoteAccounting:
      description: RemoteAccounting flag.
      type: bool
    stripPrefix:
      description: StripPrefix flag.
      type: bool
    stripSuffix:
      description: StripSuffix flag.
      type: bool
    suffixSeparator:
      description: Radius Server Sequence's suffixSeparator.
      type: str
    useAttrSetBeforeAcc:
      description: UseAttrSetBeforeAcc flag.
      type: bool
    useAttrSetOnRequest:
      description: UseAttrSetOnRequest flag.
      type: bool
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.radius_server_sequence
  - description: Complete reference of the Radius Server Sequence object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Radius Server Sequence reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.radius_server_sequence:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      BeforeAcceptAttrManipulatorsList:
      - action: ADD
        attributeName: cisco-prev-hop-ip
        changedVal: test2
        dictionaryName: Cisco
        value: test1
      - action: UPDATE
        attributeName: Cisco:cisco-ppp-vj-slot-comp
        changedVal: '13'
        dictionaryName: Cisco
        value: '12'
      OnRequestAttrManipulatorList:
      - action: ADD
        attributeName: cisco-prev-hop-ip
        changedVal: test2
        dictionaryName: Cisco
        value: test1
      - action: UPDATE
        attributeName: Cisco:cisco-ppp-vj-slot-comp
        changedVal: '13'
        dictionaryName: Cisco
        value: '12'
      RadiusServerList:
      - externalRadiusServer1
      - externalRadiusServer2
      continueAuthorzPolicy: false
      description: description
      id: id
      localAccounting: false
      name: name
      prefixSeparator: \
      remoteAccounting: true
      stripPrefix: false
      stripSuffix: false
      suffixSeparator: '@'
      useAttrSetBeforeAcc: false
      useAttrSetOnRequest: false

  - name: Update by id
    cisco.ise.radius_server_sequence:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      BeforeAcceptAttrManipulatorsList:
      - action: ADD
        attributeName: cisco-prev-hop-ip
        changedVal: test2
        dictionaryName: Cisco
        value: test1
      - action: UPDATE
        attributeName: Cisco:cisco-ppp-vj-slot-comp
        changedVal: '13'
        dictionaryName: Cisco
        value: '12'
      OnRequestAttrManipulatorList:
      - action: ADD
        attributeName: cisco-prev-hop-ip
        changedVal: test2
        dictionaryName: Cisco
        value: test1
      - action: UPDATE
        attributeName: Cisco:cisco-ppp-vj-slot-comp
        changedVal: '13'
        dictionaryName: Cisco
        value: '12'
      RadiusServerList:
      - externalRadiusServer1
      - externalRadiusServer2
      continueAuthorzPolicy: false
      description: description
      id: id
      localAccounting: false
      name: name
      prefixSeparator: \
      remoteAccounting: true
      stripPrefix: false
      stripSuffix: false
      suffixSeparator: '@'
      useAttrSetBeforeAcc: false
      useAttrSetOnRequest: false

  - name: Delete by id
    cisco.ise.radius_server_sequence:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: absent
      id: string



Return
=======

ise_response
------------

- **Description**: A dictionary or list with the response returned by the Cisco ISE Python SDK
- **Returned**: always
- **Type**: complex

**Samples**

Sample 1:

.. code-block:: json

    {}

Sample 2:

.. code-block:: json

    {}

Sample 3:

.. code-block:: json

    {}
