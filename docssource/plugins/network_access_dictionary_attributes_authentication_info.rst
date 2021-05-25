.. _network_access_dictionary_attributes_authentication_info:

========================================================
network_access_dictionary_attributes_authentication_info
========================================================

Documentation
=============

Information module for Network Access Dictionary Attributes Authentication

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Network Access Dictionary Attributes Authentication.


Options
-------
::

  options: null
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.network_access_dictionary_attributes_authentication
  - description: Complete reference of the Network Access Dictionary Attributes Authentication
      object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Access Dictionary Attributes Authentication reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Network Access Dictionary Attributes Authentication
    cisco.ise.network_access_dictionary_attributes_authentication_info:
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
