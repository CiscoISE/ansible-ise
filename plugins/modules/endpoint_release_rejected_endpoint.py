#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint_release_rejected_endpoint
short_description: Resource module for Endpoint Release Rejected Endpoint
description:
- Manage operation update of the resource Endpoint Release Rejected Endpoint.
- This API allows the client to release a rejected endpoint.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    endpoint.Endpoint.release_rejected_endpoint,

  - Paths used are
    put /ers/config/endpoint/{id}/releaserejectedendpoint,

"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.endpoint_release_rejected_endpoint:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
