# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import greeting_pb2 as greeting__pb2


class AdvancedGreeterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/advanced_greeting.AdvancedGreeter/SayHello',
                request_serializer=greeting__pb2.HelloRequest.SerializeToString,
                response_deserializer=greeting__pb2.HelloReply.FromString,
                )
        self.GreetManyTimes = channel.unary_stream(
                '/advanced_greeting.AdvancedGreeter/GreetManyTimes',
                request_serializer=greeting__pb2.HelloRequest.SerializeToString,
                response_deserializer=greeting__pb2.HelloReply.FromString,
                )
        self.LongGreet = channel.stream_unary(
                '/advanced_greeting.AdvancedGreeter/LongGreet',
                request_serializer=greeting__pb2.HelloRequest.SerializeToString,
                response_deserializer=greeting__pb2.HelloReply.FromString,
                )
        self.GreetEveryone = channel.stream_stream(
                '/advanced_greeting.AdvancedGreeter/GreetEveryone',
                request_serializer=greeting__pb2.HelloRequest.SerializeToString,
                response_deserializer=greeting__pb2.HelloReply.FromString,
                )


class AdvancedGreeterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Unary RPC
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GreetManyTimes(self, request, context):
        """Server streaming RPC
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LongGreet(self, request_iterator, context):
        """Client streaming RPC
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GreetEveryone(self, request_iterator, context):
        """Bidirectional streaming RPC
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdvancedGreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=greeting__pb2.HelloRequest.FromString,
                    response_serializer=greeting__pb2.HelloReply.SerializeToString,
            ),
            'GreetManyTimes': grpc.unary_stream_rpc_method_handler(
                    servicer.GreetManyTimes,
                    request_deserializer=greeting__pb2.HelloRequest.FromString,
                    response_serializer=greeting__pb2.HelloReply.SerializeToString,
            ),
            'LongGreet': grpc.stream_unary_rpc_method_handler(
                    servicer.LongGreet,
                    request_deserializer=greeting__pb2.HelloRequest.FromString,
                    response_serializer=greeting__pb2.HelloReply.SerializeToString,
            ),
            'GreetEveryone': grpc.stream_stream_rpc_method_handler(
                    servicer.GreetEveryone,
                    request_deserializer=greeting__pb2.HelloRequest.FromString,
                    response_serializer=greeting__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'advanced_greeting.AdvancedGreeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdvancedGreeter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/advanced_greeting.AdvancedGreeter/SayHello',
            greeting__pb2.HelloRequest.SerializeToString,
            greeting__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GreetManyTimes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/advanced_greeting.AdvancedGreeter/GreetManyTimes',
            greeting__pb2.HelloRequest.SerializeToString,
            greeting__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LongGreet(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/advanced_greeting.AdvancedGreeter/LongGreet',
            greeting__pb2.HelloRequest.SerializeToString,
            greeting__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GreetEveryone(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/advanced_greeting.AdvancedGreeter/GreetEveryone',
            greeting__pb2.HelloRequest.SerializeToString,
            greeting__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
