"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2020 Alibaba Group Holding Limited. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.any_pb2
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

class _ClusterType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ClusterTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ClusterType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    HOSTS: _ClusterType.ValueType  # 0
    K8S: _ClusterType.ValueType  # 1
    UNDEFINED: _ClusterType.ValueType  # 100

class ClusterType(_ClusterType, metaclass=_ClusterTypeEnumTypeWrapper): ...

HOSTS: ClusterType.ValueType  # 0
K8S: ClusterType.ValueType  # 1
UNDEFINED: ClusterType.ValueType  # 100
global___ClusterType = ClusterType

class _DataType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DataTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DataType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NULLVALUE: _DataType.ValueType  # 0
    INT8: _DataType.ValueType  # 1
    INT16: _DataType.ValueType  # 2
    INT32: _DataType.ValueType  # 3
    INT64: _DataType.ValueType  # 4
    INT128: _DataType.ValueType  # 5
    UINT8: _DataType.ValueType  # 6
    UINT16: _DataType.ValueType  # 7
    UINT32: _DataType.ValueType  # 8
    UINT64: _DataType.ValueType  # 9
    UINT128: _DataType.ValueType  # 10
    INT: _DataType.ValueType  # 11
    LONG: _DataType.ValueType  # 12
    LONGLONG: _DataType.ValueType  # 13
    UINT: _DataType.ValueType  # 14
    ULONG: _DataType.ValueType  # 15
    ULONGLONG: _DataType.ValueType  # 16
    FLOAT: _DataType.ValueType  # 18
    DOUBLE: _DataType.ValueType  # 19
    BOOLEAN: _DataType.ValueType  # 20
    STRING: _DataType.ValueType  # 21
    DATETIME: _DataType.ValueType  # 22
    LIST: _DataType.ValueType  # 23
    INVALID: _DataType.ValueType  # 536870911

class DataType(_DataType, metaclass=_DataTypeEnumTypeWrapper):
    """Basic data types"""

NULLVALUE: DataType.ValueType  # 0
INT8: DataType.ValueType  # 1
INT16: DataType.ValueType  # 2
INT32: DataType.ValueType  # 3
INT64: DataType.ValueType  # 4
INT128: DataType.ValueType  # 5
UINT8: DataType.ValueType  # 6
UINT16: DataType.ValueType  # 7
UINT32: DataType.ValueType  # 8
UINT64: DataType.ValueType  # 9
UINT128: DataType.ValueType  # 10
INT: DataType.ValueType  # 11
LONG: DataType.ValueType  # 12
LONGLONG: DataType.ValueType  # 13
UINT: DataType.ValueType  # 14
ULONG: DataType.ValueType  # 15
ULONGLONG: DataType.ValueType  # 16
FLOAT: DataType.ValueType  # 18
DOUBLE: DataType.ValueType  # 19
BOOLEAN: DataType.ValueType  # 20
STRING: DataType.ValueType  # 21
DATETIME: DataType.ValueType  # 22
LIST: DataType.ValueType  # 23
INVALID: DataType.ValueType  # 536870911
global___DataType = DataType

class _Direction:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DirectionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Direction.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _Direction.ValueType  # 0
    IN: _Direction.ValueType  # 1
    OUT: _Direction.ValueType  # 2

class Direction(_Direction, metaclass=_DirectionEnumTypeWrapper): ...

NONE: Direction.ValueType  # 0
IN: Direction.ValueType  # 1
OUT: Direction.ValueType  # 2
global___Direction = Direction

class _OutputType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _OutputTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OutputType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    GRAPH: _OutputType.ValueType  # 0
    APP: _OutputType.ValueType  # 1
    BOUND_APP: _OutputType.ValueType  # 2
    RESULTS: _OutputType.ValueType  # 3
    TENSOR: _OutputType.ValueType  # 4
    DATAFRAME: _OutputType.ValueType  # 5
    VINEYARD_TENSOR: _OutputType.ValueType  # 6
    VINEYARD_DATAFRAME: _OutputType.ValueType  # 7
    INTERACTIVE_QUERY: _OutputType.ValueType  # 8
    LEARNING_GRAPH: _OutputType.ValueType  # 10
    NULL_OUTPUT: _OutputType.ValueType  # 101

