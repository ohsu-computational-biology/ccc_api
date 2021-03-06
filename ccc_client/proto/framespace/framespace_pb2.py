# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/framespace/framespace.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/framespace/framespace.proto',
  package='framespace',
  syntax='proto3',
  serialized_pb=_b('\n!proto/framespace/framespace.proto\x12\nframespace\x1a\x1cgoogle/protobuf/struct.proto\")\n\x04\x41xis\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"I\n\x11SearchAxesRequest\x12\r\n\x05names\x18\x01 \x03(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"M\n\x12SearchAxesResponse\x12\x1e\n\x04\x61xes\x18\x01 \x03(\x0b\x32\x10.framespace.Axis\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xac\x01\n\x08KeySpace\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\taxis_name\x18\x03 \x01(\t\x12\x0c\n\x04keys\x18\x04 \x03(\t\x12\x34\n\x08metadata\x18\x05 \x03(\x0b\x32\".framespace.KeySpace.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x86\x01\n\x16SearchKeySpacesRequest\x12\x14\n\x0ckeyspace_ids\x18\x01 \x03(\t\x12\r\n\x05names\x18\x02 \x03(\t\x12\x12\n\naxis_names\x18\x03 \x03(\t\x12\x0c\n\x04keys\x18\x04 \x03(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\"[\n\x17SearchKeySpacesResponse\x12\'\n\tkeyspaces\x18\x01 \x03(\x0b\x32\x14.framespace.KeySpace\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\".\n\tDimension\x12\x13\n\x0bkeyspace_id\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\t\"5\n\x04Unit\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"W\n\x12SearchUnitsRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x12\r\n\x05names\x18\x02 \x03(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\"O\n\x13SearchUnitsResponse\x12\x1f\n\x05units\x18\x01 \x03(\x0b\x32\x10.framespace.Unit\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xed\x02\n\tDataFrame\x12\n\n\x02id\x18\x01 \x01(\t\x12$\n\x05major\x18\x02 \x01(\x0b\x32\x15.framespace.Dimension\x12$\n\x05minor\x18\x03 \x01(\x0b\x32\x15.framespace.Dimension\x12\x1f\n\x05units\x18\x04 \x03(\x0b\x32\x10.framespace.Unit\x12\x35\n\x08metadata\x18\x05 \x03(\x0b\x32#.framespace.DataFrame.MetadataEntry\x12\x35\n\x08\x63ontents\x18\x06 \x03(\x0b\x32#.framespace.DataFrame.ContentsEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aH\n\rContentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct:\x02\x38\x01\"\x7f\n\x17SearchDataFramesRequest\x12\x15\n\rdataframe_ids\x18\x01 \x03(\t\x12\x14\n\x0ckeyspace_ids\x18\x02 \x03(\t\x12\x10\n\x08unit_ids\x18\x03 \x03(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"^\n\x18SearchDataFramesResponse\x12)\n\ndataframes\x18\x01 \x03(\x0b\x32\x15.framespace.DataFrame\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa7\x01\n\x15SliceDataFrameRequest\x12\x14\n\x0c\x64\x61taframe_id\x18\x01 \x01(\t\x12(\n\tnew_major\x18\x02 \x01(\x0b\x32\x15.framespace.Dimension\x12(\n\tnew_minor\x18\x03 \x01(\x0b\x32\x15.framespace.Dimension\x12\x12\n\npage_start\x18\x04 \x01(\x05\x12\x10\n\x08page_end\x18\x05 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AXIS = _descriptor.Descriptor(
  name='Axis',
  full_name='framespace.Axis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='framespace.Axis.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='framespace.Axis.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=120,
)


_SEARCHAXESREQUEST = _descriptor.Descriptor(
  name='SearchAxesRequest',
  full_name='framespace.SearchAxesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='framespace.SearchAxesRequest.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='framespace.SearchAxesRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='framespace.SearchAxesRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=195,
)


_SEARCHAXESRESPONSE = _descriptor.Descriptor(
  name='SearchAxesResponse',
  full_name='framespace.SearchAxesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='axes', full_name='framespace.SearchAxesResponse.axes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='framespace.SearchAxesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=274,
)


