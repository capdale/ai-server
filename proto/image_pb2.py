# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11proto/image.proto\x12\x05image\"\'\n\x16ImageClassifierRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\":\n\x14ImageClassifierReply\x12\r\n\x05state\x18\x01 \x01(\x03\x12\x13\n\x0b\x63lass_index\x18\x02 \x01(\x03\x32\\\n\rImageClassify\x12K\n\rClassifyImage\x12\x1d.image.ImageClassifierRequest\x1a\x1b.image.ImageClassifierReplyB!Z\x1fgithub.com/capdale/rpc-protocolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.image_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\037github.com/capdale/rpc-protocol'
  _globals['_IMAGECLASSIFIERREQUEST']._serialized_start=28
  _globals['_IMAGECLASSIFIERREQUEST']._serialized_end=67
  _globals['_IMAGECLASSIFIERREPLY']._serialized_start=69
  _globals['_IMAGECLASSIFIERREPLY']._serialized_end=127
  _globals['_IMAGECLASSIFY']._serialized_start=129
  _globals['_IMAGECLASSIFY']._serialized_end=221
# @@protoc_insertion_point(module_scope)
