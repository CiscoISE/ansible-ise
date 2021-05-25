.. _anc_policy_bulk_monitor_status_info:

===================================
anc_policy_bulk_monitor_status_info
===================================

Documentation
=============

Information module for Anc Policy Bulk Monitor Status

Requirements
------------
- ciscoisesdk


Description
-----------
- Get Anc Policy Bulk Monitor Status by id.


Options
-------
::

  options:
    bulkid:
      description:
      - Bulkid path parameter.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.anc_policy_bulk_monitor_status
  - description: Complete reference of the Anc Policy Bulk Monitor Status object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Anc Policy Bulk Monitor Status reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get Anc Policy Bulk Monitor Status by id
    cisco.ise.anc_policy_bulk_monitor_status_info
      bulkid: string
    register: result



Return
=======

ise_response
------------

- **Description**: A dictionary or list with the response returned by the Cisco ISE Python SDK
- **Returned**: always
- **Type**: complex
