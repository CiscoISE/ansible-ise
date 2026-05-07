#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
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
from ansible_collections.cisco.ise.plugins.plugin_utils.ise import (
    ISESDK,
    ise_argument_spec,
)

argument_spec = ise_argument_spec()
argument_spec.update(dict(
    id=dict(type="str"),
    adAttributes=dict(type="dict"),
    adScopesNames=dict(type="str"),
    adgroups=dict(type="dict"),
    advancedSettings=dict(type="dict"),
    description=dict(type="str"),
    domain=dict(type="str"),
    enableDomainAllowedList=dict(type="bool"),
    ERSActiveDirectoryDomains=dict(type="dict"),
    name=dict(type="str"),
))

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail(
                "ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'"
            )
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._supports_check_mode = False
        self._result = None

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

        ise = ISESDK(params=self._task.args)
        params = self._task.args

        response = ise.exec(
            family="active_directory",
            function="update_activedirectory_leave_by_id",
            params=dict(
                id=params.get("id"),
                ad_attributes=params.get("adAttributes"),
                ad_scopes_names=params.get("adScopesNames"),
                adgroups=params.get("adgroups"),
                advanced_settings=params.get("advancedSettings"),
                description=params.get("description"),
                domain=params.get("domain"),
                enable_domain_allowed_list=params.get("enableDomainAllowedList"),
                ers_active_directory_domains=params.get("ERSActiveDirectoryDomains"),
                name=params.get("name"),
            ),
        ).response

        self._result.update(dict(ise_response=response))
        self._result["changed"] = True
        self._result.update(ise.exit_json())
        return self._result
