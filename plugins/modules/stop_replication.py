#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: stop_replication
short_description: Resource module for Stop Replication
description:
  - Manage operation update of the resource Stop Replication.
  - This API updates the status of Endpoint stop replication Service.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  isEnabled:
    description: IsEnabled flag.
    type: bool
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    endpoint_stop_replication_service.EndpointStopReplicationService.set_stop_replication_service,
  - Paths used are
    put /api/v1/stop-replication,
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.stop_replication:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    isEnabled: true
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "isEnabled": true
    }
ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
"""
