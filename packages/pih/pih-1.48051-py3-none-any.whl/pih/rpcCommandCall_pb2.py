# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpcCommandCall.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14rpcCommandCall.proto\x12\x05unary\".\n\nrpcCommand\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nparameters\x18\x02 \x01(\t\" \n\x10rpcCommandResult\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t2G\n\x05Unary\x12>\n\x0erpcCallCommand\x12\x11.unary.rpcCommand\x1a\x17.unary.rpcCommandResult\"\x00\x62\x06proto3')



_RPCCOMMAND = DESCRIPTOR.message_types_by_name['rpcCommand']
_RPCCOMMANDRESULT = DESCRIPTOR.message_types_by_name['rpcCommandResult']
rpcCommand = _reflection.GeneratedProtocolMessageType('rpcCommand', (_message.Message,), {
  'DESCRIPTOR' : _RPCCOMMAND,
  '__module__' : 'rpcCommandCall_pb2'
  # @@protoc_insertion_point(class_scope:unary.rpcCommand)
  })
_sym_db.RegisterMessage(rpcCommand)

rpcCommandResult = _reflection.GeneratedProtocolMessageType('rpcCommandResult', (_message.Message,), {
  'DESCRIPTOR' : _RPCCOMMANDRESULT,
  '__module__' : 'rpcCommandCall_pb2'
  # @@protoc_insertion_point(class_scope:unary.rpcCommandResult)
  })
_sym_db.RegisterMessage(rpcCommandResult)

_UNARY = DESCRIPTOR.services_by_name['Unary']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RPCCOMMAND._serialized_start=31
  _RPCCOMMAND._serialized_end=77
  _RPCCOMMANDRESULT._serialized_start=79
  _RPCCOMMANDRESULT._serialized_end=111
  _UNARY._serialized_start=113
  _UNARY._serialized_end=184
# @@protoc_insertion_point(module_scope)
