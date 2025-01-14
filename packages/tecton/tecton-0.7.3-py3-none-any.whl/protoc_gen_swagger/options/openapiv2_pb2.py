# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protoc-gen-swagger/options/openapiv2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*protoc-gen-swagger/options/openapiv2.proto\x12\'grpc.gateway.protoc_gen_swagger.options\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xb8\x08\n\x07Swagger\x12\x18\n\x07swagger\x18\x01 \x01(\tR\x07swagger\x12\x41\n\x04info\x18\x02 \x01(\x0b\x32-.grpc.gateway.protoc_gen_swagger.options.InfoR\x04info\x12\x12\n\x04host\x18\x03 \x01(\tR\x04host\x12\x1b\n\tbase_path\x18\x04 \x01(\tR\x08\x62\x61sePath\x12X\n\x07schemes\x18\x05 \x03(\x0e\x32>.grpc.gateway.protoc_gen_swagger.options.Swagger.SwaggerSchemeR\x07schemes\x12\x1a\n\x08\x63onsumes\x18\x06 \x03(\tR\x08\x63onsumes\x12\x1a\n\x08produces\x18\x07 \x03(\tR\x08produces\x12]\n\tresponses\x18\n \x03(\x0b\x32?.grpc.gateway.protoc_gen_swagger.options.Swagger.ResponsesEntryR\tresponses\x12o\n\x14security_definitions\x18\x0b \x01(\x0b\x32<.grpc.gateway.protoc_gen_swagger.options.SecurityDefinitionsR\x13securityDefinitions\x12X\n\x08security\x18\x0c \x03(\x0b\x32<.grpc.gateway.protoc_gen_swagger.options.SecurityRequirementR\x08security\x12\x63\n\rexternal_docs\x18\x0e \x01(\x0b\x32>.grpc.gateway.protoc_gen_swagger.options.ExternalDocumentationR\x0c\x65xternalDocs\x12`\n\nextensions\x18\x0f \x03(\x0b\x32@.grpc.gateway.protoc_gen_swagger.options.Swagger.ExtensionsEntryR\nextensions\x1ao\n\x0eResponsesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x31.grpc.gateway.protoc_gen_swagger.options.ResponseR\x05value:\x02\x38\x01\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\"B\n\rSwaggerScheme\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04HTTP\x10\x01\x12\t\n\x05HTTPS\x10\x02\x12\x06\n\x02WS\x10\x03\x12\x07\n\x03WSS\x10\x04J\x04\x08\x08\x10\tJ\x04\x08\t\x10\nJ\x04\x08\r\x10\x0e\"\xc2\x06\n\tOperation\x12\x12\n\x04tags\x18\x01 \x03(\tR\x04tags\x12\x18\n\x07summary\x18\x02 \x01(\tR\x07summary\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x63\n\rexternal_docs\x18\x04 \x01(\x0b\x32>.grpc.gateway.protoc_gen_swagger.options.ExternalDocumentationR\x0c\x65xternalDocs\x12!\n\x0coperation_id\x18\x05 \x01(\tR\x0boperationId\x12\x1a\n\x08\x63onsumes\x18\x06 \x03(\tR\x08\x63onsumes\x12\x1a\n\x08produces\x18\x07 \x03(\tR\x08produces\x12_\n\tresponses\x18\t \x03(\x0b\x32\x41.grpc.gateway.protoc_gen_swagger.options.Operation.ResponsesEntryR\tresponses\x12\x18\n\x07schemes\x18\n \x03(\tR\x07schemes\x12\x1e\n\ndeprecated\x18\x0b \x01(\x08R\ndeprecated\x12X\n\x08security\x18\x0c \x03(\x0b\x32<.grpc.gateway.protoc_gen_swagger.options.SecurityRequirementR\x08security\x12\x62\n\nextensions\x18\r \x03(\x0b\x32\x42.grpc.gateway.protoc_gen_swagger.options.Operation.ExtensionsEntryR\nextensions\x1ao\n\x0eResponsesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x31.grpc.gateway.protoc_gen_swagger.options.ResponseR\x05value:\x02\x38\x01\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01J\x04\x08\x08\x10\t\"\xd8\x01\n\x06Header\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x16\n\x06\x66ormat\x18\x03 \x01(\tR\x06\x66ormat\x12\x18\n\x07\x64\x65\x66\x61ult\x18\x06 \x01(\tR\x07\x64\x65\x66\x61ult\x12\x18\n\x07pattern\x18\r \x01(\tR\x07patternJ\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\tJ\x04\x08\t\x10\nJ\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0cJ\x04\x08\x0c\x10\rJ\x04\x08\x0e\x10\x0fJ\x04\x08\x0f\x10\x10J\x04\x08\x10\x10\x11J\x04\x08\x11\x10\x12J\x04\x08\x12\x10\x13\"\x90\x05\n\x08Response\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12G\n\x06schema\x18\x02 \x01(\x0b\x32/.grpc.gateway.protoc_gen_swagger.options.SchemaR\x06schema\x12X\n\x07headers\x18\x03 \x03(\x0b\x32>.grpc.gateway.protoc_gen_swagger.options.Response.HeadersEntryR\x07headers\x12[\n\x08\x65xamples\x18\x04 \x03(\x0b\x32?.grpc.gateway.protoc_gen_swagger.options.Response.ExamplesEntryR\x08\x65xamples\x12\x61\n\nextensions\x18\x05 \x03(\x0b\x32\x41.grpc.gateway.protoc_gen_swagger.options.Response.ExtensionsEntryR\nextensions\x1ak\n\x0cHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32/.grpc.gateway.protoc_gen_swagger.options.HeaderR\x05value:\x02\x38\x01\x1a;\n\rExamplesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\"\xd0\x03\n\x04Info\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12(\n\x10terms_of_service\x18\x03 \x01(\tR\x0etermsOfService\x12J\n\x07\x63ontact\x18\x04 \x01(\x0b\x32\x30.grpc.gateway.protoc_gen_swagger.options.ContactR\x07\x63ontact\x12J\n\x07license\x18\x05 \x01(\x0b\x32\x30.grpc.gateway.protoc_gen_swagger.options.LicenseR\x07license\x12\x18\n\x07version\x18\x06 \x01(\tR\x07version\x12]\n\nextensions\x18\x07 \x03(\x0b\x32=.grpc.gateway.protoc_gen_swagger.options.Info.ExtensionsEntryR\nextensions\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\"E\n\x07\x43ontact\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x12\x14\n\x05\x65mail\x18\x03 \x01(\tR\x05\x65mail\"/\n\x07License\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\"K\n\x15\x45xternalDocumentation\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\"\xe7\x02\n\x06Schema\x12T\n\x0bjson_schema\x18\x01 \x01(\x0b\x32\x33.grpc.gateway.protoc_gen_swagger.options.JSONSchemaR\njsonSchema\x12$\n\rdiscriminator\x18\x02 \x01(\tR\rdiscriminator\x12\x1b\n\tread_only\x18\x03 \x01(\x08R\x08readOnly\x12\x63\n\rexternal_docs\x18\x05 \x01(\x0b\x32>.grpc.gateway.protoc_gen_swagger.options.ExternalDocumentationR\x0c\x65xternalDocs\x12\x32\n\x07\x65xample\x18\x06 \x01(\x0b\x32\x14.google.protobuf.AnyB\x02\x18\x01R\x07\x65xample\x12%\n\x0e\x65xample_string\x18\x07 \x01(\tR\rexampleStringJ\x04\x08\x04\x10\x05\"\xdd\x07\n\nJSONSchema\x12\x10\n\x03ref\x18\x03 \x01(\tR\x03ref\x12\x14\n\x05title\x18\x05 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12\x18\n\x07\x64\x65\x66\x61ult\x18\x07 \x01(\tR\x07\x64\x65\x66\x61ult\x12\x1b\n\tread_only\x18\x08 \x01(\x08R\x08readOnly\x12\x18\n\x07\x65xample\x18\t \x01(\tR\x07\x65xample\x12\x1f\n\x0bmultiple_of\x18\n \x01(\x01R\nmultipleOf\x12\x18\n\x07maximum\x18\x0b \x01(\x01R\x07maximum\x12+\n\x11\x65xclusive_maximum\x18\x0c \x01(\x08R\x10\x65xclusiveMaximum\x12\x18\n\x07minimum\x18\r \x01(\x01R\x07minimum\x12+\n\x11\x65xclusive_minimum\x18\x0e \x01(\x08R\x10\x65xclusiveMinimum\x12\x1d\n\nmax_length\x18\x0f \x01(\x04R\tmaxLength\x12\x1d\n\nmin_length\x18\x10 \x01(\x04R\tminLength\x12\x18\n\x07pattern\x18\x11 \x01(\tR\x07pattern\x12\x1b\n\tmax_items\x18\x14 \x01(\x04R\x08maxItems\x12\x1b\n\tmin_items\x18\x15 \x01(\x04R\x08minItems\x12!\n\x0cunique_items\x18\x16 \x01(\x08R\x0buniqueItems\x12%\n\x0emax_properties\x18\x18 \x01(\x04R\rmaxProperties\x12%\n\x0emin_properties\x18\x19 \x01(\x04R\rminProperties\x12\x1a\n\x08required\x18\x1a \x03(\tR\x08required\x12\x14\n\x05\x61rray\x18\" \x03(\tR\x05\x61rray\x12]\n\x04type\x18# \x03(\x0e\x32I.grpc.gateway.protoc_gen_swagger.options.JSONSchema.JSONSchemaSimpleTypesR\x04type\x12\x16\n\x06\x66ormat\x18$ \x01(\tR\x06\x66ormat\x12\x12\n\x04\x65num\x18. \x03(\tR\x04\x65num\"w\n\x15JSONSchemaSimpleTypes\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x41RRAY\x10\x01\x12\x0b\n\x07\x42OOLEAN\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\x08\n\x04NULL\x10\x04\x12\n\n\x06NUMBER\x10\x05\x12\n\n\x06OBJECT\x10\x06\x12\n\n\x06STRING\x10\x07J\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x04\x10\x05J\x04\x08\x12\x10\x13J\x04\x08\x13\x10\x14J\x04\x08\x17\x10\x18J\x04\x08\x1b\x10\x1cJ\x04\x08\x1c\x10\x1dJ\x04\x08\x1d\x10\x1eJ\x04\x08\x1e\x10\"J\x04\x08%\x10*J\x04\x08*\x10+J\x04\x08+\x10.\"\x92\x01\n\x03Tag\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x63\n\rexternal_docs\x18\x03 \x01(\x0b\x32>.grpc.gateway.protoc_gen_swagger.options.ExternalDocumentationR\x0c\x65xternalDocsJ\x04\x08\x01\x10\x02\"\xf3\x01\n\x13SecurityDefinitions\x12\x66\n\x08security\x18\x01 \x03(\x0b\x32J.grpc.gateway.protoc_gen_swagger.options.SecurityDefinitions.SecurityEntryR\x08security\x1at\n\rSecurityEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12M\n\x05value\x18\x02 \x01(\x0b\x32\x37.grpc.gateway.protoc_gen_swagger.options.SecuritySchemeR\x05value:\x02\x38\x01\"\xf5\x06\n\x0eSecurityScheme\x12P\n\x04type\x18\x01 \x01(\x0e\x32<.grpc.gateway.protoc_gen_swagger.options.SecurityScheme.TypeR\x04type\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12J\n\x02in\x18\x04 \x01(\x0e\x32:.grpc.gateway.protoc_gen_swagger.options.SecurityScheme.InR\x02in\x12P\n\x04\x66low\x18\x05 \x01(\x0e\x32<.grpc.gateway.protoc_gen_swagger.options.SecurityScheme.FlowR\x04\x66low\x12+\n\x11\x61uthorization_url\x18\x06 \x01(\tR\x10\x61uthorizationUrl\x12\x1b\n\ttoken_url\x18\x07 \x01(\tR\x08tokenUrl\x12G\n\x06scopes\x18\x08 \x01(\x0b\x32/.grpc.gateway.protoc_gen_swagger.options.ScopesR\x06scopes\x12g\n\nextensions\x18\t \x03(\x0b\x32G.grpc.gateway.protoc_gen_swagger.options.SecurityScheme.ExtensionsEntryR\nextensions\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\"K\n\x04Type\x12\x10\n\x0cTYPE_INVALID\x10\x00\x12\x0e\n\nTYPE_BASIC\x10\x01\x12\x10\n\x0cTYPE_API_KEY\x10\x02\x12\x0f\n\x0bTYPE_OAUTH2\x10\x03\"1\n\x02In\x12\x0e\n\nIN_INVALID\x10\x00\x12\x0c\n\x08IN_QUERY\x10\x01\x12\r\n\tIN_HEADER\x10\x02\"j\n\x04\x46low\x12\x10\n\x0c\x46LOW_INVALID\x10\x00\x12\x11\n\rFLOW_IMPLICIT\x10\x01\x12\x11\n\rFLOW_PASSWORD\x10\x02\x12\x14\n\x10\x46LOW_APPLICATION\x10\x03\x12\x14\n\x10\x46LOW_ACCESS_CODE\x10\x04\"\xf2\x02\n\x13SecurityRequirement\x12\x88\x01\n\x14security_requirement\x18\x01 \x03(\x0b\x32U.grpc.gateway.protoc_gen_swagger.options.SecurityRequirement.SecurityRequirementEntryR\x13securityRequirement\x1a\x30\n\x18SecurityRequirementValue\x12\x14\n\x05scope\x18\x01 \x03(\tR\x05scope\x1a\x9d\x01\n\x18SecurityRequirementEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12k\n\x05value\x18\x02 \x01(\x0b\x32U.grpc.gateway.protoc_gen_swagger.options.SecurityRequirement.SecurityRequirementValueR\x05value:\x02\x38\x01\"\x94\x01\n\x06Scopes\x12P\n\x05scope\x18\x01 \x03(\x0b\x32:.grpc.gateway.protoc_gen_swagger.options.Scopes.ScopeEntryR\x05scope\x1a\x38\n\nScopeEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x43ZAgithub.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/optionsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protoc_gen_swagger.options.openapiv2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZAgithub.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/options'
  _SWAGGER_RESPONSESENTRY._options = None
  _SWAGGER_RESPONSESENTRY._serialized_options = b'8\001'
  _SWAGGER_EXTENSIONSENTRY._options = None
  _SWAGGER_EXTENSIONSENTRY._serialized_options = b'8\001'
  _OPERATION_RESPONSESENTRY._options = None
  _OPERATION_RESPONSESENTRY._serialized_options = b'8\001'
  _OPERATION_EXTENSIONSENTRY._options = None
  _OPERATION_EXTENSIONSENTRY._serialized_options = b'8\001'
  _RESPONSE_HEADERSENTRY._options = None
  _RESPONSE_HEADERSENTRY._serialized_options = b'8\001'
  _RESPONSE_EXAMPLESENTRY._options = None
  _RESPONSE_EXAMPLESENTRY._serialized_options = b'8\001'
  _RESPONSE_EXTENSIONSENTRY._options = None
  _RESPONSE_EXTENSIONSENTRY._serialized_options = b'8\001'
  _INFO_EXTENSIONSENTRY._options = None
  _INFO_EXTENSIONSENTRY._serialized_options = b'8\001'
  _SCHEMA.fields_by_name['example']._options = None
  _SCHEMA.fields_by_name['example']._serialized_options = b'\030\001'
  _SECURITYDEFINITIONS_SECURITYENTRY._options = None
  _SECURITYDEFINITIONS_SECURITYENTRY._serialized_options = b'8\001'
  _SECURITYSCHEME_EXTENSIONSENTRY._options = None
  _SECURITYSCHEME_EXTENSIONSENTRY._serialized_options = b'8\001'
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY._options = None
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY._serialized_options = b'8\001'
  _SCOPES_SCOPEENTRY._options = None
  _SCOPES_SCOPEENTRY._serialized_options = b'8\001'
  _SWAGGER._serialized_start=145
  _SWAGGER._serialized_end=1225
  _SWAGGER_RESPONSESENTRY._serialized_start=941
  _SWAGGER_RESPONSESENTRY._serialized_end=1052
  _SWAGGER_EXTENSIONSENTRY._serialized_start=1054
  _SWAGGER_EXTENSIONSENTRY._serialized_end=1139
  _SWAGGER_SWAGGERSCHEME._serialized_start=1141
  _SWAGGER_SWAGGERSCHEME._serialized_end=1207
  _OPERATION._serialized_start=1228
  _OPERATION._serialized_end=2062
  _OPERATION_RESPONSESENTRY._serialized_start=941
  _OPERATION_RESPONSESENTRY._serialized_end=1052
  _OPERATION_EXTENSIONSENTRY._serialized_start=1054
  _OPERATION_EXTENSIONSENTRY._serialized_end=1139
  _HEADER._serialized_start=2065
  _HEADER._serialized_end=2281
  _RESPONSE._serialized_start=2284
  _RESPONSE._serialized_end=2940
  _RESPONSE_HEADERSENTRY._serialized_start=2685
  _RESPONSE_HEADERSENTRY._serialized_end=2792
  _RESPONSE_EXAMPLESENTRY._serialized_start=2794
  _RESPONSE_EXAMPLESENTRY._serialized_end=2853
  _RESPONSE_EXTENSIONSENTRY._serialized_start=1054
  _RESPONSE_EXTENSIONSENTRY._serialized_end=1139
  _INFO._serialized_start=2943
  _INFO._serialized_end=3407
  _INFO_EXTENSIONSENTRY._serialized_start=1054
  _INFO_EXTENSIONSENTRY._serialized_end=1139
  _CONTACT._serialized_start=3409
  _CONTACT._serialized_end=3478
  _LICENSE._serialized_start=3480
  _LICENSE._serialized_end=3527
  _EXTERNALDOCUMENTATION._serialized_start=3529
  _EXTERNALDOCUMENTATION._serialized_end=3604
  _SCHEMA._serialized_start=3607
  _SCHEMA._serialized_end=3966
  _JSONSCHEMA._serialized_start=3969
  _JSONSCHEMA._serialized_end=4958
  _JSONSCHEMA_JSONSCHEMASIMPLETYPES._serialized_start=4761
  _JSONSCHEMA_JSONSCHEMASIMPLETYPES._serialized_end=4880
  _TAG._serialized_start=4961
  _TAG._serialized_end=5107
  _SECURITYDEFINITIONS._serialized_start=5110
  _SECURITYDEFINITIONS._serialized_end=5353
  _SECURITYDEFINITIONS_SECURITYENTRY._serialized_start=5237
  _SECURITYDEFINITIONS_SECURITYENTRY._serialized_end=5353
  _SECURITYSCHEME._serialized_start=5356
  _SECURITYSCHEME._serialized_end=6241
  _SECURITYSCHEME_EXTENSIONSENTRY._serialized_start=1054
  _SECURITYSCHEME_EXTENSIONSENTRY._serialized_end=1139
  _SECURITYSCHEME_TYPE._serialized_start=6007
  _SECURITYSCHEME_TYPE._serialized_end=6082
  _SECURITYSCHEME_IN._serialized_start=6084
  _SECURITYSCHEME_IN._serialized_end=6133
  _SECURITYSCHEME_FLOW._serialized_start=6135
  _SECURITYSCHEME_FLOW._serialized_end=6241
  _SECURITYREQUIREMENT._serialized_start=6244
  _SECURITYREQUIREMENT._serialized_end=6614
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTVALUE._serialized_start=6406
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTVALUE._serialized_end=6454
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY._serialized_start=6457
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY._serialized_end=6614
  _SCOPES._serialized_start=6617
  _SCOPES._serialized_end=6765
  _SCOPES_SCOPEENTRY._serialized_start=6709
  _SCOPES_SCOPEENTRY._serialized_end=6765
# @@protoc_insertion_point(module_scope)