_KEYSPACE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='framespace.KeySpace.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='framespace.KeySpace.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='framespace.KeySpace.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=449,
)

_KEYSPACE = _descriptor.Descriptor(
  name='KeySpace',
  full_name='framespace.KeySpace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='framespace.KeySpace.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='framespace.KeySpace.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='axis_name', full_name='framespace.KeySpace.axis_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keys', full_name='framespace.KeySpace.keys', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='framespace.KeySpace.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_KEYSPACE_METADATAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=449,
)


_SEARCHKEYSPACESREQUEST = _descriptor.Descriptor(
  name='SearchKeySpacesRequest',
  full_name='framespace.SearchKeySpacesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyspace_ids', full_name='framespace.SearchKeySpacesRequest.keyspace_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='names', full_name='framespace.SearchKeySpacesRequest.names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='axis_names', full_name='framespace.SearchKeySpacesRequest.axis_names', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keys', full_name='framespace.SearchKeySpacesRequest.keys', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='framespace.SearchKeySpacesRequest.page_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='framespace.SearchKeySpacesRequest.page_token', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=586,
)


_SEARCHKEYSPACESRESPONSE = _descriptor.Descriptor(
  name='SearchKeySpacesResponse',
  full_name='framespace.SearchKeySpacesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyspaces', full_name='framespace.SearchKeySpacesResponse.keyspaces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='framespace.SearchKeySpacesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=679,
)


_DIMENSION = _descriptor.Descriptor(
  name='Dimension',
  full_name='framespace.Dimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyspace_id', full_name='framespace.Dimension.keyspace_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keys', full_name='framespace.Dimension.keys', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=681,
  serialized_end=727,
)


_UNIT = _descriptor.Descriptor(
  name='Unit',
  full_name='framespace.Unit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='framespace.Unit.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='framespace.Unit.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='framespace.Unit.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=782,
)


_SEARCHUNITSREQUEST = _descriptor.Descriptor(
  name='SearchUnitsRequest',
  full_name='framespace.SearchUnitsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='framespace.SearchUnitsRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='names', full_name='framespace.SearchUnitsRequest.names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='framespace.SearchUnitsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='framespace.SearchUnitsRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=784,
  serialized_end=871,
)


_SEARCHUNITSRESPONSE = _descriptor.Descriptor(
  name='SearchUnitsResponse',
  full_name='framespace.SearchUnitsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='units', full_name='framespace.SearchUnitsResponse.units', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='framespace.SearchUnitsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=873,
  serialized_end=952,
)


_DATAFRAME_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='framespace.DataFrame.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='framespace.DataFrame.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='framespace.DataFrame.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=449,
)

_DATAFRAME_CONTENTSENTRY = _descriptor.Descriptor(
  name='ContentsEntry',
  full_name='framespace.DataFrame.ContentsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='framespace.DataFrame.ContentsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='framespace.DataFrame.ContentsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1248,
  serialized_end=1320,
)

_DATAFRAME = _descriptor.Descriptor(
  name='DataFrame',
  full_name='framespace.DataFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='framespace.DataFrame.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='major', full_name='framespace.DataFrame.major', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minor', full_name='framespace.DataFrame.minor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='units', full_name='framespace.DataFrame.units', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='framespace.DataFrame.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contents', full_name='framespace.DataFrame.contents', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DATAFRAME_METADATAENTRY, _DATAFRAME_CONTENTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=955,
  serialized_end=1320,
)


_SEARCHDATAFRAMESREQUEST = _descriptor.Descriptor(
  name='SearchDataFramesRequest',
  full_name='framespace.SearchDataFramesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataframe_ids', full_name='framespace.SearchDataFramesRequest.dataframe_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyspace_ids', full_name='framespace.SearchDataFramesRequest.keyspace_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_ids', full_name='framespace.SearchDataFramesRequest.unit_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='framespace.SearchDataFramesRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='framespace.SearchDataFramesRequest.page_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1322,
  serialized_end=1449,
)


_SEARCHDATAFRAMESRESPONSE = _descriptor.Descriptor(
  name='SearchDataFramesResponse',
  full_name='framespace.SearchDataFramesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataframes', full_name='framespace.SearchDataFramesResponse.dataframes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='framespace.SearchDataFramesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1451,
  serialized_end=1545,
)


