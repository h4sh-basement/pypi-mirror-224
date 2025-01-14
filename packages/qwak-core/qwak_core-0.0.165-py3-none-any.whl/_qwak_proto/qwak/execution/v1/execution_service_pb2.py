# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/execution/v1/execution_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from _qwak_proto.qwak.execution.v1 import backfill_pb2 as qwak_dot_execution_dot_v1_dot_backfill__pb2
from _qwak_proto.qwak.execution.v1 import batch_pb2 as qwak_dot_execution_dot_v1_dot_batch__pb2
from _qwak_proto.qwak.execution.v1 import execution_pb2 as qwak_dot_execution_dot_v1_dot_execution__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)qwak/execution/v1/execution_service.proto\x12\x1fqwak.feature.store.execution.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a qwak/execution/v1/backfill.proto\x1a\x1dqwak/execution/v1/batch.proto\x1a!qwak/execution/v1/execution.proto\"^\n\x16TriggerBackfillRequest\x12\x44\n\rbackfill_spec\x18\x01 \x01(\x0b\x32-.qwak.feature.store.execution.v1.BackfillSpec\"/\n\x17TriggerBackfillResponse\x12\x14\n\x0c\x65xecution_id\x18\x01 \x01(\t\"1\n\x19GetExecutionStatusRequest\x12\x14\n\x0c\x65xecution_id\x18\x01 \x01(\t\"h\n\x1aGetExecutionStatusResponse\x12J\n\x10\x65xecution_status\x18\x01 \x01(\x0e\x32\x30.qwak.feature.store.execution.v1.ExecutionStatus\"0\n\x18GetExecutionEntryRequest\x12\x14\n\x0c\x65xecution_id\x18\x01 \x01(\t\"e\n\x19GetExecutionEntryResponse\x12H\n\x0f\x65xecution_entry\x18\x01 \x01(\x0b\x32/.qwak.feature.store.execution.v1.ExecutionEntry\"i\n\x1dTriggerBatchFeaturesetRequest\x12H\n\x0f\x62\x61tch_ingestion\x18\x01 \x01(\x0b\x32/.qwak.feature.store.execution.v1.BatchIngestion\"6\n\x1eTriggerBatchFeaturesetResponse\x12\x14\n\x0c\x65xecution_id\x18\x01 \x01(\t2\xe3\x04\n\x1c\x46\x65\x61tureStoreExecutionService\x12\x89\x01\n\x14TriggerBatchBackfill\x12\x37.qwak.feature.store.execution.v1.TriggerBackfillRequest\x1a\x38.qwak.feature.store.execution.v1.TriggerBackfillResponse\x12\x99\x01\n\x16TriggerBatchFeatureset\x12>.qwak.feature.store.execution.v1.TriggerBatchFeaturesetRequest\x1a?.qwak.feature.store.execution.v1.TriggerBatchFeaturesetResponse\x12\x8d\x01\n\x12GetExecutionStatus\x12:.qwak.feature.store.execution.v1.GetExecutionStatusRequest\x1a;.qwak.feature.store.execution.v1.GetExecutionStatusResponse\x12\x8a\x01\n\x11GetExecutionEntry\x12\x39.qwak.feature.store.execution.v1.GetExecutionEntryRequest\x1a:.qwak.feature.store.execution.v1.GetExecutionEntryResponseB)\n%com.qwak.ai.features.execution.api.v1P\x01\x62\x06proto3')



_TRIGGERBACKFILLREQUEST = DESCRIPTOR.message_types_by_name['TriggerBackfillRequest']
_TRIGGERBACKFILLRESPONSE = DESCRIPTOR.message_types_by_name['TriggerBackfillResponse']
_GETEXECUTIONSTATUSREQUEST = DESCRIPTOR.message_types_by_name['GetExecutionStatusRequest']
_GETEXECUTIONSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['GetExecutionStatusResponse']
_GETEXECUTIONENTRYREQUEST = DESCRIPTOR.message_types_by_name['GetExecutionEntryRequest']
_GETEXECUTIONENTRYRESPONSE = DESCRIPTOR.message_types_by_name['GetExecutionEntryResponse']
_TRIGGERBATCHFEATURESETREQUEST = DESCRIPTOR.message_types_by_name['TriggerBatchFeaturesetRequest']
_TRIGGERBATCHFEATURESETRESPONSE = DESCRIPTOR.message_types_by_name['TriggerBatchFeaturesetResponse']
TriggerBackfillRequest = _reflection.GeneratedProtocolMessageType('TriggerBackfillRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERBACKFILLREQUEST,
  '__module__' : 'qwak.execution.v1.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.execution.v1.TriggerBackfillRequest)
  })
