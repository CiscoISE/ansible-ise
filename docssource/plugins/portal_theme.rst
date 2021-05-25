.. _portal_theme:

============
portal_theme
============

Documentation
=============

Resource module for Portal Theme

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Portal Theme.


Options
-------
::

  options:
    id:
      description: Id path parameter.
      type: string
    name:
      description: Portal Theme's name.
      type: str
    themeData:
      description: Portal Theme's themeData.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.portal_theme
  - description: Complete reference of the Portal Theme object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Portal Theme reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.portal_theme:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      name: New Theme
      themeData: Base64 encoded string of CSS file

  - name: Update by id
    cisco.ise.portal_theme:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      id: 935e5e90-bd06-4cba-9465-e71c475bfe1d
      name: New Theme
      themeData: More Base64 encoded string of CSS file

  - name: Delete by id
    cisco.ise.portal_theme:
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