_SLICEDATAFRAMEREQUEST = _descriptor.Descriptor(
  name='SliceDataFrameRequest',
  full_name='framespace.SliceDataFrameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataframe_id', full_name='framespace.SliceDataFrameRequest.dataframe_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_major', full_name='framespace.SliceDataFrameRequest.new_major', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_minor', full_name='framespace.SliceDataFrameRequest.new_minor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_start', full_name='framespace.SliceDataFrameRequest.page_start', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_end', full_name='framespace.SliceDataFrameRequest.page_end', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1548,
  serialized_end=1715,
)

_SEARCHAXESRESPONSE.fields_by_name['axes'].message_type = _AXIS
_KEYSPACE_METADATAENTRY.containing_type = _KEYSPACE
_KEYSPACE.fields_by_name['metadata'].message_type = _KEYSPACE_METADATAENTRY
_SEARCHKEYSPACESRESPONSE.fields_by_name['keyspaces'].message_type = _KEYSPACE
_SEARCHUNITSRESPONSE.fields_by_name['units'].message_type = _UNIT
_DATAFRAME_METADATAENTRY.containing_type = _DATAFRAME
_DATAFRAME_CONTENTSENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_DATAFRAME_CONTENTSENTRY.containing_type = _DATAFRAME
_DATAFRAME.fields_by_name['major'].message_type = _DIMENSION
_DATAFRAME.fields_by_name['minor'].message_type = _DIMENSION
_DATAFRAME.fields_by_name['units'].message_type = _UNIT
_DATAFRAME.fields_by_name['metadata'].message_type = _DATAFRAME_METADATAENTRY
_DATAFRAME.fields_by_name['contents'].message_type = _DATAFRAME_CONTENTSENTRY
_SEARCHDATAFRAMESRESPONSE.fields_by_name['dataframes'].message_type = _DATAFRAME
_SLICEDATAFRAMEREQUEST.fields_by_name['new_major'].message_type = _DIMENSION
_SLICEDATAFRAMEREQUEST.fields_by_name['new_minor'].message_type = _DIMENSION
DESCRIPTOR.message_types_by_name['Axis'] = _AXIS
DESCRIPTOR.message_types_by_name['SearchAxesRequest'] = _SEARCHAXESREQUEST
DESCRIPTOR.message_types_by_name['SearchAxesResponse'] = _SEARCHAXESRESPONSE
DESCRIPTOR.message_types_by_name['KeySpace'] = _KEYSPACE
DESCRIPTOR.message_types_by_name['SearchKeySpacesRequest'] = _SEARCHKEYSPACESREQUEST
DESCRIPTOR.message_types_by_name['SearchKeySpacesResponse'] = _SEARCHKEYSPACESRESPONSE
DESCRIPTOR.message_types_by_name['Dimension'] = _DIMENSION
DESCRIPTOR.message_types_by_name['Unit'] = _UNIT
DESCRIPTOR.message_types_by_name['SearchUnitsRequest'] = _SEARCHUNITSREQUEST
DESCRIPTOR.message_types_by_name['SearchUnitsResponse'] = _SEARCHUNITSRESPONSE
DESCRIPTOR.message_types_by_name['DataFrame'] = _DATAFRAME
DESCRIPTOR.message_types_by_name['SearchDataFramesRequest'] = _SEARCHDATAFRAMESREQUEST
DESCRIPTOR.message_types_by_name['SearchDataFramesResponse'] = _SEARCHDATAFRAMESRESPONSE
DESCRIPTOR.message_types_by_name['SliceDataFrameRequest'] = _SLICEDATAFRAMEREQUEST

Axis = _reflection.GeneratedProtocolMessageType('Axis', (_message.Message,), dict(
  DESCRIPTOR = _AXIS,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.Axis)
  ))
_sym_db.RegisterMessage(Axis)

SearchAxesRequest = _reflection.GeneratedProtocolMessageType('SearchAxesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHAXESREQUEST,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchAxesRequest)
  ))
_sym_db.RegisterMessage(SearchAxesRequest)

