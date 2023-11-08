#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: dictionary_references_info
short_description: Information module for Dictionary References Info
description:
- Get all Dictionary References Info.
- EDDA - Get a map of references to EDDA dictionaries.
version_added: '3.2_beta'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    edda.Edda.get_edda_dictionary_references,

  - Paths used are
    get /api/v1/edda/dictionary-references,

"""

EXAMPLES = r"""
- name: Get all Dictionary References Info
  cisco.ise.dictionary_references_info:
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
