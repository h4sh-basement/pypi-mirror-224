# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/monitoring/v0/alerting_channel.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)qwak/monitoring/v0/alerting_channel.proto\x12\x12qwak.monitoring.v0\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"c\n\x1c\x41lertingChannelCreateOptions\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x04spec\x18\x02 \x01(\x0b\x32\'.qwak.monitoring.v0.AlertingChannelSpec\"\x8d\x01\n\x1c\x41lertingChannelUpdateOptions\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x04spec\x18\x03 \x01(\x0b\x32\'.qwak.monitoring.v0.AlertingChannelSpec\"\x92\x01\n\x1a\x41lertingChannelDescription\x12=\n\x08metadata\x18\x01 \x01(\x0b\x32+.qwak.monitoring.v0.AlertingChannelMetadata\x12\x35\n\x04spec\x18\x02 \x01(\x0b\x32\'.qwak.monitoring.v0.AlertingChannelSpec\"\xdd\x01\n\x17\x41lertingChannelMetadata\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10last_modified_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"V\n\x13\x41lertingChannelSpec\x12?\n\rconfiguration\x18\x01 \x01(\x0b\x32(.qwak.monitoring.v0.ChannelConfiguration\"\xc4\x01\n\x14\x43hannelConfiguration\x12.\n\x05slack\x18\x01 \x01(\x0b\x32\x1d.qwak.monitoring.v0.SlackTypeH\x00\x12\x36\n\tpagerduty\x18\x02 \x01(\x0b\x32!.qwak.monitoring.v0.PagerDutyTypeH\x00\x12\x34\n\x08opsgenie\x18\x03 \x01(\x0b\x32 .qwak.monitoring.v0.OpsgenieTypeH\x00\x42\x0e\n\x0c\x63hannel_type\"\xb1\x01\n\x0cSyncResponse\x12\x45\n\x10\x63hannels_to_sync\x18\x01 \x01(\x0b\x32).qwak.monitoring.v0.AlertingChannelToSyncH\x00\x12Q\n\x12\x61lready_up_to_date\x18\x02 \x01(\x0b\x32\x33.qwak.monitoring.v0.AlertingChannelsAlreadyUpToDateH\x00\x42\x07\n\x05types\"\xa8\x01\n\x15\x41lertingChannelToSync\x12\x43\n\x0b\x64\x65scription\x18\x01 \x03(\x0b\x32..qwak.monitoring.v0.AlertingChannelDescription\x12J\n\x12\x63hannels_to_delete\x18\x03 \x03(\x0b\x32..qwak.monitoring.v0.AlertingChannelDescription\"^\n\x17\x41lertingChannelToDelete\x12\x43\n\x0b\x64\x65scription\x18\x01 \x03(\x0b\x32..qwak.monitoring.v0.AlertingChannelDescription\"!\n\x1f\x41lertingChannelsAlreadyUpToDate\"C\n\tSlackType\x12\x36\n\x07\x61pi_url\x18\x01 \x01(\x0b\x32%.qwak.monitoring.v0.SecretStringValue\"\x94\x01\n\rPagerDutyType\x12:\n\x0brouting_key\x18\x01 \x01(\x0b\x32%.qwak.monitoring.v0.SecretStringValue\x12:\n\x0bservice_key\x18\x02 \x01(\x0b\x32%.qwak.monitoring.v0.SecretStringValue\x12\x0b\n\x03url\x18\x03 \x01(\t\"F\n\x0cOpsgenieType\x12\x36\n\x07\x61pi_key\x18\x01 \x01(\x0b\x32%.qwak.monitoring.v0.SecretStringValue\"\"\n\x11SecretStringValue\x12\r\n\x05value\x18\x01 \x01(\t*k\n\x15MonitorActivityStatus\x12\x1a\n\x16MONITOR_STATUS_INVALID\x10\x00\x12\x19\n\x15MONITOR_STATUS_ACTIVE\x10\x01\x12\x1b\n\x17MONITOR_STATUS_DISABLED\x10\x02\x42\x32\n\x1d\x63om.qwak.ai.monitoring.api.v0P\x01Z\x0f.;monitoring_v0b\x06proto3')

