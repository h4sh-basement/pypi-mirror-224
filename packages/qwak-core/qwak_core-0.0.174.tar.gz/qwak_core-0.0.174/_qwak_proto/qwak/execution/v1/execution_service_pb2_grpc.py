# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from _qwak_proto.qwak.execution.v1 import execution_service_pb2 as qwak_dot_execution_dot_v1_dot_execution__service__pb2


class FeatureStoreExecutionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TriggerBatchBackfill = channel.unary_unary(
                '/qwak.feature.store.execution.v1.FeatureStoreExecutionService/TriggerBatchBackfill',
                request_serializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBackfillRequest.SerializeToString,
                response_deserializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBackfillResponse.FromString,
                )
        self.TriggerBatchFeatureset = channel.unary_unary(
                '/qwak.feature.store.execution.v1.FeatureStoreExecutionService/TriggerBatchFeatureset',
                request_serializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBatchFeaturesetRequest.SerializeToString,
                response_deserializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBatchFeaturesetResponse.FromString,
                )
        self.GetExecutionStatus = channel.unary_unary(
                '/qwak.feature.store.execution.v1.FeatureStoreExecutionService/GetExecutionStatus',
                request_serializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionStatusRequest.SerializeToString,
                response_deserializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionStatusResponse.FromString,
                )
        self.GetExecutionEntry = channel.unary_unary(
                '/qwak.feature.store.execution.v1.FeatureStoreExecutionService/GetExecutionEntry',
                request_serializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionEntryRequest.SerializeToString,
                response_deserializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionEntryResponse.FromString,
                )


class FeatureStoreExecutionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TriggerBatchBackfill(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TriggerBatchFeatureset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExecutionStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExecutionEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FeatureStoreExecutionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TriggerBatchBackfill': grpc.unary_unary_rpc_method_handler(
                    servicer.TriggerBatchBackfill,
                    request_deserializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBackfillRequest.FromString,
                    response_serializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBackfillResponse.SerializeToString,
            ),
            'TriggerBatchFeatureset': grpc.unary_unary_rpc_method_handler(
                    servicer.TriggerBatchFeatureset,
                    request_deserializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBatchFeaturesetRequest.FromString,
                    response_serializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBatchFeaturesetResponse.SerializeToString,
            ),
            'GetExecutionStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExecutionStatus,
                    request_deserializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionStatusRequest.FromString,
                    response_serializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionStatusResponse.SerializeToString,
            ),
            'GetExecutionEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExecutionEntry,
                    request_deserializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionEntryRequest.FromString,
                    response_serializer=qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionEntryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'qwak.feature.store.execution.v1.FeatureStoreExecutionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FeatureStoreExecutionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TriggerBatchBackfill(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.feature.store.execution.v1.FeatureStoreExecutionService/TriggerBatchBackfill',
            qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBackfillRequest.SerializeToString,
            qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBackfillResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TriggerBatchFeatureset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.feature.store.execution.v1.FeatureStoreExecutionService/TriggerBatchFeatureset',
            qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBatchFeaturesetRequest.SerializeToString,
            qwak_dot_execution_dot_v1_dot_execution__service__pb2.TriggerBatchFeaturesetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExecutionStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.feature.store.execution.v1.FeatureStoreExecutionService/GetExecutionStatus',
            qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionStatusRequest.SerializeToString,
            qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExecutionEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.feature.store.execution.v1.FeatureStoreExecutionService/GetExecutionEntry',
            qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionEntryRequest.SerializeToString,
            qwak_dot_execution_dot_v1_dot_execution__service__pb2.GetExecutionEntryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
