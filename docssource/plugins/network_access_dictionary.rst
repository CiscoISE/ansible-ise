.. _network_access_dictionary:

=========================
network_access_dictionary
=========================

Documentation
=============

Resource module for Network Access Dictionary

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Network Access Dictionary.


Options
-------
::

  options:
    description:
      description: The description of the Dictionary.
      type: str
    dictionaryAttrType:
      description: The dictionary attribute type.
      type: str
    id:
      description: Identifier for the dictionary.
      type: str
    name:
      description: The dictionary name.
      type: str
    version:
      description: The dictionary version.
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

  - name: Create
    cisco.ise.network_access_dictionary:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: string
      dictionaryAttrType: string
      id: string
      name: string
      version: string

  - name: Update by name
    cisco.ise.network_access_dictionary:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: string
      dictionaryAttrType: string
      id: string
      name: string
      version: string

  - name: Delete by name
    cisco.ise.network_access_dictionary:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: absent
      name: string



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

Sample 2:

.. code-block:: json

    {
      "id": "string",
      "name": "string",
      "description": "string",
      "version": "string",
      "dictionaryAttrType": "string"
    }

Sample 3:

.. code-block:: json

    {
      "id": "string",
      "name": "string",
      "description": "string",
      "version": "string",
      "dictionaryAttrType": "string"
    }
