#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_services_profiler_probe_config
short_description: Resource module for Node Services Profiler Probe Config
description:
  - Set profiler probe configuration for a specific ISE node.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  state:
    description:
      - The state of the resource.
    type: str
    default: present
    choices: [present]
  hostname:
    description:
      - Hostname path parameter. FQDN or hostname of the ISE node.
    type: str
    required: true
  activeDirectory:
    description:
      - Active Directory probe configuration.
    type: dict
  dhcp:
    description:
      - DHCP probe configuration.
    type: dict
  dhcpSpan:
    description:
      - DHCP SPAN probe configuration.
    type: dict
  dns:
    description:
      - DNS probe configuration.
    type: dict
  http:
    description:
      - HTTP probe configuration.
    type: dict
  netflow:
    description:
      - NetFlow probe configuration.
    type: dict
  nmap:
    description:
      - NMAP probe configuration list.
    type: list
    elements: dict
  pxgrid:
    description:
      - PxGrid probe configuration list.
    type: list
    elements: dict
  radius:
    description:
      - RADIUS probe configuration list.
    type: list
    elements: dict
  snmpQuery:
    description:
      - SNMP query probe configuration.
    type: dict
  snmpTrap:
    description:
      - SNMP trap probe configuration.
    type: dict
requirements:
  - ciscoisesdk >= 2.2.1
  - python >= 3.5
notes:
  - SDK Method used are
    node_services.NodeServices.set_profiler_probe_config,
  - Paths used are
    put /api/v1/profile/{hostname},
"""

EXAMPLES = r"""
---
- name: Set profiler probe configuration
  cisco.ise.node_services_profiler_probe_config:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    hostname: isenode.example.com
    dhcp:
      interfaces:
        - interface: GigabitEthernet0
      port: 67
    dns:
      timeout: 2
    pxgrid: false
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
"""
