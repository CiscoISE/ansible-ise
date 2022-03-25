#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_deployment_info
short_description: Information module for Node Deployment
description:
- Get all Node Deployment.
- Get Node Deployment by name.
- The API lists all the nodes that are deployed in the cluster.
- This API retrieves detailed information of the deployed node.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  filter:
    description:
    - >
      Filter query parameter. <div> <style type="text/css" scoped> .apiServiceTable td, .apiServiceTable th {
      padding 5px 10px !important; text-align left; } </style> <span> <b>Simple filtering</b> is available through
      the filter query string parameter. The structure of a filter is a triplet of field operator and value,
      separated by dots. More than one filter can be sent. The logical operator common to all filter criteria is
      AND by default, and can be changed by using the <i>"filterType=or"</i> query string parameter. Each resource
      Data model description should specify if an attribute is a filtered field. </span> <br /> <table
      class="apiServiceTable"> <thead> <tr> <th>OPERATOR</th> <th>DESCRIPTION</th> </tr> </thead> <tbody> <tr>
      <td>EQ</td> <td>Equals</td> </tr> <tr> <td>NEQ</td> <td>Not Equals</td> </tr> <tr> <td>STARTSW</td>
      <td>Starts With</td> </tr> <tr> <td>NSTARTSW</td> <td>Not Starts With</td> </tr> <tr> <td>ENDSW</td>
      <td>Ends With</td> </tr> <tr> <td>NENDSW</td> <td>Not Ends With</td> </tr> <tr> <td>CONTAINS</td>
      <td>Contains</td> </tr> <tr> <td>NCONTAINS</td> <td>Not Contains</td> </tr> </tbody> </table> </div>.
    elements: str
    type: list
  filterType:
    description:
    - >
      FilterType query parameter. The logical operator common to all filter criteria is AND by default, and can be
      changed by using this parameter.
    type: str
  hostname:
    description:
    - Hostname path parameter. Hostname of the deployed node.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    node_deployment.NodeDeployment.get_node_details,
    node_deployment.NodeDeployment.get_nodes,

  - Paths used are
    get /api/v1/deployment/node,
    get /api/v1/deployment/node/{hostname},

"""

EXAMPLES = r"""
- name: Get all Node Deployment
  cisco.ise.node_deployment_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    filter: []
    filterType: string
  register: result

- name: Get Node Deployment by name
  cisco.ise.node_deployment_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    hostname: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "fqdn": "string",
      "hostname": "string",
      "ipAddress": "string",
      "nodeStatus": "string",
      "roles": [
        "string"
      ],
      "services": [
        "string"
      ]
    }
"""
