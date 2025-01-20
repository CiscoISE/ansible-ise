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
argument_spec.update(
    dict(
        state=dict(type="str", default="present", choices=["present", "absent"]),
        connectedLinks=dict(type="dict"),
        customAttributes=dict(type="dict"),
        description=dict(type="str"),
        deviceType=dict(type="str"),
        groupId=dict(type="str"),
        hardwareRevision=dict(type="str"),
        id=dict(type="str"),
        identityStore=dict(type="str"),
        identityStoreId=dict(type="str"),
        ipAddress=dict(type="str"),
        mac=dict(type="str"),
        mdmAttributes=dict(type="dict"),
        name=dict(type="str"),
        portalUser=dict(type="str"),
        productId=dict(type="str"),
        profileId=dict(type="str"),
        protocol=dict(type="str"),
        serialNumber=dict(type="str"),
        softwareRevision=dict(type="str"),
        staticGroupAssignment=dict(type="bool"),
        staticProfileAssignment=dict(type="bool"),
        vendor=dict(type="str"),
        payload=dict(type="list"),
        value=dict(type="str"),
    )
)

required_if = [
    ("state", "present", ["name", "value"], True),
    ("state", "absent", ["name", "value"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class EndpointsBulk(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            connected_links=params.get("connectedLinks"),
            custom_attributes=params.get("customAttributes"),
            description=params.get("description"),
            device_type=params.get("deviceType"),
            group_id=params.get("groupId"),
            hardware_revision=params.get("hardwareRevision"),
            id=params.get("id"),
            identity_store=params.get("identityStore"),
            identity_store_id=params.get("identityStoreId"),
            ip_address=params.get("ipAddress"),
            mac=params.get("mac"),
            mdm_attributes=params.get("mdmAttributes"),
            name=params.get("name"),
            portal_user=params.get("portalUser"),
            product_id=params.get("productId"),
            profile_id=params.get("profileId"),
            protocol=params.get("protocol"),
            serial_number=params.get("serialNumber"),
            software_revision=params.get("softwareRevision"),
            static_group_assignment=params.get("staticGroupAssignment"),
            static_profile_assignment=params.get("staticProfileAssignment"),
            vendor=params.get("vendor"),
            payload=params.get("payload"),
            value=params.get("value"),
        )

    def get_object_by_name(self, name):
        # NOTICE: Get does not support/work for filter by name with EQ
        result = None
        gen_items_responses = self.ise.exec(
            family="endpoints", function="list_1_generator"
        )
        try:
            for items_response in gen_items_responses:
                items = items_response.response.get("response", [])
                result = get_dict_result(items, "name", name)
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
        try:
            result = self.ise.exec(
                family="endpoints",
                function="get_1",
                handle_func_exception=False,
                params={"id": id},
            ).response
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

    def exists(self):
        id_exists = False
        name_exists = False
        prev_obj = None
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
                raise InconsistentParameters(
                    "The 'id' and 'name' params don't refer to the same object"
                )
            if _id:
                prev_obj = self.get_object_by_id(_id)
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("connectedLinks", "connected_links"),
            ("customAttributes", "custom_attributes"),
            ("description", "description"),
            ("deviceType", "device_type"),
            ("groupId", "group_id"),
            ("hardwareRevision", "hardware_revision"),
            ("id", "id"),
            ("identityStore", "identity_store"),
            ("identityStoreId", "identity_store_id"),
            ("ipAddress", "ip_address"),
            ("mac", "mac"),
            ("mdmAttributes", "mdm_attributes"),
            ("name", "name"),
            ("portalUser", "portal_user"),
            ("productId", "product_id"),
            ("profileId", "profile_id"),
            ("protocol", "protocol"),
            ("serialNumber", "serial_number"),
            ("softwareRevision", "software_revision"),
            ("staticGroupAssignment", "static_group_assignment"),
            ("staticProfileAssignment", "static_profile_assignment"),
            ("vendor", "vendor"),
            ("payload", "payload"),
            ("value", "value"),
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
            family="endpoints",
            function="create_bulk_end_points",
            params=self.new_object,
        ).response
        return result

    def update(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if not id:
            id_ = self.get_object_by_name(name).get("id")
            self.new_object.update(dict(id=id_))
        result = self.ise.exec(
            family="endpoints", function="update_endpoint", params=self.new_object
        ).response
        return result

    def delete(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if not id:
            id_ = self.get_object_by_name(name).get("id")
            self.new_object.update(dict(id=id_))
        result = self.ise.exec(
            family="endpoints", function="delete_endpoint", params=self.new_object
        ).response
        return result


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
        obj = EndpointsBulk(self._task.args, ise)

        state = self._task.args.get("state")

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
