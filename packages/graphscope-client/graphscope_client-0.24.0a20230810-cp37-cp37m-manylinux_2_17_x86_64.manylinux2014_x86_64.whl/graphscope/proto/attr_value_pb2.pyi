"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
*

The file proto/attr_value.proto is referred and derived from project
tensorflow,

   https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/attr_value.proto

which has the following license:


Copyright 2015 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class AttrValue(google.protobuf.message.Message):
    """Comment indicates the corresponding attr type. Only the field matching the
    attr type may be filled.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _NullValue:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _NullValueEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AttrValue._NullValue.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NULL_VALUE: AttrValue._NullValue.ValueType  # 0

    class NullValue(_NullValue, metaclass=_NullValueEnumTypeWrapper): ...
    NULL_VALUE: AttrValue.NullValue.ValueType  # 0

    @typing_extensions.final
    class ListValue(google.protobuf.message.Message):
        """Allows recursive nesting"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        S_FIELD_NUMBER: builtins.int
        I_FIELD_NUMBER: builtins.int
        F_FIELD_NUMBER: builtins.int
        B_FIELD_NUMBER: builtins.int
        FUNC_FIELD_NUMBER: builtins.int
        LIST_FIELD_NUMBER: builtins.int
        @property
        def s(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
            """"list(string)" """
        @property
        def i(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
            """"list(int)" """
        @property
        def f(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
            """"list(float)" """
        @property
        def b(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bool]:
            """"list(bool)" """
        @property
        def func(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NameAttrList]:
            """"list(attr)" """
        @property
        def list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AttrValue.ListValue]:
            """"list(list)"""
        def __init__(
            self,
            *,
            s: collections.abc.Iterable[builtins.bytes] | None = ...,
            i: collections.abc.Iterable[builtins.int] | None = ...,
            f: collections.abc.Iterable[builtins.float] | None = ...,
            b: collections.abc.Iterable[builtins.bool] | None = ...,
            func: collections.abc.Iterable[global___NameAttrList] | None = ...,
            list: collections.abc.Iterable[global___AttrValue.ListValue] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["b", b"b", "f", b"f", "func", b"func", "i", b"i", "list", b"list", "s", b"s"]) -> None: ...

    NULL_FIELD_NUMBER: builtins.int
    S_FIELD_NUMBER: builtins.int
    I_FIELD_NUMBER: builtins.int
    U_FIELD_NUMBER: builtins.int
    F_FIELD_NUMBER: builtins.int
    B_FIELD_NUMBER: builtins.int
    LIST_FIELD_NUMBER: builtins.int
    FUNC_FIELD_NUMBER: builtins.int
    null: global___AttrValue.NullValue.ValueType
    """"null" """
    s: builtins.bytes
    """"string" """
    i: builtins.int
    """"int" """
    u: builtins.int
    """"uint64" """
    f: builtins.float
    """"float" """
    b: builtins.bool
    """"bool" """
    @property
    def list(self) -> global___AttrValue.ListValue:
        """any "list(...)" """
    @property
    def func(self) -> global___NameAttrList: ...
    def __init__(
        self,
        *,
        null: global___AttrValue.NullValue.ValueType = ...,
        s: builtins.bytes = ...,
        i: builtins.int = ...,
        u: builtins.int = ...,
        f: builtins.float = ...,
        b: builtins.bool = ...,
        list: global___AttrValue.ListValue | None = ...,
        func: global___NameAttrList | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["b", b"b", "f", b"f", "func", b"func", "i", b"i", "list", b"list", "null", b"null", "s", b"s", "u", b"u", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["b", b"b", "f", b"f", "func", b"func", "i", b"i", "list", b"list", "null", b"null", "s", b"s", "u", b"u", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value", b"value"]) -> typing_extensions.Literal["null", "s", "i", "u", "f", "b", "list", "func"] | None: ...

global___AttrValue = AttrValue

@typing_extensions.final
class NameAttrList(google.protobuf.message.Message):
    """A list of attr names and their values."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AttrEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___AttrValue: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___AttrValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    ATTR_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def attr(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___AttrValue]: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        attr: collections.abc.Mapping[builtins.int, global___AttrValue] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["attr", b"attr", "name", b"name"]) -> None: ...

global___NameAttrList = NameAttrList

@typing_extensions.final
class Chunk(google.protobuf.message.Message):
    """Chunk, ChunkMeta and LargeAttrValue is used for storing chunks of
    huge bytes, which is larger than the GRPC message limits(2 GB)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AttrEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___AttrValue: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___AttrValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    BUFFER_FIELD_NUMBER: builtins.int
    ATTR_FIELD_NUMBER: builtins.int
    buffer: builtins.bytes
    @property
    def attr(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___AttrValue]: ...
    def __init__(
        self,
        *,
        buffer: builtins.bytes = ...,
        attr: collections.abc.Mapping[builtins.int, global___AttrValue] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["attr", b"attr", "buffer", b"buffer"]) -> None: ...

global___Chunk = Chunk

@typing_extensions.final
class ChunkMeta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AttrEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___AttrValue: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___AttrValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    SIZE_FIELD_NUMBER: builtins.int
    ATTR_FIELD_NUMBER: builtins.int
    size: builtins.int
    """total buffer size of the chunk"""
    @property
    def attr(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___AttrValue]: ...
    def __init__(
        self,
        *,
        size: builtins.int = ...,
        attr: collections.abc.Mapping[builtins.int, global___AttrValue] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["attr", b"attr", "size", b"size"]) -> None: ...

global___ChunkMeta = ChunkMeta

@typing_extensions.final
class LargeAttrValue(google.protobuf.message.Message):
    """AttrValue for large chunk."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ChunkList(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ITEMS_FIELD_NUMBER: builtins.int
        @property
        def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Chunk]: ...
        def __init__(
            self,
            *,
            items: collections.abc.Iterable[global___Chunk] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["items", b"items"]) -> None: ...

    @typing_extensions.final
    class ChunkMetaList(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ITEMS_FIELD_NUMBER: builtins.int
        @property
        def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ChunkMeta]: ...
        def __init__(
            self,
            *,
            items: collections.abc.Iterable[global___ChunkMeta] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["items", b"items"]) -> None: ...

    CHUNK_LIST_FIELD_NUMBER: builtins.int
    CHUNK_META_LIST_FIELD_NUMBER: builtins.int
    @property
    def chunk_list(self) -> global___LargeAttrValue.ChunkList: ...
    @property
    def chunk_meta_list(self) -> global___LargeAttrValue.ChunkMetaList: ...
    def __init__(
        self,
        *,
        chunk_list: global___LargeAttrValue.ChunkList | None = ...,
        chunk_meta_list: global___LargeAttrValue.ChunkMetaList | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["chunk_list", b"chunk_list", "chunk_meta_list", b"chunk_meta_list", "large_value", b"large_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["chunk_list", b"chunk_list", "chunk_meta_list", b"chunk_meta_list", "large_value", b"large_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["large_value", b"large_value"]) -> typing_extensions.Literal["chunk_list", "chunk_meta_list"] | None: ...

global___LargeAttrValue = LargeAttrValue
