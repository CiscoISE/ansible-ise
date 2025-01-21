#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: ad_groups_info
short_description: Information module for Ad Groups Info
description:
  - Get Ad Groups Info by id.
  - Duo-IdentitySync - Get the list of all AD groups for the specified Active Directory.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  activeDirectory:
    description:
      - ActiveDirectory path parameter. List of AD groups for the specified Active Directory.
    type: str
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    ad_groups.ADGroups.get_adgroups,
  - Paths used are
    get /api/v1/duo-identitysync/adgroups/{activeDirectory},
"""

EXAMPLES = r"""
- name: Get Ad Groups Info by id
  cisco.ise.ad_groups_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    activeDirectory: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "name": "string",
        "source": "string"
      }
    ]
"""
