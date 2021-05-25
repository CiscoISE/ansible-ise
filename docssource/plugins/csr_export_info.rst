.. _csr_export_info:

===============
csr_export_info
===============

Documentation
=============

Information module for Csr Export

Requirements
------------
- ciscoisesdk


Description
-----------
- Get Csr Export by id.


Options
-------
::

  options:
    hostname:
      description:
      - Hostname path parameter. The hostname to which the CSR belongs.
      type: str
    id:
      description:
      - Id path parameter. The ID of the CSR to be exported.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.csr_export
  - description: Complete reference of the Csr Export object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Csr Export reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get Csr Export by id
    cisco.ise.csr_export_info
      hostname: string
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
