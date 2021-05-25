.. _network_access_service_name_info:

================================
network_access_service_name_info
================================

Documentation
=============

Information module for Network Access Service Name

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Network Access Service Name.


Options
-------
::

  options: null
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.network_access_service_name
  - description: Complete reference of the Network Access Service Name object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Access Service Name reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Network Access Service Name
    cisco.ise.network_access_service_name_info:
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
        "name": "string",
        "id": "string",
        "serviceType": "string",
        "isLocalAuthorization": true
      }
    ]
