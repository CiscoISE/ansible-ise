.. _device_administration_dictionary_attributes_authorization_info:

==============================================================
device_administration_dictionary_attributes_authorization_info
==============================================================

Documentation
=============

Information module for Device Administration Dictionary Attributes Authorization

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Device Administration Dictionary Attributes Authorization.


Options
-------
::

  options: null
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.device_administration_dictionary_attributes_authorization
  - description: Complete reference of the Device Administration Dictionary Attributes
      Authorization object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Device Administration Dictionary Attributes Authorization reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Device Administration Dictionary Attributes Authorization
    cisco.ise.device_administration_dictionary_attributes_authorization_info:
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
        "id": "string",
        "directionType": "string",
        "name": "string",
        "description": "string",
        "internalName": "string",
        "dataType": "string",
        "dictionaryName": "string",
        "allowedValues": [
          {
            "key": "string",
            "value": "string",
            "isDefault": true
          }
        ]
      }
    ]
