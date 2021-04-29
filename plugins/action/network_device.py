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
)

# Get common arguements specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
        state = dict(type="str", default="present", choices=["present", "absent"]),
        id=dict(type="str"),
        name=dict(type="str"),
        description=dict(type="str"),
        authenticationSettings=dict(type="dict"),
        profileName=dict(type="str"),
        coaPort=dict(type="int"),
        link=dict(type="dict"),
        NetworkDeviceIPList=dict(type="list"),
        NetworkDeviceGroupList=dict(type="list"),
    ))

required_if = [
    ("state", "present", ("id", "name"), True),
    ("state", "absent", ("id", "name"), True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class NetworkDevice(object):
    def __init__(self, params, ise):
        self.ise = ise
        new_object = dict(
            id=params.get("id")
            name=params.get("name")
            description=params.get("description")
            authenticationSettings=params.get("authenticationSettings")
            profileName=params.get("profileName")
            coaPort=params.get("coaPort")
            link=params.get("coaPort")
            NetworkDeviceIPList=params.get("NetworkDeviceIPList")
            NetworkDeviceGroupList=params.get("NetworkDeviceGroupList")
        )
        self.new_object = new_object
        self.existing_objects = self.get_objects()

    def get_objects(self):
        return self.ise.exec(family="network_device", function="networkdevice", params=None)

    def exists(self):
        result = False
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        for obj in self.existing_objects:
            if id:
                if obj.get("id") == id:
                    result = True
            elif name:
                if obj.get("name") == name:
                    result = True
        return result

    def create(self):
        result = ise.exec(
            family="network_device", 
            function='create_networkdevice',
            params=self.new_object),
        )
        return result

    def update(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if id:
            result = ise.exec(
                family="network_device",
                function='update_networkdevice_by_id',
                params=self.new_object
            )
        elif name:
            result = ise.exec(
                family="network_device",
                function='update_networkdevice_by_name',
                params=self.new_object
            )
        return result

    def delete(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if id:
            result = ise.exec(
                family="network_device",
                function='delete_networkdevice_by_id',
                params=self.new_object
            )
        elif name:
            result = ise.exec(
                family="network_device",
                function='delete_networkdevice_by_name',
                params=self.new_object
            )
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
                mutually_exclusive=mutually_exclusive),
                required_together=required_together,
            )
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

        ise = ISESDK()
        obj = NetworkDevice(self._task_args, ise)

        state = self._task.args.get("state")

        if state == "present":
            if obj.exists():
                response = obj.update()
            else:
                response = obj.create()

        elif state == "absent":
            if obj.exists():
                response = obj.delete()
         
        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
