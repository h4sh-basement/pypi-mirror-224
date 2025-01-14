# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import encryption_pb2 as admin_dot_v1_dot_encryption__pb2


class FieldEncryptionPolicyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateOrUpdateDefaultFieldEncryptionPolicy = channel.unary_unary(
                '/admin.v1.FieldEncryptionPolicyService/CreateOrUpdateDefaultFieldEncryptionPolicy',
                request_serializer=admin_dot_v1_dot_encryption__pb2.CreateOrUpdateDefaultFieldEncryptionPolicyRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_encryption__pb2.CreateOrUpdateDefaultFieldEncryptionPolicyResponse.FromString,
                )
        self.GetDefaultFieldEncryptionPolicy = channel.unary_unary(
                '/admin.v1.FieldEncryptionPolicyService/GetDefaultFieldEncryptionPolicy',
                request_serializer=admin_dot_v1_dot_encryption__pb2.GetDefaultFieldEncryptionPolicyRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_encryption__pb2.GetDefaultFieldEncryptionPolicyResponse.FromString,
                )


class FieldEncryptionPolicyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateOrUpdateDefaultFieldEncryptionPolicy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDefaultFieldEncryptionPolicy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FieldEncryptionPolicyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateOrUpdateDefaultFieldEncryptionPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrUpdateDefaultFieldEncryptionPolicy,
                    request_deserializer=admin_dot_v1_dot_encryption__pb2.CreateOrUpdateDefaultFieldEncryptionPolicyRequest.FromString,
                    response_serializer=admin_dot_v1_dot_encryption__pb2.CreateOrUpdateDefaultFieldEncryptionPolicyResponse.SerializeToString,
            ),
            'GetDefaultFieldEncryptionPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDefaultFieldEncryptionPolicy,
                    request_deserializer=admin_dot_v1_dot_encryption__pb2.GetDefaultFieldEncryptionPolicyRequest.FromString,
                    response_serializer=admin_dot_v1_dot_encryption__pb2.GetDefaultFieldEncryptionPolicyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'admin.v1.FieldEncryptionPolicyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FieldEncryptionPolicyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateOrUpdateDefaultFieldEncryptionPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admin.v1.FieldEncryptionPolicyService/CreateOrUpdateDefaultFieldEncryptionPolicy',
            admin_dot_v1_dot_encryption__pb2.CreateOrUpdateDefaultFieldEncryptionPolicyRequest.SerializeToString,
            admin_dot_v1_dot_encryption__pb2.CreateOrUpdateDefaultFieldEncryptionPolicyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDefaultFieldEncryptionPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admin.v1.FieldEncryptionPolicyService/GetDefaultFieldEncryptionPolicy',
            admin_dot_v1_dot_encryption__pb2.GetDefaultFieldEncryptionPolicyRequest.SerializeToString,
            admin_dot_v1_dot_encryption__pb2.GetDefaultFieldEncryptionPolicyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class FieldEncryptionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateFieldEncryption = channel.unary_unary(
                '/admin.v1.FieldEncryptionService/CreateFieldEncryption',
                request_serializer=admin_dot_v1_dot_encryption__pb2.CreateFieldEncryptionRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_encryption__pb2.CreateFieldEncryptionResponse.FromString,
                )
        self.GetFieldEncryptionsByDatastore = channel.unary_unary(
                '/admin.v1.FieldEncryptionService/GetFieldEncryptionsByDatastore',
                request_serializer=admin_dot_v1_dot_encryption__pb2.GetFieldEncryptionsByDatastoreRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_encryption__pb2.GetFieldEncryptionsByDatastoreResponse.FromString,
                )
        self.DeleteFieldEncryption = channel.unary_unary(
                '/admin.v1.FieldEncryptionService/DeleteFieldEncryption',
                request_serializer=admin_dot_v1_dot_encryption__pb2.DeleteFieldEncryptionRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_encryption__pb2.DeleteFieldEncryptionResponse.FromString,
                )


class FieldEncryptionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateFieldEncryption(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFieldEncryptionsByDatastore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFieldEncryption(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FieldEncryptionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateFieldEncryption': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFieldEncryption,
                    request_deserializer=admin_dot_v1_dot_encryption__pb2.CreateFieldEncryptionRequest.FromString,
                    response_serializer=admin_dot_v1_dot_encryption__pb2.CreateFieldEncryptionResponse.SerializeToString,
            ),
            'GetFieldEncryptionsByDatastore': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFieldEncryptionsByDatastore,
                    request_deserializer=admin_dot_v1_dot_encryption__pb2.GetFieldEncryptionsByDatastoreRequest.FromString,
                    response_serializer=admin_dot_v1_dot_encryption__pb2.GetFieldEncryptionsByDatastoreResponse.SerializeToString,
            ),
            'DeleteFieldEncryption': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFieldEncryption,
                    request_deserializer=admin_dot_v1_dot_encryption__pb2.DeleteFieldEncryptionRequest.FromString,
                    response_serializer=admin_dot_v1_dot_encryption__pb2.DeleteFieldEncryptionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'admin.v1.FieldEncryptionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FieldEncryptionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateFieldEncryption(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admin.v1.FieldEncryptionService/CreateFieldEncryption',
            admin_dot_v1_dot_encryption__pb2.CreateFieldEncryptionRequest.SerializeToString,
            admin_dot_v1_dot_encryption__pb2.CreateFieldEncryptionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFieldEncryptionsByDatastore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admin.v1.FieldEncryptionService/GetFieldEncryptionsByDatastore',
            admin_dot_v1_dot_encryption__pb2.GetFieldEncryptionsByDatastoreRequest.SerializeToString,
            admin_dot_v1_dot_encryption__pb2.GetFieldEncryptionsByDatastoreResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFieldEncryption(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admin.v1.FieldEncryptionService/DeleteFieldEncryption',
            admin_dot_v1_dot_encryption__pb2.DeleteFieldEncryptionRequest.SerializeToString,
            admin_dot_v1_dot_encryption__pb2.DeleteFieldEncryptionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
