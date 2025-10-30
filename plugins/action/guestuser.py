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
    get_dict_result,
)
from ansible_collections.cisco.ise.plugins.plugin_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present"]),
    customFields=dict(type="dict"),
    guestType=dict(type="str"),
    status=dict(type="str"),
    reasonForVisit=dict(type="str"),
    personBeingVisited=dict(type="str"),
    sponsorUserName=dict(type="str"),
    sponsorUserId=dict(type="str"),
    statusReason=dict(type="str"),
    portalId=dict(type="str"),
    guestAccessInfo=dict(type="dict"),
    guestInfo=dict(type="dict"),
    name=dict(type="str"),
    id=dict(type="str"),
    description=dict(type="str"),
))

required_if = [
    ("state", "present", ["name"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class Guestuser(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            custom_fields=params.get("customFields"),
            guest_type=params.get("guestType"),
            status=params.get("status"),
            reason_for_visit=params.get("reasonForVisit"),
            person_being_visited=params.get("personBeingVisited"),
            sponsor_user_name=params.get("sponsorUserName"),
            sponsor_user_id=params.get("sponsorUserId"),
            status_reason=params.get("statusReason"),
            portal_id=params.get("portalId"),
            guest_access_info=params.get("guestAccessInfo"),
            guest_info=params.get("guestInfo"),
            name=params.get("name"),
            id=params.get("id"),
            description=params.get("description"),
        )

    def get_object_by_name(self, name):
        # NOTICE: Get does not support/work for filter by name with EQ
        result = None
        gen_items_responses = self.ise.exec(
            family="guestuser",
            function="get_guestuser_generator"
        )
        try:
            for items_response in gen_items_responses:
                items = items_response.response['SearchResult']['resources']
                result = get_dict_result(items, 'name', name)
                if result:
                    return result
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
        if o_id:
            prev_obj = self.get_object_by_id(o_id)
            id_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if not id_exists and name:
            prev_obj = self.get_object_by_name(name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            if id_exists and name_exists and o_id != _id:
                raise InconsistentParameters("The 'id' and 'name' params don't refer to the same object")
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("customFields", "custom_fields"),
            ("guestType", "guest_type"),
            ("status", "status"),
            ("reasonForVisit", "reason_for_visit"),
            ("personBeingVisited", "person_being_visited"),
            ("sponsorUserName", "sponsor_user_name"),
            ("sponsorUserId", "sponsor_user_id"),
            ("statusReason", "status_reason"),
            ("portalId", "portal_id"),
            ("guestAccessInfo", "guest_access_info"),
            ("guestInfo", "guest_info"),
            ("name", "name"),
            ("id", "id"),
            ("description", "description"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(not ise_compare_equality(current_obj.get(ise_param),
                                            requested_obj.get(ansible_param))
                   for (ise_param, ansible_param) in obj_params)

    def create(self):
        result = self.ise.exec(
            family="guestuser",
            function="create_guestuser",
            params=self.new_object,
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
        obj = Guestuser(self._task.args, ise)

        state = self._task.args.get("state")

        response = None
        if state == "present":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                if obj.requires_update(prev_obj):
                    response = prev_obj
                    ise.object_present_and_different()
                else:
                    response = prev_obj
                    ise.object_already_present()
            else:
                ise_create_response = obj.create()
                (obj_exists, created_obj) = obj.exists()
                response = created_obj
                ise.object_created()

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
