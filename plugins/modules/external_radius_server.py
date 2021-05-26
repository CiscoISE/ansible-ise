#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: external_radius_server
short_description: Resource module for External Radius Server
description:
- Manage operations create, update, delete of the resource External Radius Server.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    accountingPort:
      description: External Radius Server's accountingPort.
      type: int
    authenticationPort:
      description: External Radius Server's authenticationPort.
      type: int
    authenticatorKey:
      description: External Radius Server's authenticatorKey.
      type: str
    description:
      description: External Radius Server's description.
      type: str
    enableKeyWrap:
      description: EnableKeyWrap flag.
      type: bool
    encryptionKey:
      description: External Radius Server's encryptionKey.
      type: str
    hostIP:
      description: External Radius Server's hostIP.
      type: str
    id:
      description: External Radius Server's id.
      type: str
    keyInputFormat:
      description: External Radius Server's keyInputFormat.
      type: str
    name:
      description: External Radius Server's name.
      type: str
    proxyTimeout:
      description: External Radius Server's proxyTimeout.
      type: int
    retries:
      description: External Radius Server's retries.
      type: int
    sharedSecret:
      description: External Radius Server's sharedSecret.
      type: str
    timeout:
      description: External Radius Server's timeout.
      type: int
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.external_radius_server
# Reference by Internet resource
- name: External Radius Server reference
  description: Complete reference of the External Radius Server object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.external_radius_server:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accountingPort: 1813
    authenticationPort: 1812
    authenticatorKey: '20202020202020202020'
    description: example external radius server
    enableKeyWrap: true
    encryptionKey: '1616161616161616'
    hostIP: 1.1.1.1
    id: '123456789'
    keyInputFormat: ASCII
    name: externalRadiusServer1
    proxyTimeout: 300
    retries: 3
    sharedSecret: sharedSecret
    timeout: 5

- name: Update by id
  cisco.ise.external_radius_server:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accountingPort: 1813
    authenticationPort: 1812
    authenticatorKey: '20202020202020202020'
    description: example external radius server
    enableKeyWrap: true
    encryptionKey: '1616161616161616'
    hostIP: 1.1.1.1
    id: '123456789'
    keyInputFormat: ASCII
    name: externalRadiusServer1
    proxyTimeout: 300
    retries: 3
    sharedSecret: sharedSecret
    timeout: 5

- name: Delete by id
  cisco.ise.external_radius_server:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
