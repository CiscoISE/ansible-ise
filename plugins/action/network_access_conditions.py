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
    conditionType=dict(type="str"),
    isNegate=dict(type="bool"),
    name=dict(type="str"),
    id=dict(type="str"),
    description=dict(type="str"),
    dictionaryName=dict(type="str"),
    attributeName=dict(type="str"),
    attributeId=dict(type="str"),
    operator=dict(type="str"),
    dictionaryValue=dict(type="str"),
    attributeValue=dict(type="str"),
    children=dict(type="list"),
    hoursRange=dict(type="dict"),
    hoursRangeException=dict(type="dict"),
    weekDays=dict(type="list"),
    weekDaysException=dict(type="list"),
    datesRange=dict(type="dict"),
    datesRangeException=dict(type="dict"),
))

required_if = [
    ("state", "present", ["id", "name"], True),
    ("state", "absent", ["id", "name"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class NetworkAccessConditions(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            condition_type=params.get("conditionType"),
            is_negate=params.get("isNegate"),
            name=params.get("name"),
            id=params.get("id"),
            description=params.get("description"),
            dictionary_name=params.get("dictionaryName"),
            attribute_name=params.get("attributeName"),
            attribute_id=params.get("attributeId"),
            operator=params.get("operator"),
            dictionary_value=params.get("dictionaryValue"),
            attribute_value=params.get("attributeValue"),
            children=params.get("children"),
            hours_range=params.get("hoursRange"),
            hours_range_exception=params.get("hoursRangeException"),
            week_days=params.get("weekDays"),
            week_days_exception=params.get("weekDaysException"),
            dates_range=params.get("datesRange"),
            dates_range_exception=params.get("datesRangeException"),
        )

    def get_object_by_name(self, name):
        # NOTICE: Does not have a get by name method or it is in another action
        result = None
        items = self.ise.exec(
            family="network_access_conditions",
            function="get_all_network_access_conditions",
        ).response.get('response', []) or []
        for item in items:
            if item.get('name') == name and item.get('id'):
                result = dict(item)
                return result
        return result

    def get_object_by_id(self, id):
        try:
            result = self.ise.exec(
                family="network_access_conditions",
                function="get_network_access_condition_by_id",
                params={"id": id}
            ).response.get('response')
        except Exception as e:
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
        if name:
            prev_obj = self.get_object_by_name(name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            if id_exists and name_exists and o_id != _id:
                raise InconsistentParameters("The 'id' and 'name' params don't refer to the same object")
            if _id:
                prev_obj = self.get_object_by_id(_id)
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("conditionType", "condition_type"),
            ("isNegate", "is_negate"),
            ("name", "name"),
            ("id", "id"),
            ("description", "description"),
            ("dictionaryName", "dictionary_name"),
            ("attributeName", "attribute_name"),
            ("attributeId", "attribute_id"),
            ("operator", "operator"),
            ("dictionaryValue", "dictionary_value"),
            ("attributeValue", "attribute_value"),
            ("children", "children"),
            ("hoursRange", "hours_range"),
            ("hoursRangeException", "hours_range_exception"),
            ("weekDays", "week_days"),
            ("weekDaysException", "week_days_exception"),
            ("datesRange", "dates_range"),
            ("datesRangeException", "dates_range_exception"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(not ise_compare_equality(current_obj.get(ise_param),
                                            requested_obj.get(ansible_param))
                   for (ise_param, ansible_param) in obj_params)

    def create(self):
        result = self.ise.exec(
            family="network_access_conditions",
            function="create_network_access_condition",
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
            family="network_access_conditions",
            function="update_network_access_condition_by_id",
            params=self.new_object
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
            family="network_access_conditions",
            function="delete_network_access_condition_by_id",
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
        obj = NetworkAccessConditions(self._task.args, ise)

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
