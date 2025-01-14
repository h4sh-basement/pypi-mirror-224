# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/marketplace/v1/metering/usage_record.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/marketplace/v1/metering/usage_record.proto',
  package='yandex.cloud.marketplace.v1.metering',
  syntax='proto3',
  serialized_options=b'\n(yandex.cloud.api.marketplace.v1.meteringZQgithub.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/v1/metering;metering',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7yandex/cloud/marketplace/v1/metering/usage_record.proto\x12$yandex.cloud.marketplace.v1.metering\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\x96\x01\n\x0bUsageRecord\x12\x1a\n\x04uuid\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=36\x12\x1c\n\x06sku_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x18\n\x08quantity\x18\x03 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12\x33\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe8\xc7\x31\x01\"#\n\x13\x41\x63\x63\x65ptedUsageRecord\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"\x9d\x02\n\x13RejectedUsageRecord\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12P\n\x06reason\x18\x02 \x01(\x0e\x32@.yandex.cloud.marketplace.v1.metering.RejectedUsageRecord.Reason\"\xa5\x01\n\x06Reason\x12\x16\n\x12REASON_UNSPECIFIED\x10\x00\x12\r\n\tDUPLICATE\x10\x01\x12\x0b\n\x07\x45XPIRED\x10\x02\x12\x15\n\x11INVALID_TIMESTAMP\x10\x03\x12\x12\n\x0eINVALID_SKU_ID\x10\x04\x12\x16\n\x12INVALID_PRODUCT_ID\x10\x05\x12\x14\n\x10INVALID_QUANTITY\x10\x06\x12\x0e\n\nINVALID_ID\x10\x07\x42}\n(yandex.cloud.api.marketplace.v1.meteringZQgithub.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/v1/metering;meteringb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_REJECTEDUSAGERECORD_REASON = _descriptor.EnumDescriptor(
  name='Reason',
  full_name='yandex.cloud.marketplace.v1.metering.RejectedUsageRecord.Reason',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REASON_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_TIMESTAMP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SKU_ID', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PRODUCT_ID', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_QUANTITY', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ID', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=472,
  serialized_end=637,
)
_sym_db.RegisterEnumDescriptor(_REJECTEDUSAGERECORD_REASON)


_USAGERECORD = _descriptor.Descriptor(
  name='UsageRecord',
  full_name='yandex.cloud.marketplace.v1.metering.UsageRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='yandex.cloud.marketplace.v1.metering.UsageRecord.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=36', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sku_id', full_name='yandex.cloud.marketplace.v1.metering.UsageRecord.sku_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='yandex.cloud.marketplace.v1.metering.UsageRecord.quantity', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='yandex.cloud.marketplace.v1.metering.UsageRecord.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=312,
)


_ACCEPTEDUSAGERECORD = _descriptor.Descriptor(
  name='AcceptedUsageRecord',
  full_name='yandex.cloud.marketplace.v1.metering.AcceptedUsageRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='yandex.cloud.marketplace.v1.metering.AcceptedUsageRecord.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=349,
)


_REJECTEDUSAGERECORD = _descriptor.Descriptor(
  name='RejectedUsageRecord',
  full_name='yandex.cloud.marketplace.v1.metering.RejectedUsageRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='yandex.cloud.marketplace.v1.metering.RejectedUsageRecord.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason', full_name='yandex.cloud.marketplace.v1.metering.RejectedUsageRecord.reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REJECTEDUSAGERECORD_REASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=637,
)

_USAGERECORD.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REJECTEDUSAGERECORD.fields_by_name['reason'].enum_type = _REJECTEDUSAGERECORD_REASON
_REJECTEDUSAGERECORD_REASON.containing_type = _REJECTEDUSAGERECORD
DESCRIPTOR.message_types_by_name['UsageRecord'] = _USAGERECORD
DESCRIPTOR.message_types_by_name['AcceptedUsageRecord'] = _ACCEPTEDUSAGERECORD
DESCRIPTOR.message_types_by_name['RejectedUsageRecord'] = _REJECTEDUSAGERECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UsageRecord = _reflection.GeneratedProtocolMessageType('UsageRecord', (_message.Message,), {
  'DESCRIPTOR' : _USAGERECORD,
  '__module__' : 'yandex.cloud.marketplace.v1.metering.usage_record_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.marketplace.v1.metering.UsageRecord)
  })
_sym_db.RegisterMessage(UsageRecord)

AcceptedUsageRecord = _reflection.GeneratedProtocolMessageType('AcceptedUsageRecord', (_message.Message,), {
  'DESCRIPTOR' : _ACCEPTEDUSAGERECORD,
  '__module__' : 'yandex.cloud.marketplace.v1.metering.usage_record_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.marketplace.v1.metering.AcceptedUsageRecord)
  })
_sym_db.RegisterMessage(AcceptedUsageRecord)

RejectedUsageRecord = _reflection.GeneratedProtocolMessageType('RejectedUsageRecord', (_message.Message,), {
  'DESCRIPTOR' : _REJECTEDUSAGERECORD,
  '__module__' : 'yandex.cloud.marketplace.v1.metering.usage_record_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.marketplace.v1.metering.RejectedUsageRecord)
  })
_sym_db.RegisterMessage(RejectedUsageRecord)


DESCRIPTOR._options = None
_USAGERECORD.fields_by_name['uuid']._options = None
_USAGERECORD.fields_by_name['sku_id']._options = None
_USAGERECORD.fields_by_name['quantity']._options = None
_USAGERECORD.fields_by_name['timestamp']._options = None
# @@protoc_insertion_point(module_scope)
