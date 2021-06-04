from __future__ import (absolute_import, division, print_function)
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
from urllib.parse import quote
from ansible_collections.cisco.ise.plugins.module_utils.ise import (
    ISESDK,
    ise_argument_spec,
)
from ansible_collections.cisco.ise.plugins.module_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present", "absent"]),
    rule=dict(type="dict"),
    profile=dict(type="list"),
    securityGroup=dict(type="str"),
    policyId=dict(type="str"),
    id=dict(type="str"),
))

required_if = [
    ("state", "present", ["id", "rule"], True),
    ("state", "present", ["policyId"], True),
    ("state", "absent", ["id", "rule"], True),
    ("state", "absent", ["policyId"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class NetworkAccessAuthorizationRules(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            rule=params.get("rule"),
            profile=params.get("profile"),
            security_group=params.get("securityGroup"),
            policy_id=params.get("policyId"),
            id=params.get("id"),
        )

    def get_object_by_name(self, name, policy_id):
        # NOTICE: Does not have a get by name method or it is in another action
        result = None
        items = self.ise.exec(
            family="network_access_authorization_rules",
            function="get_all_network_access_authorization_rules",
            params={"policy_id": policy_id}
        ).response.get('response', []) or []
        for item in items:
            if item.get('rule') and item['rule'].get('name') == name and item['rule'].get('id'):
                result = dict(item)
                return result
        return result

    def get_object_by_id(self, id, policy_id):
        try:
            result = self.ise.exec(
                family="network_access_authorization_rules",
                function="get_network_access_authorization_rule_by_id",
                params={"id": quote(id), "policy_id": policy_id}
            ).response
        except Exception as e:
            result = None
        return result

    def exists(self):
        id_exists = False
        name_exists = False
        o_id = self.new_object.get("id") or self.new_object.get('rule', {}).get("id")
        policy_id = self.new_object.get("policy_id")
        name = self.new_object.get('rule', {}).get("name")
        if o_id:
            if self.get_object_by_id(o_id, policy_id):
                id_exists = True
        if name:
            if self.get_object_by_name(name, policy_id):
                name_exists = True
        if id_exists and name_exists:
            _id = self.get_object_by_name(name, policy_id).get('rule', {}).get("id")
            if o_id != _id:
                raise InconsistentParameters("The 'id' and 'name' params don't refer to the same object")
        return id_exists or name_exists

    def create(self):
        result = self.ise.exec(
            family="network_access_authorization_rules",
            function="create_network_access_authorization_rule",
            params=self.new_object,
        ).response
        return result

    def update(self):
        id = self.new_object.get("id") or self.new_object.get('rule', {}).get("id")
        name = self.new_object.get('rule', {}).get("name")
        policy_id = self.new_object.get("policy_id")
        result = None
        if not id:
            id_ = self.get_object_by_name(name, policy_id).get('rule', {}).get("id")
            rule = self.new_object.get('rule', {})
            rule.update(dict(id=id_))
            self.new_object.update(dict(rule=rule, id=id_))
        result = self.ise.exec(
            family="network_access_authorization_rules",
            function="update_network_access_authorization_rule_by_id",
            params=self.new_object
        ).response
        return result

    def delete(self):
        id = self.new_object.get("id") or self.new_object.get('rule', {}).get("id")
        name = self.new_object.get('rule', {}).get("name")
        policy_id = self.new_object.get("policy_id")
        result = None
        if not id:
            id_ = self.get_object_by_name(name, policy_id).get('rule', {}).get("id")
            rule = self.new_object.get('rule', {})
            rule.update(dict(id=id_))
            self.new_object.update(dict(rule=rule, id=id_))
        result = self.ise.exec(
            family="network_access_authorization_rules",
            function="delete_network_access_authorization_rule_by_id",
            params=self.new_object
        ).response
        return result


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail("ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
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

        ise = ISESDK(self._task.args)
        obj = NetworkAccessAuthorizationRules(self._task.args, ise)

        state = self._task.args.get("state")

        response = None

        if state == "present":
            if obj.exists():
                response = obj.update()
                ise.object_updated()
            else:
                response = obj.create()
                ise.object_created()

        elif state == "absent":
            if obj.exists():
                response = obj.delete()
                ise.object_deleted()
            else:
                ise.object_already_absent()

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
