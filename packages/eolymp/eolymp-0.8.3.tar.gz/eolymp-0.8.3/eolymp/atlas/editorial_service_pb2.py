# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/atlas/editorial_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.atlas import editorial_pb2 as eolymp_dot_atlas_dot_editorial__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$eolymp/atlas/editorial_service.proto\x12\x0c\x65olymp.atlas\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\x1c\x65olymp/atlas/editorial.proto\"6\n\x13ListEditorialsInput\x12\x0e\n\x06render\x18\x01 \x01(\x08\x12\x0f\n\x07version\x18\x64 \x01(\r\"M\n\x14ListEditorialsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.eolymp.atlas.Editorial\"O\n\x16\x44\x65scribeEditorialInput\x12\x14\n\x0c\x65\x64itorial_id\x18\x02 \x01(\t\x12\x0e\n\x06render\x18\x03 \x01(\x08\x12\x0f\n\x07version\x18\x64 \x01(\r\"E\n\x17\x44\x65scribeEditorialOutput\x12*\n\teditorial\x18\x01 \x01(\x0b\x32\x17.eolymp.atlas.Editorial\"G\n\x14LookupEditorialInput\x12\x0e\n\x06locale\x18\x02 \x01(\t\x12\x0e\n\x06render\x18\x03 \x01(\x08\x12\x0f\n\x07version\x18\x64 \x01(\r\"C\n\x15LookupEditorialOutput\x12*\n\teditorial\x18\x01 \x01(\x0b\x32\x17.eolymp.atlas.Editorial\"C\n\x15PreviewEditorialInput\x12*\n\teditorial\x18\x02 \x01(\x0b\x32\x17.eolymp.atlas.Editorial\"D\n\x16PreviewEditorialOutput\x12*\n\teditorial\x18\x01 \x01(\x0b\x32\x17.eolymp.atlas.Editorial\"B\n\x14\x43reateEditorialInput\x12*\n\teditorial\x18\x02 \x01(\x0b\x32\x17.eolymp.atlas.Editorial\"-\n\x15\x43reateEditorialOutput\x12\x14\n\x0c\x65\x64itorial_id\x18\x01 \x01(\t\"X\n\x14UpdateEditorialInput\x12\x14\n\x0c\x65\x64itorial_id\x18\x02 \x01(\t\x12*\n\teditorial\x18\x03 \x01(\x0b\x32\x17.eolymp.atlas.Editorial\"\x17\n\x15UpdateEditorialOutput\",\n\x14\x44\x65leteEditorialInput\x12\x14\n\x0c\x65\x64itorial_id\x18\x02 \x01(\t\"\x17\n\x15\x44\x65leteEditorialOutput2\x8b\t\n\x10\x45\x64itorialService\x12\x99\x01\n\x0f\x43reateEditorial\x12\".eolymp.atlas.CreateEditorialInput\x1a#.eolymp.atlas.CreateEditorialOutput\"=\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\r\x1a\x0b/editorials\x12\xa8\x01\n\x0fUpdateEditorial\x12\".eolymp.atlas.UpdateEditorialInput\x1a#.eolymp.atlas.UpdateEditorialOutput\"L\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/editorials/{editorial_id}\x12\xa8\x01\n\x0f\x44\x65leteEditorial\x12\".eolymp.atlas.DeleteEditorialInput\x1a#.eolymp.atlas.DeleteEditorialOutput\"L\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x1c*\x1a/editorials/{editorial_id}\x12\xad\x01\n\x11\x44\x65scribeEditorial\x12$.eolymp.atlas.DescribeEditorialInput\x1a%.eolymp.atlas.DescribeEditorialOutput\"K\x82\xe3\n\x16\x8a\xe3\n\x12\x61tlas:problem:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x1c\x12\x1a/editorials/{editorial_id}\x12\x97\x01\n\x0fLookupEditorial\x12\".eolymp.atlas.LookupEditorialInput\x1a#.eolymp.atlas.LookupEditorialOutput\";\x82\xe3\n\x16\x8a\xe3\n\x12\x61tlas:problem:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x0c\x12\n/editorial\x12\xa2\x01\n\x10PreviewEditorial\x12#.eolymp.atlas.PreviewEditorialInput\x1a$.eolymp.atlas.PreviewEditorialOutput\"C\x82\xe3\n\x16\x8a\xe3\n\x12\x61tlas:problem:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x14\"\x12/editorial/preview\x12\x95\x01\n\x0eListEditorials\x12!.eolymp.atlas.ListEditorialsInput\x1a\".eolymp.atlas.ListEditorialsOutput\"<\x82\xe3\n\x16\x8a\xe3\n\x12\x61tlas:problem:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\r\x12\x0b/editorialsB-Z+github.com/eolymp/go-sdk/eolymp/atlas;atlasb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.atlas.editorial_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/atlas;atlas'
  _EDITORIALSERVICE.methods_by_name['CreateEditorial']._options = None
  _EDITORIALSERVICE.methods_by_name['CreateEditorial']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\r\032\013/editorials'
  _EDITORIALSERVICE.methods_by_name['UpdateEditorial']._options = None
  _EDITORIALSERVICE.methods_by_name['UpdateEditorial']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\034\032\032/editorials/{editorial_id}'
  _EDITORIALSERVICE.methods_by_name['DeleteEditorial']._options = None
  _EDITORIALSERVICE.methods_by_name['DeleteEditorial']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\034*\032/editorials/{editorial_id}'
  _EDITORIALSERVICE.methods_by_name['DescribeEditorial']._options = None
  _EDITORIALSERVICE.methods_by_name['DescribeEditorial']._serialized_options = b'\202\343\n\026\212\343\n\022atlas:problem:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\034\022\032/editorials/{editorial_id}'
  _EDITORIALSERVICE.methods_by_name['LookupEditorial']._options = None
  _EDITORIALSERVICE.methods_by_name['LookupEditorial']._serialized_options = b'\202\343\n\026\212\343\n\022atlas:problem:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\014\022\n/editorial'
  _EDITORIALSERVICE.methods_by_name['PreviewEditorial']._options = None
  _EDITORIALSERVICE.methods_by_name['PreviewEditorial']._serialized_options = b'\202\343\n\026\212\343\n\022atlas:problem:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\024\"\022/editorial/preview'
  _EDITORIALSERVICE.methods_by_name['ListEditorials']._options = None
  _EDITORIALSERVICE.methods_by_name['ListEditorials']._serialized_options = b'\202\343\n\026\212\343\n\022atlas:problem:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\r\022\013/editorials'
  _LISTEDITORIALSINPUT._serialized_start=183
  _LISTEDITORIALSINPUT._serialized_end=237
  _LISTEDITORIALSOUTPUT._serialized_start=239
  _LISTEDITORIALSOUTPUT._serialized_end=316
  _DESCRIBEEDITORIALINPUT._serialized_start=318
  _DESCRIBEEDITORIALINPUT._serialized_end=397
  _DESCRIBEEDITORIALOUTPUT._serialized_start=399
  _DESCRIBEEDITORIALOUTPUT._serialized_end=468
  _LOOKUPEDITORIALINPUT._serialized_start=470
  _LOOKUPEDITORIALINPUT._serialized_end=541
  _LOOKUPEDITORIALOUTPUT._serialized_start=543
  _LOOKUPEDITORIALOUTPUT._serialized_end=610
  _PREVIEWEDITORIALINPUT._serialized_start=612
  _PREVIEWEDITORIALINPUT._serialized_end=679
  _PREVIEWEDITORIALOUTPUT._serialized_start=681
  _PREVIEWEDITORIALOUTPUT._serialized_end=749
  _CREATEEDITORIALINPUT._serialized_start=751
  _CREATEEDITORIALINPUT._serialized_end=817
  _CREATEEDITORIALOUTPUT._serialized_start=819
  _CREATEEDITORIALOUTPUT._serialized_end=864
  _UPDATEEDITORIALINPUT._serialized_start=866
  _UPDATEEDITORIALINPUT._serialized_end=954
  _UPDATEEDITORIALOUTPUT._serialized_start=956
  _UPDATEEDITORIALOUTPUT._serialized_end=979
  _DELETEEDITORIALINPUT._serialized_start=981
  _DELETEEDITORIALINPUT._serialized_end=1025
  _DELETEEDITORIALOUTPUT._serialized_start=1027
  _DELETEEDITORIALOUTPUT._serialized_end=1050
  _EDITORIALSERVICE._serialized_start=1053
  _EDITORIALSERVICE._serialized_end=2216
# @@protoc_insertion_point(module_scope)
