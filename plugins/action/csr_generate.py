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
        allowWildCardCert=dict(type="bool"),
        certificatePolicies=dict(type="str"),
        digestType=dict(type="str"),
        hostnames=dict(type="list"),
        keyLength=dict(type="str"),
        keyType=dict(type="str"),
        portalGroupTag=dict(type="str"),
        sanDNS=dict(type="list"),
        sanDir=dict(type="list"),
        sanIP=dict(type="list"),
        sanURI=dict(type="list"),
        subjectCity=dict(type="str"),
        subjectCommonName=dict(type="str"),
        subjectCountry=dict(type="str"),
        subjectOrg=dict(type="str"),
        subjectOrgUnit=dict(type="str"),
        subjectState=dict(type="str"),
        usedFor=dict(type="str"),
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
            allow_wild_card_cert=params.get("allowWildCardCert"),
            certificate_policies=params.get("certificatePolicies"),
            digest_type=params.get("digestType"),
            hostnames=params.get("hostnames"),
            key_length=params.get("keyLength"),
            key_type=params.get("keyType"),
            portal_group_tag=params.get("portalGroupTag"),
            san_dns=params.get("sanDNS"),
            san_dir=params.get("sanDir"),
            san_ip=params.get("sanIP"),
            san_uri=params.get("sanURI"),
            subject_city=params.get("subjectCity"),
            subject_common_name=params.get("subjectCommonName"),
            subject_country=params.get("subjectCountry"),
            subject_org=params.get("subjectOrg"),
            subject_org_unit=params.get("subjectOrgUnit"),
            subject_state=params.get("subjectState"),
            used_for=params.get("usedFor"),
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
            function="generate_csr",
            params=self.get_object(params),
        ).response

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
