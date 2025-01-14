# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_data_validation/anomalies/proto/custom_validation_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow_metadata.proto.v0 import anomalies_pb2 as tensorflow__metadata_dot_proto_dot_v0_dot_anomalies__pb2
from tensorflow_metadata.proto.v0 import path_pb2 as tensorflow__metadata_dot_proto_dot_v0_dot_path__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_data_validation/anomalies/proto/custom_validation_config.proto',
  package='tensorflow.data_validation',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nItensorflow_data_validation/anomalies/proto/custom_validation_config.proto\x12\x1atensorflow.data_validation\x1a,tensorflow_metadata/proto/v0/anomalies.proto\x1a\'tensorflow_metadata/proto/v0/path.proto\"\x91\x01\n\nValidation\x12\x16\n\x0esql_expression\x18\x01 \x01(\t\x12>\n\x08severity\x18\x02 \x01(\x0e\x32,.tensorflow.metadata.v0.AnomalyInfo.Severity\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x16\n\x0ein_environment\x18\x04 \x03(\t\"\x9a\x01\n\x11\x46\x65\x61tureValidation\x12\x14\n\x0c\x64\x61taset_name\x18\x01 \x01(\t\x12\x32\n\x0c\x66\x65\x61ture_path\x18\x02 \x01(\x0b\x32\x1c.tensorflow.metadata.v0.Path\x12;\n\x0bvalidations\x18\x03 \x03(\x0b\x32&.tensorflow.data_validation.Validation\"\xf7\x01\n\x15\x46\x65\x61turePairValidation\x12\x14\n\x0c\x64\x61taset_name\x18\x01 \x01(\t\x12\x19\n\x11\x62\x61se_dataset_name\x18\x02 \x01(\t\x12\x37\n\x11\x66\x65\x61ture_test_path\x18\x03 \x01(\x0b\x32\x1c.tensorflow.metadata.v0.Path\x12\x37\n\x11\x66\x65\x61ture_base_path\x18\x04 \x01(\x0b\x32\x1c.tensorflow.metadata.v0.Path\x12;\n\x0bvalidations\x18\x05 \x03(\x0b\x32&.tensorflow.data_validation.Validation\"\xb9\x01\n\x16\x43ustomValidationConfig\x12J\n\x13\x66\x65\x61ture_validations\x18\x01 \x03(\x0b\x32-.tensorflow.data_validation.FeatureValidation\x12S\n\x18\x66\x65\x61ture_pair_validations\x18\x02 \x03(\x0b\x32\x31.tensorflow.data_validation.FeaturePairValidation'
  ,
  dependencies=[tensorflow__metadata_dot_proto_dot_v0_dot_anomalies__pb2.DESCRIPTOR,tensorflow__metadata_dot_proto_dot_v0_dot_path__pb2.DESCRIPTOR,])




_VALIDATION = _descriptor.Descriptor(
  name='Validation',
  full_name='tensorflow.data_validation.Validation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sql_expression', full_name='tensorflow.data_validation.Validation.sql_expression', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='severity', full_name='tensorflow.data_validation.Validation.severity', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='tensorflow.data_validation.Validation.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='in_environment', full_name='tensorflow.data_validation.Validation.in_environment', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=338,
)


_FEATUREVALIDATION = _descriptor.Descriptor(
  name='FeatureValidation',
  full_name='tensorflow.data_validation.FeatureValidation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_name', full_name='tensorflow.data_validation.FeatureValidation.dataset_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_path', full_name='tensorflow.data_validation.FeatureValidation.feature_path', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validations', full_name='tensorflow.data_validation.FeatureValidation.validations', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=495,
)


_FEATUREPAIRVALIDATION = _descriptor.Descriptor(
  name='FeaturePairValidation',
  full_name='tensorflow.data_validation.FeaturePairValidation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_name', full_name='tensorflow.data_validation.FeaturePairValidation.dataset_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_dataset_name', full_name='tensorflow.data_validation.FeaturePairValidation.base_dataset_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_test_path', full_name='tensorflow.data_validation.FeaturePairValidation.feature_test_path', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_base_path', full_name='tensorflow.data_validation.FeaturePairValidation.feature_base_path', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validations', full_name='tensorflow.data_validation.FeaturePairValidation.validations', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=498,
  serialized_end=745,
)


_CUSTOMVALIDATIONCONFIG = _descriptor.Descriptor(
  name='CustomValidationConfig',
  full_name='tensorflow.data_validation.CustomValidationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_validations', full_name='tensorflow.data_validation.CustomValidationConfig.feature_validations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_pair_validations', full_name='tensorflow.data_validation.CustomValidationConfig.feature_pair_validations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=748,
  serialized_end=933,
)

_VALIDATION.fields_by_name['severity'].enum_type = tensorflow__metadata_dot_proto_dot_v0_dot_anomalies__pb2._ANOMALYINFO_SEVERITY
_FEATUREVALIDATION.fields_by_name['feature_path'].message_type = tensorflow__metadata_dot_proto_dot_v0_dot_path__pb2._PATH
_FEATUREVALIDATION.fields_by_name['validations'].message_type = _VALIDATION
_FEATUREPAIRVALIDATION.fields_by_name['feature_test_path'].message_type = tensorflow__metadata_dot_proto_dot_v0_dot_path__pb2._PATH
_FEATUREPAIRVALIDATION.fields_by_name['feature_base_path'].message_type = tensorflow__metadata_dot_proto_dot_v0_dot_path__pb2._PATH
_FEATUREPAIRVALIDATION.fields_by_name['validations'].message_type = _VALIDATION
_CUSTOMVALIDATIONCONFIG.fields_by_name['feature_validations'].message_type = _FEATUREVALIDATION
_CUSTOMVALIDATIONCONFIG.fields_by_name['feature_pair_validations'].message_type = _FEATUREPAIRVALIDATION
DESCRIPTOR.message_types_by_name['Validation'] = _VALIDATION
DESCRIPTOR.message_types_by_name['FeatureValidation'] = _FEATUREVALIDATION
DESCRIPTOR.message_types_by_name['FeaturePairValidation'] = _FEATUREPAIRVALIDATION
DESCRIPTOR.message_types_by_name['CustomValidationConfig'] = _CUSTOMVALIDATIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Validation = _reflection.GeneratedProtocolMessageType('Validation', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATION,
  '__module__' : 'tensorflow_data_validation.anomalies.proto.custom_validation_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data_validation.Validation)
  })
_sym_db.RegisterMessage(Validation)

FeatureValidation = _reflection.GeneratedProtocolMessageType('FeatureValidation', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREVALIDATION,
  '__module__' : 'tensorflow_data_validation.anomalies.proto.custom_validation_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data_validation.FeatureValidation)
  })
_sym_db.RegisterMessage(FeatureValidation)

FeaturePairValidation = _reflection.GeneratedProtocolMessageType('FeaturePairValidation', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREPAIRVALIDATION,
  '__module__' : 'tensorflow_data_validation.anomalies.proto.custom_validation_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data_validation.FeaturePairValidation)
  })
_sym_db.RegisterMessage(FeaturePairValidation)

CustomValidationConfig = _reflection.GeneratedProtocolMessageType('CustomValidationConfig', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMVALIDATIONCONFIG,
  '__module__' : 'tensorflow_data_validation.anomalies.proto.custom_validation_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data_validation.CustomValidationConfig)
  })
_sym_db.RegisterMessage(CustomValidationConfig)


# @@protoc_insertion_point(module_scope)
