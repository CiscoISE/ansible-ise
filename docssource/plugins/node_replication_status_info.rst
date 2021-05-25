.. _node_replication_status_info:

============================
node_replication_status_info
============================

Documentation
=============

Information module for Node Replication Status

Requirements
------------
- ciscoisesdk


Description
-----------
- Get Node Replication Status by id.


Options
-------
::

  options:
    node:
      description:
      - Node path parameter. ID of the existing node.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.node_replication_status
  - description: Complete reference of the Node Replication Status object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Node Replication Status reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get Node Replication Status by id
    cisco.ise.node_replication_status_info
      node: string
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
      "NodeStatus": "string"
    }
