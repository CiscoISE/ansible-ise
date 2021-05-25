.. _device_administration_conditions_for_policy_set_info:

====================================================
device_administration_conditions_for_policy_set_info
====================================================

Documentation
=============

Information module for Device Administration Conditions For Policy Set

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Device Administration Conditions For Policy Set.


Options
-------
::

  options: null
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.device_administration_conditions_for_policy_set
  - description: Complete reference of the Device Administration Conditions For Policy
      Set object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Device Administration Conditions For Policy Set reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Device Administration Conditions For Policy Set
    cisco.ise.device_administration_conditions_for_policy_set_info:
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

    [
      {
        "conditionType": "string",
        "isNegate": true
      }
    ]
