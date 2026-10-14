=======================
Cisco ISE Release Notes
=======================

.. contents:: Topics

v3.3.0
======

Release Summary
---------------

Bug fixes for open issues, certificate-based authentication and the restored anc_endpoint_apply module. Requires ciscoisesdk 2.4.7.

Minor Changes
-------------

- Added certificate-based (mTLS) authentication with ise_client_cert and ise_client_key (#179).
- Restored the anc_endpoint_apply module (#190).
- The collection requires ansible-core 2.16 or later and ciscoisesdk 2.4.7 or later.
- requirements.txt is included in the collection for execution environments.
- stop_replication - isEnabled is required when state is present (#184).

Bugfixes
--------

- The documented default of ise_version is 3.5.0.
- active_directory_add_groups, active_directory_join_domain, active_directory_leave_domain, node_deployment_sync, node_group_node_create, node_group_node_delete - report changed after the operation.
- authorization_profile, certificate_profile, external_radius_server, sgmapping, sgmappinggroup, sponsor_group, sxp_connections - parameters declared as dict use bool, int or str.
- csr_export_info, trusted_certificate_export_info - fail with a clear message when filename is given without id (#185).
- endpoint - updates an existing endpoint and finds it by MAC address regardless of separators or name (#163, #181).
- guest_user and the modules of renamed SDK families work with ise_version 3.5.0 (#180).
- info modules return the object when name is given instead of None (#185).
- ipsec_enable, ipsec_disable, ipsec_delete, ``adresourcereservation_``, mnt_athentication_status_info, restidstoresettings_info, node_sync - fixed calls to SDK methods that do not exist for ISE 3.5.0.
- ise_debug - the debug output is complete on ansible-core 2.19 and later.
- network_device - applies settings missing on the device and keeps the values that are not given on update (#157, #160).
- personas_export_certs - sends hostName on export and uses the primary node credentials on import (#162).
- repository - restored path, password, serverName, userName and enablePki, and fixed the lookup and delete (#188).
- repository_files_info - lists the files when repositoryName is given. repositoryName is required (#192).
- sgt - value is an integer (#48).
- stop_replication - reads and sets the deployment status instead of failing (#184).
- tasks_info - uses taskId and the existing SDK methods (#185).

v3.2.0
======

Release Summary
---------------

Restore 16 critical modules removed in v3.0.0. All deployment, node group, node services profiler, and active directory sub-operation modules are back.

Major Changes
-------------

- Restored active_directory_add_groups module.
- Restored active_directory_groups_by_domain_info module.
- Restored active_directory_join_domain module.
- Restored active_directory_leave_domain module.
- Restored node_deployment and node_deployment_info modules.
- Restored node_deployment_sync module.
- Restored node_group and node_group_info modules.
- Restored node_group_node_info, node_group_node_create, node_group_node_delete modules.
- Restored node_secondary_to_primary module.
- Restored node_services_profiler_probe_config and node_services_profiler_probe_config_info modules.
- Restored node_standalone_to_primary module.

v3.1.0
======

Release Summary
---------------

Restore snake_case module names and add backward-compatibility routing for 3.0.x playbooks.

Bugfixes
--------

- Added 76 plugin_routing.modules redirects in meta/runtime.yml mapping 3.0.x camelCase module names (e.g. networkdevice, byodportal) to their snake_case equivalents (e.g. network_device, byod_portal), enabling backward compatibility for existing playbooks.
- Added action_groups in meta/runtime.yml for nbar_app (trustsec_nbar_app, trustsec_nbar_app_info) and virtual_network (trustsec_vn, trustsec_vn_bulk_create, trustsec_vn_bulk_delete, trustsec_vn_bulk_update, trustsec_vn_info), enabling module_defaults grouping for TrustSec modules.
- Fixed _info modules to accept id parameter for get-by-id lookups.
- Fixed generator function names in network_device_group, restid_store, sponsor_group_member, authorization_profile, guest_user, portal_theme, sponsored_guest_portal, portal_global_setting, profiler_profile, and admin_user.

v3.0.1
======

Release Summary
---------------

Update ISE version to 3.5.0

Bugfixes
--------

- networkdevice add support for 'absent' state, implement update and delete methods
- update ISE version to 3.5.0 for improved functionality.

v3.0.0
======

Release Summary
---------------

Major collection refactoring with 311 modules removed, 103 new modules added, and 234 new playbooks. Complete restructuring of module naming conventions and removal of deprecated functionality.

Major Changes
-------------

- BREAKING CHANGE - Removed 311 deprecated modules from plugins/modules.
- BREAKING CHANGE - Removed aci_* modules including aci_bindings_info, aci_settings, and aci_test_connectivity.
- BREAKING CHANGE - Removed all 12 sxp_* modules including connections, connections_bulk_monitor_status_info, connections_bulk_request, connections_info, local_bindings, local_bindings_bulk_monitor_status_info, local_bindings_bulk_request, local_bindings_info, vpns, vpns_bulk_monitor_status_info, vpns_bulk_request, and vpns_info.
- BREAKING CHANGE - Removed all 13 node_* deployment and group modules including node_deployment, node_deployment_info, node_deployment_sync, node_group, node_group_info, node_group_node_create, node_group_node_delete, node_group_node_info, node_primary_to_standalone, node_secondary_to_primary, and node_standalone_to_primary.
- BREAKING CHANGE - Removed all 14 active_directory_* modules including add_groups, groups_by_domain_info, info, is_user_member_of_group_info, join_domain, join_domain_with_all_nodes, leave_domain, leave_domain_with_all_nodes, trusted_domains_info, and user_groups_info.
- BREAKING CHANGE - Removed all 14 sg_mapping_* and sg_to_vn_to_vlan_* modules including bulk_monitor_status_info, bulk_request, deploy, deploy_all, deploy_status_info, group modules, and info modules.
- BREAKING CHANGE - Removed all 21 guest_user_* modules including approve, bulk_monitor_status_info, bulk_request, change_sponsor_password, deny, email, info, reinstate, reset_password, sms, and suspend.
- BREAKING CHANGE - Removed all 26 device_administration_* modules including authentication_rules, authorization_rules, conditions, dictionary_attributes, global_exception_rules, local_exception_rules, network_conditions, policy_set, profiles, service_names, time_date_conditions, and reset_hitcount modules.
- BREAKING CHANGE - Removed all 29 network_access_* modules including authentication_rules, authorization_rules, conditions, dictionary, global_exception_rules, local_exception_rules, network_condition, policy_set, profiles, security_groups, service_name, time_date_conditions, and reset_hitcount modules.
- BREAKING CHANGE - Removed all 32 pxgrid_* modules including access_secret, account_create, authorization, bindings_info, egress_matrices_info, egress_policies_info, endpoint_by_mac_info, endpoints_info, failures_info, healths_info, node_approve, node_delete, node_info, performances_info, profiles_info, security_group_acls_info, security_groups_info, service_lookup, service_register, service_reregister, service_unregister, session_by_ip_info, session_by_mac_info, session_for_recovery_info, sessions_info, settings_auto_approve, user_group_by_username_info, and user_groups_info.
- BREAKING CHANGE - Removed all 4 node_services_* modules including interfaces_info, profiler_probe_config, profiler_probe_config_info, sxp_interfaces, and sxp_interfaces_info.
- BREAKING CHANGE - Removed all 4 px_grid_* modules including node_approve, node_delete, node_info, and settings_auto_approve.
- BREAKING CHANGE - Removed all 4 upgrade_* modules including upgrade_proceed, upgrade_proceed_info, upgrade_stage_cancel, upgrade_stage_cancel_info, and upgrade_stage_start.
- BREAKING CHANGE - Removed all 5 subscriber_* modules including subscriber, subscriber_bulk, subscriber_info, subscriber_imsi_info, and user_equipment_subscriber_info.
- BREAKING CHANGE - Removed all 5 trustsec_sg_vn_mapping_* modules including bulk_create, bulk_delete, bulk_update, and info.
- BREAKING CHANGE - Removed all 5 trustsec_vn_vlan_mapping_* modules including bulk_create, bulk_delete, bulk_update, and info.
- BREAKING CHANGE - Removed all 5 user_equipment_* modules including user_equipment, user_equipment_bulk, user_equipment_csv, user_equipment_imei_info, and user_equipment_info.
- BREAKING CHANGE - Removed all 6 egress_matrix_cell_* modules including bulk_monitor_status_info, bulk_request, clear_all, clone, info, and set_all_status.
- BREAKING CHANGE - Removed all 8 anc_endpoint_* modules including apply, bulk_monitor_status_info, bulk_request, clear, and info.
- BREAKING CHANGE - Removed anc_policy_* modules including anc_policy_bulk_monitor_status_info and anc_policy_bulk_request.
- BREAKING CHANGE - Removed endpoint_* action modules including endpoint_bulk_monitor_status_info, endpoint_bulk_request, endpoint_certificate, endpoint_deregister, endpoint_get_rejected_endpoints_info, endpoint_register, and endpoint_release_rejected_endpoint.
- BREAKING CHANGE - Removed mnt_session_* modules including mnt_session_auth_list_info, mnt_session_by_ip_info, mnt_session_by_nas_ip_info, mnt_session_disconnect_info, mnt_session_reauthentication_info, and mnt_sessions_by_session_id_info.
- BREAKING CHANGE - Removed network_device_* modules including network_device_bulk_monitor_status_info and network_device_bulk_request.
- BREAKING CHANGE - Removed sg_acl_* modules including sg_acl_bulk_monitor_status_info and sg_acl_bulk_request.
- BREAKING CHANGE - Removed sgt_* modules including sgt_bulk_monitor_status_info and sgt_bulk_request.
- BREAKING CHANGE - Removed standalone modules - deployment_info, mnt_authentication_status_info, pan_ha_info, pan_ha_update, personas_register_node, portal_global_setting_info, system_certificate_create, system_config_version_info, and threat_vulnerabilities_clear.
- Module renamed aci_settings_info to acisettings_info.
- Module renamed active_directory_trusted_domains_info to adresourcereservation_name__info.
- Module renamed egress_matrix_cell_clone to ancendpoint_clear.
- Module renamed portal_global_setting to ``adresourcereservation_``.
- Module renamed pxgrid_account_activate to guestssid.
- Module renamed resource_version_info to restidstoresettings_info.
- Module renamed subscriber_imsi_info to adresourcereservation__info.
- Module renamed support_bundle to supportbundle.
- Module renamed support_bundle_download to supportbundledownload.
- Module renamed upgrade_stage_start_info to sxpvpns.
- Module renamed user_equipment_subscriber_info to ancpolicy.
- personas_update_roles_services replaced with personas_update_roles module with updated functionality.

Minor Changes
-------------

- Added 103 new modules to plugins/modules directory.
- Added 234 new playbook examples to playbooks directory.
- activedirectory - new module to manage Active Directory configurations.
- activedirectory_info - new module to retrieve Active Directory information.
- adminuser_info - new module to retrieve administrator user information.
- adresourcereservation_info - new module to retrieve AD resource reservation information.
- allowedprotocols - new module to manage allowed protocols.
- allowedprotocols_info - new module to retrieve allowed protocols information.
- ancendpoint_info - new module to retrieve ANC endpoint information.
- ancpolicy - new module to manage ANC policies.
- ancpolicy_info - new module to retrieve ANC policy information.
- ansible.utils dependency updated from ">=2.0.0,<6.0" to ">=2.0.0,<7.0" to support ansible.utils version 6.x.
- authorizationprofile - new module to manage authorization profiles.
- authorizationprofile_info - new module to retrieve authorization profile information.
- byodportal - new module to manage BYOD portals.
- byodportal_info - new module to retrieve BYOD portal information.
- certificateprofile - new module to manage certificate profiles.
- certificateprofile_info - new module to retrieve certificate profile information.
- certificatetemplate_info - new module to retrieve certificate template information.
- ctsenvdata - new module to manage CTS environment data.
- ctsmatrix - new module to manage CTS matrix.
- downloadableacl - new module to manage downloadable ACLs.
- downloadableacl_info - new module to retrieve downloadable ACL information.
- duo_mfainfo_info - new module to retrieve Duo MFA information.
- egressmatrixcell - new module to manage egress matrix cells.
- egressmatrixcell_info - new module to retrieve egress matrix cell information.
- endpointgroup - new module to manage endpoint groups.
- endpointgroup_info - new module to retrieve endpoint group information.
- externalradiusserver - new module to manage external RADIUS servers.
- externalradiusserver_info - new module to retrieve external RADIUS server information.
- filterpolicy - new module to manage filter policies.
- filterpolicy_info - new module to retrieve filter policy information.
- guestlocation_info - new module to retrieve guest location information.
- guestsmtpnotificationsettings - new module to manage guest SMTP notification settings.
- guestsmtpnotificationsettings_info - new module to retrieve guest SMTP notification settings information.
- guestssid_info - new module to retrieve guest SSID information.
- guesttype - new module to manage guest types.
- guesttype_info - new module to retrieve guest type information.
- guestuser - new module to manage guest users.
- guestuser_info - new module to retrieve guest user information.
- hotspotportal - new module to manage hotspot portals.
- hotspotportal_info - new module to retrieve hotspot portal information.
- identitygroup - new module to manage identity groups.
- identitygroup_info - new module to retrieve identity group information.
- idstoresequence - new module to manage ID store sequences.
- idstoresequence_info - new module to retrieve ID store sequence information.
- internaluser - new module to manage internal users.
- internaluser_info - new module to retrieve internal user information.
- ldap - new module to manage LDAP configurations.
- ldap_info - new module to retrieve LDAP information.
- mydeviceportal - new module to manage My Device portals.
- mydeviceportal_info - new module to retrieve My Device portal information.
- networkdevice - new module to manage network devices.
- networkdevice_info - new module to retrieve network device information.
- networkdevicegroup - new module to manage network device groups.
- networkdevicegroup_info - new module to retrieve network device group information.
- nspprofile_info - new module to retrieve NSP profile information.
- personas_update_roles - new module to update personas roles (replaces personas_update_roles_services).
- portalglobalsetting_info - new module to retrieve portal global setting information.
- portaltheme - new module to manage portal themes.
- portaltheme_info - new module to retrieve portal theme information.
- profilerprofile_info - new module to retrieve profiler profile information.
- pxgridnode_info - new module to retrieve pxGrid node information.
- radiusserversequence - new module to manage RADIUS server sequences.
- radiusserversequence_info - new module to retrieve RADIUS server sequence information.
- reportconfig - new module to manage report configurations.
- restidstore - new module to manage REST ID stores.
- restidstore_info - new module to retrieve REST ID store information.
- restidstorepredefinedregex_fetch_san_predefinedregexs_info - new module to retrieve predefined regex for SAN.
- restidstorepredefinedregex_fetch_snf_predefinedregexs_info - new module to retrieve predefined regex for SNF.
- selfregportal - new module to manage self-registered portals.
- selfregportal_info - new module to retrieve self-registered portal information.
- service_info - new module to retrieve service information.
- sessionservicenode_info - new module to retrieve session service node information.
- sgacl - new module to manage SGACLs.
- sgacl_info - new module to retrieve SGACL information.
- sgacls - new module to manage multiple SGACLs.
- sgmapping - new module to manage SG mappings.
- sgmapping_info - new module to retrieve SG mapping information.
- sgmappinggroup - new module to manage SG mapping groups.
- sgmappinggroup_info - new module to retrieve SG mapping group information.
- sgtvnvlan - new module to manage SGT-VN-VLAN mappings.
- sgtvnvlan_info - new module to retrieve SGT-VN-VLAN mapping information.
- smsprovider_info - new module to retrieve SMS provider information.
- sponsoredguestportal - new module to manage sponsored guest portals.
- sponsoredguestportal_info - new module to retrieve sponsored guest portal information.
- sponsorgroup - new module to manage sponsor groups.
- sponsorgroup_info - new module to retrieve sponsor group information.
- sponsorgroupmember_info - new module to retrieve sponsor group member information.
- sponsorportal - new module to manage sponsor portals.
- sponsorportal_info - new module to retrieve sponsor portal information.
- supportbundlestatus_info - new module to retrieve support bundle status information.
- sxpconnections - new module to manage SXP connections.
- sxpconnections_info - new module to retrieve SXP connections information.
- sxplocalbindings - new module to manage SXP local bindings.
- sxplocalbindings_info - new module to retrieve SXP local bindings information.
- sxpvpns_info - new module to retrieve SXP VPNs information.
- systemcertificate - new module to manage system certificates.
- tacacscommandsets - new module to manage TACACS command sets.
- tacacscommandsets_info - new module to retrieve TACACS command sets information.
- tacacsexternalservers - new module to manage TACACS external servers.
- tacacsexternalservers_info - new module to retrieve TACACS external servers information.
- tacacsprofile - new module to manage TACACS profiles.
- tacacsprofile_info - new module to retrieve TACACS profile information.
- tacacsserversequence - new module to manage TACACS server sequences.
- tacacsserversequence_info - new module to retrieve TACACS server sequence information.
- telemetryinfo_info - new module to retrieve telemetry information.

Bugfixes
--------

- Corrected import statements in refactored modules.
- Fixed galaxy.yml metadata for compatibility with newer Ansible versions.
- Fixed module documentation blocks across all updated modules.
- Updated .gitignore with additional exclusion patterns.
- Updated 234 playbook examples to align with new module naming conventions.
- Updated action plugin references to match new module names.

v2.10.0
=======

Release Summary
---------------

Fix linting issues.

Minor Changes
-------------

- Fix linting issues.

Bugfixes
--------

- personas_promote_primary - fix timeout issue.

v2.9.6
======

Release Summary
---------------

Update network_device module.

Bugfixes
--------

- network_device - Fix mask validation to handle None values in NetworkDeviceIPList

v2.9.5
======

Release Summary
---------------

Update.

Bugfixes
--------

- cisco.ise.support_bundle_download keeps failing after downloading the file

v2.9.4
======

Release Summary
---------------

Update.

Bugfixes
--------

- Collection not compatible with ansible.utils 5.x.y
- Getting deployment info for entire deployment does not work
- cisco.ise.pan_ha object has no attribute 'enable_pan_ha'

v2.9.3
======

Release Summary
---------------

Update.

Bugfixes
--------

- endpoint_group - add missing parameter parentID.
- mnt_session_active_list_info - fix response xml.
- network_device - mask param can be string or int, cast to int at the end.
- reservation - remove duplicate parameter.
- support_bundle_download - remove duplicate parameter.
- trusted_certificate - fix comparison between request and current object.

v2.9.2
======

Release Summary
---------------

Update min ansible version.

Bugfixes
--------

- Added main.yml to aws_deployment role
- Update min_ansible_version to 2.15.0 in runtime.yml and roles

v2.9.1
======

Release Summary
---------------

Update network_device_group module.

Bugfixes
--------

- network_device_group - change parameter name from ndgtype to othername.
- network_device_group_info - change parameter name from ndgtype to othername.

v2.9.0
======

Release Summary
---------------

ansible-ise now support 3.3 patch 1.

Bugfixes
--------

- Service included active_directories.
- Service included ad_groups.
- Service included custom_attributes.
- Service included duo_identity_sync.
- Service included duo_mfa.
- Service included enable_mfa.
- Service included endpoint_stop_replication_service.
- Service included endpoints.
- Service included full_upgrade.
- Service included is_mfa_enabled.
- Service included native_ipsec.
- Service included px_grid_direct.
- Service included sgt_range_reservation.
- Service included user_equipment.

v2.8.1
======

Release Summary
---------------

Changes the requirements of ansible.utils to allow > 4.0.0 versions.

Bugfixes
--------

- ansible.utils changes to `">=2.0.0,<5.0"` in galaxy.yml dependencies.

v2.8.0
======

Release Summary
---------------

Changes the minimum supported version of Ansible to v2.14.0

Minor Changes
-------------

- Changes the minimum supported version from Ansible v2.9.10 to v2.14.0

v2.7.0
======

Release Summary
---------------

Galaxy updated.

Minor Changes
-------------

- cisco.ise collection now supports ansible.utils v3

v2.6.2
======

Release Summary
---------------

Added missing import

Bugfixes
--------

- Added missing import re in endpoint module

v2.6.1
======

Release Summary
---------------

Update to use ciscoisesdk v2.1.1 or newer

Bugfixes
--------

- Updated to use ciscoisesdk v2.1.1 or newer fixing ciscoisesdk problem.

v2.6.0
======

Release Summary
---------------

ansible-ise now support 3.2_beta

Minor Changes
-------------

- Services included configuration, edda, dataconnect_services, subscriber.

v2.5.16
=======

Release Summary
---------------

Fixed active_directory_groups_by_domain_Info.

Bugfixes
--------

- Cannot get cisco.ise.active_directory_groups_by_domain_info to work.

v2.5.15
=======

Release Summary
---------------

Fixed get_object_by_id.

Bugfixes
--------

- system_certificate - fixed get_object_by_id response.

v2.5.14
=======

Release Summary
---------------

support for none value.

Bugfixes
--------

- system_certificate - added support for none value in the used_by param.

v2.5.13
=======

Release Summary
---------------

Several bugfixes in modules.

Bugfixes
--------

- Cannot get cisco.ise.rest_id_store to work fixed.
- System Certificate Update does not work but always reports Object already present temporary solution.
- cisco.ise.mnt_session_active_count_info ise_reponse is null fixed.
- node_deployment tasks fail because of timeout, adding new collection param.

v2.5.12
=======

Release Summary
---------------

Change is detected in a better way.

Bugfixes
--------

- network_access_authorization_rules - recognizes when there are changes.

v2.5.11
=======

Release Summary
---------------

Some errors have been corrected when reading the playbook and a validation was removed.

Bugfixes
--------

- network_access_authentication_rules - now read the ID correctly.
- network_access_authorization_rules - now read the ID correctly.
- node_group - search was repaired.
- node_group_node_info - removed a validation that caused a failure.

v2.5.10
=======

Release Summary
---------------

A check has been added to identify if there really are any changes

Bugfixes
--------

- network_access_authorization_rules - is now idempotent.

v2.5.9
======

Release Summary
---------------

Fixed some ansible statuses, added a missing parameter and corrected a response.

Bugfixes
--------

- licensing_eval_license_info - corrected the response
- node_primary_to_standalone - fixed ansible changed response
- node_secondary_to_primary - fixed ansible changed response
- node_standalone_to_primary - fixed ansible changed response
- system_certificate - a missing parameter was added allowWildcardDelete

v2.5.8
======

Release Summary
---------------

Added the ability to export Cisco ISE credentials as environment variables and rennamed some vars.

Bugfixes
--------

- Cisco ISE credentials can now be exported and used as env vars.
- mnt_athentication_status_info - the following variable was renamed from rec_ord_s to records.
- mnt_athentication_status_info - the following variable was renamed from sec_ond_s to seconds.
- mnt_authentication_status_info - the following variable was renamed from rec_ord_s to records.
- mnt_authentication_status_info - the following variable was renamed from sec_ond_s to seconds.
- mnt_session_disconnect_info - the following variable was renamed from dis_con_nec_tty_pe to disconnect_type.
- mnt_session_disconnect_info - the following variable was renamed from end_poi_nti_p to endpoint_ip.
- mnt_session_disconnect_info - the following variable was renamed from psn_nam_e to psn_name.
- mnt_session_reauthentication_info - the following variable was renamed from end_poi_ntm_ac to endpoint_mac.
- mnt_session_reauthentication_info - the following variable was renamed from psn_nam_e to psn_name.
- mnt_session_reauthentication_info - the following variable was renamed from rea_uth_typ_e to reauth_type.

v2.5.7
======

Release Summary
---------------

New method to compare changes

Bugfixes
--------

- A new method to compare changes for specific cases has been added.
- network_access_network_condition - Updated description of deviceGroupList.
- node_services_profiler_probe_config - Used a new method to compare changes.
- sgt - Updated the fields required for creation.

v2.5.6
======

Release Summary
---------------

Update to use ciscoisesdk v2.0.5 or newer, fixed a request body

Bugfixes
--------

- filter_policy - removed the required id when it is a post method.
- guest_smtp_notification_settings - removed the required id when it is a post method.
- network_access_network_condition - fixed a request body of the post and put method.
- sxp_connections - removed the required id when it is a post method.
- sxp_vpns - removed the required id when it is a post method.

v2.5.5
======

Release Summary
---------------

A check has been added to identify if there really are any changes

Bugfixes
--------

- personas_update_roles_services - is now idempotent.

v2.5.4
======

Release Summary
---------------

A validation has been added to the update method and warning message removed.

Bugfixes
--------

- aci_settings - A validation has been added to the update method.
- allowed_protocols - A validation has been added to the update method.
- anc_policy - A validation has been added to the update method.
- authorization_profile - A validation has been added to the update method.
- byod_portal - A validation has been added to the update method.
- certificate_profile - A validation has been added to the update method.
- downloadable_acl - A validation has been added to the update method.
- egress_matrix_cell - A validation has been added to the update method.
- endpoint - A validation has been added to the update method.
- endpoint_group - A validation has been added to the update method.
- external_radius_server - A validation has been added to the update method.
- filter_policy - A validation has been added to the update method.
- guest_smtp_notification_settings - A validation has been added to the update method.
- guest_ssid - A validation has been added to the update method.
- guest_type - A validation has been added to the update method.
- guest_user - A validation has been added to the update method.
- hotspot_portal - A validation has been added to the update method.
- id_store_sequence - A validation has been added to the update method.
- identity_group - A validation has been added to the update method.
- my_device_portal - A validation has been added to the update method.
- native_supplicant_profile - A validation has been added to the update method.
- network_device - A validation has been added to the update method.
- network_device_group - A validation has been added to the update method.
- personas_utils - Warning message removed.
- portal_global_setting - A validation has been added to the update method.
- portal_theme - A validation has been added to the update method.
- radius_server_sequence - A validation has been added to the update method.
- rest_id_store - A validation has been added to the update method.
- self_registered_portal - A validation has been added to the update method.
- sg_acl - A validation has been added to the update method.
- sg_mapping - A validation has been added to the update method.
- sg_mapping_group - A validation has been added to the update method.
- sg_to_vn_to_vlan - A validation has been added to the update method.
- sgt - A validation has been added to the update method.
- sponsor_group - A validation has been added to the update method.
- sponsor_portal - A validation has been added to the update method.
- sponsored_guest_portal - A validation has been added to the update method.
- sxp_connections - A validation has been added to the update method.
- sxp_local_bindings - A validation has been added to the update method.
- tacacs_command_sets - A validation has been added to the update method.
- tacacs_external_servers - A validation has been added to the update method.
- tacacs_profile - A validation has been added to the update method.
- tacacs_server_sequence - A validation has been added to the update method.

v2.5.3
======

Release Summary
---------------

Fixed ansible status msg and unnecessary parameter was removed.

Bugfixes
--------

- endpoint - an unnecessary parameter name has been removed because it is automatically generated by the api.
- personas_update_roles_services - fixed ansible status msg.

v2.5.2
======

Release Summary
---------------

Fixed galaxy publication

Bugfixes
--------

- An error was corrected in galaxy publication

v2.5.1
======

Release Summary
---------------

Update example of module documentation and added a new validation.

Bugfixes
--------

- downloadable_acl - update EXAMPLES block of module documentation.
- sgt - added new validation when updating a stg auto generated.

v2.5.0
======

Release Summary
---------------

Update Cisco ISE requirementes and fix some repository issues.

Minor Changes
-------------

- Update requirements to use ciscoisesdk >= 2.0.3.

Bugfixes
--------

- Fixed ISE version 3.1.1 to 3.1_Patch_1 which is the correct version name.
- repository - Fixed a bug, now repositoryName and name are used to perform the search.
- repository_files_info - Fixed a bug that did not make the get call.

v2.4.1
======

Release Summary
---------------

Change path parameter.

Bugfixes
--------

- repository - change path parameter from name to repositoryName
- repository_files_info - change path parameter from name to repositoryName
- repository_info - change path parameter from name to repositoryName

v2.4.0
======

Release Summary
---------------

Add pxGrid modules & changes some module descriptions.

Minor Changes
-------------

- pxGrid_node_approve - new module
- pxGrid_node_delete - new module
- pxGrid_node_info - new module
- pxGrid_settings_auto_approve - new module

Bugfixes
--------

- Change description from Aci to ACI
- Change description from Acl to ACL
- Change description from Anc to ANC
- Change description from Byod to BYOD
- Change description from Ca to CA
- Change description from Csr to CSR
- Change description from Mnt to MNT
- Change description from Nbar to NBAR
- Change description from Pxgrid to pxGrid
- Change description from Radius to RADIUS
- Change description from Rest to REST
- Change description from Sg Acl to SGACL
- Change description from Sg to SG
- Change description from Sgt to SGT
- Change description from Sms to SMS
- Change description from Smtp to SMTP
- Change description from Ssid to SSID
- Change description from Sxp to SXP
- Change description from Tacacs to TACACS
- Change description from Vlan to VLAN
- Change description from Vn to VN
- Change description from Vpns to VPNs
- node_services_interfaces_info - change the validation.

v2.3.2
======

Release Summary
---------------

Added a validation

Bugfixes
--------

- device_administration_authentication_rules - added a validation reading the data
- device_administration_authorization_rules - added a validation reading the data
- device_administration_global_exception_rules - added a validation reading the data
- device_administration_local_exception_rules - added a validation reading the data
- network_access_authentication_rules - added a validation reading the data
- network_access_authorization_rules - added a validation reading the data
- network_access_global_exception_rules - added a validation reading the data
- network_access_local_exception_rules - added a validation reading the data

v2.3.1
======

Release Summary
---------------

Added a validation

Bugfixes
--------

- network_access_authorization_rules - added a validation when reading the data

v2.3.0
======

Release Summary
---------------

Add ISE CSRF Check support & change download modules response to include file details

Minor Changes
-------------

- Add ise_uses_csrf_token parameter to modules
- csr_export_info - Instead of returning the data string, it now returns a dictionary. The dictionary has property data with the previous string value.
- csr_export_info - add parameter filename.
- endpoint_certificate - Instead of returning the data string, it now returns a dictionary. The dictionary has property data with the previous string value.
- endpoint_certificate - add parameter filename.
- support_bundle_download - Instead of returning the data string, it now returns a dictionary. The dictionary has property data with the previous string value.
- support_bundle_download - add parameter filename.
- system_certificate_export_info - Instead of returning the data string, it now returns a dictionary. The dictionary has property data with the previous string value.
- system_certificate_export_info - add parameter filename.
- trusted_certificate_export_info - Instead of returning the data string, it now returns a dictionary. The dictionary has property data with the previous string value.
- trusted_certificate_export_info - add parameter filename.

Bugfixes
--------

- Update README recommended SDK version in compatibility matrix
- Update README, update Compatibility matrix.
- Update recommended SDK version in modules from 1.4.0 to 1.5.0

v2.2.3
======

Release Summary
---------------

Update README, add ISE API Versioning and ISE 3.1 + Patch 1 notes

Bugfixes
--------

- Update README, add ISE 3.1 + Patch 1 and ISE API Versioning notes
- Update README, update Compatibility matrix.

v2.2.2
======

Release Summary
---------------

Update README recommended SDK version and module documentation

Bugfixes
--------

- Update README recommended SDK version in compatibility matrix
- trustsec_sg_vn_mapping_bulk_create - update EXAMPLES block of module documentation
- trustsec_sg_vn_mapping_bulk_delete - update EXAMPLES block of module documentation
- trustsec_sg_vn_mapping_bulk_update - update EXAMPLES block of module documentation
- trustsec_vn_bulk_create - update EXAMPLES block of module documentation
- trustsec_vn_bulk_delete - update EXAMPLES block of module documentation
- trustsec_vn_bulk_update - update EXAMPLES block of module documentation
- trustsec_vn_vlan_mapping_bulk_create - update EXAMPLES block of module documentation
- trustsec_vn_vlan_mapping_bulk_delete - update EXAMPLES block of module documentation
- trustsec_vn_vlan_mapping_bulk_update - update EXAMPLES block of module documentation

v2.2.1
======

Release Summary
---------------

Update README links in galaxy

Bugfixes
--------

- update README links in galaxy from relative to absolute links.

v2.2.0
======

Release Summary
---------------

Update module doc & fix licensing_tier_state_create

Minor Changes
-------------

- Update requirements to use ciscoisesdk >= 1.4.0.
- licensing_tier_state_create - fix function call.

Bugfixes
--------

- plugin/modules - update documentation block.
- update README.

v2.1.2
======

Release Summary
---------------

Fixes params used for modules

Bugfixes
--------

- node_services_profiler_probe_config - fixes params used for module.
- node_services_sxp_interfaces - fixes params used for module.
- repository - fixes params used for modules. Fix for issue 19.
- repository_files_info - fixes params used for module.

v2.1.1
======

Release Summary
---------------

Fixes on trustsec and node_group modules

Bugfixes
--------

- node_group_node_create - fix family execution call from Node Deployment to Node Group.
- node_group_node_delete - fix family execution call from Node Deployment to Node Group.
- node_group_node_info - fix family execution call from Node Deployment to Node Group.
- trustsec_sg_vn_mapping - fix version_added to 2.0.0
- trustsec_sg_vn_mapping_bulk_create - fix version_added to 2.0.0
- trustsec_sg_vn_mapping_bulk_delete - fix version_added to 2.0.0
- trustsec_sg_vn_mapping_bulk_update - fix version_added to 2.0.0
- trustsec_sg_vn_mapping_info - change filter param type from str to list
- trustsec_sg_vn_mapping_info - fix version_added to 2.0.0
- trustsec_vn_vlan_mapping - fix version_added to 2.0.0
- trustsec_vn_vlan_mapping_bulk_create - fix version_added to 2.0.0
- trustsec_vn_vlan_mapping_bulk_delete - fix version_added to 2.0.0
- trustsec_vn_vlan_mapping_bulk_update - fix version_added to 2.0.0
- trustsec_vn_vlan_mapping_info - change filter param type from str to list
- trustsec_vn_vlan_mapping_info - fix version_added to 2.0.0

v2.1.0
======

Release Summary
---------------

Update to use ciscoisesdk v1.3.0 or newer

Major Changes
-------------

- node_deployment - update parameters.
- node_deployment_info - add filter and filterType parameters.
- node_group - fixes response recollection.
- node_group_info - fixes response recollection.
- system_certificate - portalTagTransferForSameSubject parameter renamed to allowPortalTagTransferForSameSubject.
- system_certificate - roleTransferForSameSubject parameter renamed to allowRoleTransferForSameSubject.
- system_certificate_import - portalTagTransferForSameSubject parameter renamed to allowPortalTagTransferForSameSubject.
- system_certificate_import - roleTransferForSameSubject parameter renamed to allowRoleTransferForSameSubject.
- trustsec_nbar_app_info - change type from str to list.
- trustsec_vn_info - change type from str to list.

Minor Changes
-------------

- hotpatch_info - new module.
- hotpatch_install - new module.
- hotpatch_rollback - new module.
- licensing_connection_type_info - new module.
- licensing_eval_license_info - new module.
- licensing_feature_to_tier_mapping_info - new module.
- licensing_registration_create - new module.
- licensing_registration_info - new module.
- licensing_smart_state_create - new module.
- licensing_smart_state_info - new module.
- licensing_tier_state_create - new module.
- licensing_tier_state_info - new module.
- node_deployment_sync - new module.
- node_group_node_create - new module.
- node_group_node_delete - new module.
- node_group_node_info - new module.
- node_primary_to_standalone - new module.
- node_secondary_to_primary - new module.
- node_services_interfaces_info - new module.
- node_services_profiler_probe_config - new module.
- node_services_profiler_probe_config_info - new module.
- node_services_sxp_interfaces - new module.
- node_services_sxp_interfaces_info - new module.
- node_standalone_to_primary - new module.
- pan_ha_update - new module.
- patch_info - new module.
- patch_install - new module.
- patch_rollback - new module.
- proxy_connection_settings - new module.
- proxy_connection_settings_info - new module.
- selfsigned_certificate_generate - new module.
- transport_gateway_settings - new module.
- transport_gateway_settings_info - new module.

v2.0.0
======

Release Summary
---------------

Updates ISE responses and adds Trust_Sec modules

Major Changes
-------------

- Update ciscoisesdk requirement to 1.2.0
- anc_endpoint_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- anc_policy_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- backup_last_status_info - change return value, it returns response content.
- device_administration_authentication_rules - deletes parameter identitySourceId.
- device_administration_authentication_rules_info - change return value, it returns response content.
- device_administration_authorization_rules_info - change return value, it returns response content.
- device_administration_conditions - deletes parameter attributeId.
- device_administration_conditions_for_authentication_rule_info - change return value, it returns response content.
- device_administration_conditions_for_authorization_rule_info - change return value, it returns response content.
- device_administration_conditions_for_policy_set_info - change return value, it returns response content.
- device_administration_conditions_info - change return value, it returns response content.
- device_administration_dictionary_attributes_authentication_info - change return value, it returns response content.
- device_administration_dictionary_attributes_authorization_info - change return value, it returns response content.
- device_administration_dictionary_attributes_policy_set_info - change return value, it returns response content.
- device_administration_global_exception_rules_info - change return value, it returns response content.
- device_administration_network_conditions_info - change return value, it returns response content.
- device_administration_time_date_conditions - deletes parameter attributeId.
- device_administration_time_date_conditions_info - change return value, it returns response content.
- egress_matrix_cell_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- network_access_authentication_rules - deletes parameter identitySourceId.
- network_access_conditions - deletes parameter attributeId.
- network_access_time_date_conditions - deletes parameter attributeId.
- repository_files_info - change return value, it returns response content.
- repository_info - change return value, it returns response content.
- sg_acl_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sg_mapping_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sg_mapping_group_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sg_mapping_group_info - change return value, it returns BulkStatus content.
- sg_to_vn_to_vlan_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sgt - change generationId type from int to str.
- sgt_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sxp_connections_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sxp_local_bindings_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sxp_vpns_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- system_certificate - new parameters portalTagTransferForSameSubject and roleTransferForSameSubject.
- system_certificate_import - new parameters portalTagTransferForSameSubject and roleTransferForSameSubject.

Minor Changes
-------------

- aci_bindings_info - change default response to [].
- active_directory_info - change default response to [].
- admin_user_info - change default response to [].
- allowed_protocols_info - change default response to [].
- anc_endpoint_info - change default response to [].
- anc_policy_info - change default response to [].
- authorization_profile_info - change default response to [].
- backup_schedule_config_update - new module.
- byod_portal_info - change default response to [].
- certificate_profile_info - change default response to [].
- certificate_template_info - change default response to [].
- csr_info - change default response to [].
- downloadable_acl_info - change default response to [].
- egress_matrix_cell_info - change default response to [].
- endpoint_bulk_monitor_status_info - change default response to [].
- radius_server_sequence_info - change default response to [].
- rest_id_store_info - change default response to [].
- self_registered_portal_info - change default response to [].
- sg_acl_info - change default response to [].
- sg_to_vn_to_vlan_info - change default response to [].
- sgt_info - change default response to [].
- sponsor_group_info - change default response to [].
- sponsor_portal_info - change default response to [].
- sponsored_guest_portal_info - change default response to [].
- support_bundle_status_info - change default response to [].
- sxp_connections_info - change default response to [].
- sxp_local_bindings_info - change default response to [].
- sxp_vpns_info - change default response to [].
- tacacs_command_sets_info - change default response to [].
- tacacs_external_servers_info - change default response to [].
- tacacs_profile_info - change default response to [].
- tacacs_server_sequence_info - change default response to [].
- telemetry_info - change default response to [].
- trusted_certificate - change default response to [].
- trustsec_nbar_app - new module.
- trustsec_nbar_app_info - new module.
- trustsec_nbarapp - new playbook.
- trustsec_sg_vn_mapping - new module.
- trustsec_sg_vn_mapping - new playbook.
- trustsec_sg_vn_mapping_bulk_create - new module.
- trustsec_sg_vn_mapping_bulk_delete - new module.
- trustsec_sg_vn_mapping_bulk_update - new module.
- trustsec_sg_vn_mapping_info - new module.
- trustsec_vn - new module.
- trustsec_vn - new playbook.
- trustsec_vn_bulk_create - new module.
- trustsec_vn_bulk_delete - new module.
- trustsec_vn_bulk_update - new module.
- trustsec_vn_info - new module.
- trustsec_vn_vlan_mapping - new module.
- trustsec_vn_vlan_mapping - new playbook.
- trustsec_vn_vlan_mapping_bulk_create - new module.
- trustsec_vn_vlan_mapping_bulk_delete - new module.
- trustsec_vn_vlan_mapping_bulk_update - new module.
- trustsec_vn_vlan_mapping_info - new module.

Bugfixes
--------

- Update ISE version to 3.1.0 on vars example
- Update documentation of the modules.

v1.2.1
======

Release Summary
---------------

Fixes check_mode behavior

Bugfixes
--------

- On info modules comparison was removed, because info modules should always run.
- On regular modules additional comparison of check_mode was removed as Ansible already handles it.

v1.2.0
======

Release Summary
---------------

Adds ise_responses, ise_update_response values

Major Changes
-------------

- Adds ``ise_uses_api_gateway`` to module options.
- Adds ise_responses to return values of info modules.
- Adds ise_update_response to return values of non-info modules.

Minor Changes
-------------

- Update requirements.

v1.1.0
======

Release Summary
---------------

Adds mnt_authentication_status_info module

Minor Changes
-------------

- mnt_authentication_status_info - new module.

Bugfixes
--------

- Fixes check_mode behavior for non-info modules.
- Improves the changelog.
- Improves the documentation of modules.

v1.0.3
======

Release Summary
---------------

Added backup & restore and certificate management sample playbooks

Minor Changes
-------------

- Added backup_create sample playbook.
- Added backup_restore sample playbook.
- Added backup_schedule sample playbook.
- Added certificate_management sample playbook.
- Improve the documentation for MacOS users.

v1.0.2
======

Release Summary
---------------

Fix response of csr_info, system_certificate_info and trusted_certificate_info by accessing each page `response` property.

Bugfixes
--------

- Updates exception handling.
- csr_info - fixes response recollection.
- system_certificate_info - fixes response recollection.
- trusted_certificate_info - fixes response recollection.

v1.0.1
======

Release Summary
---------------

Migrated the Personas Deployment playbooks to a role

Minor Changes
-------------

- Migrated the Personas Deployment playbooks to a role.
- telemetry_info - fixes EXAMPLES documentation.

v1.0.0
======

Release Summary
---------------

Update to use ciscoisesdk v1.0.0 or newer

Major Changes
-------------

- Fixes inner logic of modules that have no get by name and have not working filter.
- Renamed module device_administration_authorization_exception_rules to device_administration_local_exception_rules.
- Renamed module device_administration_authorization_global_exception_rules to device_administration_global_exception_rules.
- Renamed module network_access_authorization_exception_rules to network_access_local_exception_rules.
- Renamed module network_access_authorization_global_exception_rules to network_access_global_exception_rules.
- Updates options required for modules.
- Updates sdk parameters for previous modules
- device_administration_authorization_exception_rules - removed module.
- device_administration_authorization_exception_rules_info - removed module.
- device_administration_authorization_global_exception_rules - removed module.
- device_administration_authorization_global_exception_rules_info - removed module.
- guest_user_reinstante - removed module.
- network_access_authorization_exception_rules - removed module.
- network_access_authorization_exception_rules_info - removed module.
- network_access_authorization_global_exception_rules - removed module.
- network_access_authorization_global_exception_rules_info - removed module.
- service_info - removed module.
- system_certificate_export - removed module.
- telemetry_info_info - removed module.

Minor Changes
-------------

- Added ise_debug parameter
- device_administration_authentication_reset_hitcount - new module.
- device_administration_authorization_reset_hitcount - new module.
- device_administration_global_exception_rules - new module.
- device_administration_global_exception_rules_info - new module.
- device_administration_global_exception_rules_reset_hitcount - new module.
- device_administration_local_exception_rules - new module.
- device_administration_local_exception_rules_info - new module.
- device_administration_local_exception_rules_reset_hitcount - new module.
- device_administration_policy_set_reset_hitcount - new module.
- guest_user_reinstate - new module.
- mnt_account_status_info - new module.
- mnt_athentication_status_info - new module.
- mnt_failure_reasons_info - new module.
- mnt_session_active_count_info - new module.
- mnt_session_active_list_info - new module.
- mnt_session_auth_list_info - new module.
- mnt_session_by_ip_info - new module.
- mnt_session_by_mac_info - new module.
- mnt_session_by_nas_ip_info - new module.
- mnt_session_by_username_info - new module.
- mnt_session_delete_all - new module.
- mnt_session_disconnect_info - new module.
- mnt_session_posture_count_info - new module.
- mnt_session_profiler_count_info - new module.
- mnt_session_reauthentication_info - new module.
- mnt_sessions_by_session_id_info - new module.
- mnt_version_info - new module.
- network_access_authentication_rules_reset_hitcount - new module.
- network_access_authorization_rules_reset_hitcount - new module.
- network_access_global_exception_rules - new module.
- network_access_global_exception_rules_info - new module.
- network_access_global_exception_rules_reset_hitcount - new module.
- network_access_local_exception_rules - new module.
- network_access_local_exception_rules_info - new module.
- network_access_local_exception_rules_reset_hitcounts - new module.
- network_access_policy_set_reset_hitcount - new module.
- px_grid_node_delete - new module.
- pxgrid_access_secret - new module.
- pxgrid_account_activate - new module.
- pxgrid_account_create - new module.
- pxgrid_authorization - new module.
- pxgrid_bindings_info - new module.
- pxgrid_egress_matrices_info - new module.
- pxgrid_egress_policies_info - new module.
- pxgrid_endpoint_by_mac_info - new module.
- pxgrid_endpoints_by_os_type_info - new module.
- pxgrid_endpoints_by_type_info - new module.
- pxgrid_endpoints_info - new module.
- pxgrid_failures_info - new module.
- pxgrid_healths_info - new module.
- pxgrid_performances_info - new module.
- pxgrid_profiles_info - new module.
- pxgrid_security_group_acls_info - new module.
- pxgrid_security_groups_info - new module.
- pxgrid_service_lookup - new module.
- pxgrid_service_register - new module.
- pxgrid_service_reregister - new module.
- pxgrid_service_unregister - new module.
- pxgrid_session_by_ip_info - new module.
- pxgrid_session_by_mac_info - new module.
- pxgrid_session_for_recovery_info - new module.
- pxgrid_sessions_info - new module.
- pxgrid_user_group_by_username_info - new module.
- pxgrid_user_groups_info - new module.
- resource_version_info - new module.
- sg_mapping_bulk_monitor_status_info - new module.
- sg_mapping_bulk_request - new module.
- system_certificate_export_info - new module.
- tasks_info - new module.
- telemetry_info - new module.

v0.0.9
======

Release Summary
---------------

Adds an Ansible role for the deployment of ISE to AWS as well as four modules for the deployment of personas to the ISE nodes.

Major Changes
-------------

- Adds a 'aws_deployment' role that allows the deployment of an arbitrary large ISE cluster to AWS.
- personas_check_standalone - Adds module for the deployment of personas to existing nodes in an ISE cluster.
- personas_export_certs - Adds module for the deployment of personas to existing nodes in an ISE cluster.
- personas_promote_primary - Adds module for the deployment of personas to existing nodes in an ISE cluster.
- personas_update_roles - Adds module for the deployment of personas to existing nodes in an ISE cluster.

v0.0.8
======

Release Summary
---------------

Fix Indentity Group modules.

Bugfixes
--------

- Fixes Identity Group parameters.
- Fixes Identity Group response recollection.

v0.0.7
======

Release Summary
---------------

Adds more playbooks. Changes credentials.yml to group_vars. Adds ISE ER S modules. Compares requested object to found object before updating to only update if necessary.

Minor Changes
-------------

- aci_bindings_info - new module.
- aci_settings - new module.
- aci_settings_info - new module.
- aci_test_connectivity - new module.
- admin_user_info - new module.
- anc_endpoint_apply - new module.
- anc_endpoint_bulk_monitor_status_info - new module.
- anc_endpoint_bulk_request - new module.
- anc_endpoint_clear - new module.
- anc_endpoint_info - new module.
- byod_portal - new module.
- byod_portal_info - new module.
- certificate_profile - new module.
- certificate_profile_info - new module.
- certificate_template_info - new module.
- deployment_info - new module.
- endpoint_certificate - new module.
- my_device_portal - new module.
- my_device_portal_info - new module.
- native_supplicant_profile - new module.
- native_supplicant_profile_info - new module.
- node_info - new module.
- profiler_profile_info - new module.
- px_grid_node_approve - new module.
- px_grid_node_info - new module.
- px_grid_settings_auto_approve - new module.
- service_info - new module.
- session_service_node_info - new module.
- sg_mapping - new module.
- sg_mapping_deploy - new module.
- sg_mapping_deploy_all - new module.
- sg_mapping_deploy_status_info - new module.
- sg_mapping_group - new module.
- sg_mapping_group_bulk_monitor_status_info - new module.
- sg_mapping_group_bulk_request - new module.
- sg_mapping_group_deploy - new module.
- sg_mapping_group_deploy_all - new module.
- sg_mapping_group_deploy_status_info - new module.
- sg_mapping_group_info - new module.
- sg_mapping_info - new module.
- sg_to_vn_to_vlan - new module.
- sg_to_vn_to_vlan_bulk_monitor_status_info - new module.
- sg_to_vn_to_vlan_bulk_request - new module.
- sg_to_vn_to_vlan_info - new module.
- support_bundle - new module.
- support_bundle_download - new module.
- support_bundle_status_info - new module.
- sxp_connections - new module.
- sxp_connections_bulk_monitor_status_info - new module.
- sxp_connections_bulk_request - new module.
- sxp_connections_info - new module.
- sxp_local_bindings - new module.
- sxp_local_bindings_bulk_monitor_status_info - new module.
- sxp_local_bindings_bulk_request - new module.
- sxp_local_bindings_info - new module.
- sxp_vpns - new module.
- sxp_vpns_bulk_monitor_status_info - new module.
- sxp_vpns_bulk_request - new module.
- sxp_vpns_info - new module.
- system_certificate_create - new module.
- system_config_version_info - new module.
- telemetry_info_info - new module.
- threat_vulnerabilities_clear - new module.

Bugfixes
--------

- Introduces comparison to see if it requires an update.
- Removes unneeded imports.
- Updates the `params` dictionary values on sdk call execution.

v0.0.6
======

Release Summary
---------------

Fix README playbook example.

v0.0.5
======

Release Summary
---------------

Update sorting params for ``info_`` modules.

Bugfixes
--------

- Changes sortdec to sortdsc query param for _info modules.

v0.0.4
======

Release Summary
---------------

Added network_access_conditions module. Most modules are still untested against a live ISE.

Minor Changes
-------------

- network_access_conditions - new module.

v0.0.3
======

Release Summary
---------------

Added other modules and playbooks. Most modules are still untested against a live ISE.

Major Changes
-------------

- import_trust_cert - removed module.

Minor Changes
-------------

- active_directory - new module.
- active_directory_add_groups - new module.
- active_directory_groups_by_domain_info - new module.
- active_directory_is_user_member_of_group_info - new module.
- active_directory_join_domain - new module.
- active_directory_join_domain_with_all_nodes - new module.
- active_directory_leave_domain - new module.
- active_directory_leave_domain_with_all_nodes - new module.
- active_directory_trusted_domains_info - new module.
- active_directory_user_groups_info - new module.
- anc_policy_bulk_request - new module.
- backup_cancel - new module.
- backup_config - new module.
- backup_restore - new module.
- backup_schedule_config - new module.
- bind_signed_certificate - new module.
- csr_delete - new module.
- csr_generate - new module.
- csr_generate_intermediate_ca - new module.
- egress_matrix_cell_bulk_request - new module.
- egress_matrix_cell_clear_all - new module.
- egress_matrix_cell_clone - new module.
- egress_matrix_cell_set_all_status - new module.
- endpoint_bulk_request - new module.
- endpoint_deregister - new module.
- endpoint_register - new module.
- endpoint_release_rejected_endpoint - new module.
- guest_smtp_notification_settings - new module.
- guest_type_email - new module.
- guest_type_sms - new module.
- guest_user_approve - new module.
- guest_user_bulk_request - new module.
- guest_user_change_sponsor_password - new module.
- guest_user_deny - new module.
- guest_user_email - new module.
- guest_user_reinstante - new module.
- guest_user_reset_password - new module.
- guest_user_sms - new module.
- guest_user_suspend - new module.
- ise_root_ca_regenerate - new module.
- network_device_bulk_request - new module.
- node_promotion - new module.
- node_sync - new module.
- pan_ha - new module.
- portal_global_setting - new module.
- renew_certificate - new module.
- repository - new module.
- repository_files_info - new module.
- repository_info - new module.
- sg_acl_bulk_request - new module.
- sgt_bulk_request - new module.
- system_certificate - new module.
- system_certificate_export - new module.
- system_certificate_import - new module.
- trusted_certificate - new module.
- trusted_certificate_import - new module.

Bugfixes
--------

- Improve the documentation of the modules.

v0.0.2
======

Release Summary
---------------

Added all idempotent modules. Most modules are still untested against a live ISE.

Minor Changes
-------------

- active_directory_info - new module.
- allowed_protocols - new module.
- allowed_protocols_info - new module.
- anc_policy - new module.
- anc_policy_bulk_monitor_status_info - new module.
- anc_policy_info - new module.
- authorization_profile - new module.
- authorization_profile_info - new module.
- backup_last_status_info - new module.
- csr_export_info - new module.
- csr_info - new module.
- device_administration_authentication_rules - new module.
- device_administration_authentication_rules_info - new module.
- device_administration_authorization_exception_rules - new module.
- device_administration_authorization_exception_rules_info - new module.
- device_administration_authorization_global_exception_rules - new module.
- device_administration_authorization_global_exception_rules_info - new module.
- device_administration_authorization_rules - new module.
- device_administration_authorization_rules_info - new module.
- device_administration_command_set_info - new module.
- device_administration_conditions - new module.
- device_administration_conditions_for_authentication_rule_info - new module.
- device_administration_conditions_for_authorization_rule_info - new module.
- device_administration_conditions_for_policy_set_info - new module.
- device_administration_conditions_info - new module.
- device_administration_dictionary_attributes_authentication_info - new module.
- device_administration_dictionary_attributes_authorization_info - new module.
- device_administration_dictionary_attributes_policy_set_info - new module.
- device_administration_identity_stores_info - new module.
- device_administration_network_conditions - new module.
- device_administration_network_conditions_info - new module.
- device_administration_policy_set - new module.
- device_administration_policy_set_info - new module.
- device_administration_profiles_info - new module.
- device_administration_service_names_info - new module.
- device_administration_time_date_conditions - new module.
- device_administration_time_date_conditions_info - new module.
- downloadable_acl - new module.
- downloadable_acl_info - new module.
- egress_matrix_cell - new module.
- egress_matrix_cell_bulk_monitor_status_info - new module.
- egress_matrix_cell_info - new module.
- endpoint - new module.
- endpoint_bulk_monitor_status_info - new module.
- endpoint_get_rejected_endpoints_info - new module.
- endpoint_group - new module.
- endpoint_group_info - new module.
- endpoint_info - new module.
- external_radius_server - new module.
- external_radius_server_info - new module.
- filter_policy - new module.
- filter_policy_info - new module.
- guest_location_info - new module.
- guest_smtp_notification_settings_info - new module.
- guest_ssid - new module.
- guest_ssid_info - new module.
- guest_type - new module.
- guest_type_info - new module.
- guest_user - new module.
- guest_user_bulk_monitor_status_info - new module.
- guest_user_info - new module.
- hotspot_portal - new module.
- hotspot_portal_info - new module.
- id_store_sequence - new module.
- id_store_sequence_info - new module.
- identity_group - new module.
- identity_group_info - new module.
- import_trust_cert - new module.
- internal_user - new module.
- internal_user_info - new module.
- network_access_authentication_rules - new module.
- network_access_authentication_rules_info - new module.
- network_access_authorization_exception_rules - new module.
- network_access_authorization_exception_rules_info - new module.
- network_access_authorization_global_exception_rules - new module.
- network_access_authorization_global_exception_rules_info - new module.
- network_access_authorization_rules - new module.
- network_access_authorization_rules_info - new module.
- network_access_conditions_for_authentication_rule_info - new module.
- network_access_conditions_for_authorization_rule_info - new module.
- network_access_conditions_for_policy_set_info - new module.
- network_access_conditions_info - new module.
- network_access_dictionary - new module.
- network_access_dictionary_attribute - new module.
- network_access_dictionary_attribute_info - new module.
- network_access_dictionary_attributes_authentication_info - new module.
- network_access_dictionary_attributes_authorization_info - new module.
- network_access_dictionary_attributes_policy_set_info - new module.
- network_access_dictionary_info - new module.
- network_access_identity_stores_info - new module.
- network_access_network_condition - new module.
- network_access_network_condition_info - new module.
- network_access_policy_set - new module.
- network_access_policy_set_info - new module.
- network_access_profiles_info - new module.
- network_access_security_groups_info - new module.
- network_access_service_name_info - new module.
- network_access_time_date_conditions - new module.
- network_access_time_date_conditions_info - new module.
- network_device - new module.
- network_device_bulk_monitor_status_info - new module.
- network_device_group - new module.
- network_device_group_info - new module.
- network_device_info - new module.
- node_deployment - new module.
- node_deployment_info - new module.
- node_group - new module.
- node_group_info - new module.
- node_replication_status_info - new module.
- pan_ha_info - new module.
- portal_global_setting_info - new module.
- portal_info - new module.
- portal_theme - new module.
- portal_theme_info - new module.
- radius_server_sequence - new module.
- radius_server_sequence_info - new module.
- rest_id_store - new module.
- rest_id_store_info - new module.
- self_registered_portal - new module.
- self_registered_portal_info - new module.
- sg_acl - new module.
- sg_acl_bulk_monitor_status_info - new module.
- sg_acl_info - new module.
- sgt - new module.
- sgt_bulk_monitor_status_info - new module.
- sgt_info - new module.
- sms_provider_info - new module.
- sponsor_group - new module.
- sponsor_group_info - new module.
- sponsor_group_member_info - new module.
- sponsor_portal - new module.
- sponsor_portal_info - new module.
- sponsored_guest_portal - new module.
- sponsored_guest_portal_info - new module.
- system_certificate_info - new module.
- tacacs_command_sets - new module.
- tacacs_command_sets_info - new module.
- tacacs_external_servers - new module.
- tacacs_external_servers_info - new module.
- tacacs_profile - new module.
- tacacs_profile_info - new module.
- tacacs_server_sequence - new module.
- tacacs_server_sequence_info - new module.
- trusted_certificate_export_info - new module.
- trusted_certificate_info - new module.

v0.0.1
======

Release Summary
---------------

This is the initial beta release of the collection.
