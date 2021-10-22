#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: personas_update_roles
short_description: Update the roles of a node
description:
- Update the roles of a node
version_added: '0.0.8'
author: Rafael Campos (@racampos)
options:
  primary_ip:
    description:
    - The public IP address of the primary node.
    type: str
  primary_username:
    description:
    - The username for the primary node.
    type: str
  primary_password:
    description:
    - The password for the primary node.
    type: str
  name:
    description:
    - The name of the node.
    type: str
  local_ip:
    description:
    - The local IP address of the node
    type: str
  username:
    description:
    - The username to log into the node.
    type: str
  password:
    description:
    - The password to log into the node.
    type: str
  domain:
    description:
    - The domain of the node.
    type: str
  roles:
    description:
    - The roles to be fulfilled by this node. Possible roles are SPAN or MNT-ACTIVE or MNT-STANDBY or PDP
    type: list
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
requirements:
- requests >= 2.25.1
- python >= 3.5
seealso:
# Reference by module name
- module: cisco.ise.plugins.modules.personas_update_roles
notes:
    - "Does not support C(check_mode)"
"""

EXAMPLES = r"""
- name: Update roles on the rest of the nodes
  cisco.ise.personas_update_roles:
    primary_ip: 10.1.1.1
    primary_username: admin
    primary_password: cisco123
    name: "{{ item.name }}"
    local_ip: "{{ item.local_ip }}"
    hostname: "{{ item.hostname }}"
    username: admin
    password: cisco123
    domain: sstcloud.com
    roles: "{{ item.roles }}"
  loop:
    - name: ISE PAN Server 2
      local_ip: 10.1.1.2
      hostname: ise-pan-server-2
      roles:
        - SPAN
        - MNT-STANDBY
    - name: ISE PSN Server 1
      local_ip: 10.1.1.3
      hostname: ise-psn-server-1
      roles:
        - PDP
    - name: ISE PSN Server 2
      local_ip: 10.1.1.4
      hostname: ise-psn-server-2
      roles:
        - PDP
"""

RETURN = r"""
ise_response:
  description: A string stating that the node was successfully updated
  returned: always
  type: str
  sample: Node ISE PAN Server 2 updated successfully
"""
