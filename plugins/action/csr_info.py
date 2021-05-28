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
    page=dict(type="int"),
    size=dict(type="int"),
    sort=dict(type="str"),
    sortBy=dict(type="str"),
    filter=dict(type="list"),
    filterType=dict(type="str"),
    hostName=dict(type="str"),
    id=dict(type="str"),
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

    def get_object(params):
        new_object = dict(
            hostnames=params.get("hostnames"),
            allow_wild_card_cert=params.get("allowWildCardCert"),
            subject_common_name=params.get("subjectCommonName"),
            subject_org_unit=params.get("subjectOrgUnit"),
            subject_org=params.get("subjectOrg"),
            subject_city=params.get("subjectCity"),
            subject_state=params.get("subjectState"),
            subject_country=params.get("subjectCountry"),
            san_dns=params.get("sanDNS"),
            san_ip=params.get("sanIP"),
            san_uri=params.get("sanURI"),
            san_dir=params.get("sanDir"),
            key_length=params.get("keyLength"),
            key_type=params.get("keyType"),
            digest_type=params.get("digestType"),
            used_for=params.get("usedFor"),
            certificate_policies=params.get("certificatePolicies"),
            portal_group_tag=params.get("portalGroupTag"),
            host_name=params.get("hostName"),
            id=params.get("id"),
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
                family="certificates",
                function='get_csr_by_id',
                params=self.get_object(self._task.args)
            ).response
            self._result.update(dict(ise_response=response))
            self._result.update(ise.exit_json())
            return self._result
        if not name and not id:
            response = []
            generator = ise.exec(
                family="certificates",
                function='get_csr_generator',
                params=self.get_object(self._task.args),
            )
            for item in generator:
                tmp_response = item.response
                if isinstance(tmp_response, list):
                    response += tmp_response
                else:
                    response.append(tmp_response)
            self._result.update(dict(ise_response=response))
            self._result.update(ise.exit_json())
            return self._result
