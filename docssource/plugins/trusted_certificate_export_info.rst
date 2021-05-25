.. _trusted_certificate_export_info:

===============================
trusted_certificate_export_info
===============================

Documentation
=============

Information module for Trusted Certificate Export

Requirements
------------
- ciscoisesdk


Description
-----------
- Get Trusted Certificate Export by id.


Options
-------
::

  options:
    id:
      description:
      - Id path parameter. The ID of the Trusted Certificate to be exported.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.trusted_certificate_export
  - description: Complete reference of the Trusted Certificate Export object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Trusted Certificate Export reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get Trusted Certificate Export by id
    cisco.ise.trusted_certificate_export_info
      id: string
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

    "string"
