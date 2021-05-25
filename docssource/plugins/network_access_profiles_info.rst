.. _network_access_profiles_info:

============================
network_access_profiles_info
============================

Documentation
=============

Information module for Network Access Profiles

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Network Access Profiles.


Options
-------
::

  options: null
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.network_access_profiles
  - description: Complete reference of the Network Access Profiles object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Access Profiles reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Network Access Profiles
    cisco.ise.network_access_profiles_info:
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
