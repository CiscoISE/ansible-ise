#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sg_mapping_deploy_status_info
short_description: Information module for Sg Mapping Deploy Status
description:
- Get all Sg Mapping Deploy Status.
- This API allows the client to get the IP to SGT mapping
  deployment status. Deploy Status will show last Deploy
  command output. The information will be saved until the
  next Deploy command.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    ip_to_sgt_mapping.IpToSgtMapping.get_deploy_status_ip_to_sgt_mapping,

  - Paths used are
    put /ers/config/sgmapping/deploy/status

"""

EXAMPLES = r"""
- name: Get all Sg Mapping Deploy Status
  cisco.ise.sg_mapping_deploy_status_info:
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
    {
      "resultValue": [
        {
          "value": "string",
          "name": "string"
        }
      ]
    }
"""
