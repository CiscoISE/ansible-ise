.. _tacacs_external_servers:

=======================
tacacs_external_servers
=======================

Documentation
=============

Resource module for Tacacs External Servers

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Tacacs External Servers.


Options
-------
::

  options:
    connectionPort:
      description: Tacacs External Servers's connectionPort.
      type: int
    description:
      description: Tacacs External Servers's description.
      type: str
    hostIP:
      description: Tacacs External Servers's hostIP.
      type: str
    id:
      description: Id path parameter.
      type: string
    name:
      description: Tacacs External Servers's name.
      type: str
    sharedSecret:
      description: Tacacs External Servers's sharedSecret.
      type: str
    singleConnect:
      description: SingleConnect flag.
      type: bool
    timeout:
      description: Tacacs External Servers's timeout.
      type: int
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.tacacs_external_servers
  - description: Complete reference of the Tacacs External Servers object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Tacacs External Servers reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.tacacs_external_servers:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      connectionPort: 0
      description: string
      hostIP: string
      name: string
      sharedSecret: string
      singleConnect: true
      timeout: 0

  - name: Update by id
    cisco.ise.tacacs_external_servers:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      connectionPort: 0
      description: string
      hostIP: string
      id: string
      name: string
      sharedSecret: string
      singleConnect: true
      timeout: 0

  - name: Delete by id
    cisco.ise.tacacs_external_servers:
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