class OutputType(_OutputType, metaclass=_OutputTypeEnumTypeWrapper):
    """The output types of evaluating an Operation"""

GRAPH: OutputType.ValueType  # 0
APP: OutputType.ValueType  # 1
BOUND_APP: OutputType.ValueType  # 2
RESULTS: OutputType.ValueType  # 3
TENSOR: OutputType.ValueType  # 4
DATAFRAME: OutputType.ValueType  # 5
VINEYARD_TENSOR: OutputType.ValueType  # 6
VINEYARD_DATAFRAME: OutputType.ValueType  # 7
INTERACTIVE_QUERY: OutputType.ValueType  # 8
LEARNING_GRAPH: OutputType.ValueType  # 10
NULL_OUTPUT: OutputType.ValueType  # 101
global___OutputType = OutputType

class _OperationType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _OperationTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OperationType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    CREATE_GRAPH: _OperationType.ValueType  # 0
    """command
    return output_type = graph
    """
    BIND_APP: _OperationType.ValueType  # 1
    """return app"""
    CREATE_APP: _OperationType.ValueType  # 2
    """do nothing"""
    MODIFY_VERTICES: _OperationType.ValueType  # 3
    """return graph"""
    MODIFY_EDGES: _OperationType.ValueType  # 4
    """return graph"""
    RUN_APP: _OperationType.ValueType  # 5
    """return result"""
    UNLOAD_APP: _OperationType.ValueType  # 6
    UNLOAD_GRAPH: _OperationType.ValueType  # 7
    REPARTITION: _OperationType.ValueType  # 8
    """return graph"""
    TRANSFORM_GRAPH: _OperationType.ValueType  # 9
    """return graph or nx_graph"""
    REPORT_GRAPH: _OperationType.ValueType  # 10
    """return scalar"""
    PROJECT_GRAPH: _OperationType.ValueType  # 11
    """return graph, general form project"""
    PROJECT_TO_SIMPLE: _OperationType.ValueType  # 12
    """return graph, specifically project to a simple graph"""
    COPY_GRAPH: _OperationType.ValueType  # 13
    ADD_VERTICES: _OperationType.ValueType  # 14
    """not used, leaves room for future development"""
    ADD_EDGES: _OperationType.ValueType  # 15
    """not used, leaves room for future development"""
    ADD_LABELS: _OperationType.ValueType  # 16
    """return graph, add new label of vertices or label of edges to existed graph"""
    TO_DIRECTED: _OperationType.ValueType  # 17
    """return graph, generate directed graph from undirected graph"""
    TO_UNDIRECTED: _OperationType.ValueType  # 18
    """return graph, generate undirected graph from directed graph"""
    CLEAR_EDGES: _OperationType.ValueType  # 19
    """clear edges"""
    CLEAR_GRAPH: _OperationType.ValueType  # 20
    """clear graph"""
    VIEW_GRAPH: _OperationType.ValueType  # 21
    """create graph view"""
    INDUCE_SUBGRAPH: _OperationType.ValueType  # 22
    """induce subgraph"""
    UNLOAD_CONTEXT: _OperationType.ValueType  # 23
    """unload context"""
    ARCHIVE_GRAPH: _OperationType.ValueType  # 24
    """archive graph"""
    SERIALIZE_GRAPH: _OperationType.ValueType  # 25
    """serialize graph"""
    DESERIALIZE_GRAPH: _OperationType.ValueType  # 26
    """desrialize graph"""
    CONSOLIDATE_COLUMNS: _OperationType.ValueType  # 27
    """consolidate property columns in the graph"""
    SUBGRAPH: _OperationType.ValueType  # 32
    """subgraph in interactive query"""
    DATA_SOURCE: _OperationType.ValueType  # 46
    """loader"""
    DATA_SINK: _OperationType.ValueType  # 47
    CONTEXT_TO_NUMPY: _OperationType.ValueType  # 50
    """data"""
    CONTEXT_TO_DATAFRAME: _OperationType.ValueType  # 51
    TO_VINEYARD_TENSOR: _OperationType.ValueType  # 53
    TO_VINEYARD_DATAFRAME: _OperationType.ValueType  # 54
    ADD_COLUMN: _OperationType.ValueType  # 55
    """return graph, add a property to a kind of vertex."""
    GRAPH_TO_NUMPY: _OperationType.ValueType  # 56
    GRAPH_TO_DATAFRAME: _OperationType.ValueType  # 57
    REGISTER_GRAPH_TYPE: _OperationType.ValueType  # 58
    GET_CONTEXT_DATA: _OperationType.ValueType  # 59
    OUTPUT: _OperationType.ValueType  # 60
    """dump result to fd"""
    FROM_NUMPY: _OperationType.ValueType  # 80
    FROM_DATAFRAME: _OperationType.ValueType  # 81
    FROM_FILE: _OperationType.ValueType  # 82
    GET_ENGINE_CONFIG: _OperationType.ValueType  # 90

