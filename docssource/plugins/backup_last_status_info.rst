.. _backup_last_status_info:

=======================
backup_last_status_info
=======================

Documentation
=============

Information module for Backup Last Status

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Backup Last Status.


Options
-------
::

  options: null
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.backup_last_status
  - description: Complete reference of the Backup Last Status object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Backup Last Status reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Backup Last Status
    cisco.ise.backup_last_status_info:
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

    {
      "response": {
        "repository": "string",
        "type": "string",
        "name": "string",
        "startDate": "string",
        "error": "string",
        "action": "string",
        "scheduled": "string",
        "status": "string",
        "message": "string",
        "justComplete": "string",
        "percentComplete": "string",
        "details": "string",
        "hostName": "string",
        "initiatedFrom": "string"
      },
      "version": "string"
    }
