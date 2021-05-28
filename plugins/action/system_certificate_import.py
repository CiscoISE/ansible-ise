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
    name=dict(type="str"),
    password=dict(type="str"),
    data=dict(type="str"),
    privateKeyData=dict(type="str"),
    portalGroupTag=dict(type="str"),
    admin=dict(type="bool"),
    eap=dict(type="bool"),
    radius=dict(type="bool"),
    pxgrid=dict(type="bool"),
    saml=dict(type="bool"),
    portal=dict(type="bool"),
    ims=dict(type="bool"),
    allowWildCardCertificates=dict(type="bool"),
    validateCertificateExtensions=dict(type="bool"),
    allowSHA1Certificates=dict(type="bool"),
    allowOutOfDateCert=dict(type="bool"),
    allowReplacementOfCertificates=dict(type="bool"),
    allowReplacementOfPortalGroupTag=dict(type="bool"),
    allowExtendedValidity=dict(type="bool"),
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
            name=params.get("name"),
            password=params.get("password"),
            data=params.get("data"),
            private_key_data=params.get("privateKeyData"),
            portal_group_tag=params.get("portalGroupTag"),
            admin=params.get("admin"),
            eap=params.get("eap"),
            radius=params.get("radius"),
            pxgrid=params.get("pxgrid"),
            saml=params.get("saml"),
            portal=params.get("portal"),
            ims=params.get("ims"),
            allow_wild_card_certificates=params.get("allowWildCardCertificates"),
            validate_certificate_extensions=params.get("validateCertificateExtensions"),
            allow_sha1_certificates=params.get("allowSHA1Certificates"),
            allow_out_of_date_cert=params.get("allowOutOfDateCert"),
            allow_replacement_of_certificates=params.get("allowReplacementOfCertificates"),
            allow_replacement_of_portal_group_tag=params.get("allowReplacementOfPortalGroupTag"),
            allow_extended_validity=params.get("allowExtendedValidity"),
        )
        return new_object

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        ise = ISESDK(params=self._task.args)

        response = ise.exec(
            family="certificates",
            function='import_system_certificate',
            params=self.get_object(self._task.args),
        ).response
        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
