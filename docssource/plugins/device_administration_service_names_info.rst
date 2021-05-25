.. _device_administration_service_names_info:

========================================
device_administration_service_names_info
========================================

Documentation
=============

Information module for Device Administration Service Names

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Device Administration Service Names.


Options
-------
::

  options: null
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.device_administration_service_names
  - description: Complete reference of the Device Administration Service Names object
      model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Device Administration Service Names reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Device Administration Service Names
    cisco.ise.device_administration_service_names_info:
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
