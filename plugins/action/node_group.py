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
from ansible_collections.cisco.ise.plugins.plugin_utils.exceptions import (
    InconsistentParameters,
)

argument_spec = ise_argument_spec()
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present", "absent"]),
    nodeGroupName=dict(type="str"),
    name=dict(type="str"),
    description=dict(type="str"),
    marCache=dict(type="dict"),
    forceDelete=dict(type="bool", default=False),
))

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class NodeGroup(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            node_group_name=params.get("nodeGroupName") or params.get("name"),
            name=params.get("name"),
            description=params.get("description"),
            mar_cache=params.get("marCache"),
            force_delete=params.get("forceDelete", False),
        )

    def get_object_by_name(self, name):
        try:
            return self.ise.exec(
                family="node_group",
                function="get_node_group",
                handle_func_exception=False,
                params={"node_group_name": name},
            ).response
        except Exception:
            return None

    def exists(self):
        group_name = self.new_object.get("node_group_name")
        prev_obj = None
        if group_name:
            prev_obj = self.get_object_by_name(group_name)
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        obj_params = [
            ("description", "description"),
            ("marCache", "mar_cache"),
        ]
        return any(
            not ise_compare_equality(current_obj.get(ise_param), self.new_object.get(ansible_param))
            for (ise_param, ansible_param) in obj_params
        )

    def create(self):
        return self.ise.exec(
            family="node_group",
            function="create_node_group",
            params=dict(
                name=self.new_object.get("name"),
                description=self.new_object.get("description"),
                mar_cache=self.new_object.get("mar_cache"),
            ),
        ).response

    def update(self):
        return self.ise.exec(
            family="node_group",
            function="update_node_group",
            params=dict(
                node_group_name=self.new_object.get("node_group_name"),
                name=self.new_object.get("name"),
                description=self.new_object.get("description"),
                mar_cache=self.new_object.get("mar_cache"),
            ),
        ).response

    def delete(self):
        return self.ise.exec(
            family="node_group",
            function="delete_node_group",
            params=dict(
                force_delete=self.new_object.get("force_delete", False),
                node_group_name=self.new_object.get("node_group_name"),
            ),
        ).response


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail(
                "ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'"
            )
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._supports_check_mode = False
        self._result = None

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
        obj = NodeGroup(self._task.args, ise)
        state = self._task.args.get("state")
        response = None

        if state == "present":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                if obj.requires_update(prev_obj):
                    ise_update_response = obj.update()
                    self._result.update(dict(ise_update_response=ise_update_response))
                    (_, updated_obj) = obj.exists()
                    ise.object_updated()
                    response = updated_obj
                else:
                    response = prev_obj
                    ise.object_already_present()
            else:
                ise_create_response = obj.create()
                self._result.update(dict(ise_create_response=ise_create_response))
                (_, created_obj) = obj.exists()
                response = created_obj
                ise.object_created()
        elif state == "absent":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                obj.delete()
                response = prev_obj
                ise.object_deleted()
            else:
                response = None
                ise.object_already_absent()

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
