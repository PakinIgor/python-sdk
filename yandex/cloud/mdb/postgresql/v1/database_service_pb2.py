# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/postgresql/v1/database_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.api import operation_pb2 as yandex_dot_api_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.mdb.postgresql.v1 import database_pb2 as yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_database__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/postgresql/v1/database_service.proto',
  package='yandex.cloud.mdb.postgresql.v1',
  syntax='proto3',
  serialized_pb=_b('\n5yandex/cloud/mdb/postgresql/v1/database_service.proto\x12\x1eyandex.cloud.mdb.postgresql.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1ayandex/api/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a&yandex/cloud/operation/operation.proto\x1a-yandex/cloud/mdb/postgresql/v1/database.proto\"l\n\x12GetDatabaseRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x34\n\rdatabase_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04\x31-63\xf2\xc7\x31\r[a-zA-Z0-9_]+\"v\n\x14ListDatabasesRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"m\n\x15ListDatabasesResponse\x12;\n\tdatabases\x18\x01 \x03(\x0b\x32(.yandex.cloud.mdb.postgresql.v1.Database\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x84\x01\n\x15\x43reateDatabaseRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12I\n\rdatabase_spec\x18\x02 \x01(\x0b\x32,.yandex.cloud.mdb.postgresql.v1.DatabaseSpecB\x04\xe8\xc7\x31\x01\"C\n\x16\x43reateDatabaseMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x15\n\rdatabase_name\x18\x02 \x01(\t\"\xdf\x01\n\x15UpdateDatabaseRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x34\n\rdatabase_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04\x31-63\xf2\xc7\x31\r[a-zA-Z0-9_]+\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12=\n\nextensions\x18\x04 \x03(\x0b\x32).yandex.cloud.mdb.postgresql.v1.Extension\"C\n\x16UpdateDatabaseMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x15\n\rdatabase_name\x18\x02 \x01(\t\"o\n\x15\x44\x65leteDatabaseRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x34\n\rdatabase_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04\x31-63\xf2\xc7\x31\r[a-zA-Z0-9_]+\"C\n\x16\x44\x65leteDatabaseMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x15\n\rdatabase_name\x18\x02 \x01(\t2\x92\x08\n\x0f\x44\x61tabaseService\x12\xb3\x01\n\x03Get\x12\x32.yandex.cloud.mdb.postgresql.v1.GetDatabaseRequest\x1a(.yandex.cloud.mdb.postgresql.v1.Database\"N\x82\xd3\xe4\x93\x02H\x12\x46/managed-postgresql/v1/clusters/{cluster_id}/databases/{database_name}\x12\xb3\x01\n\x04List\x12\x34.yandex.cloud.mdb.postgresql.v1.ListDatabasesRequest\x1a\x35.yandex.cloud.mdb.postgresql.v1.ListDatabasesResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/managed-postgresql/v1/clusters/{cluster_id}/databases\x12\xcb\x01\n\x06\x43reate\x12\x35.yandex.cloud.mdb.postgresql.v1.CreateDatabaseRequest\x1a!.yandex.cloud.operation.Operation\"g\x82\xd3\xe4\x93\x02;\"6/managed-postgresql/v1/clusters/{cluster_id}/databases:\x01*\xb2\xd2*\"\n\x16\x43reateDatabaseMetadata\x12\x08\x44\x61tabase\x12\xdb\x01\n\x06Update\x12\x35.yandex.cloud.mdb.postgresql.v1.UpdateDatabaseRequest\x1a!.yandex.cloud.operation.Operation\"w\x82\xd3\xe4\x93\x02K2F/managed-postgresql/v1/clusters/{cluster_id}/databases/{database_name}:\x01*\xb2\xd2*\"\n\x16UpdateDatabaseMetadata\x12\x08\x44\x61tabase\x12\xe6\x01\n\x06\x44\x65lete\x12\x35.yandex.cloud.mdb.postgresql.v1.DeleteDatabaseRequest\x1a!.yandex.cloud.operation.Operation\"\x81\x01\x82\xd3\xe4\x93\x02H*F/managed-postgresql/v1/clusters/{cluster_id}/databases/{database_name}\xb2\xd2*/\n\x16\x44\x65leteDatabaseMetadata\x12\x15google.protobuf.EmptyBOZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1;postgresqlb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,yandex_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_database__pb2.DESCRIPTOR,])




_GETDATABASEREQUEST = _descriptor.Descriptor(
  name='GetDatabaseRequest',
  full_name='yandex.cloud.mdb.postgresql.v1.GetDatabaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.postgresql.v1.GetDatabaseRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.postgresql.v1.GetDatabaseRequest.database_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\0041-63\362\3071\r[a-zA-Z0-9_]+')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=407,
)


