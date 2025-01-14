# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prodvana/application/application_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from prodvana.proto.prodvana.capability import capability_pb2 as prodvana_dot_capability_dot_capability__pb2
from prodvana.proto.prodvana.common_config import notification_pb2 as prodvana_dot_common__config_dot_notification__pb2
from prodvana.proto.prodvana.release_channel import release_channel_config_pb2 as prodvana_dot_release__channel_dot_release__channel__config__pb2
from prodvana.proto.prodvana.workflow import integration_config_pb2 as prodvana_dot_workflow_dot_integration__config__pb2
from prodvana.proto.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-prodvana/application/application_config.proto\x12\x14prodvana.application\x1a$prodvana/capability/capability.proto\x1a)prodvana/common_config/notification.proto\x1a\x35prodvana/release_channel/release_channel_config.proto\x1a*prodvana/workflow/integration_config.proto\x1a\x17validate/validate.proto\"\xb1\x04\n\x11\x41pplicationConfig\x12\x39\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^[a-z]([a-z0-9-]*[a-z0-9]){0,1}$\x12H\n\x10release_channels\x18\x02 \x03(\x0b\x32..prodvana.release_channel.ReleaseChannelConfig\x12\x41\n\rnotifications\x18\x04 \x01(\x0b\x32*.prodvana.common_config.NotificationConfig\x12\x31\n\x06\x61lerts\x18\x05 \x01(\x0b\x32!.prodvana.workflow.AlertingConfig\x12J\n\x0c\x63\x61pabilities\x18\x06 \x03(\x0b\x32%.prodvana.capability.CapabilityConfigB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01\x12Z\n\x14\x63\x61pability_instances\x18\x07 \x03(\x0b\x32-.prodvana.capability.CapabilityInstanceConfigB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01J\x04\x08\x03\x10\x04J\x04\x08\x08\x10\tJ\x04\x08\t\x10\nJ\x04\x08\n\x10\x0bR\x11service_templatesR\x12pipeline_templatesR\x14use_dynamic_deliveryR$enable_custom_tasks_dynamic_deliveryBPZNgithub.com/prodvana/prodvana-public/go/prodvana-sdk/proto/prodvana/applicationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'prodvana.application.application_config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZNgithub.com/prodvana/prodvana-public/go/prodvana-sdk/proto/prodvana/application'
  _APPLICATIONCONFIG.fields_by_name['name']._options = None
  _APPLICATIONCONFIG.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^[a-z]([a-z0-9-]*[a-z0-9]){0,1}$'
  _APPLICATIONCONFIG.fields_by_name['capabilities']._options = None
  _APPLICATIONCONFIG.fields_by_name['capabilities']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _APPLICATIONCONFIG.fields_by_name['capability_instances']._options = None
  _APPLICATIONCONFIG.fields_by_name['capability_instances']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _globals['_APPLICATIONCONFIG']._serialized_start=277
  _globals['_APPLICATIONCONFIG']._serialized_end=838
# @@protoc_insertion_point(module_scope)
