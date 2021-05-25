.. _allowed_protocols_info:

======================
allowed_protocols_info
======================

Documentation
=============

Information module for Allowed Protocols

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Allowed Protocols.
- Get Allowed Protocols by id.
- Get Allowed Protocols by name.


Options
-------
::

  options:
    id:
      description:
      - Id path parameter.
      type: str
    name:
      description:
      - Name path parameter.
      type: str
    page:
      description:
      - Page query parameter. Page number.
      type: int
    size:
      description:
      - Size query parameter. Number of objects returned per page.
      type: int
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.allowed_protocols
  - description: Complete reference of the Allowed Protocols object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Allowed Protocols reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Allowed Protocols
    cisco.ise.allowed_protocols_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      page: 1
      size: 20
    register: result

  - name: Get Allowed Protocols by id
    cisco.ise.allowed_protocols_info
      id: string
    register: result

  - name: Get Allowed Protocols by name
    cisco.ise.allowed_protocols_info
      name: string
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
      "AllowedProtocols": {
        "name": "string",
        "description": "string",
        "eapTls": {
          "allowEapTlsAuthOfExpiredCerts": true,
          "eapTlsEnableStatelessSessionResume": true
        },
        "peap": {
          "allowPeapEapMsChapV2": true,
          "allowPeapEapMsChapV2PwdChange": true,
          "allowPeapEapMsChapV2PwdChangeRetries": 0,
          "allowPeapEapGtc": true,
          "allowPeapEapTls": true,
          "allowPeapEapTlsAuthOfExpiredCerts": true,
          "requireCryptobinding": true,
          "allowPeapV0": true
        },
        "eapFast": {
          "allowEapFastEapMsChapV2": true,
          "allowEapFastEapMsChapV2PwdChange": true,
          "allowEapFastEapMsChapV2PwdChangeRetries": 0,
          "allowEapFastEapGtc": true,
          "allowEapFastEapGtcPwdChange": true,
          "allowEapFastEapGtcPwdChangeRetries": 0,
          "allowEapFastEapTls": true,
          "allowEapFastEapTlsAuthOfExpiredCerts": true,
          "eapFastUsePacs": true,
          "eapFastUsePacsTunnelPacTtl": 0,
          "eapFastUsePacsTunnelPacTtlUnits": "string",
          "eapFastUsePacsUseProactivePacUpdatePrecentage": 0,
          "eapFastUsePacsAllowAnonymProvisioning": true,
          "eapFastUsePacsAllowAuthenProvisioning": true,
          "eapFastUsePacsAllowMachineAuthentication": true,
          "eapFastUsePacsStatelessSessionResume": true,
          "eapFastEnableEAPChaining": true
        },
        "eapTtls": {
          "eapTtlsPapAscii": true,
          "eapTtlsChap": true,
          "eapTtlsMsChapV1": true,
          "eapTtlsMsChapV2": true,
          "eapTtlsEapMd5": true,
          "eapTtlsEapMsChapV2": true,
          "eapTtlsEapMsChapV2PwdChange": true,
          "eapTtlsEapMsChapV2PwdChangeRetries": 0
        },
        "teap": {
          "allowTeapEapMsChapV2": true,
          "allowTeapEapMsChapV2PwdChange": true,
          "allowTeapEapMsChapV2PwdChangeRetries": 0,
          "allowTeapEapTls": true,
          "allowTeapEapTlsAuthOfExpiredCerts": true,
          "acceptClientCertDuringTunnelEst": true,
          "requestBasicPwdAuth": true,
          "enableEapChaining": true
        },
        "processHostLookup": true,
        "allowPapAscii": true,
        "allowChap": true,
        "allowMsChapV1": true,
        "allowMsChapV2": true,
        "allowEapMd5": true,
        "allowLeap": true,
        "allowEapTls": true,
        "allowEapTtls": true,
        "allowEapFast": true,
        "allowPeap": true,
        "allowTeap": true,
        "allowPreferredEapProtocol": true,
        "preferredEapProtocol": "string",
        "eapTlsLBit": true,
        "allowWeakCiphersForEap": true,
        "requireMessageAuth": true
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
        ],
        "nextPage": {
          "rel": "string",
          "href": "string",
          "type": "string"
        },
        "previousPage": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    }
