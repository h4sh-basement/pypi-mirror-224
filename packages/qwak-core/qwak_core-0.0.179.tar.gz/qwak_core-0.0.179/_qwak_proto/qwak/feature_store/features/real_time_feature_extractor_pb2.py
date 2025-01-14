# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/feature_store/features/real_time_feature_extractor.proto
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
from _qwak_proto.qwak.feature_store.features import execution_pb2 as qwak_dot_feature__store_dot_features_dot_execution__pb2
from _qwak_proto.qwak.feature_store.features import deployment_pb2 as qwak_dot_feature__store_dot_features_dot_deployment__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=qwak/feature_store/features/real_time_feature_extractor.proto\x12\x1bqwak.feature.store.features\x1a\x1fgoogle/protobuf/timestamp.proto\x1a+qwak/feature_store/features/execution.proto\x1a,qwak/feature_store/features/deployment.proto\"\xdc\x01\n\x18RealTimeFeatureExtractor\x12o\n&real_time_feature_extractor_definition\x18\x01 \x01(\x0b\x32?.qwak.feature.store.features.RealTimeFeatureExtractorDefinition\x12O\n\x08metadata\x18\x02 \x01(\x0b\x32=.qwak.feature.store.features.RealTimeFeatureExtractorMetadata\"\x80\x02\n\"RealTimeFeatureExtractorDefinition\x12&\n\x1ereal_time_feature_extractor_id\x18\x01 \x01(\t\x12\x63\n real_time_feature_extractor_spec\x18\x02 \x01(\x0b\x32\x39.qwak.feature.store.features.RealTimeFeatureExtractorSpec\x12M\n\x16last_deployment_status\x18\x05 \x01(\x0e\x32-.qwak.feature.store.features.DeploymentStatus\"\xc8\x01\n RealTimeFeatureExtractorMetadata\x12\x35\n\x11\x63reated_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12?\n\x1blast_modification_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10last_modified_by\x18\x04 \x01(\t\"\xba\x02\n\x1cRealTimeFeatureExtractorSpec\x12K\n\x12real_time_artifact\x18\x01 \x01(\x0b\x32/.qwak.feature.store.features.ExtractionArtifact\x12P\n\x12\x64\x65pendency_manager\x18\x02 \x01(\x0b\x32\x34.qwak.feature.store.features.PythonDependencyManager\x12\\\n\x1c\x63lient_pod_compute_resources\x18\x03 \x01(\x0b\x32\x36.qwak.feature.store.features.ExtractorComputeResources\x12\x1d\n\x15max_staleness_seconds\x18\x04 \x01(\x03\"U\n\x12\x45xtractionArtifact\x12\x34\n\x06\x61ws_s3\x18\x01 \x01(\x0b\x32\".qwak.feature.store.features.AwsS3H\x00\x42\t\n\x07\x66s_type\"\x1e\n\x05\x41wsS3\x12\x15\n\rartifact_path\x18\x01 \x01(\t\"\x98\x02\n\x17PythonDependencyManager\x12\x42\n\x0epython_version\x18\x01 \x01(\x0e\x32*.qwak.feature.store.features.PythonVersion\x12\x45\n\nvirtualenv\x18\x02 \x01(\x0b\x32/.qwak.feature.store.features.VirtualEnvironmentH\x00\x12\x33\n\x05\x63onda\x18\x03 \x01(\x0b\x32\".qwak.feature.store.features.CondaH\x00\x12\x35\n\x06poetry\x18\x04 \x01(\x0b\x32#.qwak.feature.store.features.PoetryH\x00\x42\x06\n\x04type\"*\n\x05\x43onda\x12!\n\x19\x62\x61se64_encoded_conda_file\x18\x01 \x01(\t\"*\n\x06Poetry\x12 \n\x18\x62\x61se64_encoded_lock_file\x18\x01 \x01(\t\"=\n\x12VirtualEnvironment\x12\'\n\x1f\x62\x61se64_encoded_requirements_txt\x18\x01 \x01(\t\"\xac\x01\n\x19\x45xtractorComputeResources\x12[\n\x19\x63ompute_resource_template\x18\x01 \x01(\x0e\x32\x36.qwak.feature.store.features.execution.ClusterTemplateH\x00\x12\x13\n\x0bparallelism\x18\x02 \x01(\x05\x12\x10\n\x08replicas\x18\x03 \x01(\x05\x42\x0b\n\tresources\"\xd3\x02\n\"RealtimeFeatureExtractorDeployment\x12\x15\n\rdeployment_id\x18\x01 \x01(\t\x12\x14\n\x0c\x65xtractor_id\x18\x02 \x01(\t\x12\x16\n\x0e\x65nvironment_id\x18\x03 \x01(\t\x12\x17\n\x0f\x63reated_user_id\x18\x04 \x01(\t\x12\x17\n\x0fupdated_user_id\x18\x05 \x01(\t\x12\x35\n\x11\x63reated_timestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x11updated_timestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n\x11\x64\x65ployment_status\x18\x08 \x01(\x0e\x32-.qwak.feature.store.features.DeploymentStatus\"\xcf\x03\n/RealtimeFeatureExtractorDeploymentUpdateRequest\x12\x19\n\x11update_request_id\x18\x01 \x01(\t\x12\x15\n\rdeployment_id\x18\x02 \x01(\t\x12\x16\n\x0e\x65nvironment_id\x18\x03 \x01(\t\x12\x17\n\x0f\x63reated_user_id\x18\x04 \x01(\t\x12P\n\rrequest_state\x18\x05 \x01(\x0b\x32\x39.qwak.feature.store.features.DeploymentUpdateRequestState\x12\x62\n\x1e\x64\x65ployment_failure_reason_code\x18\x06 \x01(\x0e\x32\x38.qwak.feature.store.features.DeploymentFailureReasonCodeH\x00\x12\x35\n\x11\x63reated_timestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x11updated_timestamp\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x15\n\x13\x66\x61ilure_reason_code*s\n\rPythonVersion\x12\x1a\n\x16PYTHON_VERSION_INVALID\x10\x00\x12\x16\n\x12PYTHON_VERSION_3_7\x10\x01\x12\x16\n\x12PYTHON_VERSION_3_8\x10\x02\x12\x16\n\x12PYTHON_VERSION_3_9\x10\x03\x42[\n&com.qwak.ai.feature.store.features.apiP\x01Z/qwak/featurestore/features;featurestorefeaturesb\x06proto3')

