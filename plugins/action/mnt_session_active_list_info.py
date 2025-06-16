#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible_collections.cisco.ise.plugins.plugin_utils.action import ActionModule as ActionBase
from ansible_collections.cisco.ise.plugins.plugin_utils.ise import (
    ISESDK,
    ise_argument_spec,
)

# Get common arguements specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict())

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class ActionModule(ActionBase):
    _supports_check_mode = True

    def get_object(self, params):
        new_object = dict()
        return new_object

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

        self._result.update(dict(ise_response={}))

        ise = ISESDK(params=params)

        id = params.get("id")
        name = params.get("name")
        if not name and not id:
            response = ise.exec(
                family="misc",
                function="get_active_list",
                params=self.get_object(params),
            ).response["activeList"]["@noOfActiveSession"]
            self._result.update(dict(ise_response=response))
            self._result.update(ise.exit_json())
            return self._result
