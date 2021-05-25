.. _tacacs_server_sequence:

======================
tacacs_server_sequence
======================

Documentation
=============

Resource module for Tacacs Server Sequence

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Tacacs Server Sequence.


Options
-------
::

  options:
    id:
      description: Id path parameter.
      type: string
    localAccounting:
      description: LocalAccounting flag.
      type: bool
    name:
      description: Tacacs Server Sequence's name.
      type: str
    prefixDelimiter:
      description: Tacacs Server Sequence's prefixDelimiter.
      type: str
    prefixStrip:
      description: PrefixStrip flag.
      type: bool
    remoteAccounting:
      description: RemoteAccounting flag.
      type: bool
    serverList:
      description: Tacacs Server Sequence's serverList.
      type: str
    suffixDelimiter:
      description: Tacacs Server Sequence's suffixDelimiter.
      type: str
    suffixStrip:
      description: SuffixStrip flag.
      type: bool
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.tacacs_server_sequence
  - description: Complete reference of the Tacacs Server Sequence object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Tacacs Server Sequence reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.tacacs_server_sequence:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      localAccounting: true
      name: string
      prefixDelimiter: string
      prefixStrip: true
      remoteAccounting: true
      serverList: string
      suffixDelimiter: string
      suffixStrip: true

  - name: Update by id
    cisco.ise.tacacs_server_sequence:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      id: string
      localAccounting: true
      name: string
      prefixDelimiter: string
      prefixStrip: true
      remoteAccounting: true
      serverList: string
      suffixDelimiter: string
      suffixStrip: true

  - name: Delete by id
    cisco.ise.tacacs_server_sequence:
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
