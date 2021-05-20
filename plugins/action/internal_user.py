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

# Get common arguments specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
        state = dict(type="str", default="present", choices=["present", "absent"]),
        id=dict(type="str"),
        name=dict(type="str"),
        description=dict(type="str"),
        enabled=dict(type="bool"),
        email=dict(type="str"),
        password=dict(type="str"),
        firstName=dict(type="str"),
        lastName=dict(type="str"),
        changePassword=dict(type="bool"),
        identityGroups=dict(type="str"),
        expiryDateEnabled=dict(type="bool"),
        expiryDate=dict(type="str"),
        enablePassword=dict(type="str"),
        customAttributes=dict(type="dict"),
        passwordIDStore=dict(type="str"),
    ))

required_if = [
    ("state", "present", ("id", "name"), True),
    ("state", "absent", ("id", "name"), True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class InternalUser(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            id=params.get("id"),
            name=params.get("name"),
            description=params.get("description"),
            enabled=params.get("enabled"),
            email=params.get("email"),
            password=params.get("password"),
            first_name=params.get("firstName"),
            last_name=params.get("lastName"),
            change_password=params.get("changePassword"),
            identity_groups=params.get("identityGroups"),
            expiry_date_enabled=params.get("expiryDateEnabled"),
            expiry_date=params.get("expiryDate"),
            enable_password=params.get("enablePassword"),
            custom_attributes=params.get("customAttributes"),
            password_idstore=params.get("passwordIDStore"),
        )


    def get_object_by_name(self, name):
        try:
            result = self.ise.exec(
                family="internal_user",
                function="get_internal_user_by_name",
                params={"name": quote(name)}
                ).response['InternalUser']
        except Exception as e:
            result = None
        return result

    def get_object_by_id(self, id):
        try:
            result = self.ise.exec(
                family="internal_user",
                function="internaluser_by_id",
                params={"id": quote(id)}
                ).response['InternalUser']
        except Exception as e:
            result = None
        return result

    def exists(self):
        result = False
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        if id:
            if self.get_object_by_id(id):
                result = True
        elif name:
            if self.get_object_by_name(name):
                result = True
        return result

    def create(self):
        result = self.ise.exec(
            family="internal_user",
            function="create_internal_user",
            params=self.new_object,
        ).response
        return result

    def update(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if id:
            result = self.ise.exec(
                family="internal_user",
                function="update_internal_user_by_id",
                params=self.new_object
            ).response
        elif name:
            result = self.ise.exec(
                family="internal_user",
                function="update_internal_user_by_name",
                params=self.new_object
            ).response
        return result

    def delete(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if id:
            result = self.ise.exec(
                family="internal_user",
                function="delete_internal_user_by_id",
                params=self.new_object
            ).response
        elif name:
            result = self.ise.exec(
                family="internal_user",
                function="delete_internal_user_by_name",
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
        obj = InternalUser(self._task.args, ise)

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
