# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from _qwak_proto.qwak.self_service.user.v1 import user_service_pb2 as qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateApiKey = channel.unary_unary(
                '/qwak.self_service.user.v1.UserService/GenerateApiKey',
                request_serializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GenerateApiKeyRequest.SerializeToString,
                response_deserializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GenerateApiKeyResponse.FromString,
                )
        self.RevokeApiKey = channel.unary_unary(
                '/qwak.self_service.user.v1.UserService/RevokeApiKey',
                request_serializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.RevokeApiKeyRequest.SerializeToString,
                response_deserializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.RevokeApiKeyResponse.FromString,
                )
        self.ListApiKeyDetails = channel.unary_unary(
                '/qwak.self_service.user.v1.UserService/ListApiKeyDetails',
                request_serializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.ListApiKeyDetailsRequest.SerializeToString,
                response_deserializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.ListApiKeyDetailsResponse.FromString,
                )
        self.GetUserProfile = channel.unary_unary(
                '/qwak.self_service.user.v1.UserService/GetUserProfile',
                request_serializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GetUserProfileRequest.SerializeToString,
                response_deserializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GetUserProfileResponse.FromString,
                )
        self.UpdateUserProfile = channel.unary_unary(
                '/qwak.self_service.user.v1.UserService/UpdateUserProfile',
                request_serializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.UpdateUserProfileRequest.SerializeToString,
                response_deserializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.UpdateUserProfileResponse.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GenerateApiKey(self, request, context):
        """Invoke password reset process for a given user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeApiKey(self, request, context):
        """Revoke API key for a given user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListApiKeyDetails(self, request, context):
        """List API key details per environment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserProfile(self, request, context):
        """Get user profile
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUserProfile(self, request, context):
        """Update user profile
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateApiKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateApiKey,
                    request_deserializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GenerateApiKeyRequest.FromString,
                    response_serializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GenerateApiKeyResponse.SerializeToString,
            ),
            'RevokeApiKey': grpc.unary_unary_rpc_method_handler(
                    servicer.RevokeApiKey,
                    request_deserializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.RevokeApiKeyRequest.FromString,
                    response_serializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.RevokeApiKeyResponse.SerializeToString,
            ),
            'ListApiKeyDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.ListApiKeyDetails,
                    request_deserializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.ListApiKeyDetailsRequest.FromString,
                    response_serializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.ListApiKeyDetailsResponse.SerializeToString,
            ),
            'GetUserProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserProfile,
                    request_deserializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GetUserProfileRequest.FromString,
                    response_serializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GetUserProfileResponse.SerializeToString,
            ),
            'UpdateUserProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUserProfile,
                    request_deserializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.UpdateUserProfileRequest.FromString,
                    response_serializer=qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.UpdateUserProfileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'qwak.self_service.user.v1.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GenerateApiKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.self_service.user.v1.UserService/GenerateApiKey',
            qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GenerateApiKeyRequest.SerializeToString,
            qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GenerateApiKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevokeApiKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.self_service.user.v1.UserService/RevokeApiKey',
            qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.RevokeApiKeyRequest.SerializeToString,
            qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.RevokeApiKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListApiKeyDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.self_service.user.v1.UserService/ListApiKeyDetails',
            qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.ListApiKeyDetailsRequest.SerializeToString,
            qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.ListApiKeyDetailsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.self_service.user.v1.UserService/GetUserProfile',
            qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GetUserProfileRequest.SerializeToString,
            qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.GetUserProfileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUserProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.self_service.user.v1.UserService/UpdateUserProfile',
            qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.UpdateUserProfileRequest.SerializeToString,
            qwak_dot_self__service_dot_user_dot_v1_dot_user__service__pb2.UpdateUserProfileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
