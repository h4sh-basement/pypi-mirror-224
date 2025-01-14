# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/auth/service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ftecton_proto/auth/service.proto\x12\x11tecton_proto.auth\x1a google/protobuf/descriptor.proto\"\x96\x01\n\x10\x41uditLogMetadata\x12+\n\x12write_to_audit_log\x18\x01 \x01(\x08R\x0fwriteToAuditLog\x12;\n\x1a\x63ustomer_facing_event_name\x18\x02 \x01(\tR\x17\x63ustomerFacingEventName\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version\"\xff\x03\n\x0c\x41uthMetadata\x12\x36\n\x13skip_authentication\x18\x01 \x01(\x08:\x05\x66\x61lseR\x12skipAuthentication\x12\x34\n\x12skip_authorization\x18\x02 \x01(\x08:\x05\x66\x61lseR\x11skipAuthorization\x12.\n\npermission\x18\x05 \x01(\t:\x0enot_configuredR\npermission\x12i\n\x1d\x61\x64vanced_permission_overrides\x18\x06 \x03(\x0b\x32%.tecton_proto.auth.PermissionOverrideR\x1b\x61\x64vancedPermissionOverrides\x12S\n\x12resource_reference\x18\x03 \x01(\x0b\x32$.tecton_proto.auth.ResourceReferenceR\x11resourceReference\x12\x45\n\x1cLEGACY_require_admin_api_key\x18\x07 \x01(\x08:\x05\x66\x61lseR\x18LEGACYRequireAdminApiKey\x12J\n\x1e\x64\x65\x66\x65r_authorization_to_service\x18\x08 \x01(\x08:\x05\x66\x61lseR\x1b\x64\x65\x66\x65rAuthorizationToService\"\xa0\x01\n\x12PermissionOverride\x12\x30\n\x14\x63ondition_field_path\x18\x01 \x01(\tR\x12\x63onditionFieldPath\x12\'\n\x0f\x63ondition_value\x18\x02 \x01(\tR\x0e\x63onditionValue\x12/\n\x13permission_override\x18\x03 \x01(\tR\x12permissionOverride\"c\n\x11ResourceReference\x12:\n\x04type\x18\x01 \x01(\x0e\x32&.tecton_proto.auth.ResourceRefTypeEnumR\x04type\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path*\xae\x01\n\x13ResourceRefTypeEnum\x12\x1d\n\x19RESOURCE_REF_TYPE_UNKNOWN\x10\x00\x12$\n RESOURCE_REF_TYPE_WORKSPACE_NAME\x10\x01\x12(\n$RESOURCE_REF_TYPE_SERVICE_ACCOUNT_ID\x10\x02\x12(\n$RESOURCE_REF_TYPE_PRINCIPAL_GROUP_ID\x10\x03:g\n\rauth_metadata\x12\x1e.google.protobuf.MethodOptions\x18\xc4\xe7\x8cX \x01(\x0b\x32\x1f.tecton_proto.auth.AuthMetadataR\x0c\x61uthMetadata:t\n\x12\x61udit_log_metadata\x12\x1e.google.protobuf.MethodOptions\x18\xc5\xe7\x8cX \x01(\x0b\x32#.tecton_proto.auth.AuditLogMetadataR\x10\x61uditLogMetadata')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.auth.service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(auth_metadata)
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(audit_log_metadata)

  DESCRIPTOR._options = None
  _RESOURCEREFTYPEENUM._serialized_start=1020
  _RESOURCEREFTYPEENUM._serialized_end=1194
  _AUDITLOGMETADATA._serialized_start=89
  _AUDITLOGMETADATA._serialized_end=239
  _AUTHMETADATA._serialized_start=242
  _AUTHMETADATA._serialized_end=753
  _PERMISSIONOVERRIDE._serialized_start=756
  _PERMISSIONOVERRIDE._serialized_end=916
  _RESOURCEREFERENCE._serialized_start=918
  _RESOURCEREFERENCE._serialized_end=1017
# @@protoc_insertion_point(module_scope)
