.. _external_radius_server:

======================
external_radius_server
======================

Documentation
=============

Resource module for External Radius Server

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource External Radius Server.


Options
-------
::

  options:
    accountingPort:
      description: External Radius Server's accountingPort.
      type: int
    authenticationPort:
      description: External Radius Server's authenticationPort.
      type: int
    authenticatorKey:
      description: External Radius Server's authenticatorKey.
      type: str
    description:
      description: External Radius Server's description.
      type: str
    enableKeyWrap:
      description: EnableKeyWrap flag.
      type: bool
    encryptionKey:
      description: External Radius Server's encryptionKey.
      type: str
    hostIP:
      description: External Radius Server's hostIP.
      type: str
    id:
      description: External Radius Server's id.
      type: str
    keyInputFormat:
      description: External Radius Server's keyInputFormat.
      type: str
    name:
      description: External Radius Server's name.
      type: str
    proxyTimeout:
      description: External Radius Server's proxyTimeout.
      type: int
    retries:
      description: External Radius Server's retries.
      type: int
    sharedSecret:
      description: External Radius Server's sharedSecret.
      type: str
    timeout:
      description: External Radius Server's timeout.
      type: int
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.external_radius_server
  - description: Complete reference of the External Radius Server object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: External Radius Server reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.external_radius_server:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      accountingPort: 1813
      authenticationPort: 1812
      authenticatorKey: '20202020202020202020'
      description: example external radius server
      enableKeyWrap: true
      encryptionKey: '1616161616161616'
      hostIP: 1.1.1.1
      id: '123456789'
      keyInputFormat: ASCII
      name: externalRadiusServer1
      proxyTimeout: 300
      retries: 3
      sharedSecret: sharedSecret
      timeout: 5

  - name: Update by id
    cisco.ise.external_radius_server:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      accountingPort: 1813
      authenticationPort: 1812
      authenticatorKey: '20202020202020202020'
      description: example external radius server
      enableKeyWrap: true
      encryptionKey: '1616161616161616'
      hostIP: 1.1.1.1
      id: '123456789'
      keyInputFormat: ASCII
      name: externalRadiusServer1
      proxyTimeout: 300
      retries: 3
      sharedSecret: sharedSecret
      timeout: 5

  - name: Delete by id
    cisco.ise.external_radius_server:
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
