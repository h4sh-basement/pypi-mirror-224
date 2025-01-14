# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/kube_deployment_captain/alert.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(qwak/kube_deployment_captain/alert.proto\x12\x1cqwak.kube.deployment.captain\"\x87\x01\n\rKubeAlertRule\x12\x1d\n\x15notification_channels\x18\x02 \x03(\t\x12?\n\nalert_spec\x18\x03 \x01(\x0b\x32+.qwak.kube.deployment.captain.KubeAlertSpec\x12\x16\n\x0evariation_name\x18\x04 \x01(\t\"\xc0\x02\n\rKubeAlertSpec\x12K\n\x10reducer_function\x18\x01 \x01(\x0e\x32\x31.qwak.kube.deployment.captain.KubeReducerFunction\x12G\n\x0e\x65valuator_type\x18\x02 \x01(\x0e\x32/.qwak.kube.deployment.captain.KubeEvaluatorType\x12\x1f\n\x13\x65valuator_threshold\x18\x03 \x01(\x05\x42\x02\x18\x01\x12\x19\n\x11\x65valuation_period\x18\x04 \x01(\x05\x12?\n\nalert_type\x18\x05 \x01(\x0e\x32+.qwak.kube.deployment.captain.KubeAlertType\x12\x1c\n\x14\x65valuation_threshold\x18\x06 \x01(\x02\"\xae\x01\n\x17KubeNotificationChannel\x12\x1f\n\x17notification_channel_id\x18\x01 \x01(\t\x12!\n\x19notification_channel_name\x18\x02 \x01(\t\x12O\n\x08settings\x18\x03 \x01(\x0b\x32=.qwak.kube.deployment.captain.KubeNotificationChannelSettings\"\xef\x01\n\x1fKubeNotificationChannelSettings\x12\\\n\x0eslack_settings\x18\x01 \x01(\x0b\x32\x42.qwak.kube.deployment.captain.KubeSlackNotificationChannelSettingsH\x00\x12\x62\n\x11opsgenie_settings\x18\x02 \x01(\x0b\x32\x45.qwak.kube.deployment.captain.KubeOpsgenieNotificationChannelSettingsH\x00\x42\n\n\x08settings\"H\n$KubeSlackNotificationChannelSettings\x12 \n\x18notification_channel_url\x18\x01 \x01(\t\"K\n\'KubeOpsgenieNotificationChannelSettings\x12\x0f\n\x07\x61pi_url\x18\x01 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x02 \x01(\t*v\n\rKubeAlertType\x12\x18\n\x14\x41LERT_TYPE_NOT_VALID\x10\x00\x12\x0e\n\nERROR_RATE\x10\x01\x12\x0e\n\nTHROUGHPUT\x10\x02\x12\x0b\n\x07LATENCY\x10\x03\x12\x0e\n\nLATENCY_90\x10\x04\x12\x0e\n\nLATENCY_95\x10\x05*\xb1\x01\n\x13KubeReducerFunction\x12\x1e\n\x1aREDUCER_FUNCTION_NOT_VALID\x10\x00\x12\x07\n\x03MIN\x10\x01\x12\x07\n\x03MAX\x10\x02\x12\x07\n\x03SUM\x10\x03\x12\t\n\x05\x43OUNT\x10\x04\x12\x08\n\x04LAST\x10\x05\x12\n\n\x06MEDIAN\x10\x06\x12\x08\n\x04\x44IFF\x10\x07\x12\x0c\n\x08\x44IFF_ABS\x10\x08\x12\x10\n\x0cPERCENT_DIFF\x10\t\x12\x14\n\x10PERCENT_DIFF_ABS\x10\n*M\n\x11KubeEvaluatorType\x12\x1c\n\x18\x45VALUATOR_TYPE_NOT_VALID\x10\x00\x12\x0c\n\x08IS_ABOVE\x10\x01\x12\x0c\n\x08IS_BELOW\x10\x02\x42+\n\'com.qwak.ai.kube.deployment.captain.apiP\x01\x62\x06proto3')

_KUBEALERTTYPE = DESCRIPTOR.enum_types_by_name['KubeAlertType']
KubeAlertType = enum_type_wrapper.EnumTypeWrapper(_KUBEALERTTYPE)
_KUBEREDUCERFUNCTION = DESCRIPTOR.enum_types_by_name['KubeReducerFunction']
KubeReducerFunction = enum_type_wrapper.EnumTypeWrapper(_KUBEREDUCERFUNCTION)
_KUBEEVALUATORTYPE = DESCRIPTOR.enum_types_by_name['KubeEvaluatorType']
KubeEvaluatorType = enum_type_wrapper.EnumTypeWrapper(_KUBEEVALUATORTYPE)
ALERT_TYPE_NOT_VALID = 0
ERROR_RATE = 1
THROUGHPUT = 2
LATENCY = 3
LATENCY_90 = 4
LATENCY_95 = 5
REDUCER_FUNCTION_NOT_VALID = 0
MIN = 1
MAX = 2
SUM = 3
COUNT = 4
LAST = 5
MEDIAN = 6
DIFF = 7
DIFF_ABS = 8
PERCENT_DIFF = 9
PERCENT_DIFF_ABS = 10
EVALUATOR_TYPE_NOT_VALID = 0
IS_ABOVE = 1
IS_BELOW = 2


