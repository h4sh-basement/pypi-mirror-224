# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/helpdesk/ticket.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.ecm import content_pb2 as eolymp_dot_ecm_dot_content__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x65olymp/helpdesk/ticket.proto\x12\x0f\x65olymp.helpdesk\x1a\x18\x65olymp/ecm/content.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x87\x07\n\x06Ticket\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x04type\x18\x02 \x01(\x0e\x32\x1c.eolymp.helpdesk.Ticket.Type\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x12\n\nuser_email\x18\x04 \x01(\t\x12\x37\n\x08metadata\x18\x05 \x03(\x0b\x32%.eolymp.helpdesk.Ticket.MetadataEntry\x12.\n\x06status\x18\x06 \x01(\x0e\x32\x1e.eolymp.helpdesk.Ticket.Status\x12\x0e\n\x06locale\x18\t \x01(\t\x12.\n\ncreated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06secret\x18\x0c \x01(\t\x12\x0f\n\x07subject\x18\x14 \x01(\t\x12$\n\x07message\x18\x32 \x01(\x0b\x32\x13.eolymp.ecm.Content\x1a\xb2\x02\n\x07\x43omment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x12\n\nuser_email\x18\x04 \x01(\t\x12?\n\x08metadata\x18\x05 \x03(\x0b\x32-.eolymp.helpdesk.Ticket.Comment.MetadataEntry\x12.\n\ncreated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12$\n\x07message\x18\x32 \x01(\x0b\x32\x13.eolymp.ecm.Content\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"@\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08QUESTION\x10\x01\x12\x12\n\x0eQUOTA_INCREASE\x10\x02\x12\x0c\n\x08\x46\x45\x45\x44\x42\x41\x43K\x10\x03\"X\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08\x41WAITING\x10\x02\x12\n\n\x06\x43LOSED\x10\x03\x12\x0c\n\x08\x41PPROVED\x10\x04\x12\x0c\n\x08REJECTED\x10\x05\x42\x33Z1github.com/eolymp/go-sdk/eolymp/helpdesk;helpdeskb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.helpdesk.ticket_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/eolymp/go-sdk/eolymp/helpdesk;helpdesk'
  _TICKET_COMMENT_METADATAENTRY._options = None
  _TICKET_COMMENT_METADATAENTRY._serialized_options = b'8\001'
  _TICKET_METADATAENTRY._options = None
  _TICKET_METADATAENTRY._serialized_options = b'8\001'
  _TICKET._serialized_start=109
  _TICKET._serialized_end=1012
  _TICKET_COMMENT._serialized_start=501
  _TICKET_COMMENT._serialized_end=807
  _TICKET_COMMENT_METADATAENTRY._serialized_start=760
  _TICKET_COMMENT_METADATAENTRY._serialized_end=807
  _TICKET_METADATAENTRY._serialized_start=760
  _TICKET_METADATAENTRY._serialized_end=807
  _TICKET_TYPE._serialized_start=858
  _TICKET_TYPE._serialized_end=922
  _TICKET_STATUS._serialized_start=924
  _TICKET_STATUS._serialized_end=1012
# @@protoc_insertion_point(module_scope)
