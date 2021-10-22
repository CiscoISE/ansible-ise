#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):

    # Standard files documentation fragment
    DOCUMENTATION = r'''
options:
    ise_hostname:
        description:
          - The Identity Services Engine hostname.
        type: str
        required: true
    ise_username:
        description:
          - The Identity Services Engine username to authenticate.
        type: str
        required: true
    ise_password:
        description:
          - The Identity Services Engine password to authenticate.
        type: str
        required: true
    ise_verify:
        description:
          - Flag to enable or disable SSL certificate verification.
        type: bool
        default: true
    ise_version:
        description:
          - Informs the SDK which version of Identity Services Engine to use.
        type: str
        default: 3.1.0
    ise_wait_on_rate_limit:
        description:
          - Flag for Identity Services Engine SDK to enable automatic rate-limit handling.
        type: bool
        default: true
    ise_debug:
        description:
          - Flag for Identity Services Engine SDK to enable debugging.
        type: bool
        default: false
    ise_uses_api_gateway:
        description:
          - Flag that informs the SDK whether to use the Identity Services Engine's API Gateway to send requests.
          - If it is true, it uses the ISE's API Gateway and sends requests to https://{{ise_hostname}}.
          - If it is false, it sends the requests to https://{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).
        type: bool
        default: true
        version_added: "1.1.0"
notes:
    - "Supports C(check_mode)"
'''