_PYTHONVERSION = DESCRIPTOR.enum_types_by_name['PythonVersion']
PythonVersion = enum_type_wrapper.EnumTypeWrapper(_PYTHONVERSION)
PYTHON_VERSION_INVALID = 0
PYTHON_VERSION_3_7 = 1
PYTHON_VERSION_3_8 = 2
PYTHON_VERSION_3_9 = 3


_REALTIMEFEATUREEXTRACTOR = DESCRIPTOR.message_types_by_name['RealTimeFeatureExtractor']
_REALTIMEFEATUREEXTRACTORDEFINITION = DESCRIPTOR.message_types_by_name['RealTimeFeatureExtractorDefinition']
_REALTIMEFEATUREEXTRACTORMETADATA = DESCRIPTOR.message_types_by_name['RealTimeFeatureExtractorMetadata']
_REALTIMEFEATUREEXTRACTORSPEC = DESCRIPTOR.message_types_by_name['RealTimeFeatureExtractorSpec']
_EXTRACTIONARTIFACT = DESCRIPTOR.message_types_by_name['ExtractionArtifact']
_AWSS3 = DESCRIPTOR.message_types_by_name['AwsS3']
_PYTHONDEPENDENCYMANAGER = DESCRIPTOR.message_types_by_name['PythonDependencyManager']
_CONDA = DESCRIPTOR.message_types_by_name['Conda']
_POETRY = DESCRIPTOR.message_types_by_name['Poetry']
_VIRTUALENVIRONMENT = DESCRIPTOR.message_types_by_name['VirtualEnvironment']
_EXTRACTORCOMPUTERESOURCES = DESCRIPTOR.message_types_by_name['ExtractorComputeResources']
_REALTIMEFEATUREEXTRACTORDEPLOYMENT = DESCRIPTOR.message_types_by_name['RealtimeFeatureExtractorDeployment']
_REALTIMEFEATUREEXTRACTORDEPLOYMENTUPDATEREQUEST = DESCRIPTOR.message_types_by_name['RealtimeFeatureExtractorDeploymentUpdateRequest']
RealTimeFeatureExtractor = _reflection.GeneratedProtocolMessageType('RealTimeFeatureExtractor', (_message.Message,), {
  'DESCRIPTOR' : _REALTIMEFEATUREEXTRACTOR,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.RealTimeFeatureExtractor)
  })
_sym_db.RegisterMessage(RealTimeFeatureExtractor)

RealTimeFeatureExtractorDefinition = _reflection.GeneratedProtocolMessageType('RealTimeFeatureExtractorDefinition', (_message.Message,), {
  'DESCRIPTOR' : _REALTIMEFEATUREEXTRACTORDEFINITION,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.RealTimeFeatureExtractorDefinition)
  })
_sym_db.RegisterMessage(RealTimeFeatureExtractorDefinition)

RealTimeFeatureExtractorMetadata = _reflection.GeneratedProtocolMessageType('RealTimeFeatureExtractorMetadata', (_message.Message,), {
  'DESCRIPTOR' : _REALTIMEFEATUREEXTRACTORMETADATA,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.RealTimeFeatureExtractorMetadata)
  })
_sym_db.RegisterMessage(RealTimeFeatureExtractorMetadata)

RealTimeFeatureExtractorSpec = _reflection.GeneratedProtocolMessageType('RealTimeFeatureExtractorSpec', (_message.Message,), {
  'DESCRIPTOR' : _REALTIMEFEATUREEXTRACTORSPEC,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.RealTimeFeatureExtractorSpec)
  })
_sym_db.RegisterMessage(RealTimeFeatureExtractorSpec)

