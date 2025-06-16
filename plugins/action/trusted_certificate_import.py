#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible_collections.cisco.ise.plugins.plugin_utils.action import ActionModule as ActionBase
from ansible_collections.cisco.ise.plugins.plugin_utils.ise import (
    ISESDK,
    ise_argument_spec,
)

# Get common arguements specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(
    dict(
        allowBasicConstraintCAFalse=dict(type="bool"),
        allowOutOfDateCert=dict(type="bool"),
        allowSHA1Certificates=dict(type="bool"),
        data=dict(type="str"),
        description=dict(type="str"),
        name=dict(type="str"),
        trustForCertificateBasedAdminAuth=dict(type="bool"),
        trustForCiscoServicesAuth=dict(type="bool"),
        trustForClientAuth=dict(type="bool"),
        trustForIseAuth=dict(type="bool"),
        validateCertificateExtensions=dict(type="bool"),
    )
)

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class ActionModule(ActionBase):
    _supports_check_mode = False

    def get_object(self, params):
        new_object = dict(
            allow_basic_constraint_cafalse=params.get("allowBasicConstraintCAFalse"),
            allow_out_of_date_cert=params.get("allowOutOfDateCert"),
            allow_sha1_certificates=params.get("allowSHA1Certificates"),
            data=params.get("data"),
            description=params.get("description"),
            name=params.get("name"),
            trust_for_certificate_based_admin_auth=params.get(
                "trustForCertificateBasedAdminAuth"
            ),
            trust_for_cisco_services_auth=params.get("trustForCiscoServicesAuth"),
            trust_for_client_auth=params.get("trustForClientAuth"),
            trust_for_ise_auth=params.get("trustForIseAuth"),
            validate_certificate_extensions=params.get("validateCertificateExtensions"),
        )
        return new_object

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        _, validated_arguments = self.validate_argument_spec(
            argument_spec=argument_spec,
            mutually_exclusive=mutually_exclusive,
            required_if=required_if,
            required_one_of=required_one_of,
            required_together=required_together,
        )
        params = {k: v, for k, v in validated_arguments if k in self._task.args}

        ise = ISESDK(params=params)

        response = ise.exec(
            family="certificates",
            function="import_trust_certificate",
            params=self.get_object(params),
        ).response

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
