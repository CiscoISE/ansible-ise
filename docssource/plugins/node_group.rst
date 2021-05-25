.. _node_group:

==========
node_group
==========

Documentation
=============

Resource module for Node Group

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Node Group.


Options
-------
::

  options:
    description:
      description: Node Group's description.
      type: str
    mar_cache:
      suboptions:
        enabled:
          description: Enabled flag.
          type: bool
        query-attempts:
          description: Node Group's query-attempts.
          type: int
        query-timeout:
          description: Node Group's query-timeout.
          type: int
        replication-attempts:
          description: Node Group's replication-attempts.
          type: int
        replication-timeout:
          description: Node Group's replication-timeout.
          type: int
      type: dict
    node_group_name:
      description: Node-group-name path parameter. ID of the existing node group.
      type: string
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.node_group
  - description: Complete reference of the Node Group object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Node Group reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.node_group:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: string
      mar_cache:
        enabled: true
        query-attempts: 0
        query-timeout: 0
        replication-attempts: 0
        replication-timeout: 0

  - name: Update by name
    cisco.ise.node_group:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: string
      mar_cache:
        enabled: true
        query-attempts: 0
        query-timeout: 0
        replication-attempts: 0
        replication-timeout: 0
      node_group_name: string

  - name: Delete by name
    cisco.ise.node_group:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: absent
      node_group_name: string



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
      "code": 0,
      "message": "string",
      "rootCause": "string"
    }

Sample 2:

.. code-block:: json

    {
      "code": 0,
      "message": "string",
      "rootCause": "string"
    }

Sample 3:

.. code-block:: json

    {
      "code": 0,
      "message": "string",
      "rootCause": "string"
    }
