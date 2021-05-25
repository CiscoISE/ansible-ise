.. _network_access_dictionary_info:

==============================
network_access_dictionary_info
==============================

Documentation
=============

Information module for Network Access Dictionary

Requirements
------------
- ciscoisesdk


Description
-----------
- Get Network Access Dictionary by name.


Options
-------
::

  options:
    name:
      description:
      - Name path parameter. The dictionary name.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.network_access_dictionary
  - description: Complete reference of the Network Access Dictionary object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Network Access Dictionary reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get Network Access Dictionary by name
    cisco.ise.network_access_dictionary_info
      name: string
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
      "name": "string",
      "description": "string",
      "version": "string",
      "dictionaryAttrType": "string"
    }