_MONITORACTIVITYSTATUS = DESCRIPTOR.enum_types_by_name['MonitorActivityStatus']
MonitorActivityStatus = enum_type_wrapper.EnumTypeWrapper(_MONITORACTIVITYSTATUS)
MONITOR_STATUS_INVALID = 0
MONITOR_STATUS_ACTIVE = 1
MONITOR_STATUS_DISABLED = 2


_ALERTINGCHANNELCREATEOPTIONS = DESCRIPTOR.message_types_by_name['AlertingChannelCreateOptions']
_ALERTINGCHANNELUPDATEOPTIONS = DESCRIPTOR.message_types_by_name['AlertingChannelUpdateOptions']
_ALERTINGCHANNELDESCRIPTION = DESCRIPTOR.message_types_by_name['AlertingChannelDescription']
_ALERTINGCHANNELMETADATA = DESCRIPTOR.message_types_by_name['AlertingChannelMetadata']
_ALERTINGCHANNELSPEC = DESCRIPTOR.message_types_by_name['AlertingChannelSpec']
_CHANNELCONFIGURATION = DESCRIPTOR.message_types_by_name['ChannelConfiguration']
_SYNCRESPONSE = DESCRIPTOR.message_types_by_name['SyncResponse']
_ALERTINGCHANNELTOSYNC = DESCRIPTOR.message_types_by_name['AlertingChannelToSync']
_ALERTINGCHANNELTODELETE = DESCRIPTOR.message_types_by_name['AlertingChannelToDelete']
_ALERTINGCHANNELSALREADYUPTODATE = DESCRIPTOR.message_types_by_name['AlertingChannelsAlreadyUpToDate']
_SLACKTYPE = DESCRIPTOR.message_types_by_name['SlackType']
_PAGERDUTYTYPE = DESCRIPTOR.message_types_by_name['PagerDutyType']
_OPSGENIETYPE = DESCRIPTOR.message_types_by_name['OpsgenieType']
_SECRETSTRINGVALUE = DESCRIPTOR.message_types_by_name['SecretStringValue']
AlertingChannelCreateOptions = _reflection.GeneratedProtocolMessageType('AlertingChannelCreateOptions', (_message.Message,), {
  'DESCRIPTOR' : _ALERTINGCHANNELCREATEOPTIONS,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.AlertingChannelCreateOptions)
  })
_sym_db.RegisterMessage(AlertingChannelCreateOptions)

AlertingChannelUpdateOptions = _reflection.GeneratedProtocolMessageType('AlertingChannelUpdateOptions', (_message.Message,), {
  'DESCRIPTOR' : _ALERTINGCHANNELUPDATEOPTIONS,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.AlertingChannelUpdateOptions)
  })
_sym_db.RegisterMessage(AlertingChannelUpdateOptions)

AlertingChannelDescription = _reflection.GeneratedProtocolMessageType('AlertingChannelDescription', (_message.Message,), {
  'DESCRIPTOR' : _ALERTINGCHANNELDESCRIPTION,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.AlertingChannelDescription)
  })
_sym_db.RegisterMessage(AlertingChannelDescription)

AlertingChannelMetadata = _reflection.GeneratedProtocolMessageType('AlertingChannelMetadata', (_message.Message,), {
  'DESCRIPTOR' : _ALERTINGCHANNELMETADATA,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.AlertingChannelMetadata)
  })
_sym_db.RegisterMessage(AlertingChannelMetadata)

AlertingChannelSpec = _reflection.GeneratedProtocolMessageType('AlertingChannelSpec', (_message.Message,), {
  'DESCRIPTOR' : _ALERTINGCHANNELSPEC,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.AlertingChannelSpec)
  })
_sym_db.RegisterMessage(AlertingChannelSpec)

ChannelConfiguration = _reflection.GeneratedProtocolMessageType('ChannelConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELCONFIGURATION,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.ChannelConfiguration)
  })
_sym_db.RegisterMessage(ChannelConfiguration)

SyncResponse = _reflection.GeneratedProtocolMessageType('SyncResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYNCRESPONSE,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.SyncResponse)
  })
_sym_db.RegisterMessage(SyncResponse)

AlertingChannelToSync = _reflection.GeneratedProtocolMessageType('AlertingChannelToSync', (_message.Message,), {
  'DESCRIPTOR' : _ALERTINGCHANNELTOSYNC,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.AlertingChannelToSync)
  })
