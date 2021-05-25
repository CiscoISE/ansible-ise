.. _endpoint_get_rejected_endpoints_info:

====================================
endpoint_get_rejected_endpoints_info
====================================

Documentation
=============

Information module for Endpoint Get Rejected Endpoints

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Endpoint Get Rejected Endpoints.


Options
-------
::

  options: null
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.endpoint_get_rejected_endpoints
  - description: Complete reference of the Endpoint Get Rejected Endpoints object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Endpoint Get Rejected Endpoints reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Endpoint Get Rejected Endpoints
    cisco.ise.endpoint_get_rejected_endpoints_info:
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
      "OperationResult": {
        "resultValue": [
          {
            "value": "string",
            "name": "string"
          }
        ]
      }
    }
