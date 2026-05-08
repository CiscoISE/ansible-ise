#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: active_directory_leave_domain
short_description: Resource module for Active Directory Leave Domain
description:
  - Remove a Cisco ISE node from an Active Directory domain.
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
  adAttributes:
    description:
      - AD attributes configuration.
    type: dict
  adScopesNames:
    description:
      - Comma-separated list of Active Directory scopes.
    type: str
  adgroups:
    description:
      - AD groups configuration.
    type: dict
  advancedSettings:
    description:
      - Advanced settings for the Active Directory leave operation.
    type: dict
  description:
    description:
      - Description of the Active Directory configuration.
    type: str
  domain:
    description:
      - Active Directory domain to leave.
    type: str
  enableDomainAllowedList:
    description:
      - Enable domain allowed list.
    type: bool
  ERSActiveDirectoryDomains:
    description:
      - ERS Active Directory domains configuration.
    type: dict
  name:
    description:
      - Name of the Active Directory configuration.
    type: str
requirements:
  - ciscoisesdk >= 2.2.1
  - python >= 3.5
notes:
  - SDK Method used are
    active_directory.ActiveDirectory.update_activedirectory_leave_by_id,
  - Paths used are
    put /ers/config/activedirectory/{id}/leave,
"""

EXAMPLES = r"""
---
- name: Leave Active Directory domain
  cisco.ise.active_directory_leave_domain:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: "{{ad_config_id}}"
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
