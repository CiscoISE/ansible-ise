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

    def get_object(self, params):
        new_object = dict(
            name=params.get("name"),
            status=params.get("status"),
            description=params.get("description"),
            enable_ocs_p_validation=params.get("enableOCSPValidation"),
            selected_ocs_p_service=params.get("selectedOCSPService"),
            reject_if_no_status_from_ocs_p=params.get("rejectIfNoStatusFromOCSP"),
            reject_if_unreachable_from_ocs_p=params.get("rejectIfUnreachableFromOCSP"),
            download_crl=params.get("downloadCRL"),
            crl_distribution_url=params.get("crlDistributionUrl"),
            automatic_crl_update=params.get("automaticCRLUpdate"),
            automatic_crl_update_period=params.get("automaticCRLUpdatePeriod"),
            automatic_crl_update_units=params.get("automaticCRLUpdateUnits"),
            non_automatic_crl_update_period=params.get("nonAutomaticCRLUpdatePeriod"),
            non_automatic_crl_update_units=params.get("nonAutomaticCRLUpdateUnits"),
            crl_download_failure_retries=params.get("crlDownloadFailureRetries"),
            crl_download_failure_retries_units=params.get("crlDownloadFailureRetriesUnits"),
            enable_server_identity_check=params.get("enableServerIdentityCheck"),
            authenticate_before_crl_received=params.get("authenticateBeforeCRLReceived"),
            ignore_crl_expiration=params.get("ignoreCRLExpiration"),
            trust_for_ise_auth=params.get("trustForIseAuth"),
            trust_for_client_auth=params.get("trustForClientAuth"),
            trust_for_cisco_services_auth=params.get("trustForCiscoServicesAuth"),
            trust_for_certificate_based_admin_auth=params.get("trustForCertificateBasedAdminAuth"),
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
                function='get_trusted_certificate_by_id',
                params=self.get_object(self._task.args)
            ).response
            self._result.update(dict(ise_response=response))
            self._result.update(ise.exit_json())
            return self._result
        if not name and not id:
            response = []
            generator = ise.exec(
                family="certificates",
                function='get_all_trusted_certificates_generator',
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
