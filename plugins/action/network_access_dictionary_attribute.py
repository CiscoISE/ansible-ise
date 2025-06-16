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
        allowedValues=dict(type="list"),
        dataType=dict(type="str"),
        description=dict(type="str"),
        dictionaryName=dict(type="str"),
        directionType=dict(type="str"),
        id=dict(type="str"),
        internalName=dict(type="str"),
        name=dict(type="str"),
    )
)

required_if = [
    ("state", "present", ["dictionaryName"], True),
    ("state", "present", ["name"], True),
    ("state", "absent", ["dictionaryName"], True),
    ("state", "absent", ["name"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class NetworkAccessDictionaryAttribute(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            allowed_values=params.get("allowedValues"),
            data_type=params.get("dataType"),
            description=params.get("description"),
            dictionary_name=params.get("dictionaryName"),
            direction_type=params.get("directionType"),
            id=params.get("id"),
            internal_name=params.get("internalName"),
            name=params.get("name"),
        )

    def get_object_by_name(self, name, dictionary_name):
        try:
            result = self.ise.exec(
                family="network_access_dictionary_attribute",
                function="get_network_access_dictionary_attribute_by_name",
                params={"name": name, "dictionary_name": dictionary_name},
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
        name = self.new_object.get("name")
        dictionary_name = self.new_object.get("dictionary_name")
        if o_id:
            prev_obj = self.get_object_by_id(o_id)
            id_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if not id_exists and name:
            prev_obj = self.get_object_by_name(name, dictionary_name)
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
            ("allowedValues", "allowed_values"),
            ("dataType", "data_type"),
            ("description", "description"),
            ("dictionaryName", "dictionary_name"),
            ("directionType", "direction_type"),
            ("id", "id"),
            ("internalName", "internal_name"),
            ("name", "name"),
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
            family="network_access_dictionary_attribute",
            function="create_network_access_dictionary_attribute",
            params=self.new_object,
        ).response
        return result

    def update(self):
        result = self.ise.exec(
            family="network_access_dictionary_attribute",
            function="update_network_access_dictionary_attribute_by_name",
            params=self.new_object,
        ).response
        return result

    def delete(self):
        result = self.ise.exec(
            family="network_access_dictionary_attribute",
            function="delete_network_access_dictionary_attribute_by_name",
            params=self.new_object,
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
        obj = NetworkAccessDictionaryAttribute(params, ise)

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
