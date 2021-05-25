.. _tacacs_profile:

==============
tacacs_profile
==============

Documentation
=============

Resource module for Tacacs Profile

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Tacacs Profile.


Options
-------
::

  options:
    description:
      description: Tacacs Profile's description.
      type: str
    id:
      description: Tacacs Profile's id.
      type: str
    name:
      description: Tacacs Profile's name.
      type: str
    sessionAttributes:
      suboptions:
        sessionAttributeList:
          description: Tacacs Profile's sessionAttributeList.
          suboptions:
          - suboptions:
              name:
                description: Tacacs Profile's name.
                type: str
              type:
                description: Tacacs Profile's type.
                type: str
              value:
                description: Tacacs Profile's value.
                type: str
            type: dict
          type: list
      type: dict
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.tacacs_profile
  - description: Complete reference of the Tacacs Profile object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Tacacs Profile reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.tacacs_profile:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: string
      id: string
      name: string
      sessionAttributes:
        sessionAttributeList:
        - name: string
          type: string
          value: string

  - name: Update by id
    cisco.ise.tacacs_profile:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: string
      id: string
      name: string
      sessionAttributes:
        sessionAttributeList:
        - name: string
          type: string
          value: string

  - name: Delete by id
    cisco.ise.tacacs_profile:
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
