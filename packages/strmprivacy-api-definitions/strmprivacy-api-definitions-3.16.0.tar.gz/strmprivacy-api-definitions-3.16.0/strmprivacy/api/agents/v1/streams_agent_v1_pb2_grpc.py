# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from strmprivacy.api.agents.v1 import streams_agent_v1_pb2 as strmprivacy_dot_api_dot_agents_dot_v1_dot_streams__agent__v1__pb2


class StreamsAgentServiceStub(object):
    """(-- api-linter: core::0136::prepositions=disabled
    aip.dev/not-precedent: This is an internal API and the alternative with oneof is good either. --)
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStreams = channel.unary_unary(
                '/strmprivacy.api.agents.v1.StreamsAgentService/GetStreams',
                request_serializer=strmprivacy_dot_api_dot_agents_dot_v1_dot_streams__agent__v1__pb2.GetStreamsRequest.SerializeToString,
                response_deserializer=strmprivacy_dot_api_dot_agents_dot_v1_dot_streams__agent__v1__pb2.GetStreamsResponse.FromString,
                )


class StreamsAgentServiceServicer(object):
    """(-- api-linter: core::0136::prepositions=disabled
    aip.dev/not-precedent: This is an internal API and the alternative with oneof is good either. --)
    """

    def GetStreams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamsAgentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStreams': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStreams,
                    request_deserializer=strmprivacy_dot_api_dot_agents_dot_v1_dot_streams__agent__v1__pb2.GetStreamsRequest.FromString,
                    response_serializer=strmprivacy_dot_api_dot_agents_dot_v1_dot_streams__agent__v1__pb2.GetStreamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'strmprivacy.api.agents.v1.StreamsAgentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamsAgentService(object):
    """(-- api-linter: core::0136::prepositions=disabled
    aip.dev/not-precedent: This is an internal API and the alternative with oneof is good either. --)
    """

    @staticmethod
    def GetStreams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strmprivacy.api.agents.v1.StreamsAgentService/GetStreams',
            strmprivacy_dot_api_dot_agents_dot_v1_dot_streams__agent__v1__pb2.GetStreamsRequest.SerializeToString,
            strmprivacy_dot_api_dot_agents_dot_v1_dot_streams__agent__v1__pb2.GetStreamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