class OperationType(_OperationType, metaclass=_OperationTypeEnumTypeWrapper):
    """All possible operation types"""

CREATE_GRAPH: OperationType.ValueType  # 0
"""command
return output_type = graph
"""
BIND_APP: OperationType.ValueType  # 1
"""return app"""
CREATE_APP: OperationType.ValueType  # 2
"""do nothing"""
MODIFY_VERTICES: OperationType.ValueType  # 3
"""return graph"""
MODIFY_EDGES: OperationType.ValueType  # 4
"""return graph"""
RUN_APP: OperationType.ValueType  # 5
"""return result"""
UNLOAD_APP: OperationType.ValueType  # 6
UNLOAD_GRAPH: OperationType.ValueType  # 7
REPARTITION: OperationType.ValueType  # 8
"""return graph"""
TRANSFORM_GRAPH: OperationType.ValueType  # 9
"""return graph or nx_graph"""
REPORT_GRAPH: OperationType.ValueType  # 10
"""return scalar"""
PROJECT_GRAPH: OperationType.ValueType  # 11
"""return graph, general form project"""
PROJECT_TO_SIMPLE: OperationType.ValueType  # 12
"""return graph, specifically project to a simple graph"""
COPY_GRAPH: OperationType.ValueType  # 13
ADD_VERTICES: OperationType.ValueType  # 14
"""not used, leaves room for future development"""
ADD_EDGES: OperationType.ValueType  # 15
"""not used, leaves room for future development"""
ADD_LABELS: OperationType.ValueType  # 16
"""return graph, add new label of vertices or label of edges to existed graph"""
TO_DIRECTED: OperationType.ValueType  # 17
"""return graph, generate directed graph from undirected graph"""
TO_UNDIRECTED: OperationType.ValueType  # 18
"""return graph, generate undirected graph from directed graph"""
CLEAR_EDGES: OperationType.ValueType  # 19
"""clear edges"""
CLEAR_GRAPH: OperationType.ValueType  # 20
"""clear graph"""
VIEW_GRAPH: OperationType.ValueType  # 21
"""create graph view"""
INDUCE_SUBGRAPH: OperationType.ValueType  # 22
"""induce subgraph"""
UNLOAD_CONTEXT: OperationType.ValueType  # 23
"""unload context"""
ARCHIVE_GRAPH: OperationType.ValueType  # 24
"""archive graph"""
SERIALIZE_GRAPH: OperationType.ValueType  # 25
"""serialize graph"""
DESERIALIZE_GRAPH: OperationType.ValueType  # 26
"""desrialize graph"""
CONSOLIDATE_COLUMNS: OperationType.ValueType  # 27
"""consolidate property columns in the graph"""
SUBGRAPH: OperationType.ValueType  # 32
"""subgraph in interactive query"""
DATA_SOURCE: OperationType.ValueType  # 46
"""loader"""
DATA_SINK: OperationType.ValueType  # 47
CONTEXT_TO_NUMPY: OperationType.ValueType  # 50
"""data"""
CONTEXT_TO_DATAFRAME: OperationType.ValueType  # 51
TO_VINEYARD_TENSOR: OperationType.ValueType  # 53
TO_VINEYARD_DATAFRAME: OperationType.ValueType  # 54
ADD_COLUMN: OperationType.ValueType  # 55
"""return graph, add a property to a kind of vertex."""
GRAPH_TO_NUMPY: OperationType.ValueType  # 56
GRAPH_TO_DATAFRAME: OperationType.ValueType  # 57
REGISTER_GRAPH_TYPE: OperationType.ValueType  # 58
GET_CONTEXT_DATA: OperationType.ValueType  # 59
OUTPUT: OperationType.ValueType  # 60
"""dump result to fd"""
FROM_NUMPY: OperationType.ValueType  # 80
FROM_DATAFRAME: OperationType.ValueType  # 81
FROM_FILE: OperationType.ValueType  # 82
GET_ENGINE_CONFIG: OperationType.ValueType  # 90
global___OperationType = OperationType

