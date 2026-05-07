#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: active_directory_add_groups
short_description: Resource module for Active Directory Add Groups
description:
  - Add AD groups to the Cisco ISE Active Directory configuration.
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
      - AD groups to add. Contains the groups dict with group entries.
    type: dict
  advancedSettings:
    description:
      - Advanced settings for the Active Directory configuration.
    type: dict
  description:
    description:
      - Description of the Active Directory configuration.
    type: str
  domain:
    description:
      - Active Directory domain name.
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
    active_directory.ActiveDirectory.update_activedirectory_addgroups_by_id,
  - Paths used are
    put /ers/config/activedirectory/{id}/addGroups,
"""

EXAMPLES = r"""
---
- name: Add AD groups to ISE Active Directory configuration
  cisco.ise.active_directory_add_groups:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: "{{ad_config_id}}"
    adgroups:
      groups:
        - name: CORP\\Domain Users
          sid: S-1-5-21-...
          type: BUILT_IN
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
