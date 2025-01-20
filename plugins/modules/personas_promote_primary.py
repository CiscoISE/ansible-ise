#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: personas_promote_primary
short_description: Promote a node as the primary node
description:
  - Promote a node as the primary node
version_added: '0.0.8'
author: Rafael Campos (@racampos)
options:
  ip:
    description:
      - The public IP address of the primary node
    type: str
  hostname:
    description:
      - The hostname of the primary node.
    type: str
  username:
    description:
      - The username to log into the primary node.
    type: str
  password:
    description:
      - The password to log into the primary node.
    type: str
  roles:
    description:
      - The roles to be fulfilled by this node. Must contain at least PPAN and any of MNT-ACTIVE or MNT-STANDBY or PDP
    type: list
    elements: str
  ise_verify:
    description:
      - Whether or not to verify the identity of the node.
    type: bool
  ise_version:
    description:
      - The version of the ISE node.
    type: str
  ise_wait_on_rate_limit:
    description:
      - Whether or not to wait on rate limit
    type: bool
  timeout:
    description:
      - The timeout for the request in seconds. Default is 60 seconds.
    type: int
requirements:
  - requests >= 2.25.1
  - python >= 3.5
seealso:
  # Reference by module name
  - module: cisco.ise.plugins.modules.personas_promote_primary
notes:
  - "Does not support C(check_mode)"
"""

EXAMPLES = r"""
- name: Promote primary node
  cisco.ise.personas_promote_primary:
    ip: 10.1.1.1
    hostname: ise-pan-server-1
    username: admin
    password: cisco123
    roles:
      - PPAN
      - MNT-ACTIVE
    timeout: 60
"""

RETURN = r"""
ise_response:
  description: A string stating that the node was promoted to primary
  returned: always
  type: str
  sample: Primary node was successfully updated
"""
