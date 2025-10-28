#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: mnt_session_by_mac_info
short_description: Information module for MNT Session By Mac
description:
  - Get MNT Session By Mac by id.
  - Returns detailed information for a given MAC address.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  mac:
    description:
      - Mac path parameter. The MAC address to retrieve information for.
    type: str
requirements:
  - ciscoisesdk >= 2.0.1
  - python >= 3.5
notes:
  - SDK Method used are
    misc.Misc.get_full_s_d_mac_info,
  - Paths used are
    get /Session/MACAddress/{mac},
"""
EXAMPLES = r"""
---
- name: Get MNT Session By Mac by id
  cisco.ise.mnt_session_by_mac_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    mac: 00:14:22:01:23:45
  register: result
"""
RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "passed": {},
      "failed": {},
      "user_name": "string",
      "nas_ip_address": "string",
      "failure_reason": "string",
      "calling_station_id": "string",
      "orig_calling_station_id": "string",
      "cpmsession_id": "string",
      "destination_ip_address": "string",
      "device_ip_address": "string",
      "identity_group": "string",
      "network_device_name": "string",
      "acs_server": "string",
      "authentication_method": "string",
      "authentication_protocol": "string",
      "framed_ip_address": "string",
      "auth_acs_timestamp": "string",
      "execution_steps": "string",
      "response": "string",
      "audit_session_id": "string",
      "nas_port_id": "string",
      "posture_status": "string",
      "selected_azn_profiles": "string",
      "service_type": "string",
      "message_code": "string",
      "auth_acsview_timestamp": "string",
      "auth_id": 0,
      "identity_store": "string",
      "cts_security_group": "string",
      "location": "string",
      "device_type": "string",
      "response_time": 0,
      "nas_ipv6_address": "string",
      "framed_ipv6_address": {
        "ipv6_address": [
          "string"
        ]
      },
      "other_attr_string": "string",
      "acct_id": 0,
      "acct_acs_timestamp": "string",
      "acct_acsview_timestamp": "string",
      "acct_session_id": "string",
      "acct_status_type": "string",
      "acct_session_time": 0,
      "acct_input_octets": "string",
      "acct_output_octets": "string",
      "acct_input_packets": 0,
      "acct_output_packets": 0,
      "acct_class": "string",
      "acct_terminate_cause": "string",
      "acct_multi_session_id": "string",
      "acct_authentic": "string",
      "termination_action": "string",
      "session_timeout": "string",
      "idle_timeout": "string",
      "acct_interim_interval": "string",
      "acct_delay_time": "string",
      "event_timestamp": "string",
      "acct_tunnel_connection": "string",
      "acct_tunnel_packet_lost": "string",
      "security_group": "string",
      "cisco_h323_setup_time": "string",
      "cisco_h323_connect_time": "string",
      "cisco_h323_disconnect_time": "string",
      "framed_protocol": "string",
      "started": {},
      "stopped": {},
      "ckpt_id": 0,
      "type": 0,
      "nad_acsview_timestamp": "string",
      "vlan": "string",
      "dacl": "string",
      "authentication_type": "string",
      "interface_name": "string",
      "reason": "string",
      "endpoint_policy": "string",
      "vn": "string"
    }
"""
