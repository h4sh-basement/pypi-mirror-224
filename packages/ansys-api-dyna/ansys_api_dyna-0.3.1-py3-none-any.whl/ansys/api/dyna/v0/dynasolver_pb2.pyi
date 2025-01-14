"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class DynaSolverRelay(google.protobuf.message.Message):
    """The request packet, and also the reply packet, for most
    communications that get passed to DYNA
    There does not seem to be a 32 bit or 64 bit float in grpc,
    just 'float' and 'double', so I hope these work OK
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TAG_FIELD_NUMBER: builtins.int
    I8_FIELD_NUMBER: builtins.int
    R8_FIELD_NUMBER: builtins.int
    I4_FIELD_NUMBER: builtins.int
    R4_FIELD_NUMBER: builtins.int
    B_FIELD_NUMBER: builtins.int
    tag: builtins.int = ...
    @property
    def i8(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def r8(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def i4(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def r4(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    b: builtins.bytes = ...
    def __init__(self,
        *,
        tag : builtins.int = ...,
        i8 : typing.Optional[typing.Iterable[builtins.int]] = ...,
        r8 : typing.Optional[typing.Iterable[builtins.float]] = ...,
        i4 : typing.Optional[typing.Iterable[builtins.int]] = ...,
        r4 : typing.Optional[typing.Iterable[builtins.float]] = ...,
        b : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["b",b"b","i4",b"i4","i8",b"i8","r4",b"r4","r8",b"r8","tag",b"tag"]) -> None: ...
global___DynaSolverRelay = DynaSolverRelay

class LogLevel(google.protobuf.message.Message):
    """Set logging level on the server"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LEVEL_FIELD_NUMBER: builtins.int
    level: builtins.bytes = ...
    def __init__(self,
        *,
        level : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["level",b"level"]) -> None: ...
global___LogLevel = LogLevel

class QuitServer(google.protobuf.message.Message):
    """No data needed"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___QuitServer = QuitServer

class DynaSolverFileData(google.protobuf.message.Message):
    """Sent or returned byte stream for file contents"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    B_FIELD_NUMBER: builtins.int
    b: builtins.bytes = ...
    def __init__(self,
        *,
        b : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["b",b"b"]) -> None: ...
global___DynaSolverFileData = DynaSolverFileData

class DynaSolverStart(google.protobuf.message.Message):
    """Command to start DYNA executable on the given number of cores"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXENAME_FIELD_NUMBER: builtins.int
    NPROC_FIELD_NUMBER: builtins.int
    exename: builtins.bytes = ...
    nproc: builtins.int = ...
    def __init__(self,
        *,
        exename : builtins.bytes = ...,
        nproc : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["exename",b"exename","nproc",b"nproc"]) -> None: ...
global___DynaSolverStart = DynaSolverStart

class DynaSolverFileRequest(google.protobuf.message.Message):
    """File name to download, or optional filter text for list_files"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.bytes = ...
    def __init__(self,
        *,
        name : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DynaSolverFileRequest = DynaSolverFileRequest

class DynaSolverTailRequest(google.protobuf.message.Message):
    """Which file to monitor/return: 1=stdout, 2=stderr"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WHICH_FIELD_NUMBER: builtins.int
    which: builtins.int = ...
    def __init__(self,
        *,
        which : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["which",b"which"]) -> None: ...
global___DynaSolverTailRequest = DynaSolverTailRequest

class DynaSolverStatus(google.protobuf.message.Message):
    """Command status flag, for commands that don't return other content"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int
    status: builtins.int = ...
    def __init__(self,
        *,
        status : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["status",b"status"]) -> None: ...
global___DynaSolverStatus = DynaSolverStatus

class DynaSolverFileList(google.protobuf.message.Message):
    """Directory listing information"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    @property
    def name(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    @property
    def size(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        name : typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        size : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","size",b"size"]) -> None: ...
global___DynaSolverFileList = DynaSolverFileList
