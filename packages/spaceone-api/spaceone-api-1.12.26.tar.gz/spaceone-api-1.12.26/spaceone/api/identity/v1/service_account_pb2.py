# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v1/service_account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2
from spaceone.api.identity.v1 import project_pb2 as spaceone_dot_api_dot_identity_dot_v1_dot_project__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.spaceone/api/identity/v1/service_account.proto\x12\x18spaceone.api.identity.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\x1a&spaceone/api/identity/v1/project.proto\"\xf4\x01\n\x1b\x43reateServiceAccountRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x12\n\nproject_id\x18\x04 \x01(\t\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x1c\n\x14service_account_type\x18\x0b \x01(\t\x12\"\n\x1atrusted_service_account_id\x18\x0c \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"\x89\x02\n\x1bUpdateServiceAccountRequest\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nproject_id\x18\x04 \x01(\t\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\"\n\x1atrusted_service_account_id\x18\x06 \x01(\t\x12\'\n\x1frelease_trusted_service_account\x18\x07 \x01(\x08\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"F\n\x15ServiceAccountRequest\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"W\n\x18GetServiceAccountRequest\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\x89\x02\n\x13ServiceAccountQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x1a\n\x12service_account_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1c\n\x14service_account_type\x18\x04 \x01(\t\x12\x10\n\x08provider\x18\x05 \x01(\t\x12\"\n\x1atrusted_service_account_id\x18\x06 \x01(\t\x12\x12\n\nproject_id\x18\x07 \x01(\t\x12\r\n\x05scope\x18\x08 \x01(\t\x12\x12\n\nhas_secret\x18\t \x01(\x08\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"\xd3\x02\n\x12ServiceAccountInfo\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1c\n\x14service_account_type\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08provider\x18\x05 \x01(\t\x12\"\n\x1atrusted_service_account_id\x18\x06 \x01(\t\x12;\n\x0cproject_info\x18\x07 \x01(\x0b\x32%.spaceone.api.identity.v1.ProjectInfo\x12\r\n\x05scope\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12%\n\x04tags\x18\x16 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\ncreated_at\x18\x17 \x01(\t\"i\n\x13ServiceAccountsInfo\x12=\n\x07results\x18\x01 \x03(\x0b\x32,.spaceone.api.identity.v1.ServiceAccountInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"v\n\x17ServiceAccountStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x12\n\nhas_secret\x18\x03 \x01(\x08\x32\x85\x07\n\x0eServiceAccount\x12\x9d\x01\n\x06\x63reate\x12\x35.spaceone.api.identity.v1.CreateServiceAccountRequest\x1a,.spaceone.api.identity.v1.ServiceAccountInfo\".\x82\xd3\xe4\x93\x02(\"#/identity/v1/service-account/create:\x01*\x12\x9d\x01\n\x06update\x12\x35.spaceone.api.identity.v1.UpdateServiceAccountRequest\x1a,.spaceone.api.identity.v1.ServiceAccountInfo\".\x82\xd3\xe4\x93\x02(\"#/identity/v1/service-account/update:\x01*\x12\x81\x01\n\x06\x64\x65lete\x12/.spaceone.api.identity.v1.ServiceAccountRequest\x1a\x16.google.protobuf.Empty\".\x82\xd3\xe4\x93\x02(\"#/identity/v1/service-account/delete:\x01*\x12\x94\x01\n\x03get\x12\x32.spaceone.api.identity.v1.GetServiceAccountRequest\x1a,.spaceone.api.identity.v1.ServiceAccountInfo\"+\x82\xd3\xe4\x93\x02%\" /identity/v1/service-account/get:\x01*\x12\x93\x01\n\x04list\x12-.spaceone.api.identity.v1.ServiceAccountQuery\x1a-.spaceone.api.identity.v1.ServiceAccountsInfo\"-\x82\xd3\xe4\x93\x02\'\"\"/identity/v1/service-accounts/list:\x01*\x12\x81\x01\n\x04stat\x12\x31.spaceone.api.identity.v1.ServiceAccountStatQuery\x1a\x17.google.protobuf.Struct\"-\x82\xd3\xe4\x93\x02\'\"\"/identity/v1/service-accounts/stat:\x01*B?Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v1b\x06proto3')



_CREATESERVICEACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['CreateServiceAccountRequest']
_UPDATESERVICEACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['UpdateServiceAccountRequest']
_SERVICEACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['ServiceAccountRequest']
_GETSERVICEACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['GetServiceAccountRequest']
_SERVICEACCOUNTQUERY = DESCRIPTOR.message_types_by_name['ServiceAccountQuery']
_SERVICEACCOUNTINFO = DESCRIPTOR.message_types_by_name['ServiceAccountInfo']
_SERVICEACCOUNTSINFO = DESCRIPTOR.message_types_by_name['ServiceAccountsInfo']
_SERVICEACCOUNTSTATQUERY = DESCRIPTOR.message_types_by_name['ServiceAccountStatQuery']
CreateServiceAccountRequest = _reflection.GeneratedProtocolMessageType('CreateServiceAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVICEACCOUNTREQUEST,
  '__module__' : 'spaceone.api.identity.v1.service_account_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.CreateServiceAccountRequest)
  })
_sym_db.RegisterMessage(CreateServiceAccountRequest)

UpdateServiceAccountRequest = _reflection.GeneratedProtocolMessageType('UpdateServiceAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESERVICEACCOUNTREQUEST,
  '__module__' : 'spaceone.api.identity.v1.service_account_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.UpdateServiceAccountRequest)
  })
_sym_db.RegisterMessage(UpdateServiceAccountRequest)

ServiceAccountRequest = _reflection.GeneratedProtocolMessageType('ServiceAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEACCOUNTREQUEST,
  '__module__' : 'spaceone.api.identity.v1.service_account_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ServiceAccountRequest)
  })
