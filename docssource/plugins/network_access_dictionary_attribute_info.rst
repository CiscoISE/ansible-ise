.. _network_access_dictionary_attribute_info:

========================================
network_access_dictionary_attribute_info
========================================

Documentation
=============

Information module for Network Access Dictionary Attribute

Requirements
------------
- ciscoisesdk


Description
-----------
- Get Network Access Dictionary Attribute by name.


Options
-------
::

  options:
    dictionaryName:
      description:
      - DictionaryName path parameter. The name of the dictionary the dictionary attribute
        belongs to.
      type: str
    name:
      description:
      - Name path parameter. The dictionary attribute name.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.network_access_dictionary_attribute
  - description: Complete reference of the Network Access Dictionary Attribute object
      model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Access Dictionary Attribute reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get Network Access Dictionary Attribute by name
    cisco.ise.network_access_dictionary_attribute_info
      name: string
      dictionaryName: string
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
