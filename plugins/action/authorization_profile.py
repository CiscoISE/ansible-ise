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
    state=dict(type="str", default="present", choices=["present", "absent"]),
    id=dict(type="str"),
    name=dict(type="str"),
    description=dict(type="str"),
    advancedAttributes=dict(type="list"),
    accessType=dict(type="str"),
    authzProfileType=dict(type="str"),
    vlan=dict(type="dict"),
    reauth=dict(type="dict"),
    airespaceACL=dict(type="str"),
    airespaceIPv6ACL=dict(type="str"),
    webRedirection=dict(type="dict"),
    acl=dict(type="str"),
    trackMovement=dict(type="bool"),
    serviceTemplate=dict(type="bool"),
    easywiredSessionCandidate=dict(type="bool"),
    daclName=dict(type="str"),
    voiceDomainPermission=dict(type="bool"),
    neat=dict(type="bool"),
    webAuth=dict(type="bool"),
    autoSmartPort=dict(type="str"),
    interfaceTemplate=dict(type="str"),
    ipv6ACLFilter=dict(type="str"),
    avcProfile=dict(type="str"),
    macSecPolicy=dict(type="str"),
    asaVpn=dict(type="str"),
    profileName=dict(type="str"),
    ipv6DaclName=dict(type="str"),
))

required_if = [
    ("state", "present", ["id", "name"], True),
    ("state", "absent", ["id", "name"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class AuthorizationProfile(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            id=params.get("id"),
            name=params.get("name"),
            description=params.get("description"),
            advanced_attributes=params.get("advancedAttributes"),
            access_type=params.get("accessType"),
            authz_profile_type=params.get("authzProfileType"),
            vlan=params.get("vlan"),
            reauth=params.get("reauth"),
            airespace_acl=params.get("airespaceACL"),
            airespace_i_pv6_acl=params.get("airespaceIPv6ACL"),
            web_redirection=params.get("webRedirection"),
            acl=params.get("acl"),
            track_movement=params.get("trackMovement"),
            service_template=params.get("serviceTemplate"),
            easywired_session_candidate=params.get("easywiredSessionCandidate"),
            dacl_name=params.get("daclName"),
            voice_domain_permission=params.get("voiceDomainPermission"),
            neat=params.get("neat"),
            web_auth=params.get("webAuth"),
            auto_smart_port=params.get("autoSmartPort"),
            interface_template=params.get("interfaceTemplate"),
            ipv6_acl_filter=params.get("ipv6ACLFilter"),
            avc_profile=params.get("avcProfile"),
            mac_sec_policy=params.get("macSecPolicy"),
            asa_vpn=params.get("asaVpn"),
            profile_name=params.get("profileName"),
            ipv6_dacl_name=params.get("ipv6DaclName"),
        )

    def get_object_by_name(self, name):
        try:
            result = self.ise.exec(
                family="authorization_profile",
                function="get_authorization_profile_by_name",
                params={"name": quote(name)}
            ).response['AuthorizationProfile']
        except Exception as e:
            result = None
        return result

    def get_object_by_id(self, id):
        try:
            result = self.ise.exec(
                family="authorization_profile",
                function="get_authorization_profile_by_id",
                params={"id": quote(id)}
            ).response['AuthorizationProfile']
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
            family="authorization_profile",
            function="create_authorization_profile",
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
            family="authorization_profile",
            function="update_authorization_profile_by_id",
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
            family="authorization_profile",
            function="delete_authorization_profile_by_id",
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
        obj = AuthorizationProfile(self._task.args, ise)

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
