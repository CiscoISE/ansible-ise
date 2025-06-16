#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible_collections.cisco.ise.plugins.plugin_utils.action import ActionModule as ActionBase
from ansible_collections.cisco.ise.plugins.plugin_utils.personas_utils import Node

argument_spec = dict(
    ip=dict(type="str", required=True),
    hostname=dict(type="str", required=True),
    username=dict(type="str", required=True),
    password=dict(type="str", required=True),
    roles=dict(type="list", required=True),
    ise_verify=dict(type="bool", default=True),
    ise_version=dict(type="str", default="3.1.0"),
    ise_wait_on_rate_limit=dict(type="bool", default=True),
    timeout=dict(type="int", default=60),
)

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class ActionModule(ActionBase):
    _supports_check_mode = False

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        _, validated_arguments = self.validate_argument_spec(
            argument_spec=argument_spec,
            mutually_exclusive=mutually_exclusive,
            required_if=required_if,
            required_one_of=required_one_of,
            required_together=required_together,
        )
        params = {k: v, for k, v in validated_arguments if k in self._task.args}

        node = Node(
            dict(
                ip=params.get("ip"),
                hostname=params.get("hostname"),
                username=params.get("username"),
                password=params.get("password"),
                roles=params.get("roles"),
            )
        )

        timeout = params.get("timeout")
        if node.is_primary(timeout=timeout):
            response = "Node is already primary"
            self._result.update(dict(result="Object already present"))
        else:
            node.promote_to_primary(timeout=timeout)
            response = "Primary node was successfully updated"

        self._result.update(dict(ise_response=response))
        return self._result
