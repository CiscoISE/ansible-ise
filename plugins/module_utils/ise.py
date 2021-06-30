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

try:
    from ansible.errors import AnsibleActionFail
except ImportError:
    ANSIBLE_ERRORS_INSTALLED = False
else:
    ANSIBLE_ERRORS_INSTALLED = True


def is_list_complex(x):
    return isinstance(x[0], dict) or isinstance(x[0], list)


def has_diff_elem(ls1, ls2):
    return any((elem not in ls1 for elem in ls2))


def compare_list(list1, list2):
    len_list1 = len(list1)
    len_list2 = len(list2)
    if len_list1 != len_list2:
        return False

    if len_list1 == 0:
        return True

    attempt_std_cmp = list1 == list2
    if attempt_std_cmp:
        return True

    if not is_list_complex(list1) and not is_list_complex(list2):
        return set(list1) == set(list2)

    # Compare normally if it exceeds expected size * 2 (len_list1==len_list2)
    MAX_SIZE_CMP = 100
    # Fail fast if elem not in list, thanks to any and generators
    if len_list1 > MAX_SIZE_CMP:
        return attempt_std_cmp
    else:
        # not changes 'has diff elem' to list1 != list2 ':lists are not equal'
        return not(has_diff_elem(list1, list2)) or not(has_diff_elem(list2, list1))


def fn_comp_key(k, dict1, dict2):
    return ise_compare_equality(dict1.get(k), dict2.get(k))


def ise_compare_equality(current_value, requested_value):
    if requested_value is None:
        return True
    if current_value is None:
        return True
    if isinstance(current_value, dict) and isinstance(requested_value, dict):
        all_dict_params = list(current_value.keys()) + list(requested_value.keys())
        return not any((not fn_comp_key(param, current_value, requested_value) for param in all_dict_params))
    elif isinstance(current_value, list) and isinstance(requested_value, list):
        return compare_list(current_value, requested_value)
    else:
        return current_value == requested_value


def get_dict_result(result, key, value):
    if isinstance(result, list):
        if len(result) == 1:
            if isinstance(result[0], dict):
                result = result[0]
            else:
                result = None
        else:
            for item in result:
                if isinstance(item, dict) and item.get(key) == value:
                    result = item
                    return result
            result = None
    elif not isinstance(result, dict):
        result = None
    return result


def ise_argument_spec():
    argument_spec = dict(
        ise_hostname=dict(type="str", required=True),
        ise_username=dict(type="str", required=True),
        ise_password=dict(type="str", required=True, no_log=True),
        ise_verify=dict(type="bool", default=True),
        ise_version=dict(type="str", default="3.0.0"),
        ise_wait_on_rate_limit=dict(type="bool", default=True),  # TODO: verify what the true default value should be
    )
    return argument_spec


class ISESDK(object):
    def __init__(self, params):
        self.result = dict(changed=False, result="")
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

    def object_already_present(self):
        self.result["result"] = "Object already present"

    def object_present_and_different(self):
        self.result["result"] = "Object already present, but it has different values to the requested"

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
        except exceptions.ciscoisesdkException as e:
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
