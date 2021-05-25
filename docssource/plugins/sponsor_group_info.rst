.. _sponsor_group_info:

==================
sponsor_group_info
==================

Documentation
=============

Information module for Sponsor Group

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Sponsor Group.
- Get Sponsor Group by id.


Options
-------
::

  options:
    filter:
      description:
      - Filter query parameter. <br/> **Simple filtering** should be available through
        the filter query string parameter. The structure of a filter is a triplet of
        field operator and value separated with dots. More than one filter can be sent.
        The logical operator common to ALL filter criteria will be by default AND, and
        can be changed by using the "filterType=or" query string parameter. Each resource
        Data model description should specify if an attribute is a filtered field. <br/>
        Operator | Description <br/> ------------|----------------- <br/> EQ | Equals
        <br/> NEQ | Not Equals <br/> GT | Greater Than <br/> LT | Less Then <br/> STARTSW
        | Starts With <br/> NSTARTSW | Not Starts With <br/> ENDSW | Ends With <br/>
        NENDSW | Not Ends With <br/> CONTAINS | Contains <br/> NCONTAINS | Not Contains
        <br/>.
      type: list
    filterType:
      description:
      - FilterType query parameter. The logical operator common to ALL filter criteria
        will be by default AND, and can be changed by using the parameter.
      type: str
    id:
      description:
      - Id path parameter.
      type: str
    page:
      description:
      - Page query parameter. Page number.
      type: int
    size:
      description:
      - Size query parameter. Number of objects returned per page.
      type: int
    sortasc:
      description:
      - Sortasc query parameter. Sort asc.
      type: str
    sortdec:
      description:
      - Sortdec query parameter. Sort desc.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.sponsor_group
  - description: Complete reference of the Sponsor Group object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Sponsor Group reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Sponsor Group
    cisco.ise.sponsor_group_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
      filter: []
      filterType: AND
      sortasc: asc
      sortdec: string
    register: result

  - name: Get Sponsor Group by id
    cisco.ise.sponsor_group_info
      id: string
    register: result



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

    {
      "SponsorGroup": {
        "id": "string",
        "name": "string",
        "description": "string",
        "isEnabled": true,
        "isDefaultGroup": true,
        "memberGroups": [
          "string"
        ],
        "guestTypes": [
          "string"
        ],
        "locations": [
          "string"
        ],
        "autoNotification": true,
        "createPermissions": {
          "canImportMultipleAccounts": true,
          "importBatchSizeLimit": 0,
          "canCreateRandomAccounts": true,
          "randomBatchSizeLimit": 0,
          "canSpecifyUsernamePrefix": true,
          "canSetFutureStartDate": true,
          "startDateFutureLimitDays": 0
        },
        "managePermission": "string",
        "otherPermissions": {
          "canUpdateGuestContactInfo": true,
          "canViewGuestPasswords": true,
          "canSendSmsNotifications": true,
          "canResetGuestPasswords": true,
          "canExtendGuestAccounts": true,
          "canDeleteGuestAccounts": true,
          "canSuspendGuestAccounts": true,
          "requireSuspensionReason": true,
          "canReinstateSuspendedAccounts": true,
          "canApproveSelfregGuests": true,
          "limitApprovalToSponsorsGuests": true,
          "canAccessViaRest": true
        },
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    }

Sample 2:

.. code-block:: json

    {
      "SearchResult": {
        "total": 0,
        "resources": [
          {
            "id": "string",
            "name": "string",
            "description": "string",
            "link": {
              "rel": "string",
              "href": "string",
              "type": "string"
            }
          }
        ]
      }
    }
