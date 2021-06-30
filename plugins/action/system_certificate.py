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

# Get common arguments specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present", "absent"]),
    name=dict(type="str"),
    description=dict(type="str"),
    admin=dict(type="bool"),
    eap=dict(type="bool"),
    radius=dict(type="bool"),
    pxgrid=dict(type="bool"),
    saml=dict(type="bool"),
    portal=dict(type="bool"),
    ims=dict(type="bool"),
    portalGroupTag=dict(type="str"),
    allowReplacementOfPortalGroupTag=dict(type="bool"),
    renewSelfSignedCertificate=dict(type="bool"),
    expirationTTLPeriod=dict(type="int"),
    expirationTTLUnits=dict(type="str"),
    id=dict(type="str"),
    hostName=dict(type="str"),
))

required_if = [
    ("state", "present", ["hostName"], True),
    ("state", "present", ["id", "name"], True),
    ("state", "present", ["hostName"], True),
    ("state", "absent", ["id", "name"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class SystemCertificate(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            name=params.get("name"),
            description=params.get("description"),
            admin=params.get("admin"),
            eap=params.get("eap"),
            radius=params.get("radius"),
            pxgrid=params.get("pxgrid"),
            saml=params.get("saml"),
            portal=params.get("portal"),
            ims=params.get("ims"),
            portal_group_tag=params.get("portalGroupTag"),
            allow_replacement_of_portal_group_tag=params.get("allowReplacementOfPortalGroupTag"),
            renew_self_signed_certificate=params.get("renewSelfSignedCertificate"),
            expiration_ttl_period=params.get("expirationTTLPeriod"),
            expiration_ttl_units=params.get("expirationTTLUnits"),
            id=params.get("id"),
            host_name=params.get("hostName"),
        )

    def get_object_by_name(self, name, host_name):
        result = None
        gen_items_responses = self.ise.exec(
            family="certificates",
            function="get_all_system_certificates_generator",
            params={"host_name": host_name}
        )
        for items_response in gen_items_responses:
            items = items_response.response.get('response', []) or []
            for item in items:
                if item.get('friendlyName') == name and item.get('id'):
                    result = dict(item)
                    return result
        return result

    def get_object_by_id(self, id, host_name):
        try:
            result = self.ise.exec(
                family="certificates",
                function="get_system_certificate_by_id",
                params={"id": id, "host_name": host_name}
            ).response
        except Exception as e:
            result = None
        return result

    def exists(self):
        prev_obj = None
        result = False
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        host_name = self.new_object.get("host_name")
        if id:
            prev_obj = self.get_object_by_id(id, host_name)
            result = prev_obj is not None and isinstance(prev_obj, dict)
        elif name:
            prev_obj = self.get_object_by_name(name, host_name)
            result = prev_obj is not None and isinstance(prev_obj, dict)
        return (result, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("name", "name"),
            ("description", "description"),
            ("admin", "admin"),
            ("eap", "eap"),
            ("radius", "radius"),
            ("pxgrid", "pxgrid"),
            ("saml", "saml"),
            ("portal", "portal"),
            ("ims", "ims"),
            ("portalGroupTag", "portal_group_tag"),
            ("allowReplacementOfPortalGroupTag", "allow_replacement_of_portal_group_tag"),
            ("renewSelfSignedCertificate", "renew_self_signed_certificate"),
            ("expirationTTLPeriod", "expiration_ttl_period"),
            ("expirationTTLUnits", "expiration_ttl_units"),
            ("id", "id"),
            ("hostName", "host_name"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(not ise_compare_equality(current_obj.get(ise_param),
                                            requested_obj.get(ansible_param))
                   for (ise_param, ansible_param) in obj_params)

    def update(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        host_name = self.new_object.get("host_name")
        result = None
        if not id:
            id_ = self.get_object_by_name(name, host_name).get("id")
            self.new_object.update(dict(id=id_))
        result = self.ise.exec(
            family="certificates",
            function="update_system_certificate",
            params=self.new_object
        ).response
        return result

    def delete(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        host_name = self.new_object.get("host_name")
        result = None
        if not id:
            id_ = self.get_object_by_name(name, host_name).get("id")
            self.new_object.update(dict(id=id_))
        result = self.ise.exec(
            family="certificates",
            function="delete_system_certificate_by_id",
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
        obj = SystemCertificate(self._task.args, ise)

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
                ise.fail_json("Object does not exists, plugin only has update")
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
