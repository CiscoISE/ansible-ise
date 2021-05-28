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

# Get common arguements specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    id=dict(type="str"),
    name=dict(type="str"),
))

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


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

    def get_object(self, params):
        new_object = dict(
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
        return new_object

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        ise = ISESDK(params=self._task.args)

        id = self._task.args.get("id")
        name = self._task.args.get("name")
        if id:
            response = ise.exec(
                family="device_administration_conditions",
                function='get_device_admin_condition_by_id',
                params=self.get_object(self._task.args)
            ).response
            self._result.update(dict(ise_response=response))
            self._result.update(ise.exit_json())
            return self._result
        if name:
            response = ise.exec(
                family="device_administration_conditions",
                function='get_device_admin_condition_by_name',
                params=self.get_object(self._task.args)
            ).response
            self._result.update(dict(ise_response=response))
            self._result.update(ise.exit_json())
            return self._result
        if not name and not id:
            response = ise.exec(
                family="device_administration_conditions",
                function='get_all_device_admin_conditions',
                params=self.get_object(self._task.args),
            ).response
            self._result.update(dict(ise_response=response))
            self._result.update(ise.exit_json())
            return self._result
