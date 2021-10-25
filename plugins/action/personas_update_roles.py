#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible.errors import AnsibleActionFail
from urllib.parse import quote
import time
from ansible_collections.cisco.ise.plugins.plugin_utils.personas_utils import (
    Node,
    ISEDeployment,
)

argument_spec = dict(
    primary_ip=dict(type="str", required=True),
    primary_username=dict(type="str", required=True),
    primary_password=dict(type="str", required=True),
    name=dict(type="str", required=True),
    local_ip=dict(type="str", required=True),
    hostname=dict(type="str", required=True),
    username=dict(type="str", required=True),
    password=dict(type="str", required=True),
    domain=dict(type="str", required=True),
    roles=dict(type="list", required=True),
    ise_verify=dict(type="bool", default=True),
    ise_version=dict(type="str", default="3.1.0"),
    ise_wait_on_rate_limit=dict(type="bool", default=True),
)

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail("ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._supports_check_mode = False
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(
                required_if=required_if,
                required_one_of=required_one_of,
                mutually_exclusive=mutually_exclusive,
                required_together=required_together,
            ),
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            raise AnsibleActionFail(errors)

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        primary_node = dict(ip=self._task.args.get("primary_ip"),
                            username=self._task.args.get("primary_username"),
                            password=self._task.args.get("primary_password"),
                            )

        other_node = dict(name=self._task.args.get("name"),
                          local_ip=self._task.args.get("local_ip"),
                          hostname=self._task.args.get("hostname"),
                          username=self._task.args.get("username"),
                          password=self._task.args.get("password"),
                          domain=self._task.args.get("domain"),
                          roles=self._task.args.get("roles"),
                          )

        if "PPAN" in other_node.get("roles"):
            raise AnsibleActionFail("Only the primary node can have the 'PPAN' role")

        ise_deployment = ISEDeployment()
        ise_deployment.add_primary(primary_node)
        ise_deployment.add_node(other_node)
        secondary_node = ise_deployment.nodes[0]

        retries_left = 10
        wait_interval = 120
        while retries_left > 0:
            if ise_deployment.primary.app_server_is_running():
                secondary_node.register_node(ise_deployment.primary)
                break
            else:
                retries_left -= 1
                time.sleep(wait_interval)

        response = "Node {name} updated successfully".format(name=self._task.args.get("name"))

        self._result.update(dict(ise_response=response))
        return self._result
