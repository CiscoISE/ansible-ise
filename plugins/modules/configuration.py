#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: configuration
short_description: Resource module for Configuration
description:
  - Manage operation update of the resource Configuration.
  - API to enable/disable LSD settings.
version_added: '2.8.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  enableEPO:
    description: To enable/disable LSD ownership settings.
    type: bool
  enableRCM:
    description: To enable/disable random mac(RCM) settings. Please note that this flag will be set to false if enableEPO flag is false.
    type: bool
requirements:
  - ciscoisesdk >= 2.2.3
  - python >= 3.5
notes:
  - SDK Method used are
    configuration.Configuration.update_configuration,
  - Paths used are
    put /api/v1/lsd/updateLsdSettings,
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.configuration:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    enableEPO: true
    enableRCM: true
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "enableEPO": true,
      "enableRCM": true
    }
ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "enableEPO": true,
      "enableRCM": true
    }
"""
