"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import ansys.api.dbu.v0.dbumodels_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetImageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FORMAT_FIELD_NUMBER: builtins.int
    format: ansys.api.dbu.v0.dbumodels_pb2.ImageFormat.ValueType = ...
    """The format of the image being requested."""

    def __init__(self,
        *,
        format : ansys.api.dbu.v0.dbumodels_pb2.ImageFormat.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["format",b"format"]) -> None: ...
global___GetImageRequest = GetImageRequest

class SetViewRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VIEW_FIELD_NUMBER: builtins.int
    view: ansys.api.dbu.v0.dbumodels_pb2.WindowView.ValueType = ...
    """The view operation being requested."""

    def __init__(self,
        *,
        view : ansys.api.dbu.v0.dbumodels_pb2.WindowView.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["view",b"view"]) -> None: ...
global___SetViewRequest = SetViewRequest
