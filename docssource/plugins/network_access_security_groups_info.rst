.. _network_access_security_groups_info:

===================================
network_access_security_groups_info
===================================

Documentation
=============

Information module for Network Access Security Groups

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Network Access Security Groups.


Options
-------
::

  options: null
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.network_access_security_groups
  - description: Complete reference of the Network Access Security Groups object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Access Security Groups reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Network Access Security Groups
    cisco.ise.network_access_security_groups_info:
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
      {
        "name": "string"
      }
    ]
