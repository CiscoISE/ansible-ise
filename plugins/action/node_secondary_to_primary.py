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
    get_dict_result,
)
from ansible_collections.cisco.ise.plugins.plugin_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguements specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(
    dict(
        hostname=dict(type="str"),
    )
)

required_if = []
required_one_of = [
    ("hostname"),
]
mutually_exclusive = []
required_together = []


class NodeSecondaryToPrimary(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            hostname=params.get("hostname"),
        )

    def get_object_by_name(self, name):
        try:
            result = self.ise.exec(
                family="node_deployment",
                function="get_node_details",
                params={"hostname": name},
                handle_func_exception=False,
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
        name = self.new_object.get("hostname")
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
        if "SecondaryAdmin" in current_obj.roles:
            return True
        return False


class ActionModule(ActionBase):
    _supports_check_mode = False

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

        ise = ISESDK(params=params)
        obj = NodeSecondaryToPrimary(params, ise)

        name = params.get("hostname")

        response = None
        (obj_exists, prev_obj) = obj.exists()
        if obj_exists:
            if obj.requires_update(prev_obj):
                response = ise.exec(
                    family="node_deployment",
                    function="promote_node",
                    params=self.get_object(params),
                ).response
                ise.object_updated()
            else:
                if "PrimaryAdmin" in prev_obj.roles:
                    ise.result["result"] = "Node is already Primary"
                else:
                    ise.fail_json("Invoke this API on Secondary PAN node only")
        else:
            ise.fail_json(
                "No such HostConfig with hostName [{hostname}]".format(hostname=name)
            )

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