_LISTDATABASESREQUEST = _descriptor.Descriptor(
  name='ListDatabasesRequest',
  full_name='yandex.cloud.mdb.postgresql.v1.ListDatabasesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.postgresql.v1.ListDatabasesRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.mdb.postgresql.v1.ListDatabasesRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\3071\006<=1000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.mdb.postgresql.v1.ListDatabasesRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3101\005<=100')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=527,
)


_LISTDATABASESRESPONSE = _descriptor.Descriptor(
  name='ListDatabasesResponse',
  full_name='yandex.cloud.mdb.postgresql.v1.ListDatabasesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='databases', full_name='yandex.cloud.mdb.postgresql.v1.ListDatabasesResponse.databases', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.mdb.postgresql.v1.ListDatabasesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=638,
)


_CREATEDATABASEREQUEST = _descriptor.Descriptor(
  name='CreateDatabaseRequest',
  full_name='yandex.cloud.mdb.postgresql.v1.CreateDatabaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.postgresql.v1.CreateDatabaseRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database_spec', full_name='yandex.cloud.mdb.postgresql.v1.CreateDatabaseRequest.database_spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=641,
  serialized_end=773,
)


_CREATEDATABASEMETADATA = _descriptor.Descriptor(
  name='CreateDatabaseMetadata',
  full_name='yandex.cloud.mdb.postgresql.v1.CreateDatabaseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.postgresql.v1.CreateDatabaseMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.postgresql.v1.CreateDatabaseMetadata.database_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=775,
  serialized_end=842,
)


_UPDATEDATABASEREQUEST = _descriptor.Descriptor(
  name='UpdateDatabaseRequest',
  full_name='yandex.cloud.mdb.postgresql.v1.UpdateDatabaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.postgresql.v1.UpdateDatabaseRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.postgresql.v1.UpdateDatabaseRequest.database_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\0041-63\362\3071\r[a-zA-Z0-9_]+')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.mdb.postgresql.v1.UpdateDatabaseRequest.update_mask', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extensions', full_name='yandex.cloud.mdb.postgresql.v1.UpdateDatabaseRequest.extensions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=1068,
)


_UPDATEDATABASEMETADATA = _descriptor.Descriptor(
  name='UpdateDatabaseMetadata',
  full_name='yandex.cloud.mdb.postgresql.v1.UpdateDatabaseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.postgresql.v1.UpdateDatabaseMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.postgresql.v1.UpdateDatabaseMetadata.database_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1070,
  serialized_end=1137,
)


_DELETEDATABASEREQUEST = _descriptor.Descriptor(
  name='DeleteDatabaseRequest',
  full_name='yandex.cloud.mdb.postgresql.v1.DeleteDatabaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.postgresql.v1.DeleteDatabaseRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.postgresql.v1.DeleteDatabaseRequest.database_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\0041-63\362\3071\r[a-zA-Z0-9_]+')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1139,
  serialized_end=1250,
)


_DELETEDATABASEMETADATA = _descriptor.Descriptor(
  name='DeleteDatabaseMetadata',
  full_name='yandex.cloud.mdb.postgresql.v1.DeleteDatabaseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.postgresql.v1.DeleteDatabaseMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.postgresql.v1.DeleteDatabaseMetadata.database_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1252,
  serialized_end=1319,
)

