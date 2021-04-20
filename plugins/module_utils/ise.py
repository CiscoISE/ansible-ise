#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
try:
    from isesdk import api
except ImportError:
    ISE_SDK_IS_INSTALLED = False
else:
    ISE_SDK_IS_INSTALLED = True
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.ise.plugins.module_utils.exceptions import (
    
)
try:
    from ansible.errors import AnsibleActionFail
except ImportError:
    ANSIBLE_ERRORS_INSTALLED = False
else:
    ANSIBLE_ERRORS_INSTALLED = True


def ise_argument_spec():
    argument_spec = dict(
        ise_host=dict(type="str", required=True),
        ise_port=dict(type="int", required=False, default=443),
        ise_username=dict(type="str", default="admin", aliases=["user"]),
        ise_password=dict(type="str", no_log=True),
        ise_verify=dict(type="bool", default=True),
        ise_version=dict(type="str", default="2.1.1"),
        validate_response_schema=dict(type="bool", default=True),
        state=dict(type="str", required=True, choices=["present", "absent", "query"]),
    )
    return argument_spec


class ISEModule(object):
    def __init__(self, moddef, params, verbosity):
        self.params = params
        self.verbosity = verbosity
        self.result = dict(changed=False)
        self.validate_response_schema = self.params.get("validate_response_schema")
        if ISE_SDK_IS_INSTALLED:
            self.api = api.ISEAPI(
                username=self.params.get("ise_username"),
                password=self.params.get("ise_password"),
                base_url="https://{ise_host}:{ise_port}".format(
                    ise_host=self.params.get("ise_host"), ise_port=self.params.get("ise_port")
                ),
                version=self.params.get("ise_version"),
                verify=self.params.get("ise_verify"),
            )
        else:
            self.fail_json(msg="Cisco ISE Python SDK is not installed. Execute 'pip install isesdk'")

    def changed(self):
        self.result["changed"] = True

    def disable_validation(self):
        self.params["active_validation"] = False

    def fail_json(self, msg, **kwargs):
        self.result.update(**kwargs)
        raise AnsibleActionFail(msg, kwargs)

    def exit_json(self):
        return self.result


def main():
    pass


if __name__ == "__main__":
    main()
