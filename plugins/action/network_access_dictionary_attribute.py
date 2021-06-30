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
from ansible_collections.cisco.ise.plugins.module_utils.ise import (
    ISESDK,
    ise_argument_spec,
    ise_compare_equality,
    get_dict_result,
)
from ansible_collections.cisco.ise.plugins.module_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present", "absent"]),
    id=dict(type="str"),
    directionType=dict(type="str"),
    name=dict(type="str"),
    description=dict(type="str"),
    internalName=dict(type="str"),
    dataType=dict(type="str"),
    dictionaryName=dict(type="str"),
    allowedValues=dict(type="list"),
))

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
            id=params.get("id"),
            direction_type=params.get("directionType"),
            name=params.get("name"),
            description=params.get("description"),
            internal_name=params.get("internalName"),
            data_type=params.get("dataType"),
            dictionary_name=params.get("dictionaryName"),
            allowed_values=params.get("allowedValues"),
        )

    def get_object_by_name(self, name, dictionary_name):
        try:
            result = self.ise.exec(
                family="network_access_dictionary_attribute",
                function="get_network_access_dictionary_attribute_by_name",
                params={"name": name, "dictionary_name": dictionary_name}
            ).response
            result = get_dict_result(result, 'name', name)
        except Exception as e:
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
        if name:
            prev_obj = self.get_object_by_name(name, dictionary_name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            if o_id != _id:
                raise InconsistentParameters("The 'id' and 'name' params don't refer to the same object")
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("id", "id"),
            ("directionType", "direction_type"),
            ("name", "name"),
            ("description", "description"),
            ("internalName", "internal_name"),
            ("dataType", "data_type"),
            ("dictionaryName", "dictionary_name"),
            ("allowedValues", "allowed_values"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(not ise_compare_equality(current_obj.get(ise_param),
                                            requested_obj.get(ansible_param))
                   for (ise_param, ansible_param) in obj_params)

    def create(self):
        result = self.ise.exec(
            family="network_access_dictionary_attribute",
            function="create_network_access_dictionary_attribute_for_dictionary",
            params=self.new_object,
        ).response
        return result

    def update(self):
        result = self.ise.exec(
            family="network_access_dictionary_attribute",
            function="update_network_access_dictionary_attribute_by_name",
            params=self.new_object
        ).response
        return result

    def delete(self):
        result = self.ise.exec(
            family="network_access_dictionary_attribute",
            function="delete_network_access_dictionary_attribute_by_name",
            params=self.new_object
        ).response
        return result


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail("ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = True
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
        obj = NetworkAccessDictionaryAttribute(self._task.args, ise)

        state = self._task.args.get("state")

        response = None

        if state == "present":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                if obj.requires_update(prev_obj):
                    response = obj.update()
                    ise.object_updated()
                else:
                    response = prev_obj
                    ise.object_already_present()
            else:
                response = obj.create()
                ise.object_created()

        elif state == "absent":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                response = obj.delete()
                ise.object_deleted()
            else:
                ise.object_already_absent()

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
