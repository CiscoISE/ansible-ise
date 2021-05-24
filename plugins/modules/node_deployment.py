#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: node_deployment
short_description: Resource module for Node Deployment
description:
- Manage operations create, update, delete of the resource Node Deployment.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    administration:
      suboptions:
        isEnabled:
          description: IsEnabled flag.
          type: bool
        role:
          description: Node Deployment's role.
          type: str
      type: dict
    fdqn:
      description: Node Deployment's fdqn.
      type: str
    generalSettings:
      suboptions:
        monitoring:
          suboptions:
            enablePXGrid:
              description: EnablePXGrid flag.
              type: bool
            isEnabled:
              description: IsEnabled flag.
              type: bool
            isMntDedicated:
              description: IsMntDedicated flag.
              type: bool
            otherMonitoringNode:
              description: Node Deployment's otherMonitoringNode.
              type: str
            policyservice:
              suboptions:
                enableDeviceAdminService:
                  description: EnableDeviceAdminService flag.
                  type: bool
                enableNACService:
                  description: EnableNACService flag.
                  type: bool
                enablePassiveIdentityService:
                  description: EnablePassiveIdentityService flag.
                  type: bool
                enableProfilingService:
                  description: EnableProfilingService flag.
                  type: bool
                enabled:
                  description: Enabled flag.
                  type: bool
                sessionService:
                  suboptions:
                    isEnabled:
                      description: IsEnabled flag.
                      type: bool
                    nodegroup:
                      description: Node Deployment's nodegroup.
                      type: str
                  type: dict
                sxpservice:
                  suboptions:
                    isEnabled:
                      description: IsEnabled flag.
                      type: bool
                    userInterface:
                      description: Node Deployment's userInterface.
                      type: str
                  type: dict
              type: dict
            role:
              description: Node Deployment's role.
              type: str
          type: dict
      type: dict
    hostname:
      description: Hostname path parameter. Node name of the existing deployed node.
      type: string
    password:
      description: Node Deployment's password.
      type: str
    profileConfiguration:
      suboptions:
        activeDirectory:
          suboptions:
            daysBeforeRescan:
              description: Node Deployment's daysBeforeRescan.
              type: int
            description:
              description: Node Deployment's description.
              type: str
            enabled:
              description: Enabled flag.
              type: bool
          type: dict
        dhcp:
          suboptions:
            description:
              description: Node Deployment's description.
              type: str
            enabled:
              description: Enabled flag.
              type: bool
            interface:
              description: Node Deployment's interface.
              type: str
            port:
              description: Node Deployment's port.
              type: null
          type: dict
        dhcpSpan:
          suboptions:
            description:
              description: Node Deployment's description.
              type: str
            enabled:
              description: Enabled flag.
              type: bool
            interface:
              description: Node Deployment's interface.
              type: str
          type: dict
        dns:
          suboptions:
            description:
              description: Node Deployment's description.
              type: str
            enabled:
              description: Enabled flag.
              type: bool
          type: dict
        http:
          suboptions:
            description:
              description: Node Deployment's description.
              type: str
            enabled:
              description: Enabled flag.
              type: bool
            interface:
              description: Node Deployment's interface.
              type: str
          type: dict
        netflow:
          suboptions:
            description:
              description: Node Deployment's description.
              type: str
            enabled:
              description: Enabled flag.
              type: bool
            interface:
              description: Node Deployment's interface.
              type: str
            port:
              description: Node Deployment's port.
              type: null
          type: dict
        nmap:
          suboptions:
            description:
              description: Node Deployment's description.
              type: str
            enabled:
              description: Enabled flag.
              type: bool
          type: dict
        pxgrid:
          suboptions:
            description:
              description: Node Deployment's description.
              type: str
            enabled:
              description: Enabled flag.
              type: bool
          type: dict
        radius:
          suboptions:
            description:
              description: Node Deployment's description.
              type: str
            enabled:
              description: Enabled flag.
              type: bool
          type: dict
        snmpQuery:
          suboptions:
            description:
              description: Node Deployment's description.
              type: str
            enabled:
              description: Enabled flag.
              type: bool
            eventTimeout:
              description: Node Deployment's eventTimeout.
              type: int
            retries:
              description: Node Deployment's retries.
              type: int
            timeout:
              description: Node Deployment's timeout.
              type: int
          type: dict
        snmpTrap:
          suboptions:
            description:
              description: Node Deployment's description.
              type: str
            interface:
              description: Node Deployment's interface.
              type: str
            linkTrapQuery:
              description: LinkTrapQuery flag.
              type: bool
            macTrapQuery:
              description: MacTrapQuery flag.
              type: bool
            port:
              description: Node Deployment's port.
              type: null
          type: dict
      type: dict
    userName:
      description: Node Deployment's userName.
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
- name: Create
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    administration:
      isEnabled: true
      role: string
    fdqn: string
    generalSettings:
      monitoring:
        enablePXGrid: true
        isEnabled: true
        isMntDedicated: true
        otherMonitoringNode: string
        policyservice:
          enableDeviceAdminService: true
          enableNACService: true
          enablePassiveIdentityService: true
          enableProfilingService: true
          enabled: true
          sessionService:
            isEnabled: true
            nodegroup: string
          sxpservice:
            isEnabled: true
            userInterface: string
        role: string
    password: string
    profileConfiguration:
      activeDirectory:
        daysBeforeRescan: 0
        description: string
        enabled: true
      dhcp:
        description: string
        enabled: true
        interface: string
        port: {}
      dhcpSpan:
        description: string
        enabled: true
        interface: string
      dns:
        description: string
        enabled: true
      http:
        description: string
        enabled: true
        interface: string
      netflow:
        description: string
        enabled: true
        interface: string
        port: {}
      nmap:
        description: string
        enabled: true
      pxgrid:
        description: string
        enabled: true
      radius:
        description: string
        enabled: true
      snmpQuery:
        description: string
        enabled: true
        eventTimeout: 0
        retries: 0
        timeout: 0
      snmpTrap:
        description: string
        interface: string
        linkTrapQuery: true
        macTrapQuery: true
        port: {}
    userName: string

