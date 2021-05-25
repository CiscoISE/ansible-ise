.. _id_store_sequence:

=================
id_store_sequence
=================

Documentation
=============

Resource module for Id Store Sequence

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Id Store Sequence.


Options
-------
::

  options:
    description:
      description: Id Store Sequence's description.
      type: str
    id:
      description: Id Store Sequence's id.
      type: str
    name:
      description: Id Store Sequence's name.
      type: str
    parent:
      description: Id Store Sequence's parent.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.id_store_sequence
  - description: Complete reference of the Id Store Sequence object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Id Store Sequence reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.id_store_sequence:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: description
      id: id
      name: name
      parent: parent

  - name: Update by id
    cisco.ise.id_store_sequence:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: description
      id: id
      name: name
      parent: parent

  - name: Delete by id
    cisco.ise.id_store_sequence:
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