class _ParamKey:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ParamKeyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ParamKey.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    GRAPH_NAME: _ParamKey.ValueType  # 0
    DST_GRAPH_NAME: _ParamKey.ValueType  # 1
    CONTEXT_KEY: _ParamKey.ValueType  # 2
    GRAPH_TYPE: _ParamKey.ValueType  # 3
    DST_GRAPH_TYPE: _ParamKey.ValueType  # 4
    OID_TYPE: _ParamKey.ValueType  # 5
    VID_TYPE: _ParamKey.ValueType  # 6
    V_DATA_TYPE: _ParamKey.ValueType  # 7
    E_DATA_TYPE: _ParamKey.ValueType  # 8
    V_LABEL_ID: _ParamKey.ValueType  # 9
    E_LABEL_ID: _ParamKey.ValueType  # 10
    V_PROP_ID: _ParamKey.ValueType  # 11
    E_PROP_ID: _ParamKey.ValueType  # 12
    LINE_PARSER: _ParamKey.ValueType  # 13
    E_FILE: _ParamKey.ValueType  # 14
    V_FILE: _ParamKey.ValueType  # 15
    VERTEX_LABEL_NUM: _ParamKey.ValueType  # 16
    EDGE_LABEL_NUM: _ParamKey.ValueType  # 17
    DIRECTED: _ParamKey.ValueType  # 18
    V_PROP_KEY: _ParamKey.ValueType  # 19
    E_PROP_KEY: _ParamKey.ValueType  # 20
    V_DEFAULT_VAL: _ParamKey.ValueType  # 21
    E_DEFAULT_VAL: _ParamKey.ValueType  # 22
    GRAPH_TEMPLATE_CLASS: _ParamKey.ValueType  # 23
    REPARTITION_STRATEGY: _ParamKey.ValueType  # 24
    PARAM: _ParamKey.ValueType  # 26
    DISTRIBUTED: _ParamKey.ValueType  # 27
    SCHEMA_PATH: _ParamKey.ValueType  # 31
    GIE_GREMLIN_QUERY_MESSAGE: _ParamKey.ValueType  # 35
    GIE_GREMLIN_REQUEST_OPTIONS: _ParamKey.ValueType  # 36
    GIE_GREMLIN_FETCH_RESULT_TYPE: _ParamKey.ValueType  # 37
    APP_SIGNATURE: _ParamKey.ValueType  # 40
    GRAPH_SIGNATURE: _ParamKey.ValueType  # 41
    IS_FROM_VINEYARD_ID: _ParamKey.ValueType  # 42
    VINEYARD_ID: _ParamKey.ValueType  # 43
    VINEYARD_NAME: _ParamKey.ValueType  # 44
    VERTEX_MAP_TYPE: _ParamKey.ValueType  # 45
    COMPACT_EDGES: _ParamKey.ValueType  # 46
    USE_PERFECT_HASH: _ParamKey.ValueType  # 47
    CONSOLIDATE_COLUMNS_LABEL: _ParamKey.ValueType  # 48
    CONSOLIDATE_COLUMNS_COLUMNS: _ParamKey.ValueType  # 49
    CONSOLIDATE_COLUMNS_RESULT_COLUMN: _ParamKey.ValueType  # 50
    VERTEX_COLLECTIONS: _ParamKey.ValueType  # 51
    """project"""
    EDGE_COLLECTIONS: _ParamKey.ValueType  # 52
    GLE_HANDLE: _ParamKey.ValueType  # 60
    """learning graph"""
    GLE_CONFIG: _ParamKey.ValueType  # 61
    GLE_GEN_LABELS: _ParamKey.ValueType  # 62
    IS_FROM_GAR: _ParamKey.ValueType  # 70
    """GraphAr"""
    GRAPH_INFO_PATH: _ParamKey.ValueType  # 71
    APP_NAME: _ParamKey.ValueType  # 100
    APP_ALGO: _ParamKey.ValueType  # 101
    APP_LIBRARY_PATH: _ParamKey.ValueType  # 102
    OUTPUT_PREFIX: _ParamKey.ValueType  # 103
    VERTEX_RANGE: _ParamKey.ValueType  # 104
    SELECTOR: _ParamKey.ValueType  # 105
    AXIS: _ParamKey.ValueType  # 106
    GAR: _ParamKey.ValueType  # 107
    TYPE_SIGNATURE: _ParamKey.ValueType  # 108
    CMAKE_EXTRA_OPTIONS: _ParamKey.ValueType  # 109
    REPORT_TYPE: _ParamKey.ValueType  # 200
    MODIFY_TYPE: _ParamKey.ValueType  # 201
    NODE: _ParamKey.ValueType  # 202
    EDGE: _ParamKey.ValueType  # 203
    FID: _ParamKey.ValueType  # 204
    LID: _ParamKey.ValueType  # 205
    EDGE_KEY: _ParamKey.ValueType  # 206
    NODES: _ParamKey.ValueType  # 207
    EDGES: _ParamKey.ValueType  # 208
    COPY_TYPE: _ParamKey.ValueType  # 209
    VIEW_TYPE: _ParamKey.ValueType  # 210
    ARROW_PROPERTY_DEFINITION: _ParamKey.ValueType  # 300
    PROTOCOL: _ParamKey.ValueType  # 301
    VALUES: _ParamKey.ValueType  # 302
    VID: _ParamKey.ValueType  # 303
    SRC_VID: _ParamKey.ValueType  # 304
    DST_VID: _ParamKey.ValueType  # 305
    LABEL: _ParamKey.ValueType  # 306
    SRC_LABEL: _ParamKey.ValueType  # 307
    DST_LABEL: _ParamKey.ValueType  # 308
    PROPERTIES: _ParamKey.ValueType  # 309
    LOADER: _ParamKey.ValueType  # 310
    LOAD_STRATEGY: _ParamKey.ValueType  # 311
    ROW_NUM: _ParamKey.ValueType  # 312
    COLUMN_NUM: _ParamKey.ValueType  # 313
    SUB_LABEL: _ParamKey.ValueType  # 315
    GENERATE_EID: _ParamKey.ValueType  # 316
    DEFAULT_LABEL_ID: _ParamKey.ValueType  # 317
    GID: _ParamKey.ValueType  # 318
    RETAIN_OID: _ParamKey.ValueType  # 319
    STORAGE_OPTIONS: _ParamKey.ValueType  # 321
    READ_OPTIONS: _ParamKey.ValueType  # 322
    FD: _ParamKey.ValueType  # 323
    """file descriptor"""
    SOURCE: _ParamKey.ValueType  # 324
    WRITE_OPTIONS: _ParamKey.ValueType  # 325
    CHUNK_NAME: _ParamKey.ValueType  # 341
    """large attr"""
    CHUNK_TYPE: _ParamKey.ValueType  # 342
    GRAPH_LIBRARY_PATH: _ParamKey.ValueType  # 400
    GRAPH_SERIALIZATION_PATH: _ParamKey.ValueType  # 401
    """serialization path"""
    VFORMAT: _ParamKey.ValueType  # 500
    """vertex input format"""
    EFORMAT: _ParamKey.ValueType  # 501
    """edge input format"""
    JAVA_CLASS_PATH: _ParamKey.ValueType  # 502
    """java class path"""
    JVM_OPTS: _ParamKey.ValueType  # 503
    """opts str to start a jvm"""

