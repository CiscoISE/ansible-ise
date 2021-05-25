.. _rest_id_store:

=============
rest_id_store
=============

Documentation
=============

Resource module for Rest Id Store

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Rest Id Store.


Options
-------
::

  options:
    description:
      description: Rest Id Store's description.
      type: str
    ersRestIDStoreAttributes:
      suboptions:
        headers:
          description: Rest Id Store's headers.
          suboptions:
          - suboptions:
              key:
                description: Rest Id Store's key.
                type: str
              value:
                description: Rest Id Store's value.
                type: str
            type: dict
          type: list
        predefined:
          description: Rest Id Store's predefined.
          type: str
        rootUrl:
          description: Rest Id Store's rootUrl.
          type: str
        usernameSuffix:
          description: Rest Id Store's usernameSuffix.
          type: str
      type: dict
    id:
      description: Id path parameter.
      type: string
    name:
      description: Rest Id Store's name.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.rest_id_store
  - description: Complete reference of the Rest Id Store object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Rest Id Store reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.rest_id_store:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: '{{description}}'
      ersRestIDStoreAttributes:
        headers:
        - key: clientID
          value: '{{clientID}}'
        - key: clientSecret
          value: '{{clientSecret}}'
        - key: tenantID
          value: '{{tenantID}}'
        predefined: Azure
        rootUrl: http://169.254.6.2:9601/azure
        usernameSuffix: '{{usernameSuffix}}'
      name: '{{name}}'

  - name: Update by id
    cisco.ise.rest_id_store:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: my new description
      id: '{{id}}'
      name: ISE_AzureAD_ROPC

  - name: Delete by id
    cisco.ise.rest_id_store:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: absent
      id: string

  - name: Update by name
    cisco.ise.rest_id_store:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: my new description
      name: string

  - name: Delete by name
    cisco.ise.rest_id_store:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: absent
      name: string



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
      "ERSResponse": {
        "operation": "string",
        "messages": [
          {
            "title": "string",
            "type": "string",
            "code": "string"
          }
        ],
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    }

Sample 3:

.. code-block:: json

    {}

Sample 4:

.. code-block:: json

    {
      "ERSResponse": {
        "operation": "string",
        "messages": [
          {
            "title": "string",
            "type": "string",
            "code": "string"
          }
        ],
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    }

Sample 5:

.. code-block:: json

    {}
