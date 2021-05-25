.. _node_group_info:

===============
node_group_info
===============

Documentation
=============

Information module for Node Group

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Node Group.
- Get Node Group by name.


Options
-------
::

  options:
    node_group_name:
      description:
      - Node-group-name path parameter. ID of the existing node group.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.node_group
  - description: Complete reference of the Node Group object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Node Group reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Node Group
    cisco.ise.node_group_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
    register: result

  - name: Get Node Group by name
    cisco.ise.node_group_info
      node_group_name: string
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
      "name": "string",
      "description": "string",
      "mar-cache": {
        "enabled": true,
        "replication-timeout": 0,
        "replication-attempts": 0,
        "query-timeout": 0,
        "query-attempts": 0
      }
    }

Sample 2:

.. code-block:: json

    {
      "response": [
        {
          "name": "string",
          "description": "string",
          "mar-cache": {
            "enabled": true,
            "replication-timeout": 0,
            "replication-attempts": 0,
            "query-timeout": 0,
            "query-attempts": 0
          }
        }
      ]
    }