class ParamKey(_ParamKey, metaclass=_ParamKeyEnumTypeWrapper):
    """All possible key of the map in AttrValue in attr_value.proto"""

GRAPH_NAME: ParamKey.ValueType  # 0
DST_GRAPH_NAME: ParamKey.ValueType  # 1
CONTEXT_KEY: ParamKey.ValueType  # 2
GRAPH_TYPE: ParamKey.ValueType  # 3
DST_GRAPH_TYPE: ParamKey.ValueType  # 4
OID_TYPE: ParamKey.ValueType  # 5
VID_TYPE: ParamKey.ValueType  # 6
V_DATA_TYPE: ParamKey.ValueType  # 7
E_DATA_TYPE: ParamKey.ValueType  # 8
V_LABEL_ID: ParamKey.ValueType  # 9
E_LABEL_ID: ParamKey.ValueType  # 10
V_PROP_ID: ParamKey.ValueType  # 11
E_PROP_ID: ParamKey.ValueType  # 12
LINE_PARSER: ParamKey.ValueType  # 13
E_FILE: ParamKey.ValueType  # 14
V_FILE: ParamKey.ValueType  # 15
VERTEX_LABEL_NUM: ParamKey.ValueType  # 16
EDGE_LABEL_NUM: ParamKey.ValueType  # 17
DIRECTED: ParamKey.ValueType  # 18
V_PROP_KEY: ParamKey.ValueType  # 19
E_PROP_KEY: ParamKey.ValueType  # 20
V_DEFAULT_VAL: ParamKey.ValueType  # 21
E_DEFAULT_VAL: ParamKey.ValueType  # 22
GRAPH_TEMPLATE_CLASS: ParamKey.ValueType  # 23
REPARTITION_STRATEGY: ParamKey.ValueType  # 24
PARAM: ParamKey.ValueType  # 26
DISTRIBUTED: ParamKey.ValueType  # 27
SCHEMA_PATH: ParamKey.ValueType  # 31
GIE_GREMLIN_QUERY_MESSAGE: ParamKey.ValueType  # 35
GIE_GREMLIN_REQUEST_OPTIONS: ParamKey.ValueType  # 36
GIE_GREMLIN_FETCH_RESULT_TYPE: ParamKey.ValueType  # 37
APP_SIGNATURE: ParamKey.ValueType  # 40
GRAPH_SIGNATURE: ParamKey.ValueType  # 41
IS_FROM_VINEYARD_ID: ParamKey.ValueType  # 42
VINEYARD_ID: ParamKey.ValueType  # 43
VINEYARD_NAME: ParamKey.ValueType  # 44
VERTEX_MAP_TYPE: ParamKey.ValueType  # 45
COMPACT_EDGES: ParamKey.ValueType  # 46
USE_PERFECT_HASH: ParamKey.ValueType  # 47
CONSOLIDATE_COLUMNS_LABEL: ParamKey.ValueType  # 48
CONSOLIDATE_COLUMNS_COLUMNS: ParamKey.ValueType  # 49
CONSOLIDATE_COLUMNS_RESULT_COLUMN: ParamKey.ValueType  # 50
VERTEX_COLLECTIONS: ParamKey.ValueType  # 51
"""project"""
EDGE_COLLECTIONS: ParamKey.ValueType  # 52
GLE_HANDLE: ParamKey.ValueType  # 60
"""learning graph"""
GLE_CONFIG: ParamKey.ValueType  # 61
GLE_GEN_LABELS: ParamKey.ValueType  # 62
IS_FROM_GAR: ParamKey.ValueType  # 70
"""GraphAr"""
GRAPH_INFO_PATH: ParamKey.ValueType  # 71
APP_NAME: ParamKey.ValueType  # 100
APP_ALGO: ParamKey.ValueType  # 101
APP_LIBRARY_PATH: ParamKey.ValueType  # 102
OUTPUT_PREFIX: ParamKey.ValueType  # 103
VERTEX_RANGE: ParamKey.ValueType  # 104
SELECTOR: ParamKey.ValueType  # 105
AXIS: ParamKey.ValueType  # 106
GAR: ParamKey.ValueType  # 107
TYPE_SIGNATURE: ParamKey.ValueType  # 108
CMAKE_EXTRA_OPTIONS: ParamKey.ValueType  # 109
REPORT_TYPE: ParamKey.ValueType  # 200
MODIFY_TYPE: ParamKey.ValueType  # 201
NODE: ParamKey.ValueType  # 202
EDGE: ParamKey.ValueType  # 203
FID: ParamKey.ValueType  # 204
LID: ParamKey.ValueType  # 205
EDGE_KEY: ParamKey.ValueType  # 206
NODES: ParamKey.ValueType  # 207
EDGES: ParamKey.ValueType  # 208
COPY_TYPE: ParamKey.ValueType  # 209
VIEW_TYPE: ParamKey.ValueType  # 210
ARROW_PROPERTY_DEFINITION: ParamKey.ValueType  # 300
PROTOCOL: ParamKey.ValueType  # 301
VALUES: ParamKey.ValueType  # 302
VID: ParamKey.ValueType  # 303
SRC_VID: ParamKey.ValueType  # 304
DST_VID: ParamKey.ValueType  # 305
LABEL: ParamKey.ValueType  # 306
SRC_LABEL: ParamKey.ValueType  # 307
DST_LABEL: ParamKey.ValueType  # 308
PROPERTIES: ParamKey.ValueType  # 309
LOADER: ParamKey.ValueType  # 310
LOAD_STRATEGY: ParamKey.ValueType  # 311
ROW_NUM: ParamKey.ValueType  # 312
COLUMN_NUM: ParamKey.ValueType  # 313
SUB_LABEL: ParamKey.ValueType  # 315
GENERATE_EID: ParamKey.ValueType  # 316
DEFAULT_LABEL_ID: ParamKey.ValueType  # 317
GID: ParamKey.ValueType  # 318
RETAIN_OID: ParamKey.ValueType  # 319
STORAGE_OPTIONS: ParamKey.ValueType  # 321
READ_OPTIONS: ParamKey.ValueType  # 322
FD: ParamKey.ValueType  # 323
"""file descriptor"""
SOURCE: ParamKey.ValueType  # 324
WRITE_OPTIONS: ParamKey.ValueType  # 325
CHUNK_NAME: ParamKey.ValueType  # 341
"""large attr"""
CHUNK_TYPE: ParamKey.ValueType  # 342
GRAPH_LIBRARY_PATH: ParamKey.ValueType  # 400
GRAPH_SERIALIZATION_PATH: ParamKey.ValueType  # 401
"""serialization path"""
VFORMAT: ParamKey.ValueType  # 500
"""vertex input format"""
EFORMAT: ParamKey.ValueType  # 501
"""edge input format"""
JAVA_CLASS_PATH: ParamKey.ValueType  # 502
"""java class path"""
JVM_OPTS: ParamKey.ValueType  # 503
"""opts str to start a jvm"""
global___ParamKey = ParamKey

