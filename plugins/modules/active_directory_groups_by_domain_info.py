#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: active_directory_groups_by_domain_info
short_description: Information module for Active Directory Groups By Domain
description:
  - Get Active Directory groups for a specific domain.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  id:
    description:
      - Id path parameter. ID of the Active Directory configuration.
    type: str
    required: true
  additionalData:
    description:
      - List of name/value pairs to filter the domain groups query.
        Typical entries include domain, username, and password.
      - "Example: [{name: domain, value: CORP.EXAMPLE.COM},
        {name: username, value: jdoe}, {name: password, value: secret}]"
    type: list
    elements: dict
requirements:
  - ciscoisesdk >= 2.2.1
  - python >= 3.5
notes:
  - SDK Method used are
    active_directory.ActiveDirectory.update_activedirectory_getgroupsbydomain_by_id,
  - Paths used are
    put /ers/config/activedirectory/{id}/getGroupsByDomain,
"""

EXAMPLES = r"""
---
- name: Get AD groups by domain
  cisco.ise.active_directory_groups_by_domain_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: "{{ad_config_id}}"
    additionalData:
      - name: domain
        value: CORP.EXAMPLE.COM
      - name: username
        value: jdoe
      - name: password
        value: "{{domain_password}}"
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "ERSActiveDirectoryGroups": {
        "groups": [
          {
            "name": "string",
            "sid": "string",
            "type": "string"
          }
        ]
      }
    }
"""
