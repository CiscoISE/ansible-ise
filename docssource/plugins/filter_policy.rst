.. _filter_policy:

=============
filter_policy
=============

Documentation
=============

Resource module for Filter Policy

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Filter Policy.


Options
-------
::

  options:
    domains:
      description: Filter Policy's domains.
      type: str
    id:
      description: Id path parameter.
      type: string
    sgt:
      description: Filter Policy's sgt.
      type: str
    subnet:
      description: Filter Policy's subnet.
      type: str
    vn:
      description: Filter Policy's vn.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.filter_policy
  - description: Complete reference of the Filter Policy object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Filter Policy reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.filter_policy:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      domains: Sxp Vpn Name
      sgt: sgt
      subnet: subnetAddress
      vn: virtualNetwork

  - name: Update by id
    cisco.ise.filter_policy:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      domains: Sxp Vpn Name
      id: string
      sgt: sgt
      subnet: subnetAddress
      vn: virtualNetwork

  - name: Delete by id
    cisco.ise.filter_policy:
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