class _ModifyType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ModifyTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ModifyType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NX_ADD_NODES: _ModifyType.ValueType  # 0
    NX_ADD_EDGES: _ModifyType.ValueType  # 1
    NX_DEL_NODES: _ModifyType.ValueType  # 2
    NX_DEL_EDGES: _ModifyType.ValueType  # 3
    NX_UPDATE_NODES: _ModifyType.ValueType  # 4
    NX_UPDATE_EDGES: _ModifyType.ValueType  # 5

class ModifyType(_ModifyType, metaclass=_ModifyTypeEnumTypeWrapper):
    """For simulating networkx modifing functionalities"""

NX_ADD_NODES: ModifyType.ValueType  # 0
NX_ADD_EDGES: ModifyType.ValueType  # 1
NX_DEL_NODES: ModifyType.ValueType  # 2
NX_DEL_EDGES: ModifyType.ValueType  # 3
NX_UPDATE_NODES: ModifyType.ValueType  # 4
NX_UPDATE_EDGES: ModifyType.ValueType  # 5
global___ModifyType = ModifyType

class _ReportType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ReportTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ReportType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NODE_NUM: _ReportType.ValueType  # 0
    EDGE_NUM: _ReportType.ValueType  # 1
    HAS_NODE: _ReportType.ValueType  # 2
    HAS_EDGE: _ReportType.ValueType  # 3
    NODE_DATA: _ReportType.ValueType  # 4
    EDGE_DATA: _ReportType.ValueType  # 5
    SUCCS_BY_NODE: _ReportType.ValueType  # 6
    PREDS_BY_NODE: _ReportType.ValueType  # 7
    SELFLOOPS_NUM: _ReportType.ValueType  # 8
    NODE_ID_CACHE_BY_GID: _ReportType.ValueType  # 9
    NODE_ATTR_CACHE_BY_GID: _ReportType.ValueType  # 10
    SUCC_BY_GID: _ReportType.ValueType  # 11
    PRED_BY_GID: _ReportType.ValueType  # 12
    SUCC_ATTR_BY_GID: _ReportType.ValueType  # 13
    PRED_ATTR_BY_GID: _ReportType.ValueType  # 14
    SUCC_ATTR_BY_NODE: _ReportType.ValueType  # 15
    PRED_ATTR_BY_NODE: _ReportType.ValueType  # 16

