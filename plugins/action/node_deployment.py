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
    hostname=dict(type="str"),
    allowCertImport=dict(type="bool"),
    fqdn=dict(type="str"),
    password=dict(type="str", no_log=True),
    roles=dict(type="list", elements="str"),
    services=dict(type="list", elements="str"),
    userName=dict(type="str"),
))

required_if = [
    ("state", "present", ["hostname"], False),
    ("state", "absent", ["hostname"], False),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class NodeDeployment(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            hostname=params.get("hostname"),
            allow_cert_import=params.get("allowCertImport"),
            fqdn=params.get("fqdn"),
            password=params.get("password"),
            roles=params.get("roles"),
            services=params.get("services"),
            user_name=params.get("userName"),
        )

    def get_object_by_hostname(self, hostname):
        try:
            return self.ise.exec(
                family="node_deployment",
                function="get_node_details",
                handle_func_exception=False,
                params={"hostname": hostname},
            ).response
        except Exception:
            return None

    def exists(self):
        hostname = self.new_object.get("hostname")
        prev_obj = None
        if hostname:
            prev_obj = self.get_object_by_hostname(hostname)
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        obj_params = [
            ("roles", "roles"),
            ("services", "services"),
        ]
        return any(
            not ise_compare_equality(current_obj.get(ise_param), self.new_object.get(ansible_param))
            for (ise_param, ansible_param) in obj_params
        )

    def create(self):
        return self.ise.exec(
            family="node_deployment",
            function="register_node",
            params=self.new_object,
        ).response

    def update(self):
        return self.ise.exec(
            family="node_deployment",
            function="update_node",
            params=self.new_object,
        ).response

    def delete(self):
        return self.ise.exec(
            family="node_deployment",
            function="delete_node",
            params={"hostname": self.new_object.get("hostname")},
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
        obj = NodeDeployment(self._task.args, ise)
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
