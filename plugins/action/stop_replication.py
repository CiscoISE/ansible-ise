#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

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
from ansible_collections.cisco.ise.plugins.plugin_utils.ise import (
    ISESDK,
    ise_argument_spec,
    ise_compare_equality,
)

# Get common arguments specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present"]),
    isEnabled=dict(type="bool"),
))

required_if = [
    ("state", "present", ["isEnabled"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class StopReplication(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            is_enabled=params.get("isEnabled"),
        )

    def get_object(self):
        # NOTICE: Endpoint stop replication is a single deployment wide switch,
        # so there is no id or name to look it up by, only its current status.
        response = self.ise.exec(
            family="endpoint_stop_replication_service",
            function="get_stop_replication_status"
        ).response
        if isinstance(response, dict):
            return response.get('response')
        return None

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("isEnabled", "is_enabled"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(not ise_compare_equality(current_obj.get(ise_param),
                                            requested_obj.get(ansible_param))
                   for (ise_param, ansible_param) in obj_params)

    def update(self):
        result = self.ise.exec(
            family="endpoint_stop_replication_service",
            function="set_stop_replication_service",
            params=self.new_object
        ).response
        return result


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

        ise = ISESDK(params=self._task.args)
        obj = StopReplication(self._task.args, ise)

        state = self._task.args.get("state")

        response = None
        if state == "present":
            prev_obj = obj.get_object()
            if prev_obj is None or obj.requires_update(prev_obj):
                ise_update_response = obj.update()
                self._result.update(dict(ise_update_response=ise_update_response))
                response = obj.get_object()
                ise.object_updated()
            else:
                response = prev_obj
                ise.object_already_present()

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
