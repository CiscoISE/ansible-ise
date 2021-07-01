#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: deployment_info
short_description: Information module for Deployment
description:
- Get all Deployment.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.deployment
# Reference by Internet resource
- name: Deployment reference
  description: Complete reference of the Deployment object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Deployment
  cisco.ise.deployment_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "networkAccessInfo": {
        "deploymentID": "string",
        "nodeList": {
          "nodeAndScope": [
            {
              "content": [
                {
                  "name": "string",
                  "declaredType": "string",
                  "scope": "string",
                  "value": {
                    "ndghierarchyMap": "string",
                    "ndgheierarchyNADMap": "string",
                    "policyLineCount": 0,
                    "localIdentityNonAdminUserCount": 0,
                    "restIDInfo": [
                      {
                        "restIDType": [
                          "string"
                        ],
                        "restidcount": 0
                      }
                    ],
                    "odbcInfo": [
                      {
                        "odbctype": [
                          "string"
                        ],
                        "odbccount": 0
                      }
                    ],
                    "rsaidstoreCount": 0,
                    "radiusidstoreCount": 0,
                    "adauthStoreCount": 0,
                    "ldapidstoreCount": 0,
                    "activeVLANCount": 0,
                    "activedACLCount": 0
                  },
                  "nil": true,
                  "globalScope": true,
                  "typeSubstituted": true
                }
              ]
            }
          ]
        },
        "sdaVNs": [
          "string"
        ],
        "trustSecControl": "string",
        "radius3RdParty": [
          "string"
        ]
      },
      "profilerInfo": {
        "deploymentID": "string",
        "nodeList": {
          "node": [
            {
              "profiles": {
                "profile": [
                  "string"
                ],
                "customProfilesCount": 0,
                "endpointTypes": "string",
                "totalProfilesCount": 0,
                "uniqueEndpointsCount": 0,
                "unknownEndpointsCount": 0,
                "totalEndpointsCount": 0,
                "unknownEndpointsPercentage": 0
              },
              "onlineSubscriptionEnabled": true,
              "lastAppliedFeedDateTime": "string",
              "scope": "string"
            }
          ]
        }
      },
      "deploymentInfo": {
        "deploymentID": "string",
        "nodeList": {
          "nodeAndNodeCountAndCountInfo": [
            {
              "name": "string",
              "declaredType": "string",
              "scope": "string",
              "value": {
                "content": [
                  {
                    "name": "string",
                    "declaredType": "string",
                    "scope": "string",
                    "value": {
                      "fromDate": "string",
                      "toDate": "string",
                      "total": "string",
                      "free": "string",
                      "percent": "string",
                      "fileSystem": [
                        {
                          "name": "string",
                          "total": "string",
                          "used": "string",
                          "available": "string",
                          "percent": "string",
                          "mountPoint": "string"
                        }
                      ],
                      "loadAvgOne": "string",
                      "loadAvgFive": "string",
                      "loadAvgFifteen": "string",
                      "content": [
                        {
                          "name": "string",
                          "declaredType": "string",
                          "scope": "string",
                          "value": true,
                          "nil": true,
                          "globalScope": true,
                          "typeSubstituted": true
                        }
                      ]
                    },
                    "nil": true,
                    "globalScope": true,
                    "typeSubstituted": true
                  }
                ],
                "fromDate": "string",
                "toDate": "string",
                "currentPostureEndptCount": 0,
                "currentGuestUserCount": 0,
                "currentMDMEndPtCount": 0,
                "currentPxGridClientCount": 0
              },
              "nil": true,
              "globalScope": true,
              "typeSubstituted": true
            }
          ]
        },
        "fipsstatus": "string"
      },
      "nadInfo": {
        "deploymentID": "string",
        "nodeList": {
          "nodeAndScope": [
            {
              "content": [
                {
                  "name": "string",
                  "declaredType": "string",
                  "scope": "string",
                  "value": {
                    "name": "string",
                    "isCiscoProvided": true,
                    "isDefProfile": true,
                    "isTacacsSupported": true,
                    "isRadiusSupported": true,
                    "isTrustSecSupported": true,
                    "activeNADCount": 0,
                    "totalNADCount": 0
                  },
                  "nil": true,
                  "globalScope": true,
                  "typeSubstituted": true
                }
              ]
            }
          ]
        },
        "nadcountInfo": {
          "totalActiveNADCount": 0
        }
      },
      "mdmInfo": {
        "activeMdmServersCount": "string",
        "activeDesktopMdmServersCount": "string",
        "activeMobileMdmServersCount": "string",
        "deploymentID": "string",
        "nodeList": {
          "nodeAndScope": [
            {
              "content": [
                "string"
              ]
            }
          ]
        }
      },
      "licensesInfo": {
        "deploymentID": "string",
        "nodeList": {
          "nodeAndScope": [
            {
              "content": [
                {
                  "name": "string",
                  "declaredType": "string",
                  "scope": "string",
                  "value": {
                    "serviceTypes": "string",
                    "count": 0,
                    "remainingDays": 0,
                    "fileName": "string",
                    "isExpired": true,
                    "isEvaluation": true,
                    "isWiredEnabled": true,
                    "term": 0,
                    "primaryUDI": "string",
                    "secondaryUDI": "string"
                  },
                  "nil": true,
                  "globalScope": true,
                  "typeSubstituted": true
                }
              ]
            }
          ]
        }
      },
      "postureInfo": {
        "content": [
          {
            "name": "string",
            "declaredType": "string",
            "scope": "string",
            "value": 0,
            "nil": true,
            "globalScope": true,
            "typeSubstituted": true
          }
        ]
      },
      "kongInfo": {
        "deploymentID": "string",
        "nodeList": {
          "node": [
            "string"
          ]
        }
      }
    }
"""
