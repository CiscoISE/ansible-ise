.. _pan_ha_info:

===========
pan_ha_info
===========

Documentation
=============

Information module for Pan Ha

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Pan Ha.


Options
-------
::

  options: null
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.pan_ha
  - description: Complete reference of the Pan Ha object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Pan Ha reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Pan Ha
    cisco.ise.pan_ha_info:
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
      "response": [
        {
          "isEnabled": true,
          "primaryHealthCheckNode": "string",
          "secondaryHealthCheckNode": "string",
          "pollingInterval": 0,
          "failedAttempts": 0
        }
      ]
    }