ExtractionArtifact = _reflection.GeneratedProtocolMessageType('ExtractionArtifact', (_message.Message,), {
  'DESCRIPTOR' : _EXTRACTIONARTIFACT,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.ExtractionArtifact)
  })
_sym_db.RegisterMessage(ExtractionArtifact)

AwsS3 = _reflection.GeneratedProtocolMessageType('AwsS3', (_message.Message,), {
  'DESCRIPTOR' : _AWSS3,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.AwsS3)
  })
_sym_db.RegisterMessage(AwsS3)

PythonDependencyManager = _reflection.GeneratedProtocolMessageType('PythonDependencyManager', (_message.Message,), {
  'DESCRIPTOR' : _PYTHONDEPENDENCYMANAGER,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.PythonDependencyManager)
  })
_sym_db.RegisterMessage(PythonDependencyManager)

Conda = _reflection.GeneratedProtocolMessageType('Conda', (_message.Message,), {
  'DESCRIPTOR' : _CONDA,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.Conda)
  })
_sym_db.RegisterMessage(Conda)

Poetry = _reflection.GeneratedProtocolMessageType('Poetry', (_message.Message,), {
  'DESCRIPTOR' : _POETRY,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.Poetry)
  })
_sym_db.RegisterMessage(Poetry)

VirtualEnvironment = _reflection.GeneratedProtocolMessageType('VirtualEnvironment', (_message.Message,), {
  'DESCRIPTOR' : _VIRTUALENVIRONMENT,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.VirtualEnvironment)
  })
_sym_db.RegisterMessage(VirtualEnvironment)

ExtractorComputeResources = _reflection.GeneratedProtocolMessageType('ExtractorComputeResources', (_message.Message,), {
  'DESCRIPTOR' : _EXTRACTORCOMPUTERESOURCES,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.ExtractorComputeResources)
  })
_sym_db.RegisterMessage(ExtractorComputeResources)

RealtimeFeatureExtractorDeployment = _reflection.GeneratedProtocolMessageType('RealtimeFeatureExtractorDeployment', (_message.Message,), {
  'DESCRIPTOR' : _REALTIMEFEATUREEXTRACTORDEPLOYMENT,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.RealtimeFeatureExtractorDeployment)
  })
_sym_db.RegisterMessage(RealtimeFeatureExtractorDeployment)

RealtimeFeatureExtractorDeploymentUpdateRequest = _reflection.GeneratedProtocolMessageType('RealtimeFeatureExtractorDeploymentUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _REALTIMEFEATUREEXTRACTORDEPLOYMENTUPDATEREQUEST,
  '__module__' : 'qwak.feature_store.features.real_time_feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.RealtimeFeatureExtractorDeploymentUpdateRequest)
  })
_sym_db.RegisterMessage(RealtimeFeatureExtractorDeploymentUpdateRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&com.qwak.ai.feature.store.features.apiP\001Z/qwak/featurestore/features;featurestorefeatures'
  _PYTHONVERSION._serialized_start=2756
  _PYTHONVERSION._serialized_end=2871
  _REALTIMEFEATUREEXTRACTOR._serialized_start=219
  _REALTIMEFEATUREEXTRACTOR._serialized_end=439
  _REALTIMEFEATUREEXTRACTORDEFINITION._serialized_start=442
  _REALTIMEFEATUREEXTRACTORDEFINITION._serialized_end=698
  _REALTIMEFEATUREEXTRACTORMETADATA._serialized_start=701
  _REALTIMEFEATUREEXTRACTORMETADATA._serialized_end=901
  _REALTIMEFEATUREEXTRACTORSPEC._serialized_start=904
  _REALTIMEFEATUREEXTRACTORSPEC._serialized_end=1218
  _EXTRACTIONARTIFACT._serialized_start=1220
  _EXTRACTIONARTIFACT._serialized_end=1305
  _AWSS3._serialized_start=1307
  _AWSS3._serialized_end=1337
  _PYTHONDEPENDENCYMANAGER._serialized_start=1340
  _PYTHONDEPENDENCYMANAGER._serialized_end=1620
  _CONDA._serialized_start=1622
  _CONDA._serialized_end=1664
  _POETRY._serialized_start=1666
  _POETRY._serialized_end=1708
  _VIRTUALENVIRONMENT._serialized_start=1710
  _VIRTUALENVIRONMENT._serialized_end=1771
  _EXTRACTORCOMPUTERESOURCES._serialized_start=1774
  _EXTRACTORCOMPUTERESOURCES._serialized_end=1946
  _REALTIMEFEATUREEXTRACTORDEPLOYMENT._serialized_start=1949
  _REALTIMEFEATUREEXTRACTORDEPLOYMENT._serialized_end=2288
  _REALTIMEFEATUREEXTRACTORDEPLOYMENTUPDATEREQUEST._serialized_start=2291
  _REALTIMEFEATUREEXTRACTORDEPLOYMENTUPDATEREQUEST._serialized_end=2754
# @@protoc_insertion_point(module_scope)
