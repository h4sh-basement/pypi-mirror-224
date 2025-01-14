# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..common import objects_pb2 as objects__pb2
from ..common import submitter_common_pb2 as submitter__common__pb2


class SubmitterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetServiceConfiguration = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/GetServiceConfiguration',
                request_serializer=objects__pb2.Empty.SerializeToString,
                response_deserializer=objects__pb2.Configuration.FromString,
                )
        self.CreateSession = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/CreateSession',
                request_serializer=submitter__common__pb2.CreateSessionRequest.SerializeToString,
                response_deserializer=submitter__common__pb2.CreateSessionReply.FromString,
                )
        self.CancelSession = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/CancelSession',
                request_serializer=objects__pb2.Session.SerializeToString,
                response_deserializer=objects__pb2.Empty.FromString,
                )
        self.CreateSmallTasks = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/CreateSmallTasks',
                request_serializer=submitter__common__pb2.CreateSmallTaskRequest.SerializeToString,
                response_deserializer=submitter__common__pb2.CreateTaskReply.FromString,
                )
        self.CreateLargeTasks = channel.stream_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/CreateLargeTasks',
                request_serializer=submitter__common__pb2.CreateLargeTaskRequest.SerializeToString,
                response_deserializer=submitter__common__pb2.CreateTaskReply.FromString,
                )
        self.ListTasks = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/ListTasks',
                request_serializer=submitter__common__pb2.TaskFilter.SerializeToString,
                response_deserializer=objects__pb2.TaskIdList.FromString,
                )
        self.ListSessions = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/ListSessions',
                request_serializer=submitter__common__pb2.SessionFilter.SerializeToString,
                response_deserializer=submitter__common__pb2.SessionIdList.FromString,
                )
        self.CountTasks = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/CountTasks',
                request_serializer=submitter__common__pb2.TaskFilter.SerializeToString,
                response_deserializer=objects__pb2.Count.FromString,
                )
        self.TryGetResultStream = channel.unary_stream(
                '/armonik.api.grpc.v1.submitter.Submitter/TryGetResultStream',
                request_serializer=objects__pb2.ResultRequest.SerializeToString,
                response_deserializer=submitter__common__pb2.ResultReply.FromString,
                )
        self.TryGetTaskOutput = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/TryGetTaskOutput',
                request_serializer=objects__pb2.TaskOutputRequest.SerializeToString,
                response_deserializer=objects__pb2.Output.FromString,
                )
        self.WaitForAvailability = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/WaitForAvailability',
                request_serializer=objects__pb2.ResultRequest.SerializeToString,
                response_deserializer=submitter__common__pb2.AvailabilityReply.FromString,
                )
        self.WaitForCompletion = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/WaitForCompletion',
                request_serializer=submitter__common__pb2.WaitRequest.SerializeToString,
                response_deserializer=objects__pb2.Count.FromString,
                )
        self.CancelTasks = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/CancelTasks',
                request_serializer=submitter__common__pb2.TaskFilter.SerializeToString,
                response_deserializer=objects__pb2.Empty.FromString,
                )
        self.GetTaskStatus = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/GetTaskStatus',
                request_serializer=submitter__common__pb2.GetTaskStatusRequest.SerializeToString,
                response_deserializer=submitter__common__pb2.GetTaskStatusReply.FromString,
                )
        self.GetResultStatus = channel.unary_unary(
                '/armonik.api.grpc.v1.submitter.Submitter/GetResultStatus',
                request_serializer=submitter__common__pb2.GetResultStatusRequest.SerializeToString,
                response_deserializer=submitter__common__pb2.GetResultStatusReply.FromString,
                )
        self.WatchResults = channel.stream_stream(
                '/armonik.api.grpc.v1.submitter.Submitter/WatchResults',
                request_serializer=submitter__common__pb2.WatchResultRequest.SerializeToString,
                response_deserializer=submitter__common__pb2.WatchResultStream.FromString,
                )


class SubmitterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetServiceConfiguration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSmallTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateLargeTasks(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSessions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CountTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TryGetResultStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TryGetTaskOutput(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WaitForAvailability(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WaitForCompletion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTaskStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetResultStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchResults(self, request_iterator, context):
        """*
        This endpoint allows a user to watch a list of results and be notified when there is any change.
        The user sends the list of ids they want to watch.
        The submitter will then send the statuses for all requested ids immediately and keep the stream open.
        Ids not present in DB will be returned at that time with the special state NOTFOUND.
        The submitter will send updates to the client via the opened stream.
        Any reply can be implicitely chunked if there are too many event to report at the same time (or for the first reply).
        It is possible to filter out specific statuses from events.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SubmitterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetServiceConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceConfiguration,
                    request_deserializer=objects__pb2.Empty.FromString,
                    response_serializer=objects__pb2.Configuration.SerializeToString,
            ),
            'CreateSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSession,
                    request_deserializer=submitter__common__pb2.CreateSessionRequest.FromString,
                    response_serializer=submitter__common__pb2.CreateSessionReply.SerializeToString,
            ),
            'CancelSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelSession,
                    request_deserializer=objects__pb2.Session.FromString,
                    response_serializer=objects__pb2.Empty.SerializeToString,
            ),
            'CreateSmallTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSmallTasks,
                    request_deserializer=submitter__common__pb2.CreateSmallTaskRequest.FromString,
                    response_serializer=submitter__common__pb2.CreateTaskReply.SerializeToString,
            ),
            'CreateLargeTasks': grpc.stream_unary_rpc_method_handler(
                    servicer.CreateLargeTasks,
                    request_deserializer=submitter__common__pb2.CreateLargeTaskRequest.FromString,
                    response_serializer=submitter__common__pb2.CreateTaskReply.SerializeToString,
            ),
            'ListTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTasks,
                    request_deserializer=submitter__common__pb2.TaskFilter.FromString,
                    response_serializer=objects__pb2.TaskIdList.SerializeToString,
            ),
            'ListSessions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSessions,
                    request_deserializer=submitter__common__pb2.SessionFilter.FromString,
                    response_serializer=submitter__common__pb2.SessionIdList.SerializeToString,
            ),
            'CountTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.CountTasks,
                    request_deserializer=submitter__common__pb2.TaskFilter.FromString,
                    response_serializer=objects__pb2.Count.SerializeToString,
            ),
            'TryGetResultStream': grpc.unary_stream_rpc_method_handler(
                    servicer.TryGetResultStream,
                    request_deserializer=objects__pb2.ResultRequest.FromString,
                    response_serializer=submitter__common__pb2.ResultReply.SerializeToString,
            ),
            'TryGetTaskOutput': grpc.unary_unary_rpc_method_handler(
                    servicer.TryGetTaskOutput,
                    request_deserializer=objects__pb2.TaskOutputRequest.FromString,
                    response_serializer=objects__pb2.Output.SerializeToString,
            ),
            'WaitForAvailability': grpc.unary_unary_rpc_method_handler(
                    servicer.WaitForAvailability,
                    request_deserializer=objects__pb2.ResultRequest.FromString,
                    response_serializer=submitter__common__pb2.AvailabilityReply.SerializeToString,
            ),
            'WaitForCompletion': grpc.unary_unary_rpc_method_handler(
                    servicer.WaitForCompletion,
                    request_deserializer=submitter__common__pb2.WaitRequest.FromString,
                    response_serializer=objects__pb2.Count.SerializeToString,
            ),
            'CancelTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelTasks,
                    request_deserializer=submitter__common__pb2.TaskFilter.FromString,
                    response_serializer=objects__pb2.Empty.SerializeToString,
            ),
            'GetTaskStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTaskStatus,
                    request_deserializer=submitter__common__pb2.GetTaskStatusRequest.FromString,
                    response_serializer=submitter__common__pb2.GetTaskStatusReply.SerializeToString,
            ),
            'GetResultStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetResultStatus,
                    request_deserializer=submitter__common__pb2.GetResultStatusRequest.FromString,
                    response_serializer=submitter__common__pb2.GetResultStatusReply.SerializeToString,
            ),
            'WatchResults': grpc.stream_stream_rpc_method_handler(
                    servicer.WatchResults,
                    request_deserializer=submitter__common__pb2.WatchResultRequest.FromString,
                    response_serializer=submitter__common__pb2.WatchResultStream.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'armonik.api.grpc.v1.submitter.Submitter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Submitter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetServiceConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/GetServiceConfiguration',
            objects__pb2.Empty.SerializeToString,
            objects__pb2.Configuration.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/CreateSession',
            submitter__common__pb2.CreateSessionRequest.SerializeToString,
            submitter__common__pb2.CreateSessionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/CancelSession',
            objects__pb2.Session.SerializeToString,
            objects__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSmallTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/CreateSmallTasks',
            submitter__common__pb2.CreateSmallTaskRequest.SerializeToString,
            submitter__common__pb2.CreateTaskReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateLargeTasks(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/armonik.api.grpc.v1.submitter.Submitter/CreateLargeTasks',
            submitter__common__pb2.CreateLargeTaskRequest.SerializeToString,
            submitter__common__pb2.CreateTaskReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/ListTasks',
            submitter__common__pb2.TaskFilter.SerializeToString,
            objects__pb2.TaskIdList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSessions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/ListSessions',
            submitter__common__pb2.SessionFilter.SerializeToString,
            submitter__common__pb2.SessionIdList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CountTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/CountTasks',
            submitter__common__pb2.TaskFilter.SerializeToString,
            objects__pb2.Count.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TryGetResultStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/armonik.api.grpc.v1.submitter.Submitter/TryGetResultStream',
            objects__pb2.ResultRequest.SerializeToString,
            submitter__common__pb2.ResultReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TryGetTaskOutput(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/TryGetTaskOutput',
            objects__pb2.TaskOutputRequest.SerializeToString,
            objects__pb2.Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WaitForAvailability(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/WaitForAvailability',
            objects__pb2.ResultRequest.SerializeToString,
            submitter__common__pb2.AvailabilityReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WaitForCompletion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/WaitForCompletion',
            submitter__common__pb2.WaitRequest.SerializeToString,
            objects__pb2.Count.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/CancelTasks',
            submitter__common__pb2.TaskFilter.SerializeToString,
            objects__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTaskStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/GetTaskStatus',
            submitter__common__pb2.GetTaskStatusRequest.SerializeToString,
            submitter__common__pb2.GetTaskStatusReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetResultStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/armonik.api.grpc.v1.submitter.Submitter/GetResultStatus',
            submitter__common__pb2.GetResultStatusRequest.SerializeToString,
            submitter__common__pb2.GetResultStatusReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WatchResults(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/armonik.api.grpc.v1.submitter.Submitter/WatchResults',
            submitter__common__pb2.WatchResultRequest.SerializeToString,
            submitter__common__pb2.WatchResultStream.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