_sym_db.RegisterMessage(AlertingChannelToSync)

AlertingChannelToDelete = _reflection.GeneratedProtocolMessageType('AlertingChannelToDelete', (_message.Message,), {
  'DESCRIPTOR' : _ALERTINGCHANNELTODELETE,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.AlertingChannelToDelete)
  })
_sym_db.RegisterMessage(AlertingChannelToDelete)

AlertingChannelsAlreadyUpToDate = _reflection.GeneratedProtocolMessageType('AlertingChannelsAlreadyUpToDate', (_message.Message,), {
  'DESCRIPTOR' : _ALERTINGCHANNELSALREADYUPTODATE,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.AlertingChannelsAlreadyUpToDate)
  })
_sym_db.RegisterMessage(AlertingChannelsAlreadyUpToDate)

SlackType = _reflection.GeneratedProtocolMessageType('SlackType', (_message.Message,), {
  'DESCRIPTOR' : _SLACKTYPE,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.SlackType)
  })
_sym_db.RegisterMessage(SlackType)

PagerDutyType = _reflection.GeneratedProtocolMessageType('PagerDutyType', (_message.Message,), {
  'DESCRIPTOR' : _PAGERDUTYTYPE,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.PagerDutyType)
  })
_sym_db.RegisterMessage(PagerDutyType)

OpsgenieType = _reflection.GeneratedProtocolMessageType('OpsgenieType', (_message.Message,), {
  'DESCRIPTOR' : _OPSGENIETYPE,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.OpsgenieType)
  })
_sym_db.RegisterMessage(OpsgenieType)

SecretStringValue = _reflection.GeneratedProtocolMessageType('SecretStringValue', (_message.Message,), {
  'DESCRIPTOR' : _SECRETSTRINGVALUE,
  '__module__' : 'qwak.monitoring.v0.alerting_channel_pb2'
  # @@protoc_insertion_point(class_scope:qwak.monitoring.v0.SecretStringValue)
  })
_sym_db.RegisterMessage(SecretStringValue)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.qwak.ai.monitoring.api.v0P\001Z\017.;monitoring_v0'
  _MONITORACTIVITYSTATUS._serialized_start=1845
  _MONITORACTIVITYSTATUS._serialized_end=1952
  _ALERTINGCHANNELCREATEOPTIONS._serialized_start=130
  _ALERTINGCHANNELCREATEOPTIONS._serialized_end=229
  _ALERTINGCHANNELUPDATEOPTIONS._serialized_start=232
  _ALERTINGCHANNELUPDATEOPTIONS._serialized_end=373
  _ALERTINGCHANNELDESCRIPTION._serialized_start=376
  _ALERTINGCHANNELDESCRIPTION._serialized_end=522
  _ALERTINGCHANNELMETADATA._serialized_start=525
  _ALERTINGCHANNELMETADATA._serialized_end=746
  _ALERTINGCHANNELSPEC._serialized_start=748
  _ALERTINGCHANNELSPEC._serialized_end=834
  _CHANNELCONFIGURATION._serialized_start=837
  _CHANNELCONFIGURATION._serialized_end=1033
  _SYNCRESPONSE._serialized_start=1036
  _SYNCRESPONSE._serialized_end=1213
  _ALERTINGCHANNELTOSYNC._serialized_start=1216
  _ALERTINGCHANNELTOSYNC._serialized_end=1384
  _ALERTINGCHANNELTODELETE._serialized_start=1386
  _ALERTINGCHANNELTODELETE._serialized_end=1480
  _ALERTINGCHANNELSALREADYUPTODATE._serialized_start=1482
  _ALERTINGCHANNELSALREADYUPTODATE._serialized_end=1515
  _SLACKTYPE._serialized_start=1517
  _SLACKTYPE._serialized_end=1584
  _PAGERDUTYTYPE._serialized_start=1587
  _PAGERDUTYTYPE._serialized_end=1735
  _OPSGENIETYPE._serialized_start=1737
  _OPSGENIETYPE._serialized_end=1807
  _SECRETSTRINGVALUE._serialized_start=1809
  _SECRETSTRINGVALUE._serialized_end=1843
# @@protoc_insertion_point(module_scope)
