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
    ise_compare_equality,
    get_dict_result,
)
from ansible_collections.cisco.ise.plugins.plugin_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(
    dict(
        state=dict(type="str", default="present", choices=["present"]),
        authType=dict(type="str"),
        certId=dict(type="str"),
        configureVti=dict(type="bool"),
        espAhProtocol=dict(type="str"),
        hostName=dict(type="str"),
        iface=dict(type="str"),
        ikeReAuthTime=dict(type="int"),
        ikeVersion=dict(type="str"),
        localInternalIp=dict(type="str"),
        modeOption=dict(type="str"),
        nadIp=dict(type="str"),
        phaseOneDHGroup=dict(type="str"),
        phaseOneEncryptionAlgo=dict(type="str"),
        phaseOneHashAlgo=dict(type="str"),
        phaseOneLifeTime=dict(type="int"),
        phaseTwoDHGroup=dict(type="str"),
        phaseTwoEncryptionAlgo=dict(type="str"),
        phaseTwoHashAlgo=dict(type="str"),
        phaseTwoLifeTime=dict(type="int"),
        psk=dict(type="str"),
        remotePeerInternalIp=dict(type="str"),
    )
)

required_if = [
    ("state", "present", [], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class Ipsec(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            auth_type=params.get("authType"),
            cert_id=params.get("certId"),
            configure_vti=params.get("configureVti"),
            esp_ah_protocol=params.get("espAhProtocol"),
            host_name=params.get("hostName"),
            iface=params.get("iface"),
            ike_re_auth_time=params.get("ikeReAuthTime"),
            ike_version=params.get("ikeVersion"),
            local_internal_ip=params.get("localInternalIp"),
            mode_option=params.get("modeOption"),
            nad_ip=params.get("nadIp"),
            phase_one_dhgroup=params.get("phaseOneDHGroup"),
            phase_one_encryption_algo=params.get("phaseOneEncryptionAlgo"),
            phase_one_hash_algo=params.get("phaseOneHashAlgo"),
            phase_one_life_time=params.get("phaseOneLifeTime"),
            phase_two_dhgroup=params.get("phaseTwoDHGroup"),
            phase_two_encryption_algo=params.get("phaseTwoEncryptionAlgo"),
            phase_two_hash_algo=params.get("phaseTwoHashAlgo"),
            phase_two_life_time=params.get("phaseTwoLifeTime"),
            psk=params.get("psk"),
            remote_peer_internal_ip=params.get("remotePeerInternalIp"),
        )

    def get_object_by_name(self, name):
        # NOTICE: Get does not support/work for filter by name with EQ
        result = None
        gen_items_responses = self.ise.exec(
            family="native_ipsec", function="get_ipsec_enabled_nodes_generator"
        )
        try:
            for items_response in gen_items_responses:
                items = items_response.response.get("response", [])
                result = get_dict_result(items, "name", name)
                if result:
                    return result
        except (TypeError, AttributeError) as e:
            self.ise.fail_json(
                msg=(
                    "An error occured when executing operation."
                    " Check the configuration of your API Settings and API Gateway settings on your ISE server."
                    " This collection assumes that the API Gateway, the ERS APIs and OpenAPIs are enabled."
                    " You may want to enable the (ise_debug: True) argument."
                    " The error was: {error}"
                ).format(error=e)
            )
        except Exception:
            result = None
            return result
        return result

    def get_object_by_id(self, id):
        # NOTICE: Does not have a get by id method or it is in another action
        result = None
        return result

    def exists(self):
        prev_obj = None
        id_exists = False
        name_exists = False
        o_id = self.new_object.get("id")
        name = self.new_object.get("name")
        if o_id:
            prev_obj = self.get_object_by_id(o_id)
            id_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if not id_exists and name:
            prev_obj = self.get_object_by_name(name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            if id_exists and name_exists and o_id != _id:
                raise InconsistentParameters(
                    "The 'id' and 'name' params don't refer to the same object"
                )
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("authType", "auth_type"),
            ("certId", "cert_id"),
            ("configureVti", "configure_vti"),
            ("espAhProtocol", "esp_ah_protocol"),
            ("hostName", "host_name"),
            ("iface", "iface"),
            ("ikeReAuthTime", "ike_re_auth_time"),
            ("ikeVersion", "ike_version"),
            ("localInternalIp", "local_internal_ip"),
            ("modeOption", "mode_option"),
            ("nadIp", "nad_ip"),
            ("phaseOneDHGroup", "phase_one_dhgroup"),
            ("phaseOneEncryptionAlgo", "phase_one_encryption_algo"),
            ("phaseOneHashAlgo", "phase_one_hash_algo"),
            ("phaseOneLifeTime", "phase_one_life_time"),
            ("phaseTwoDHGroup", "phase_two_dhgroup"),
            ("phaseTwoEncryptionAlgo", "phase_two_encryption_algo"),
            ("phaseTwoHashAlgo", "phase_two_hash_algo"),
            ("phaseTwoLifeTime", "phase_two_life_time"),
            ("psk", "psk"),
            ("remotePeerInternalIp", "remote_peer_internal_ip"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(
            not ise_compare_equality(
                current_obj.get(ise_param), requested_obj.get(ansible_param)
            )
            for (ise_param, ansible_param) in obj_params
        )

    def create(self):
        result = self.ise.exec(
            family="native_ipsec",
            function="create_ipsec_connection",
            params=self.new_object,
        ).response
        return result

    def update(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        result = self.ise.exec(
            family="native_ipsec",
            function="update_ipsec_connection_config",
            params=self.new_object,
        ).response
        return result


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

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        ise = ISESDK(params=self._task.args)
        obj = Ipsec(self._task.args, ise)

        state = self._task.args.get("state")

        response = None
        if state == "present":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                if obj.requires_update(prev_obj):
                    ise_update_response = obj.update()
                    self._result.update(dict(ise_update_response=ise_update_response))
                    (obj_exists, updated_obj) = obj.exists()
                    response = updated_obj
                    ise.object_updated()
                else:
                    response = prev_obj
                    ise.object_already_present()
            else:
                ise_create_response = obj.create()
                (obj_exists, created_obj) = obj.exists()
                response = created_obj
                ise.object_created()

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
