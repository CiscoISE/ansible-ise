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
        ise_hostname=dict(type="str", required=True),
        ise_username=dict(type="str", required=True),
        ise_password=dict(type="str", required=True, no_log=True),
        ise_verify=dict(type="bool", default=True),
        ise_version=dict(type="str", default="3.0.0"),
        ise_wait_on_rate_limit=dict(type="bool", default=True), # TODO: verify what the true default value should be 
    )
    return argument_spec


class ISESDK(object):
    def __init__(self):
        self.result = dict(changed=False)
        if ISE_SDK_IS_INSTALLED:
            self.api = api.IdentityServicesEngineAPI(
                username=self.params.get("ise_username"),
                password=self.params.get("ise_password"),
                base_url="https://{ise_hostname}".format(ise_hostname=self.params.get("ise_hostname")),
                verify=self.params.get("ise_verify"),
                version=self.params.get("ise_version"),
                wait_on_rate_limit=self.params.get("ise_wait_on_rate_limit"),
            )
        else:
            self.fail_json(msg="Cisco ISE Python SDK is not installed. Execute 'pip install isesdk'")

    def changed(self):
        self.result["changed"] = True

    def exec(self, family, function, params):
        try:
            family = getattr(self.api, family)
            func = getattr(family, function)
        except Exception as e:
            self.fail_json(msg=e)

        try:
            response = func(params)
        except Exception as e:
            self.fail_json(
                msg=(
                    "An error occured when executing operation."
                    " The error was: {error}"
                ).format(error=to_native(e))
            )
        return response



    def fail_json(self, msg, **kwargs):
        self.result.update(**kwargs)
        raise AnsibleActionFail(msg, kwargs)

    def exit_json(self):
        return self.result


def main():
    pass


if __name__ == "__main__":
    main()
