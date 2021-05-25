.. _network_access_identity_stores_info:

===================================
network_access_identity_stores_info
===================================

Documentation
=============

Information module for Network Access Identity Stores

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Network Access Identity Stores.


Options
-------
::

  options: null
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.network_access_identity_stores
  - description: Complete reference of the Network Access Identity Stores object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Access Identity Stores reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Network Access Identity Stores
    cisco.ise.network_access_identity_stores_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
    register: result



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

    [
      "string"
    ]
