from google.protobuf import timestamp_pb2 as _timestamp_pb2
from . import result_status_pb2 as _result_status_pb2
from . import results_fields_pb2 as _results_fields_pb2
from . import results_filters_pb2 as _results_filters_pb2
from . import sort_direction_pb2 as _sort_direction_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResultRaw(_message.Message):
    __slots__ = ["session_id", "name", "owner_task_id", "status", "created_at", "completed_at", "result_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    name: str
    owner_task_id: str
    status: _result_status_pb2.ResultStatus
    created_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    result_id: str
    def __init__(self, session_id: _Optional[str] = ..., name: _Optional[str] = ..., owner_task_id: _Optional[str] = ..., status: _Optional[_Union[_result_status_pb2.ResultStatus, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., result_id: _Optional[str] = ...) -> None: ...

class ListResultsRequest(_message.Message):
    __slots__ = ["page", "page_size", "filters", "sort"]
    class Sort(_message.Message):
        __slots__ = ["field", "direction"]
        FIELD_FIELD_NUMBER: _ClassVar[int]
        DIRECTION_FIELD_NUMBER: _ClassVar[int]
        field: _results_fields_pb2.ResultField
        direction: _sort_direction_pb2.SortDirection
        def __init__(self, field: _Optional[_Union[_results_fields_pb2.ResultField, _Mapping]] = ..., direction: _Optional[_Union[_sort_direction_pb2.SortDirection, str]] = ...) -> None: ...
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    filters: _results_filters_pb2.Filters
    sort: ListResultsRequest.Sort
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ..., filters: _Optional[_Union[_results_filters_pb2.Filters, _Mapping]] = ..., sort: _Optional[_Union[ListResultsRequest.Sort, _Mapping]] = ...) -> None: ...

class ListResultsResponse(_message.Message):
    __slots__ = ["results", "page", "page_size", "total"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ResultRaw]
    page: int
    page_size: int
    total: int
    def __init__(self, results: _Optional[_Iterable[_Union[ResultRaw, _Mapping]]] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., total: _Optional[int] = ...) -> None: ...

class GetResultRequest(_message.Message):
    __slots__ = ["result_id"]
    RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    result_id: str
    def __init__(self, result_id: _Optional[str] = ...) -> None: ...

class GetResultResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: ResultRaw
    def __init__(self, result: _Optional[_Union[ResultRaw, _Mapping]] = ...) -> None: ...

class GetOwnerTaskIdRequest(_message.Message):
    __slots__ = ["session_id", "result_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    result_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, session_id: _Optional[str] = ..., result_id: _Optional[_Iterable[str]] = ...) -> None: ...

class GetOwnerTaskIdResponse(_message.Message):
    __slots__ = ["result_task", "session_id"]
    class MapResultTask(_message.Message):
        __slots__ = ["result_id", "task_id"]
        RESULT_ID_FIELD_NUMBER: _ClassVar[int]
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        result_id: str
        task_id: str
        def __init__(self, result_id: _Optional[str] = ..., task_id: _Optional[str] = ...) -> None: ...
    RESULT_TASK_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    result_task: _containers.RepeatedCompositeFieldContainer[GetOwnerTaskIdResponse.MapResultTask]
    session_id: str
    def __init__(self, result_task: _Optional[_Iterable[_Union[GetOwnerTaskIdResponse.MapResultTask, _Mapping]]] = ..., session_id: _Optional[str] = ...) -> None: ...

class CreateResultsMetaDataRequest(_message.Message):
    __slots__ = ["results", "session_id"]
    class ResultCreate(_message.Message):
        __slots__ = ["name"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[CreateResultsMetaDataRequest.ResultCreate]
    session_id: str
    def __init__(self, results: _Optional[_Iterable[_Union[CreateResultsMetaDataRequest.ResultCreate, _Mapping]]] = ..., session_id: _Optional[str] = ...) -> None: ...

class CreateResultsMetaDataResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ResultRaw]
    def __init__(self, results: _Optional[_Iterable[_Union[ResultRaw, _Mapping]]] = ...) -> None: ...

class CreateResultsRequest(_message.Message):
    __slots__ = ["results", "session_id"]
    class ResultCreate(_message.Message):
        __slots__ = ["name", "data"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        name: str
        data: bytes
        def __init__(self, name: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[CreateResultsRequest.ResultCreate]
    session_id: str
    def __init__(self, results: _Optional[_Iterable[_Union[CreateResultsRequest.ResultCreate, _Mapping]]] = ..., session_id: _Optional[str] = ...) -> None: ...

class CreateResultsResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ResultRaw]
    def __init__(self, results: _Optional[_Iterable[_Union[ResultRaw, _Mapping]]] = ...) -> None: ...

class UploadResultDataRequest(_message.Message):
    __slots__ = ["id", "data_chunk"]
    class ResultIdentifier(_message.Message):
        __slots__ = ["session_id", "result_id"]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        RESULT_ID_FIELD_NUMBER: _ClassVar[int]
        session_id: str
        result_id: str
        def __init__(self, session_id: _Optional[str] = ..., result_id: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_CHUNK_FIELD_NUMBER: _ClassVar[int]
    id: UploadResultDataRequest.ResultIdentifier
    data_chunk: bytes
    def __init__(self, id: _Optional[_Union[UploadResultDataRequest.ResultIdentifier, _Mapping]] = ..., data_chunk: _Optional[bytes] = ...) -> None: ...

class UploadResultDataResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: ResultRaw
    def __init__(self, result: _Optional[_Union[ResultRaw, _Mapping]] = ...) -> None: ...

class ResultsServiceConfigurationResponse(_message.Message):
    __slots__ = ["data_chunk_max_size"]
    DATA_CHUNK_MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    data_chunk_max_size: int
    def __init__(self, data_chunk_max_size: _Optional[int] = ...) -> None: ...

class DownloadResultDataRequest(_message.Message):
    __slots__ = ["session_id", "result_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    result_id: str
    def __init__(self, session_id: _Optional[str] = ..., result_id: _Optional[str] = ...) -> None: ...

class DownloadResultDataResponse(_message.Message):
    __slots__ = ["data_chunk"]
    DATA_CHUNK_FIELD_NUMBER: _ClassVar[int]
    data_chunk: bytes
    def __init__(self, data_chunk: _Optional[bytes] = ...) -> None: ...

class DeleteResultsDataRequest(_message.Message):
    __slots__ = ["session_id", "result_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    result_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, session_id: _Optional[str] = ..., result_id: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteResultsDataResponse(_message.Message):
    __slots__ = ["session_id", "result_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    result_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, session_id: _Optional[str] = ..., result_id: _Optional[_Iterable[str]] = ...) -> None: ...
