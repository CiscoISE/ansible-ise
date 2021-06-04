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
    name=dict(type="str"),
    description=dict(type="str"),
    eapTls=dict(type="dict"),
    peap=dict(type="dict"),
    eapFast=dict(type="dict"),
    eapTtls=dict(type="dict"),
    teap=dict(type="dict"),
    processHostLookup=dict(type="bool"),
    allowPapAscii=dict(type="bool"),
    allowChap=dict(type="bool"),
    allowMsChapV1=dict(type="bool"),
    allowMsChapV2=dict(type="bool"),
    allowEapMd5=dict(type="bool"),
    allowLeap=dict(type="bool"),
    allowEapTls=dict(type="bool"),
    allowEapTtls=dict(type="bool"),
    allowEapFast=dict(type="bool"),
    allowPeap=dict(type="bool"),
    allowTeap=dict(type="bool"),
    allowPreferredEapProtocol=dict(type="bool"),
    preferredEapProtocol=dict(type="str"),
    eapTlsLBit=dict(type="bool"),
    allowWeakCiphersForEap=dict(type="bool"),
    requireMessageAuth=dict(type="bool"),
    id=dict(type="str"),
))

required_if = [
    ("state", "present", ["id", "name"], True),
    ("state", "absent", ["id", "name"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class AllowedProtocols(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            name=params.get("name"),
            description=params.get("description"),
            eap_tls=params.get("eapTls"),
            peap=params.get("peap"),
            eap_fast=params.get("eapFast"),
            eap_ttls=params.get("eapTtls"),
            teap=params.get("teap"),
            process_host_lookup=params.get("processHostLookup"),
            allow_pap_ascii=params.get("allowPapAscii"),
            allow_chap=params.get("allowChap"),
            allow_ms_chap_v1=params.get("allowMsChapV1"),
            allow_ms_chap_v2=params.get("allowMsChapV2"),
            allow_eap_md5=params.get("allowEapMd5"),
            allow_leap=params.get("allowLeap"),
            allow_eap_tls=params.get("allowEapTls"),
            allow_eap_ttls=params.get("allowEapTtls"),
            allow_eap_fast=params.get("allowEapFast"),
            allow_peap=params.get("allowPeap"),
            allow_teap=params.get("allowTeap"),
            allow_preferred_eap_protocol=params.get("allowPreferredEapProtocol"),
            preferred_eap_protocol=params.get("preferredEapProtocol"),
            eap_tls_l_bit=params.get("eapTlsLBit"),
            allow_weak_ciphers_for_eap=params.get("allowWeakCiphersForEap"),
            require_message_auth=params.get("requireMessageAuth"),
            id=params.get("id"),
        )

    def get_object_by_name(self, name):
        try:
            result = self.ise.exec(
                family="allowed_protocols",
                function="get_allowed_protocol_by_name",
                params={"name": quote(name)}
            ).response['AllowedProtocols']
        except Exception as e:
            result = None
        return result

    def get_object_by_id(self, id):
        try:
            result = self.ise.exec(
                family="allowed_protocols",
                function="get_allowed_protocol_by_id",
                params={"id": quote(id)}
            ).response['AllowedProtocols']
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
            family="allowed_protocols",
            function="create_allowed_protocol",
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
            family="allowed_protocols",
            function="update_allowed_protocol_by_id",
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
            family="allowed_protocols",
            function="delete_allowed_protocol_by_id",
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
        obj = AllowedProtocols(self._task.args, ise)

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
