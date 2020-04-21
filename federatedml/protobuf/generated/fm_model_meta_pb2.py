# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fm-model-meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fm-model-meta.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer.fm',
  syntax='proto3',
  serialized_options=_b('B\020FMModelMetaProto'),
  serialized_pb=_b('\n\x13\x66m-model-meta.proto\x12)com.webank.ai.fate.core.mlmodel.buffer.fm\"\x81\x02\n\x0b\x46MModelMeta\x12\x0f\n\x07penalty\x18\x01 \x01(\t\x12\x0b\n\x03tol\x18\x02 \x01(\x01\x12\r\n\x05\x61lpha\x18\x03 \x01(\x01\x12\x11\n\toptimizer\x18\x04 \x01(\t\x12\x14\n\x0cparty_weight\x18\x05 \x01(\x01\x12\x12\n\nbatch_size\x18\x06 \x01(\x03\x12\x15\n\rlearning_rate\x18\x07 \x01(\x01\x12\x10\n\x08max_iter\x18\x08 \x01(\x03\x12\x12\n\nearly_stop\x18\t \x01(\t\x12\x1a\n\x12re_encrypt_batches\x18\n \x01(\x03\x12\x15\n\rfit_intercept\x18\x0b \x01(\x08\x12\x18\n\x10need_one_vs_rest\x18\x0c \x01(\x08\x42\x12\x42\x10\x46MModelMetaProtob\x06proto3')
)




_FMMODELMETA = _descriptor.Descriptor(
  name='FMModelMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='penalty', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.penalty', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tol', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.tol', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alpha', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.alpha', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.optimizer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='party_weight', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.party_weight', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.batch_size', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.learning_rate', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_iter', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.max_iter', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='early_stop', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.early_stop', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='re_encrypt_batches', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.re_encrypt_batches', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fit_intercept', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.fit_intercept', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_one_vs_rest', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta.need_one_vs_rest', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=67,
  serialized_end=324,
)

DESCRIPTOR.message_types_by_name['FMModelMeta'] = _FMMODELMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FMModelMeta = _reflection.GeneratedProtocolMessageType('FMModelMeta', (_message.Message,), dict(
  DESCRIPTOR = _FMMODELMETA,
  __module__ = 'fm_model_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelMeta)
  ))
_sym_db.RegisterMessage(FMModelMeta)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
