#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        super(ActionModule, self).__init__(*args, **kwargs)
        self._result = None
