.. _downloadable_acl:

================
downloadable_acl
================

Documentation
=============

Resource module for Downloadable Acl

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Downloadable Acl.


Options
-------
::

  options:
    dacl:
      description: Downloadable Acl's dacl.
      type: str
    daclType:
      description: Downloadable Acl's daclType.
      type: str
    description:
      description: Downloadable Acl's description.
      type: str
    id:
      description: Id path parameter.
      type: string
    name:
      description: Downloadable Acl's name.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.downloadable_acl
  - description: Complete reference of the Downloadable Acl object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Downloadable Acl reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.downloadable_acl:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      dacl: permit ip any any
      daclType: IPV4
      description: MyDACL
      name: MyDACL6

  - name: Update by id
    cisco.ise.downloadable_acl:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      dacl: deny ip any any
      daclType: IPV4
      description: MyDACL6
      id: string
      name: MyDACL6

  - name: Delete by id
    cisco.ise.downloadable_acl:
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
