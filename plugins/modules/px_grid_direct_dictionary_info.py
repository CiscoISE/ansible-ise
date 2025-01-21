#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: px_grid_direct_dictionary_info
short_description: Information module for Px Grid Direct Dictionary Info
description:
  - Get all Px Grid Direct Dictionary Info.
  - PxGrid Direct - Get a map of references to pxgrid-direct dictionaries.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    px_grid_direct.PxGridDirect.getpxgrid_direct_dictionary_references,
  - Paths used are
    get /api/v1/pxgrid-direct/dictionary-references,
"""

EXAMPLES = r"""
- name: Get all Px Grid Direct Dictionary Info
  cisco.ise.px_grid_direct_dictionary_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
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