SearchAxesResponse = _reflection.GeneratedProtocolMessageType('SearchAxesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHAXESRESPONSE,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchAxesResponse)
  ))
_sym_db.RegisterMessage(SearchAxesResponse)

KeySpace = _reflection.GeneratedProtocolMessageType('KeySpace', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _KEYSPACE_METADATAENTRY,
    __module__ = 'proto.framespace.framespace_pb2'
    # @@protoc_insertion_point(class_scope:framespace.KeySpace.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _KEYSPACE,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.KeySpace)
  ))
_sym_db.RegisterMessage(KeySpace)
_sym_db.RegisterMessage(KeySpace.MetadataEntry)

SearchKeySpacesRequest = _reflection.GeneratedProtocolMessageType('SearchKeySpacesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHKEYSPACESREQUEST,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchKeySpacesRequest)
  ))
_sym_db.RegisterMessage(SearchKeySpacesRequest)

SearchKeySpacesResponse = _reflection.GeneratedProtocolMessageType('SearchKeySpacesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHKEYSPACESRESPONSE,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchKeySpacesResponse)
  ))
_sym_db.RegisterMessage(SearchKeySpacesResponse)

Dimension = _reflection.GeneratedProtocolMessageType('Dimension', (_message.Message,), dict(
  DESCRIPTOR = _DIMENSION,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.Dimension)
  ))
_sym_db.RegisterMessage(Dimension)

Unit = _reflection.GeneratedProtocolMessageType('Unit', (_message.Message,), dict(
  DESCRIPTOR = _UNIT,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.Unit)
  ))
_sym_db.RegisterMessage(Unit)

SearchUnitsRequest = _reflection.GeneratedProtocolMessageType('SearchUnitsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHUNITSREQUEST,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchUnitsRequest)
  ))
_sym_db.RegisterMessage(SearchUnitsRequest)

SearchUnitsResponse = _reflection.GeneratedProtocolMessageType('SearchUnitsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHUNITSRESPONSE,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchUnitsResponse)
  ))
_sym_db.RegisterMessage(SearchUnitsResponse)

DataFrame = _reflection.GeneratedProtocolMessageType('DataFrame', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATAFRAME_METADATAENTRY,
    __module__ = 'proto.framespace.framespace_pb2'
    # @@protoc_insertion_point(class_scope:framespace.DataFrame.MetadataEntry)
    ))
  ,

  ContentsEntry = _reflection.GeneratedProtocolMessageType('ContentsEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATAFRAME_CONTENTSENTRY,
    __module__ = 'proto.framespace.framespace_pb2'
    # @@protoc_insertion_point(class_scope:framespace.DataFrame.ContentsEntry)
    ))
  ,
  DESCRIPTOR = _DATAFRAME,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.DataFrame)
  ))
_sym_db.RegisterMessage(DataFrame)
_sym_db.RegisterMessage(DataFrame.MetadataEntry)
_sym_db.RegisterMessage(DataFrame.ContentsEntry)

SearchDataFramesRequest = _reflection.GeneratedProtocolMessageType('SearchDataFramesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHDATAFRAMESREQUEST,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchDataFramesRequest)
  ))
_sym_db.RegisterMessage(SearchDataFramesRequest)

SearchDataFramesResponse = _reflection.GeneratedProtocolMessageType('SearchDataFramesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHDATAFRAMESRESPONSE,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchDataFramesResponse)
  ))
_sym_db.RegisterMessage(SearchDataFramesResponse)

SliceDataFrameRequest = _reflection.GeneratedProtocolMessageType('SliceDataFrameRequest', (_message.Message,), dict(
  DESCRIPTOR = _SLICEDATAFRAMEREQUEST,
  __module__ = 'proto.framespace.framespace_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SliceDataFrameRequest)
  ))
_sym_db.RegisterMessage(SliceDataFrameRequest)


_KEYSPACE_METADATAENTRY.has_options = True
_KEYSPACE_METADATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DATAFRAME_METADATAENTRY.has_options = True
_DATAFRAME_METADATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DATAFRAME_CONTENTSENTRY.has_options = True
_DATAFRAME_CONTENTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
import abc
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