_LISTDATABASESRESPONSE.fields_by_name['databases'].message_type = yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_database__pb2._DATABASE
_CREATEDATABASEREQUEST.fields_by_name['database_spec'].message_type = yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_database__pb2._DATABASESPEC
_UPDATEDATABASEREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATEDATABASEREQUEST.fields_by_name['extensions'].message_type = yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_database__pb2._EXTENSION
DESCRIPTOR.message_types_by_name['GetDatabaseRequest'] = _GETDATABASEREQUEST
DESCRIPTOR.message_types_by_name['ListDatabasesRequest'] = _LISTDATABASESREQUEST
DESCRIPTOR.message_types_by_name['ListDatabasesResponse'] = _LISTDATABASESRESPONSE
DESCRIPTOR.message_types_by_name['CreateDatabaseRequest'] = _CREATEDATABASEREQUEST
DESCRIPTOR.message_types_by_name['CreateDatabaseMetadata'] = _CREATEDATABASEMETADATA
DESCRIPTOR.message_types_by_name['UpdateDatabaseRequest'] = _UPDATEDATABASEREQUEST
DESCRIPTOR.message_types_by_name['UpdateDatabaseMetadata'] = _UPDATEDATABASEMETADATA
DESCRIPTOR.message_types_by_name['DeleteDatabaseRequest'] = _DELETEDATABASEREQUEST
DESCRIPTOR.message_types_by_name['DeleteDatabaseMetadata'] = _DELETEDATABASEMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetDatabaseRequest = _reflection.GeneratedProtocolMessageType('GetDatabaseRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETDATABASEREQUEST,
  __module__ = 'yandex.cloud.mdb.postgresql.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.postgresql.v1.GetDatabaseRequest)
  ))
_sym_db.RegisterMessage(GetDatabaseRequest)

ListDatabasesRequest = _reflection.GeneratedProtocolMessageType('ListDatabasesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTDATABASESREQUEST,
  __module__ = 'yandex.cloud.mdb.postgresql.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.postgresql.v1.ListDatabasesRequest)
  ))
_sym_db.RegisterMessage(ListDatabasesRequest)

ListDatabasesResponse = _reflection.GeneratedProtocolMessageType('ListDatabasesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTDATABASESRESPONSE,
  __module__ = 'yandex.cloud.mdb.postgresql.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.postgresql.v1.ListDatabasesResponse)
  ))
_sym_db.RegisterMessage(ListDatabasesResponse)

CreateDatabaseRequest = _reflection.GeneratedProtocolMessageType('CreateDatabaseRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEDATABASEREQUEST,
  __module__ = 'yandex.cloud.mdb.postgresql.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.postgresql.v1.CreateDatabaseRequest)
  ))
_sym_db.RegisterMessage(CreateDatabaseRequest)

CreateDatabaseMetadata = _reflection.GeneratedProtocolMessageType('CreateDatabaseMetadata', (_message.Message,), dict(
  DESCRIPTOR = _CREATEDATABASEMETADATA,
  __module__ = 'yandex.cloud.mdb.postgresql.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.postgresql.v1.CreateDatabaseMetadata)
  ))
_sym_db.RegisterMessage(CreateDatabaseMetadata)

UpdateDatabaseRequest = _reflection.GeneratedProtocolMessageType('UpdateDatabaseRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEDATABASEREQUEST,
  __module__ = 'yandex.cloud.mdb.postgresql.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.postgresql.v1.UpdateDatabaseRequest)
  ))
_sym_db.RegisterMessage(UpdateDatabaseRequest)

UpdateDatabaseMetadata = _reflection.GeneratedProtocolMessageType('UpdateDatabaseMetadata', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEDATABASEMETADATA,
  __module__ = 'yandex.cloud.mdb.postgresql.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.postgresql.v1.UpdateDatabaseMetadata)
  ))
_sym_db.RegisterMessage(UpdateDatabaseMetadata)

DeleteDatabaseRequest = _reflection.GeneratedProtocolMessageType('DeleteDatabaseRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEDATABASEREQUEST,
  __module__ = 'yandex.cloud.mdb.postgresql.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.postgresql.v1.DeleteDatabaseRequest)
  ))
_sym_db.RegisterMessage(DeleteDatabaseRequest)

