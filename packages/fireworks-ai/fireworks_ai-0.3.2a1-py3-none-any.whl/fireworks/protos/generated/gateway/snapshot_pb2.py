# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/snapshot.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import status_pb2 as gateway_dot_status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16gateway/snapshot.proto\x12\x07gateway\x1a\x14gateway/status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa0\x02\n\x08Snapshot\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0\x41\x03\xe0\x41\x05\x12\x37\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x06\xe0\x41\x03\xe0\x41\x05\x12.\n\x05state\x18\x03 \x01(\x0e\x32\x17.gateway.Snapshot.StateB\x06\xe0\x41\x03\xe0\x41\x05\x12\'\n\x06status\x18\x04 \x01(\x0b\x32\x0f.gateway.StatusB\x06\xe0\x41\x03\xe0\x41\x05\x12\x19\n\timage_ref\x18\x05 \x01(\tB\x06\xe0\x41\x03\xe0\x41\x05\"Q\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\"\x88\x01\n\x14ListSnapshotsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x16\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01\x12\x13\n\x06\x66ilter\x18\x04 \x01(\tB\x03\xe0\x41\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0\x41\x01\"j\n\x15ListSnapshotsResponse\x12$\n\tsnapshots\x18\x01 \x03(\x0b\x32\x11.gateway.Snapshot\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05\x42\x0cZ\n./;gatewayb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gateway.snapshot_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\n./;gateway'
  _SNAPSHOT.fields_by_name['name']._options = None
  _SNAPSHOT.fields_by_name['name']._serialized_options = b'\340A\003\340A\005'
  _SNAPSHOT.fields_by_name['create_time']._options = None
  _SNAPSHOT.fields_by_name['create_time']._serialized_options = b'\340A\003\340A\005'
  _SNAPSHOT.fields_by_name['state']._options = None
  _SNAPSHOT.fields_by_name['state']._serialized_options = b'\340A\003\340A\005'
  _SNAPSHOT.fields_by_name['status']._options = None
  _SNAPSHOT.fields_by_name['status']._serialized_options = b'\340A\003\340A\005'
  _SNAPSHOT.fields_by_name['image_ref']._options = None
  _SNAPSHOT.fields_by_name['image_ref']._serialized_options = b'\340A\003\340A\005'
  _LISTSNAPSHOTSREQUEST.fields_by_name['parent']._options = None
  _LISTSNAPSHOTSREQUEST.fields_by_name['parent']._serialized_options = b'\340A\002'
  _LISTSNAPSHOTSREQUEST.fields_by_name['page_size']._options = None
  _LISTSNAPSHOTSREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTSNAPSHOTSREQUEST.fields_by_name['page_token']._options = None
  _LISTSNAPSHOTSREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _LISTSNAPSHOTSREQUEST.fields_by_name['filter']._options = None
  _LISTSNAPSHOTSREQUEST.fields_by_name['filter']._serialized_options = b'\340A\001'
  _LISTSNAPSHOTSREQUEST.fields_by_name['order_by']._options = None
  _LISTSNAPSHOTSREQUEST.fields_by_name['order_by']._serialized_options = b'\340A\001'
  _SNAPSHOT._serialized_start=124
  _SNAPSHOT._serialized_end=412
  _SNAPSHOT_STATE._serialized_start=331
  _SNAPSHOT_STATE._serialized_end=412
  _LISTSNAPSHOTSREQUEST._serialized_start=415
  _LISTSNAPSHOTSREQUEST._serialized_end=551
  _LISTSNAPSHOTSRESPONSE._serialized_start=553
  _LISTSNAPSHOTSRESPONSE._serialized_end=659
# @@protoc_insertion_point(module_scope)
