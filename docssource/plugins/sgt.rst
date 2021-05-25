.. _sgt:

===
sgt
===

Documentation
=============

Resource module for Sgt

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Sgt.


Options
-------
::

  options:
    description:
      description: Sgt's description.
      type: str
    generationId:
      description: Sgt's generationId.
      type: str
    id:
      description: Id path parameter.
      type: string
    name:
      description: Sgt's name.
      type: str
    propogateToApic:
      description: PropogateToApic flag.
      type: bool
    value:
      description: Sgt's value.
      type: int
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.sgt
  - description: Complete reference of the Sgt object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Sgt reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.sgt:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: Printers
      generationId: '0'
      name: Printers
      propogateToApic: true
      value: 999

  - name: Update by id
    cisco.ise.sgt:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: Printers
      generationId: '0'
      id: string
      name: Printers
      propogateToApic: true
      value: 999

  - name: Delete by id
    cisco.ise.sgt:
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