_sym_db.RegisterMessage(TriggerBackfillRequest)

TriggerBackfillResponse = _reflection.GeneratedProtocolMessageType('TriggerBackfillResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERBACKFILLRESPONSE,
  '__module__' : 'qwak.execution.v1.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.execution.v1.TriggerBackfillResponse)
  })
_sym_db.RegisterMessage(TriggerBackfillResponse)

GetExecutionStatusRequest = _reflection.GeneratedProtocolMessageType('GetExecutionStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEXECUTIONSTATUSREQUEST,
  '__module__' : 'qwak.execution.v1.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.execution.v1.GetExecutionStatusRequest)
  })
_sym_db.RegisterMessage(GetExecutionStatusRequest)

GetExecutionStatusResponse = _reflection.GeneratedProtocolMessageType('GetExecutionStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETEXECUTIONSTATUSRESPONSE,
  '__module__' : 'qwak.execution.v1.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.execution.v1.GetExecutionStatusResponse)
  })
_sym_db.RegisterMessage(GetExecutionStatusResponse)

GetExecutionEntryRequest = _reflection.GeneratedProtocolMessageType('GetExecutionEntryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEXECUTIONENTRYREQUEST,
  '__module__' : 'qwak.execution.v1.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.execution.v1.GetExecutionEntryRequest)
  })
_sym_db.RegisterMessage(GetExecutionEntryRequest)

GetExecutionEntryResponse = _reflection.GeneratedProtocolMessageType('GetExecutionEntryResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETEXECUTIONENTRYRESPONSE,
  '__module__' : 'qwak.execution.v1.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.execution.v1.GetExecutionEntryResponse)
  })
_sym_db.RegisterMessage(GetExecutionEntryResponse)

TriggerBatchFeaturesetRequest = _reflection.GeneratedProtocolMessageType('TriggerBatchFeaturesetRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERBATCHFEATURESETREQUEST,
  '__module__' : 'qwak.execution.v1.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.execution.v1.TriggerBatchFeaturesetRequest)
  })
_sym_db.RegisterMessage(TriggerBatchFeaturesetRequest)

TriggerBatchFeaturesetResponse = _reflection.GeneratedProtocolMessageType('TriggerBatchFeaturesetResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERBATCHFEATURESETRESPONSE,
  '__module__' : 'qwak.execution.v1.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.execution.v1.TriggerBatchFeaturesetResponse)
  })
_sym_db.RegisterMessage(TriggerBatchFeaturesetResponse)

_FEATURESTOREEXECUTIONSERVICE = DESCRIPTOR.services_by_name['FeatureStoreExecutionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.qwak.ai.features.execution.api.v1P\001'
  _TRIGGERBACKFILLREQUEST._serialized_start=211
  _TRIGGERBACKFILLREQUEST._serialized_end=305
  _TRIGGERBACKFILLRESPONSE._serialized_start=307
  _TRIGGERBACKFILLRESPONSE._serialized_end=354
  _GETEXECUTIONSTATUSREQUEST._serialized_start=356
  _GETEXECUTIONSTATUSREQUEST._serialized_end=405
  _GETEXECUTIONSTATUSRESPONSE._serialized_start=407
  _GETEXECUTIONSTATUSRESPONSE._serialized_end=511
  _GETEXECUTIONENTRYREQUEST._serialized_start=513
  _GETEXECUTIONENTRYREQUEST._serialized_end=561
  _GETEXECUTIONENTRYRESPONSE._serialized_start=563
  _GETEXECUTIONENTRYRESPONSE._serialized_end=664
  _TRIGGERBATCHFEATURESETREQUEST._serialized_start=666
  _TRIGGERBATCHFEATURESETREQUEST._serialized_end=771
  _TRIGGERBATCHFEATURESETRESPONSE._serialized_start=773
  _TRIGGERBATCHFEATURESETRESPONSE._serialized_end=827
  _FEATURESTOREEXECUTIONSERVICE._serialized_start=830
  _FEATURESTOREEXECUTIONSERVICE._serialized_end=1441
# @@protoc_insertion_point(module_scope)