_KUBEALERTRULE = DESCRIPTOR.message_types_by_name['KubeAlertRule']
_KUBEALERTSPEC = DESCRIPTOR.message_types_by_name['KubeAlertSpec']
_KUBENOTIFICATIONCHANNEL = DESCRIPTOR.message_types_by_name['KubeNotificationChannel']
_KUBENOTIFICATIONCHANNELSETTINGS = DESCRIPTOR.message_types_by_name['KubeNotificationChannelSettings']
_KUBESLACKNOTIFICATIONCHANNELSETTINGS = DESCRIPTOR.message_types_by_name['KubeSlackNotificationChannelSettings']
_KUBEOPSGENIENOTIFICATIONCHANNELSETTINGS = DESCRIPTOR.message_types_by_name['KubeOpsgenieNotificationChannelSettings']
KubeAlertRule = _reflection.GeneratedProtocolMessageType('KubeAlertRule', (_message.Message,), {
  'DESCRIPTOR' : _KUBEALERTRULE,
  '__module__' : 'qwak.kube_deployment_captain.alert_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.KubeAlertRule)
  })
_sym_db.RegisterMessage(KubeAlertRule)

KubeAlertSpec = _reflection.GeneratedProtocolMessageType('KubeAlertSpec', (_message.Message,), {
  'DESCRIPTOR' : _KUBEALERTSPEC,
  '__module__' : 'qwak.kube_deployment_captain.alert_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.KubeAlertSpec)
  })
_sym_db.RegisterMessage(KubeAlertSpec)

KubeNotificationChannel = _reflection.GeneratedProtocolMessageType('KubeNotificationChannel', (_message.Message,), {
  'DESCRIPTOR' : _KUBENOTIFICATIONCHANNEL,
  '__module__' : 'qwak.kube_deployment_captain.alert_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.KubeNotificationChannel)
  })
_sym_db.RegisterMessage(KubeNotificationChannel)

KubeNotificationChannelSettings = _reflection.GeneratedProtocolMessageType('KubeNotificationChannelSettings', (_message.Message,), {
  'DESCRIPTOR' : _KUBENOTIFICATIONCHANNELSETTINGS,
  '__module__' : 'qwak.kube_deployment_captain.alert_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.KubeNotificationChannelSettings)
  })
_sym_db.RegisterMessage(KubeNotificationChannelSettings)

KubeSlackNotificationChannelSettings = _reflection.GeneratedProtocolMessageType('KubeSlackNotificationChannelSettings', (_message.Message,), {
  'DESCRIPTOR' : _KUBESLACKNOTIFICATIONCHANNELSETTINGS,
  '__module__' : 'qwak.kube_deployment_captain.alert_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.KubeSlackNotificationChannelSettings)
  })
_sym_db.RegisterMessage(KubeSlackNotificationChannelSettings)

KubeOpsgenieNotificationChannelSettings = _reflection.GeneratedProtocolMessageType('KubeOpsgenieNotificationChannelSettings', (_message.Message,), {
  'DESCRIPTOR' : _KUBEOPSGENIENOTIFICATIONCHANNELSETTINGS,
  '__module__' : 'qwak.kube_deployment_captain.alert_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.KubeOpsgenieNotificationChannelSettings)
  })
_sym_db.RegisterMessage(KubeOpsgenieNotificationChannelSettings)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'com.qwak.ai.kube.deployment.captain.apiP\001'
  _KUBEALERTSPEC.fields_by_name['evaluator_threshold']._options = None
  _KUBEALERTSPEC.fields_by_name['evaluator_threshold']._serialized_options = b'\030\001'
  _KUBEALERTTYPE._serialized_start=1105
  _KUBEALERTTYPE._serialized_end=1223
  _KUBEREDUCERFUNCTION._serialized_start=1226
  _KUBEREDUCERFUNCTION._serialized_end=1403
  _KUBEEVALUATORTYPE._serialized_start=1405
  _KUBEEVALUATORTYPE._serialized_end=1482
  _KUBEALERTRULE._serialized_start=75
  _KUBEALERTRULE._serialized_end=210
  _KUBEALERTSPEC._serialized_start=213
  _KUBEALERTSPEC._serialized_end=533
  _KUBENOTIFICATIONCHANNEL._serialized_start=536
  _KUBENOTIFICATIONCHANNEL._serialized_end=710
  _KUBENOTIFICATIONCHANNELSETTINGS._serialized_start=713
  _KUBENOTIFICATIONCHANNELSETTINGS._serialized_end=952
  _KUBESLACKNOTIFICATIONCHANNELSETTINGS._serialized_start=954
  _KUBESLACKNOTIFICATIONCHANNELSETTINGS._serialized_end=1026
  _KUBEOPSGENIENOTIFICATIONCHANNELSETTINGS._serialized_start=1028
  _KUBEOPSGENIENOTIFICATIONCHANNELSETTINGS._serialized_end=1103
# @@protoc_insertion_point(module_scope)
