# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import write_service_pb2 as write__service__pb2


class ClientWriteStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getClientId = channel.unary_unary(
                '/gs.rpc.groot.ClientWrite/getClientId',
                request_serializer=write__service__pb2.GetClientIdRequest.SerializeToString,
                response_deserializer=write__service__pb2.GetClientIdResponse.FromString,
                )
        self.batchWrite = channel.unary_unary(
                '/gs.rpc.groot.ClientWrite/batchWrite',
                request_serializer=write__service__pb2.BatchWriteRequest.SerializeToString,
                response_deserializer=write__service__pb2.BatchWriteResponse.FromString,
                )
        self.remoteFlush = channel.unary_unary(
                '/gs.rpc.groot.ClientWrite/remoteFlush',
                request_serializer=write__service__pb2.RemoteFlushRequest.SerializeToString,
                response_deserializer=write__service__pb2.RemoteFlushResponse.FromString,
                )


class ClientWriteServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getClientId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def batchWrite(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remoteFlush(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientWriteServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getClientId': grpc.unary_unary_rpc_method_handler(
                    servicer.getClientId,
                    request_deserializer=write__service__pb2.GetClientIdRequest.FromString,
                    response_serializer=write__service__pb2.GetClientIdResponse.SerializeToString,
            ),
            'batchWrite': grpc.unary_unary_rpc_method_handler(
                    servicer.batchWrite,
                    request_deserializer=write__service__pb2.BatchWriteRequest.FromString,
                    response_serializer=write__service__pb2.BatchWriteResponse.SerializeToString,
            ),
            'remoteFlush': grpc.unary_unary_rpc_method_handler(
                    servicer.remoteFlush,
                    request_deserializer=write__service__pb2.RemoteFlushRequest.FromString,
                    response_serializer=write__service__pb2.RemoteFlushResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gs.rpc.groot.ClientWrite', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClientWrite(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getClientId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gs.rpc.groot.ClientWrite/getClientId',
            write__service__pb2.GetClientIdRequest.SerializeToString,
            write__service__pb2.GetClientIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def batchWrite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gs.rpc.groot.ClientWrite/batchWrite',
            write__service__pb2.BatchWriteRequest.SerializeToString,
            write__service__pb2.BatchWriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def remoteFlush(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gs.rpc.groot.ClientWrite/remoteFlush',
            write__service__pb2.RemoteFlushRequest.SerializeToString,
            write__service__pb2.RemoteFlushResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
