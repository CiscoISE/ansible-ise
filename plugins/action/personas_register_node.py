#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.ise.plugins.plugin_utils.action import ActionModule as ActionBase
from ansible_collections.cisco.ise.plugins.plugin_utils.personas_utils import Node

argument_spec = dict(
    primary_ip=dict(type="str", required=True),
    primary_username=dict(type="str", required=True),
    primary_password=dict(type="str", required=True),
    fqdn=dict(type="str", required=True),
    username=dict(type="str", required=True),
    password=dict(type="str", required=True),
    roles=dict(type="list", required=True),
    services=dict(type="list", required=True),
    ise_verify=dict(type="bool", default=True),
    ise_version=dict(type="str", default="3.1.0"),
    ise_wait_on_rate_limit=dict(type="bool", default=True),
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

        primary_node = Node(
            dict(
                ip=params.get("primary_ip"),
                username=params.get("primary_username"),
                password=params.get("primary_password"),
            )
        )

        this_node = Node(
            dict(
                name=params.get("name"),
                fqdn=params.get("fqdn"),
                username=params.get("username"),
                password=params.get("password"),
                roles=params.get("roles"),
                services=params.get("services"),
            )
        )

        if primary_node.app_server_is_running():
            this_node.register_to_primary(primary_node)
        else:
            raise AnsibleActionFail("Application server is not running.")

        response = "Node {fqdn} updated successfully".format(
            fqdn=params.get("fqdn")
        )

        self._result.update(dict(ise_response=response))
        return self._result