DeleteDatabaseMetadata = _reflection.GeneratedProtocolMessageType('DeleteDatabaseMetadata', (_message.Message,), dict(
  DESCRIPTOR = _DELETEDATABASEMETADATA,
  __module__ = 'yandex.cloud.mdb.postgresql.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.postgresql.v1.DeleteDatabaseMetadata)
  ))
_sym_db.RegisterMessage(DeleteDatabaseMetadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1;postgresql'))
_GETDATABASEREQUEST.fields_by_name['cluster_id'].has_options = True
_GETDATABASEREQUEST.fields_by_name['cluster_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50'))
_GETDATABASEREQUEST.fields_by_name['database_name'].has_options = True
_GETDATABASEREQUEST.fields_by_name['database_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\0041-63\362\3071\r[a-zA-Z0-9_]+'))
_LISTDATABASESREQUEST.fields_by_name['cluster_id'].has_options = True
_LISTDATABASESREQUEST.fields_by_name['cluster_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50'))
_LISTDATABASESREQUEST.fields_by_name['page_size'].has_options = True
_LISTDATABASESREQUEST.fields_by_name['page_size']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\3071\006<=1000'))
_LISTDATABASESREQUEST.fields_by_name['page_token'].has_options = True
_LISTDATABASESREQUEST.fields_by_name['page_token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3101\005<=100'))
_CREATEDATABASEREQUEST.fields_by_name['cluster_id'].has_options = True
_CREATEDATABASEREQUEST.fields_by_name['cluster_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50'))
_CREATEDATABASEREQUEST.fields_by_name['database_spec'].has_options = True
_CREATEDATABASEREQUEST.fields_by_name['database_spec']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001'))
_UPDATEDATABASEREQUEST.fields_by_name['cluster_id'].has_options = True
_UPDATEDATABASEREQUEST.fields_by_name['cluster_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50'))
_UPDATEDATABASEREQUEST.fields_by_name['database_name'].has_options = True
_UPDATEDATABASEREQUEST.fields_by_name['database_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\0041-63\362\3071\r[a-zA-Z0-9_]+'))
_DELETEDATABASEREQUEST.fields_by_name['cluster_id'].has_options = True
_DELETEDATABASEREQUEST.fields_by_name['cluster_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50'))
_DELETEDATABASEREQUEST.fields_by_name['database_name'].has_options = True
_DELETEDATABASEREQUEST.fields_by_name['database_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\0041-63\362\3071\r[a-zA-Z0-9_]+'))

_DATABASESERVICE = _descriptor.ServiceDescriptor(
  name='DatabaseService',
  full_name='yandex.cloud.mdb.postgresql.v1.DatabaseService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1322,
  serialized_end=2364,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.mdb.postgresql.v1.DatabaseService.Get',
    index=0,
    containing_service=None,
    input_type=_GETDATABASEREQUEST,
    output_type=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_database__pb2._DATABASE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002H\022F/managed-postgresql/v1/clusters/{cluster_id}/databases/{database_name}')),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.mdb.postgresql.v1.DatabaseService.List',
    index=1,
    containing_service=None,
    input_type=_LISTDATABASESREQUEST,
    output_type=_LISTDATABASESRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0028\0226/managed-postgresql/v1/clusters/{cluster_id}/databases')),
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.mdb.postgresql.v1.DatabaseService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATEDATABASEREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002;\"6/managed-postgresql/v1/clusters/{cluster_id}/databases:\001*\262\322*\"\n\026CreateDatabaseMetadata\022\010Database')),
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.mdb.postgresql.v1.DatabaseService.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEDATABASEREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002K2F/managed-postgresql/v1/clusters/{cluster_id}/databases/{database_name}:\001*\262\322*\"\n\026UpdateDatabaseMetadata\022\010Database')),
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.mdb.postgresql.v1.DatabaseService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETEDATABASEREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002H*F/managed-postgresql/v1/clusters/{cluster_id}/databases/{database_name}\262\322*/\n\026DeleteDatabaseMetadata\022\025google.protobuf.Empty')),
  ),
])
_sym_db.RegisterServiceDescriptor(_DATABASESERVICE)

DESCRIPTOR.services_by_name['DatabaseService'] = _DATABASESERVICE

# @@protoc_insertion_point(module_scope)