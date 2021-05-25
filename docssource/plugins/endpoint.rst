.. _endpoint:

========
endpoint
========

Documentation
=============

Resource module for Endpoint

Requirements
------------
- ciscoisesdk


Description
-----------
- Manage operations create, update, delete of the resource Endpoint.


Options
-------
::

  options:
    customAttributes:
      suboptions:
        customAttributes:
          suboptions:
            key1:
              description: Endpoint's key1.
              type: str
            key2:
              description: Endpoint's key2.
              type: str
          type: dict
      type: dict
    description:
      description: Endpoint's description.
      type: str
    groupId:
      description: Endpoint's groupId.
      type: str
    id:
      description: Endpoint's id.
      type: str
    identityStore:
      description: Endpoint's identityStore.
      type: str
    identityStoreId:
      description: Endpoint's identityStoreId.
      type: str
    mac:
      description: Endpoint's mac.
      type: str
    mdmAttributes:
      suboptions:
        mdmComplianceStatus:
          description: MdmComplianceStatus flag.
          type: bool
        mdmEncrypted:
          description: MdmEncrypted flag.
          type: bool
        mdmEnrolled:
          description: MdmEnrolled flag.
          type: bool
        mdmIMEI:
          description: Endpoint's mdmIMEI.
          type: str
        mdmJailBroken:
          description: MdmJailBroken flag.
          type: bool
        mdmManufacturer:
          description: Endpoint's mdmManufacturer.
          type: str
        mdmModel:
          description: Endpoint's mdmModel.
          type: str
        mdmOS:
          description: Endpoint's mdmOS.
          type: str
        mdmPhoneNumber:
          description: Endpoint's mdmPhoneNumber.
          type: str
        mdmPinlock:
          description: MdmPinlock flag.
          type: bool
        mdmReachable:
          description: MdmReachable flag.
          type: bool
        mdmSerial:
          description: Endpoint's mdmSerial.
          type: str
        mdmServerName:
          description: Endpoint's mdmServerName.
          type: str
      type: dict
    name:
      description: Endpoint's name.
      type: str
    portalUser:
      description: Endpoint's portalUser.
      type: str
    profileId:
      description: Endpoint's profileId.
      type: str
    staticGroupAssignment:
      description: StaticGroupAssignment flag.
      type: bool
    staticProfileAssignment:
      description: StaticProfileAssignment flag.
      type: bool
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.endpoint
  - description: Complete reference of the Endpoint object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Endpoint reference
  version_added: 1.0.0


Examples
=========

::

  - name: Create
    cisco.ise.endpoint:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: MyEndpoint
      groupId: aa13bb40-8bff-11e6-996c-525400b48521
      mac: 11:22:33:44:55:66
      name: MyEndpoint
      staticGroupAssignment: true

  - name: Update by id
    cisco.ise.endpoint:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      state: present
      description: a new description
      groupId: 3a1b38d0-8c00-11e6-996c-525400b48521
      id: string

  - name: Delete by id
    cisco.ise.endpoint:
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