class ReportType(_ReportType, metaclass=_ReportTypeEnumTypeWrapper):
    """For simulating networkx reporting functionalities"""

NODE_NUM: ReportType.ValueType  # 0
EDGE_NUM: ReportType.ValueType  # 1
HAS_NODE: ReportType.ValueType  # 2
HAS_EDGE: ReportType.ValueType  # 3
NODE_DATA: ReportType.ValueType  # 4
EDGE_DATA: ReportType.ValueType  # 5
SUCCS_BY_NODE: ReportType.ValueType  # 6
PREDS_BY_NODE: ReportType.ValueType  # 7
SELFLOOPS_NUM: ReportType.ValueType  # 8
NODE_ID_CACHE_BY_GID: ReportType.ValueType  # 9
NODE_ATTR_CACHE_BY_GID: ReportType.ValueType  # 10
SUCC_BY_GID: ReportType.ValueType  # 11
PRED_BY_GID: ReportType.ValueType  # 12
SUCC_ATTR_BY_GID: ReportType.ValueType  # 13
PRED_ATTR_BY_GID: ReportType.ValueType  # 14
SUCC_ATTR_BY_NODE: ReportType.ValueType  # 15
PRED_ATTR_BY_NODE: ReportType.ValueType  # 16
global___ReportType = ReportType

@typing_extensions.final
class QueryArgs(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ARGS_FIELD_NUMBER: builtins.int
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """pack messages from data_types.proto"""
    def __init__(
        self,
        *,
        args: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args"]) -> None: ...

global___QueryArgs = QueryArgs
