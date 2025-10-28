#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: ldap
short_description: Resource module for Ldap
description:
- Manage operation create of the resource Ldap.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  attributes:
    description: Ldap's attributes.
    suboptions:
      attributes:
        description: List of Attributes.
        type: list
    type: dict
  connectionSettings:
    description: Ldap's connectionSettings.
    suboptions:
      alwaysAccessPrimaryFirst:
        description: AlwaysAccessPrimaryFirst.
        type: bool
      failbackRetryDelay:
        description: FailbackRetryDelay.
        type: float
      failoverToSecondary:
        description: FailoverToSecondary.
        type: bool
      ldapNodeData:
        description: LdapNodeData.
        elements: dict
        type: list
      primaryServer:
        description: Ldap's primaryServer.
        suboptions:
          adminDN:
            description: AdminDN.
            type: str
          adminPassword:
            description: AdminPassword.
            type: str
          enableForceReconnect:
            description: EnableForceReconnect.
            type: bool
          enableSecureConnection:
            description: EnableSecureConnection.
            type: bool
          enableServerIdentityCheck:
            description: EnableServerIdentityCheck.
            type: bool
          forceReconnectTime:
            description: ForceReconnectTime.
            type: float
          hostName:
            description: HostName.
            type: str
          issuerCACertificate:
            description: IssuerCACertificate.
            type: str
          maxConnections:
            description: MaxConnections.
            type: float
          port:
            description: Port.
            type: float
          serverTimeout:
            description: ServerTimeout.
            type: float
          trustCertificate:
            description: TrustCertificate.
            type: str
          useAdminAccess:
            description: UseAdminAccess.
            type: bool
        type: dict
      secondaryServer:
        description: Ldap's secondaryServer.
        suboptions:
          adminDN:
            description: AdminDN.
            type: str
          adminPassword:
            description: AdminPassword.
            type: str
          enableForceReconnect:
            description: EnableForceReconnect.
            type: bool
          enableSecureConnection:
            description: EnableSecureConnection.
            type: bool
          enableServerIdentityCheck:
            description: EnableServerIdentityCheck.
            type: bool
          forceReconnectTime:
            description: ForceReconnectTime.
            type: float
          hostName:
            description: HostName.
            type: str
          issuerCACertificate:
            description: IssuerCACertificate.
            type: str
          maxConnections:
            description: MaxConnections.
            type: float
          port:
            description: Port.
            type: float
          serverTimeout:
            description: ServerTimeout.
            type: float
          trustCertificate:
            description: TrustCertificate.
            type: str
          useAdminAccess:
            description: UseAdminAccess.
            type: bool
        type: dict
      specifyServerForEachISENode:
        description: SpecifyServerForEachISENode.
        type: bool
    type: dict
  description:
    description: Description.
    type: str
  directoryOrganization:
    description: Ldap's directoryOrganization.
    suboptions:
      groupDirectorySubtree:
        description: GroupDirectorySubtree.
        type: str
      macFormat:
        description: MacFormat.
        type: dict
      prefixSeparator:
        description: PrefixSeparator.
        type: str
      stripPrefix:
        description: StripPrefix.
        type: bool
      stripSuffix:
        description: StripSuffix.
        type: str
      suffixSeparator:
        description: SuffixSeparator.
        type: str
      userDirectorySubtree:
        description: UserDirectorySubtree.
        type: str
    type: dict
  enablePasswordChangeLDAP:
    description: EnablePasswordChangeLDAP.
    type: bool
  generalSettings:
    description: Ldap's generalSettings.
    suboptions:
      certificate:
        description: Certificate.
        type: str
      groupMapAttributeName:
        description: GroupMapAttributeName.
        type: str
      groupMemberReference:
        description: GroupMemberReference.
        type: dict
      groupNameAttribute:
        description: GroupNameAttribute.
        type: str
      groupObjectClass:
        description: GroupObjectClass.
        type: str
      schema:
        description: Schema.
        type: dict
      userInfoAttributes:
        description: Ldap's userInfoAttributes.
        suboptions:
          additionalAttribute:
            description: AdditionalAttribute.
            type: str
          country:
            description: Country.
            type: str
          department:
            description: Department.
            type: str
          email:
            description: Email.
            type: str
          firstName:
            description: FirstName.
            type: str
          jobTitle:
            description: JobTitle.
            type: str
          lastName:
            description: LastName.
            type: str
          locality:
            description: Locality.
            type: str
          organizationalUnit:
            description: OrganizationalUnit.
            type: str
          stateOrProvince:
            description: StateOrProvince.
            type: str
          streetAddress:
            description: StreetAddress.
            type: str
          telephone:
            description: Telephone.
            type: str
        type: dict
      userNameAttribute:
        description: UserNameAttribute.
        type: str
      userObjectClass:
        description: UserObjectClass.
        type: str
    type: dict
  groups:
    description: Ldap's groups.
    suboptions:
      groupsNames:
        description: List of groups.
        type: list
    type: dict
  id:
    description: Id.
    type: str
  name:
    description: Name.
    type: str
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    ldap.Ldap.create_ldap,

  - Paths used are
    post /ldap/,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.ldap:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    attributes:
      attributes:
      - defaultValue: ' '
        internalName: whenChanged
        name: whenChanged
        type: STRING
    connectionSettings:
      alwaysAccessPrimaryFirst: true
      failbackRetryDelay: 5
      failoverToSecondary: true
      ldapNodeData:
      - name: ise222
        primaryHostname: ipAddress
        primaryPort: 389
        secondaryHostname: ipAddress
        secondaryPort: 389
      - name: ise223
        primaryHostname: ipAddress
        primaryPort: 389
        secondaryHostname: ipAddress
        secondaryPort: 389
      primaryServer:
        adminDN: cn=administrator,cn=users,dc=ise,dc=com
        adminPassword: Lab@123
        enableForceReconnect: false
        enableSecureConnection: false
        enableServerIdentityCheck: false
        forceReconnectTime: 20
        hostName: ''
        issuerCACertificate: ''
        maxConnections: 20
        port: 389
        serverTimeout: 10
        trustCertificate: ''
        useAdminAccess: true
      secondaryServer:
        adminDN: cn=administrator,cn=users,dc=ise,dc=com
        adminPassword: Lab@123
        enableForceReconnect: false
        enableSecureConnection: false
        enableServerIdentityCheck: false
        forceReconnectTime: 20
        hostName: ''
        issuerCACertificate: ''
        maxConnections: 20
        port: 389
        serverTimeout: 10
        trustCertificate: ''
        useAdminAccess: true
      specifyServerForEachISENode: true
    description: Description
    directoryOrganization:
      groupDirectorySubtree: groupDirectorySubtree
      macFormat: DASH
      prefixSeparator: \
      stripPrefix: false
      stripSuffix: false
      suffixSeparator: ' '
      userDirectorySubtree: userDirectorySubtree
    enablePasswordChangeLDAP: false
    generalSettings:
      certificate: userCertificate
      groupMapAttributeName: memberOf
      groupMemberReference: USERNAME
      groupNameAttribute: dn
      groupObjectClass: Group
      groupReference: GROUP_TO_USER
      schema: ACTIVE_DIRECTORY
      userInfoAttributes:
        country: co
        department: department
        email: email
        firstName: givenName
        lastName: sn
        locality: l
        organizationalUnit: company
        stateOrProvince: st
        streetAddress: streetAddress
        telephone: telephoneNumber
      userNameAttribute: userPrincipalName
      userObjectClass: Person
    groups:
      groupsNames:
      - CN=TestLDAP,CN=Users,DC=ISE,DC=COM
    name: sample

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""
