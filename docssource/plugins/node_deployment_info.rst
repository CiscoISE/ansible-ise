.. _node_deployment_info:

====================
node_deployment_info
====================

Documentation
=============

Information module for Node Deployment

Requirements
------------
- ciscoisesdk


Description
-----------
- Get all Node Deployment.
- Get Node Deployment by name.


Options
-------
::

  options:
    hostname:
      description:
      - Hostname path parameter. ID of the existing deployed node.
      type: str
  seealso:
  - module: cisco.ise.plugins.module_utils.definitions.node_deployment
  - description: Complete reference of the Node Deployment object model.
    link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
    name: Node Deployment reference
  version_added: 1.0.0


Examples
=========

::

  - name: Get all Node Deployment
    cisco.ise.node_deployment_info:
      ise_hostname: "{{ise_hostname}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
    register: result

  - name: Get Node Deployment by name
    cisco.ise.node_deployment_info
      hostname: string
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
      "response": {
        "hostname": "string",
        "fqdn": "string",
        "ipAddress": "string",
        "nodeType": "string",
        "administration": {
          "isEnabled": true,
          "role": "string"
        },
        "generalSettings": {
          "monitoring": {
            "isEnabled": true,
            "role": "string",
            "otherMonitoringNode": "string",
            "isMntDedicated": true,
            "policyservice": {
              "enabled": true,
              "sessionService": {
                "isEnabled": true,
                "nodegroup": "string"
              },
              "enableProfilingService": true,
              "enableNACService": true,
              "sxpservice": {
                "isEnabled": true,
                "userInterface": "string"
              },
              "enableDeviceAdminService": true,
              "enablePassiveIdentityService": true
            },
            "enablePXGrid": true
          }
        },
        "profilingConfiguration": {
          "netflow": {
            "enabled": true,
            "interface": "string",
            "port": {},
            "description": "string"
          },
          "dhcp": {
            "enabled": true,
            "interface": "string",
            "port": {},
            "description": "string"
          },
          "dhcpSpan": {
            "enabled": true,
            "interface": "string",
            "description": "string"
          },
          "http": {
            "enabled": true,
            "interface": "string",
            "description": "string"
          },
          "radius": {
            "enabled": true,
            "description": "string"
          },
          "nmap": {
            "enabled": true,
            "description": "string"
          },
          "dns": {
            "enabled": true,
            "description": "string"
          },
          "snmpQuery": {
            "enabled": true,
            "description": "string",
            "retries": 0,
            "timeout": 0,
            "eventTimeout": 0
          },
          "snmpTrap": {
            "linkTrapQuery": true,
            "macTrapQuery": true,
            "interface": "string",
            "port": {},
            "description": "string"
          },
          "activeDirectory": {
            "enabled": true,
            "daysBeforeRescan": 0,
            "description": "string"
          },
          "pxgrid": {
            "enabled": true,
            "description": "string"
          }
        }
      }
    }

Sample 2:

.. code-block:: json

    {
      "response": [
        {
          "hostname": "string",
          "personaType": [
            "string"
          ],
          "roles": [
            "string"
          ],
          "services": [
            "string"
          ],
          "nodeStatus": "string"
        }
      ]
    }
