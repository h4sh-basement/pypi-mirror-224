# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ansys/api/dbu/v0/drivingdimensions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ansys.api.dbu.v0 import dbumodels_pb2 as ansys_dot_api_dot_dbu_dot_v0_dot_dbumodels__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(ansys/api/dbu/v0/drivingdimensions.proto\x12\"ansys.api.dbu.v0.drivingdimensions\x1a ansys/api/dbu/v0/dbumodels.proto\"\x1f\n\rGetAllRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\"P\n\x0eGetAllResponse\x12>\n\x12\x64riving_dimensions\x18\x01 \x03(\x0b\x32\".ansys.api.dbu.v0.DrivingDimension\"N\n\rUpdateRequest\x12=\n\x11\x64riving_dimension\x18\x01 \x01(\x0b\x32\".ansys.api.dbu.v0.DrivingDimension2\xb4\x02\n\x11\x44rivingDimensions\x12M\n\x03Get\x12\".ansys.api.dbu.v0.EntityIdentifier\x1a\".ansys.api.dbu.v0.DrivingDimension\x12o\n\x06GetAll\x12\x31.ansys.api.dbu.v0.drivingdimensions.GetAllRequest\x1a\x32.ansys.api.dbu.v0.drivingdimensions.GetAllResponse\x12_\n\x06Update\x12\x31.ansys.api.dbu.v0.drivingdimensions.UpdateRequest\x1a\".ansys.api.dbu.v0.DrivingDimensionB%\xaa\x02\"Ansys.Api.Dbu.V0.DrivingDimensionsb\x06proto3')



_GETALLREQUEST = DESCRIPTOR.message_types_by_name['GetAllRequest']
_GETALLRESPONSE = DESCRIPTOR.message_types_by_name['GetAllResponse']
_UPDATEREQUEST = DESCRIPTOR.message_types_by_name['UpdateRequest']
GetAllRequest = _reflection.GeneratedProtocolMessageType('GetAllRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETALLREQUEST,
  '__module__' : 'ansys.api.dbu.v0.drivingdimensions_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.dbu.v0.drivingdimensions.GetAllRequest)
  })
_sym_db.RegisterMessage(GetAllRequest)

GetAllResponse = _reflection.GeneratedProtocolMessageType('GetAllResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETALLRESPONSE,
  '__module__' : 'ansys.api.dbu.v0.drivingdimensions_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.dbu.v0.drivingdimensions.GetAllResponse)
  })
_sym_db.RegisterMessage(GetAllResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'ansys.api.dbu.v0.drivingdimensions_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.dbu.v0.drivingdimensions.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

_DRIVINGDIMENSIONS = DESCRIPTOR.services_by_name['DrivingDimensions']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\"Ansys.Api.Dbu.V0.DrivingDimensions'
  _GETALLREQUEST._serialized_start=114
  _GETALLREQUEST._serialized_end=145
  _GETALLRESPONSE._serialized_start=147
  _GETALLRESPONSE._serialized_end=227
  _UPDATEREQUEST._serialized_start=229
  _UPDATEREQUEST._serialized_end=307
  _DRIVINGDIMENSIONS._serialized_start=310
  _DRIVINGDIMENSIONS._serialized_end=618
# @@protoc_insertion_point(module_scope)
