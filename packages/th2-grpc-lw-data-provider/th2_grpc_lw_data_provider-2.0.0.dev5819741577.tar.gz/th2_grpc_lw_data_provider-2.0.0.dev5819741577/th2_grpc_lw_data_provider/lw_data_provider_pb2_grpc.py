# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from th2_grpc_common import common_pb2 as th2__grpc__common_dot_common__pb2
from th2_grpc_lw_data_provider import lw_data_provider_pb2 as th2__grpc__lw__data__provider_dot_lw__data__provider__pb2


class DataProviderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEvent = channel.unary_unary(
                '/th2.data_provider.lw.DataProvider/GetEvent',
                request_serializer=th2__grpc__common_dot_common__pb2.EventID.SerializeToString,
                response_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.EventResponse.FromString,
                )
        self.GetMessage = channel.unary_unary(
                '/th2.data_provider.lw.DataProvider/GetMessage',
                request_serializer=th2__grpc__common_dot_common__pb2.MessageID.SerializeToString,
                response_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageGroupResponse.FromString,
                )
        self.GetMessageStreams = channel.unary_unary(
                '/th2.data_provider.lw.DataProvider/GetMessageStreams',
                request_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageStreamsRequest.SerializeToString,
                response_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageStreamsResponse.FromString,
                )
        self.SearchMessages = channel.unary_stream(
                '/th2.data_provider.lw.DataProvider/SearchMessages',
                request_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageSearchRequest.SerializeToString,
                response_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageSearchResponse.FromString,
                )
        self.SearchEvents = channel.unary_stream(
                '/th2.data_provider.lw.DataProvider/SearchEvents',
                request_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.EventSearchRequest.SerializeToString,
                response_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.EventSearchResponse.FromString,
                )
        self.SearchMessageGroups = channel.unary_stream(
                '/th2.data_provider.lw.DataProvider/SearchMessageGroups',
                request_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageGroupsSearchRequest.SerializeToString,
                response_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageSearchResponse.FromString,
                )
        self.GetBooks = channel.unary_unary(
                '/th2.data_provider.lw.DataProvider/GetBooks',
                request_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.BooksRequest.SerializeToString,
                response_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.BooksResponse.FromString,
                )
        self.GetPageInfo = channel.unary_stream(
                '/th2.data_provider.lw.DataProvider/GetPageInfo',
                request_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.PageInfoRequest.SerializeToString,
                response_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.PageInfoResponse.FromString,
                )


class DataProviderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetEvent(self, request, context):
        """returns a single event with the specified id 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMessage(self, request, context):
        """returns a single message with the specified id 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMessageStreams(self, request, context):
        """returns a list of message stream names 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchMessages(self, request, context):
        """creates a message stream that matches the filter. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchEvents(self, request, context):
        """creates an event or an event metadata stream that matches the filter. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchMessageGroups(self, request, context):
        """
        Searches for messages groups in specified timestamp
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBooks(self, request, context):
        """Returns the set of books stored in cradle cache
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPageInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataProviderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEvent,
                    request_deserializer=th2__grpc__common_dot_common__pb2.EventID.FromString,
                    response_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.EventResponse.SerializeToString,
            ),
            'GetMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMessage,
                    request_deserializer=th2__grpc__common_dot_common__pb2.MessageID.FromString,
                    response_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageGroupResponse.SerializeToString,
            ),
            'GetMessageStreams': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMessageStreams,
                    request_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageStreamsRequest.FromString,
                    response_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageStreamsResponse.SerializeToString,
            ),
            'SearchMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.SearchMessages,
                    request_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageSearchRequest.FromString,
                    response_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageSearchResponse.SerializeToString,
            ),
            'SearchEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.SearchEvents,
                    request_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.EventSearchRequest.FromString,
                    response_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.EventSearchResponse.SerializeToString,
            ),
            'SearchMessageGroups': grpc.unary_stream_rpc_method_handler(
                    servicer.SearchMessageGroups,
                    request_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageGroupsSearchRequest.FromString,
                    response_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageSearchResponse.SerializeToString,
            ),
            'GetBooks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBooks,
                    request_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.BooksRequest.FromString,
                    response_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.BooksResponse.SerializeToString,
            ),
            'GetPageInfo': grpc.unary_stream_rpc_method_handler(
                    servicer.GetPageInfo,
                    request_deserializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.PageInfoRequest.FromString,
                    response_serializer=th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.PageInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'th2.data_provider.lw.DataProvider', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataProvider(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.lw.DataProvider/GetEvent',
            th2__grpc__common_dot_common__pb2.EventID.SerializeToString,
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.EventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.lw.DataProvider/GetMessage',
            th2__grpc__common_dot_common__pb2.MessageID.SerializeToString,
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMessageStreams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.lw.DataProvider/GetMessageStreams',
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageStreamsRequest.SerializeToString,
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageStreamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/th2.data_provider.lw.DataProvider/SearchMessages',
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageSearchRequest.SerializeToString,
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/th2.data_provider.lw.DataProvider/SearchEvents',
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.EventSearchRequest.SerializeToString,
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.EventSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchMessageGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/th2.data_provider.lw.DataProvider/SearchMessageGroups',
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageGroupsSearchRequest.SerializeToString,
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.MessageSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBooks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.lw.DataProvider/GetBooks',
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.BooksRequest.SerializeToString,
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.BooksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPageInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/th2.data_provider.lw.DataProvider/GetPageInfo',
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.PageInfoRequest.SerializeToString,
            th2__grpc__lw__data__provider_dot_lw__data__provider__pb2.PageInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
