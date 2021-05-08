#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
try:
    from ciscoisesdk import api, exceptions
except ImportError:
    ISE_SDK_IS_INSTALLED = False
else:
    ISE_SDK_IS_INSTALLED = True
from ansible.module_utils.basic import AnsibleModule
#from ansible_collections.cisco.ise.plugins.module_utils.exceptions import ()
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
    def __init__(self, params):
        self.result = dict(changed=False,result="")
        if ISE_SDK_IS_INSTALLED:
            self.api = api.IdentityServicesEngineAPI(
                username=params.get("ise_username"),
                password=params.get("ise_password"),
                base_url="https://{ise_hostname}".format(ise_hostname=params.get("ise_hostname")),
                verify=params.get("ise_verify"),
                version=params.get("ise_version"),
                wait_on_rate_limit=params.get("ise_wait_on_rate_limit"),
            )
        else:
            self.fail_json(msg="Cisco ISE Python SDK is not installed. Execute 'pip install ciscoisesdk'")

    def changed(self):
        self.result["changed"] = True

    def object_created(self):
        self.changed()
        self.result["result"] = "Object created"

    def object_updated(self):
        self.changed()
        self.result["result"] = "Object updated"

    def object_deleted(self):
        self.changed()
        self.result["result"] = "Object deleted"

    def object_already_absent(self):
        self.result["result"] = "Object already absent"

    def exec(self, family, function, params=None):
        try:
            family = getattr(self.api, family)
            func = getattr(family, function)
        except Exception as e:
            self.fail_json(msg=e)

        try:
            if params:
                response = func(**params)
            else:
                response = func()
        except exceptions.ApiError as e:
            self.fail_json(
                msg=(
                    "An error occured when executing operation."
                    " The error was: {error}"
                ).format(error=e)
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
