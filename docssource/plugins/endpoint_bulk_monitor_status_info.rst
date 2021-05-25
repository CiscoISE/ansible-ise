.. _endpoint_bulk_monitor_status_info:

=================================
endpoint_bulk_monitor_status_info
=================================

Documentation
=============

Information module for Endpoint Bulk Monitor Status

Requirements
------------
- ciscoisesdk


Description
-----------
- Get Endpoint Bulk Monitor Status by id.


Options
-------
::

  options:
    bulkid:
      description:
      - Bulkid path parameter.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.endpoint_bulk_monitor_status
  - description: Complete reference of the Endpoint Bulk Monitor Status object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Endpoint Bulk Monitor Status reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get Endpoint Bulk Monitor Status by id
    cisco.ise.endpoint_bulk_monitor_status_info
      bulkid: string
    register: result



Return
=======

ise_response
------------

- **Description**: A dictionary or list with the response returned by the Cisco ISE Python SDK
- **Returned**: always
- **Type**: complex
