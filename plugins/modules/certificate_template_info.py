#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: certificate_template_info
short_description: Information module for Certificate Template
description:
- Get all Certificate Template.
- Get Certificate Template by id.
- Get Certificate Template by name.
- This API allows the client to get a certificate template by ID.
- This API allows the client to get a certificate template by name.
- This API allows the client to get aall the certificate templates.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  name:
    description:
    - Name path parameter.
    type: str
  id:
    description:
    - Id path parameter.
    type: str
  page:
    description:
    - Page query parameter. Page number.
    type: int
  size:
    description:
    - Size query parameter. Number of objects returned per page.
    type: int
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    certificate_template.CertificateTemplate.get_certificate_template_by_id,
    certificate_template.CertificateTemplate.get_certificate_template_by_name,
    certificate_template.CertificateTemplate.get_certificate_template_generator,

  - Paths used are
    get /ers/config/certificatetemplate/,
    get /ers/config/certificatetemplate/name/{name},
    get /ers/config/certificatetemplate/{id},

"""

EXAMPLES = r"""
- name: Get all Certificate Template
  cisco.ise.certificate_template_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result

- name: Get Certificate Template by id
  cisco.ise.certificate_template_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

- name: Get Certificate Template by name
  cisco.ise.certificate_template_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "keySize": 0,
      "validityPeriod": 0,
      "raprofile": "string"
    }

ise_responses:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "keySize": 0,
        "validityPeriod": 0,
        "raprofile": "string"
      }
    ]
"""
