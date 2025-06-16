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
    ise_compare_equality,
    get_dict_result,
)
from ansible_collections.cisco.ise.plugins.plugin_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(
    dict(
        state=dict(type="str", default="present", choices=["present", "absent"]),
        description=dict(type="str"),
        marCache=dict(type="dict"),
        name=dict(type="str"),
        nodeGroupName=dict(type="str"),
        forceDelete=dict(type="bool"),
    )
)

required_if = [
    ("state", "present", ["name", "nodeGroupName"], True),
    ("state", "absent", ["name", "nodeGroupName"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class NodeGroup(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            description=params.get("description"),
            mar_cache=params.get("marCache"),
            name=params.get("name"),
            node_group_name=params.get("nodeGroupName") or params.get("name"),
            force_delete=params.get("forceDelete"),
        )

    def get_object_by_name(self, name):
        try:
            result = self.ise.exec(
                family="node_group",
                function="get_node_group",
                handle_func_exception=False,
                params={"node_group_name": name},
            ).response["response"]
            result = get_dict_result(result, "name", name)
        except (TypeError, AttributeError) as e:
            self.ise.fail_json(
                msg=(
                    "An error occured when executing operation."
                    " Check the configuration of your API Settings and API Gateway settings on your ISE server."
                    " This collection assumes that the API Gateway, the ERS APIs and OpenAPIs are enabled."
                    " You may want to enable the (ise_debug: True) argument."
                    " The error was: {error}"
                ).format(error=e)
            )
        except Exception:
            result = None
        return result

    def get_object_by_id(self, id):
        # NOTICE: Does not have a get by id method or it is in another action
        result = None
        return result

    def exists(self):
        prev_obj = None
        id_exists = False
        name_exists = False
        o_id = self.new_object.get("id")
        name = self.new_object.get("node_group_name")
        if o_id:
            prev_obj = self.get_object_by_id(o_id)
            id_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if not id_exists and name:
            prev_obj = self.get_object_by_name(name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            if id_exists and name_exists and o_id != _id:
                raise InconsistentParameters(
                    "The 'id' and 'name' params don't refer to the same object"
                )
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("description", "description"),
            ("marCache", "mar_cache"),
            ("name", "name"),
            ("nodeGroupName", "node_group_name"),
            ("forceDelete", "force_delete"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(
            not ise_compare_equality(
                current_obj.get(ise_param), requested_obj.get(ansible_param)
            )
            for (ise_param, ansible_param) in obj_params
        )

    def create(self):
        result = self.ise.exec(
            family="node_group",
            function="create_node_group",
            params=self.new_object,
        ).response
        return result

    def update(self):
        result = self.ise.exec(
            family="node_group", function="update_node_group", params=self.new_object
        ).response
        return result

    def delete(self):
        result = self.ise.exec(
            family="node_group", function="delete_node_group", params=self.new_object
        ).response
        return result


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

        ise = ISESDK(params=params)
        obj = NodeGroup(params, ise)

        state = params.get("state")

        response = None

        if state == "present":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                if obj.requires_update(prev_obj):
                    ise_update_response = obj.update()
                    self._result.update(dict(ise_update_response=ise_update_response))
                    (obj_exists, updated_obj) = obj.exists()
                    response = updated_obj
                    ise.object_updated()
                else:
                    response = prev_obj
                    ise.object_already_present()
            else:
                ise_create_response = obj.create()
                (obj_exists, created_obj) = obj.exists()
                response = created_obj
                ise.object_created()

        elif state == "absent":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                obj.delete()
                response = prev_obj
                ise.object_deleted()
            else:
                ise.object_already_absent()

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
