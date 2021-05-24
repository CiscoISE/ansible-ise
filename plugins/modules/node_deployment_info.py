#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: node_deployment_info
short_description: Information module for Node Deployment
description:
- Get all Node Deployment.
- Get Node Deployment by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  hostname:
    description:
    - Hostname path parameter. ID of the existing deployed node.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.node_deployment
# Reference by Internet resource
- name: Node Deployment reference
  description: Complete reference of the Node Deployment object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
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

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'response': {'hostname': 'string', 'fqdn': 'string', 'ipAddress': 'string', 'nodeType': 'string', 'administration': {'isEnabled': True, 'role': 'string'}, 'generalSettings': {'monitoring': {'isEnabled': True, 'role': 'string', 'otherMonitoringNode': 'string', 'isMntDedicated': True, 'policyservice': {'enabled': True, 'sessionService': {'isEnabled': True, 'nodegroup': 'string'}, 'enableProfilingService': True, 'enableNACService': True, 'sxpservice': {'isEnabled': True, 'userInterface': 'string'}, 'enableDeviceAdminService': True, 'enablePassiveIdentityService': True}, 'enablePXGrid': True}}, 'profilingConfiguration': {'netflow': {'enabled': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'dhcp': {'enabled': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'dhcpSpan': {'enabled': True, 'interface': 'string', 'description': 'string'}, 'http': {'enabled': True, 'interface': 'string', 'description': 'string'}, 'radius': {'enabled': True, 'description': 'string'}, 'nmap': {'enabled': True, 'description': 'string'}, 'dns': {'enabled': True, 'description': 'string'}, 'snmpQuery': {'enabled': True, 'description': 'string', 'retries': 0, 'timeout': 0, 'eventTimeout': 0}, 'snmpTrap': {'linkTrapQuery': True, 'macTrapQuery': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'activeDirectory': {'enabled': True, 'daysBeforeRescan': 0, 'description': 'string'}, 'pxgrid': {'enabled': True, 'description': 'string'}}}}
  - {'response': [{'hostname': 'string', 'personaType': ['string'], 'roles': ['string'], 'services': ['string'], 'nodeStatus': 'string'}]}
"""
