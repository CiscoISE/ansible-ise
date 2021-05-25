.. _sg_acl:

======
sg_acl
======

Documentation
=============

Resource module for Sg Acl

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Sg Acl.


Options
-------
::

  options:
    aclcontent:
      description: Sg Acl's aclcontent.
      type: str
    description:
      description: Sg Acl's description.
      type: str
    id:
      description: Sg Acl's id.
      type: str
    ipVersion:
      description: Sg Acl's ipVersion.
      type: str
    name:
      description: Sg Acl's name.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.sg_acl
  - description: Complete reference of the Sg Acl object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Sg Acl reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.sg_acl:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      aclcontent: Permit IP
      description: description
      id: id
      ipVersion: IPV4
      name: name

  - name: Update by id
    cisco.ise.sg_acl:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      aclcontent: Permit IP
      description: description
      id: id
      ipVersion: IPV4
      name: name

  - name: Delete by id
    cisco.ise.sg_acl:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: absent
      id: string



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

    {}

Sample 2:

.. code-block:: json

    {}

Sample 3:

.. code-block:: json

    {}
