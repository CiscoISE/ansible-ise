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
        default: 3.0.0
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
notes:
    - "Supports C(check_mode)"
'''