- name: Update by name
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    generalSettings:
      monitoring:
        enablePXGrid: true
        isEnabled: true
        isMntDedicated: true
        otherMonitoringNode: string
        policyservice:
          enableDeviceAdminService: true
          enableNACService: true
          enablePassiveIdentityService: true
          enableProfilingService: true
          enabled: true
          sessionService:
            isEnabled: true
            nodegroup: string
          sxpservice:
            isEnabled: true
            userInterface: string
        role: string
    hostname: string
    profileConfiguration:
      activeDirectory:
        daysBeforeRescan: 0
        description: string
        enabled: true
      dhcp:
        description: string
        enabled: true
        interface: string
        port: {}
      dhcpSpan:
        description: string
        enabled: true
        interface: string
      dns:
        description: string
        enabled: true
      http:
        description: string
        enabled: true
        interface: string
      netflow:
        description: string
        enabled: true
        interface: string
        port: {}
      nmap:
        description: string
        enabled: true
      pxgrid:
        description: string
        enabled: true
      radius:
        description: string
        enabled: true
      snmpQuery:
        description: string
        enabled: true
        eventTimeout: 0
        retries: 0
        timeout: 0
      snmpTrap:
        description: string
        interface: string
        linkTrapQuery: true
        macTrapQuery: true
        port: {}

- name: Delete by name
  cisco.ise.node_deployment:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    hostname: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'code': 0, 'message': 'string', 'rootCause': 'string'}
  - {'code': 0, 'message': 'string', 'rootCause': 'string'}
  - {'code': 0, 'message': 'string', 'rootCause': 'string'}
"""
