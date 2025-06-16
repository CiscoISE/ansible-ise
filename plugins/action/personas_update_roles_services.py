from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.ise.plugins.plugin_utils.action import ActionModule as ActionBase
from ansible_collections.cisco.ise.plugins.plugin_utils.personas_utils import Node
from ansible_collections.cisco.ise.plugins.plugin_utils.ise import (
    ise_compare_equality,
)

argument_spec = dict(
    ip=dict(type="str", required=True),
    username=dict(type="str", required=True),
    password=dict(type="str", required=True),
    hostname=dict(type="str", required=True),
    roles=dict(type="list", required=True),
    services=dict(type="list", required=True),
    ise_verify=dict(type="bool", default=True),
    ise_version=dict(type="str", default="3.0.0"),
    ise_wait_on_rate_limit=dict(
        type="bool", default=True
    ),  # TODO: verify what the true default value should be
)

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class NodeDeployment(object):
    def requires_update(self, current_obj, requested_obj):
        obj_params = [
            ("roles", "roles"),
            ("services", "services"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(
            not ise_compare_equality(
                current_obj.get(ise_param), requested_obj.get(ansible_param)
            )
            for (ise_param, ansible_param) in obj_params
        )


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
        obj = NodeDeployment()
        request_obj = dict(
            ip=params.get("ip"),
            username=params.get("username"),
            password=params.get("password"),
            hostname=params.get("hostname"),
            roles=params.get("roles"),
            services=params.get("services"),
        )
        node = Node(request_obj)
        prev_obj = False
        result = dict(changed=False, result="")
        response = None
        if not node.app_server_is_running():
            raise AnsibleActionFail(
                "Couldn't connect, the node might be still initializing, try again in a few minutes. Error received: 502"
            )
        try:
            prev_obj = node.get_roles_services()
        except Exception as e:
            raise AnsibleActionFail(e)
        if prev_obj:
            if obj.requires_update(prev_obj, request_obj):
                try:
                    node.update_roles_services()
                    response = node.get_roles_services()
                    result["changed"] = True
                    result["result"] = "Object updated"
                except Exception as e:
                    raise AnsibleActionFail(
                        "The node might be still initializing. Error received: {e}".format(
                            e=e
                        )
                    )
            else:
                response = prev_obj
                result["result"] = "Object already present"
        self._result.update(dict(ise_response=response))
        self._result.update(result)
        return self._result
