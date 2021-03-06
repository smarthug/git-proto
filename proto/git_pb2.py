# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: git.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='git.proto',
  package='git',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tgit.proto\x12\x03git\"\x1b\n\x0bRequestPath\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x1b\n\x0bRequestHash\x12\x0c\n\x04hash\x18\x01 \x01(\t\"Q\n\x0bRequestFile\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x10\n\x08\x66iledata\x18\x02 \x01(\x0c\x12\x10\n\x08\x66ilename\x18\x03 \x01(\t\x12\x10\n\x08\x66ilemode\x18\x04 \x01(\r\" \n\x0eResponseResult\x12\x0e\n\x06result\x18\x01 \x01(\t\"(\n\x0cResponseTree\x12\x18\n\x05trees\x18\x01 \x03(\x0b\x32\t.git.Tree\"0\n\x04Tree\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x0c\n\x04Mode\x18\x02 \x01(\r\x12\x0c\n\x04Hash\x18\x03 \x01(\t2\xef\x01\n\x03Git\x12\x41\n\x16\x43reateAndInitDirectory\x12\x10.git.RequestPath\x1a\x13.git.ResponseResult\"\x00\x12:\n\x0f\x41\x64\x64OrUpdateFile\x12\x10.git.RequestFile\x1a\x13.git.ResponseResult\"\x00\x12\x34\n\x0bGetRepoTree\x12\x10.git.RequestPath\x1a\x11.git.ResponseTree\"\x00\x12\x33\n\nRenderTree\x12\x10.git.RequestHash\x1a\x11.git.ResponseTree\"\x00\x62\x06proto3')
)




_REQUESTPATH = _descriptor.Descriptor(
  name='RequestPath',
  full_name='git.RequestPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='git.RequestPath.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=45,
)


_REQUESTHASH = _descriptor.Descriptor(
  name='RequestHash',
  full_name='git.RequestHash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='git.RequestHash.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=74,
)


_REQUESTFILE = _descriptor.Descriptor(
  name='RequestFile',
  full_name='git.RequestFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='git.RequestFile.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filedata', full_name='git.RequestFile.filedata', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='git.RequestFile.filename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filemode', full_name='git.RequestFile.filemode', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=157,
)


_RESPONSERESULT = _descriptor.Descriptor(
  name='ResponseResult',
  full_name='git.ResponseResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='git.ResponseResult.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=191,
)


_RESPONSETREE = _descriptor.Descriptor(
  name='ResponseTree',
  full_name='git.ResponseTree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trees', full_name='git.ResponseTree.trees', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=233,
)


_TREE = _descriptor.Descriptor(
  name='Tree',
  full_name='git.Tree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='git.Tree.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Mode', full_name='git.Tree.Mode', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Hash', full_name='git.Tree.Hash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=283,
)

_RESPONSETREE.fields_by_name['trees'].message_type = _TREE
DESCRIPTOR.message_types_by_name['RequestPath'] = _REQUESTPATH
DESCRIPTOR.message_types_by_name['RequestHash'] = _REQUESTHASH
DESCRIPTOR.message_types_by_name['RequestFile'] = _REQUESTFILE
DESCRIPTOR.message_types_by_name['ResponseResult'] = _RESPONSERESULT
DESCRIPTOR.message_types_by_name['ResponseTree'] = _RESPONSETREE
DESCRIPTOR.message_types_by_name['Tree'] = _TREE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestPath = _reflection.GeneratedProtocolMessageType('RequestPath', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTPATH,
  __module__ = 'git_pb2'
  # @@protoc_insertion_point(class_scope:git.RequestPath)
  ))
_sym_db.RegisterMessage(RequestPath)

RequestHash = _reflection.GeneratedProtocolMessageType('RequestHash', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTHASH,
  __module__ = 'git_pb2'
  # @@protoc_insertion_point(class_scope:git.RequestHash)
  ))
_sym_db.RegisterMessage(RequestHash)

RequestFile = _reflection.GeneratedProtocolMessageType('RequestFile', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTFILE,
  __module__ = 'git_pb2'
  # @@protoc_insertion_point(class_scope:git.RequestFile)
  ))
_sym_db.RegisterMessage(RequestFile)

ResponseResult = _reflection.GeneratedProtocolMessageType('ResponseResult', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSERESULT,
  __module__ = 'git_pb2'
  # @@protoc_insertion_point(class_scope:git.ResponseResult)
  ))
_sym_db.RegisterMessage(ResponseResult)

ResponseTree = _reflection.GeneratedProtocolMessageType('ResponseTree', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSETREE,
  __module__ = 'git_pb2'
  # @@protoc_insertion_point(class_scope:git.ResponseTree)
  ))
_sym_db.RegisterMessage(ResponseTree)

Tree = _reflection.GeneratedProtocolMessageType('Tree', (_message.Message,), dict(
  DESCRIPTOR = _TREE,
  __module__ = 'git_pb2'
  # @@protoc_insertion_point(class_scope:git.Tree)
  ))
_sym_db.RegisterMessage(Tree)



_GIT = _descriptor.ServiceDescriptor(
  name='Git',
  full_name='git.Git',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=286,
  serialized_end=525,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateAndInitDirectory',
    full_name='git.Git.CreateAndInitDirectory',
    index=0,
    containing_service=None,
    input_type=_REQUESTPATH,
    output_type=_RESPONSERESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddOrUpdateFile',
    full_name='git.Git.AddOrUpdateFile',
    index=1,
    containing_service=None,
    input_type=_REQUESTFILE,
    output_type=_RESPONSERESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRepoTree',
    full_name='git.Git.GetRepoTree',
    index=2,
    containing_service=None,
    input_type=_REQUESTPATH,
    output_type=_RESPONSETREE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RenderTree',
    full_name='git.Git.RenderTree',
    index=3,
    containing_service=None,
    input_type=_REQUESTHASH,
    output_type=_RESPONSETREE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GIT)

DESCRIPTOR.services_by_name['Git'] = _GIT

# @@protoc_insertion_point(module_scope)