_sym_db.RegisterMessage(ServiceAccountRequest)

GetServiceAccountRequest = _reflection.GeneratedProtocolMessageType('GetServiceAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVICEACCOUNTREQUEST,
  '__module__' : 'spaceone.api.identity.v1.service_account_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.GetServiceAccountRequest)
  })
_sym_db.RegisterMessage(GetServiceAccountRequest)

ServiceAccountQuery = _reflection.GeneratedProtocolMessageType('ServiceAccountQuery', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEACCOUNTQUERY,
  '__module__' : 'spaceone.api.identity.v1.service_account_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ServiceAccountQuery)
  })
_sym_db.RegisterMessage(ServiceAccountQuery)

ServiceAccountInfo = _reflection.GeneratedProtocolMessageType('ServiceAccountInfo', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEACCOUNTINFO,
  '__module__' : 'spaceone.api.identity.v1.service_account_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ServiceAccountInfo)
  })
_sym_db.RegisterMessage(ServiceAccountInfo)

ServiceAccountsInfo = _reflection.GeneratedProtocolMessageType('ServiceAccountsInfo', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEACCOUNTSINFO,
  '__module__' : 'spaceone.api.identity.v1.service_account_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ServiceAccountsInfo)
  })
_sym_db.RegisterMessage(ServiceAccountsInfo)

ServiceAccountStatQuery = _reflection.GeneratedProtocolMessageType('ServiceAccountStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEACCOUNTSTATQUERY,
  '__module__' : 'spaceone.api.identity.v1.service_account_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ServiceAccountStatQuery)
  })
_sym_db.RegisterMessage(ServiceAccountStatQuery)

_SERVICEACCOUNT = DESCRIPTOR.services_by_name['ServiceAccount']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v1'
  _SERVICEACCOUNT.methods_by_name['create']._options = None
  _SERVICEACCOUNT.methods_by_name['create']._serialized_options = b'\202\323\344\223\002(\"#/identity/v1/service-account/create:\001*'
  _SERVICEACCOUNT.methods_by_name['update']._options = None
  _SERVICEACCOUNT.methods_by_name['update']._serialized_options = b'\202\323\344\223\002(\"#/identity/v1/service-account/update:\001*'
  _SERVICEACCOUNT.methods_by_name['delete']._options = None
  _SERVICEACCOUNT.methods_by_name['delete']._serialized_options = b'\202\323\344\223\002(\"#/identity/v1/service-account/delete:\001*'
  _SERVICEACCOUNT.methods_by_name['get']._options = None
  _SERVICEACCOUNT.methods_by_name['get']._serialized_options = b'\202\323\344\223\002%\" /identity/v1/service-account/get:\001*'
  _SERVICEACCOUNT.methods_by_name['list']._options = None
  _SERVICEACCOUNT.methods_by_name['list']._serialized_options = b'\202\323\344\223\002\'\"\"/identity/v1/service-accounts/list:\001*'
  _SERVICEACCOUNT.methods_by_name['stat']._options = None
  _SERVICEACCOUNT.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\'\"\"/identity/v1/service-accounts/stat:\001*'
  _CREATESERVICEACCOUNTREQUEST._serialized_start=240
  _CREATESERVICEACCOUNTREQUEST._serialized_end=484
  _UPDATESERVICEACCOUNTREQUEST._serialized_start=487
  _UPDATESERVICEACCOUNTREQUEST._serialized_end=752
  _SERVICEACCOUNTREQUEST._serialized_start=754
  _SERVICEACCOUNTREQUEST._serialized_end=824
  _GETSERVICEACCOUNTREQUEST._serialized_start=826
  _GETSERVICEACCOUNTREQUEST._serialized_end=913
  _SERVICEACCOUNTQUERY._serialized_start=916
  _SERVICEACCOUNTQUERY._serialized_end=1181
  _SERVICEACCOUNTINFO._serialized_start=1184
  _SERVICEACCOUNTINFO._serialized_end=1523
  _SERVICEACCOUNTSINFO._serialized_start=1525
  _SERVICEACCOUNTSINFO._serialized_end=1630
  _SERVICEACCOUNTSTATQUERY._serialized_start=1632
  _SERVICEACCOUNTSTATQUERY._serialized_end=1750
  _SERVICEACCOUNT._serialized_start=1753
  _SERVICEACCOUNT._serialized_end=2654
# @@protoc_insertion_point(module_scope)
