.. _anc_policy:

==========
anc_policy
==========

Documentation
=============

Resource module for Anc Policy

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Anc Policy.


Options
-------
::

  options:
    actions:
      description: Anc Policy's actions.
      elements:
        type: str
      type: list
    id:
      description: Id path parameter.
      type: string
    name:
      description: Anc Policy's name.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.anc_policy
  - description: Complete reference of the Anc Policy object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Anc Policy reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.anc_policy:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      actions:
      - QUARANTINE
      name: policy1

  - name: Update by id
    cisco.ise.anc_policy:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      actions:
      - QUARANTINE
      id: string
      name: policy1

  - name: Delete by id
    cisco.ise.anc_policy:
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

    {
      "UpdatedFieldsList": {
        "updatedField": [
          {
            "field": "string",
            "oldValue": "string",
            "newValue": "string"
          }
        ]
      }
    }

Sample 3:

.. code-block:: json

    {}
