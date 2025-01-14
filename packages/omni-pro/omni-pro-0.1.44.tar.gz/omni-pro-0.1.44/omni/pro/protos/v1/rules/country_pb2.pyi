from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Country(_message.Message):
    __slots__ = ["id", "name", "code", "country_doc_id", "active", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    country_doc_id: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        country_doc_id: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class CountryCreateRequest(_message.Message):
    __slots__ = ["name", "code", "category_doc_id", "context"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    category_doc_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        category_doc_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CountryCreateResponse(_message.Message):
    __slots__ = ["country", "response_standard"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    country: Country
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        country: _Optional[_Union[Country, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class CountryReadRequest(_message.Message):
    __slots__ = ["group_by", "sort_by", "fields", "filter", "paginated", "id", "context"]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    sort_by: _base_pb2.SortBy
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    paginated: _base_pb2.Paginated
    id: str
    context: _base_pb2.Context
    def __init__(
        self,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CountryReadResponse(_message.Message):
    __slots__ = ["countries", "meta_data", "response_standard"]
    COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    countries: _containers.RepeatedCompositeFieldContainer[Country]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        countries: _Optional[_Iterable[_Union[Country, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class CountryUpdateRequest(_message.Message):
    __slots__ = ["country", "context"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    country: Country
    context: _base_pb2.Context
    def __init__(
        self,
        country: _Optional[_Union[Country, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CountryUpdateResponse(_message.Message):
    __slots__ = ["country", "response_standard"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    country: Country
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        country: _Optional[_Union[Country, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class CountryDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class CountryDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
