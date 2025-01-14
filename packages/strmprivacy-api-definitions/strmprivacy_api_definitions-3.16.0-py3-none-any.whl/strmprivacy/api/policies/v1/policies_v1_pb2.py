# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: strmprivacy/api/policies/v1/policies_v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from strmprivacy.api.entities.v1 import entities_v1_pb2 as strmprivacy_dot_api_dot_entities_dot_v1_dot_entities__v1__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-strmprivacy/api/policies/v1/policies_v1.proto\x12\x1bstrmprivacy.api.policies.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a google/protobuf/field_mask.proto\x1a-strmprivacy/api/entities/v1/entities_v1.proto\x1a\x17validate/validate.proto\"\x15\n\x13ListPoliciesRequest\"W\n\x14ListPoliciesResponse\x12?\n\x08policies\x18\x01 \x03(\x0b\x32#.strmprivacy.api.entities.v1.PolicyR\x08policies\"<\n\x13\x44\x65letePolicyRequest\x12%\n\tpolicy_id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x08policyId\"\x16\n\x14\x44\x65letePolicyResponse\"\\\n\x13\x43reatePolicyRequest\x12\x45\n\x06policy\x18\x01 \x01(\x0b\x32#.strmprivacy.api.entities.v1.PolicyB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x06policy\"X\n\x14\x43reatePolicyResponse\x12@\n\x06policy\x18\x01 \x01(\x0b\x32#.strmprivacy.api.entities.v1.PolicyB\x03\xe0\x41\x02R\x06policy\"\xa3\x01\n\x13UpdatePolicyRequest\x12\x45\n\x06policy\x18\x01 \x01(\x0b\x32#.strmprivacy.api.entities.v1.PolicyB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x06policy\x12\x45\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\nupdateMask\"X\n\x14UpdatePolicyResponse\x12@\n\x06policy\x18\x01 \x01(\x0b\x32#.strmprivacy.api.entities.v1.PolicyB\x03\xe0\x41\x02R\x06policy\"<\n\x10GetPolicyRequest\x12(\n\tpolicy_id\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xd0\x01\x01\xb0\x01\x01R\x08policyId\"P\n\x11GetPolicyResponse\x12;\n\x06policy\x18\x01 \x01(\x0b\x32#.strmprivacy.api.entities.v1.PolicyR\x06policy2\xd1\x04\n\x0fPoliciesService\x12s\n\x0cListPolicies\x12\x30.strmprivacy.api.policies.v1.ListPoliciesRequest\x1a\x31.strmprivacy.api.policies.v1.ListPoliciesResponse\x12j\n\tGetPolicy\x12-.strmprivacy.api.policies.v1.GetPolicyRequest\x1a..strmprivacy.api.policies.v1.GetPolicyResponse\x12s\n\x0c\x44\x65letePolicy\x12\x30.strmprivacy.api.policies.v1.DeletePolicyRequest\x1a\x31.strmprivacy.api.policies.v1.DeletePolicyResponse\x12s\n\x0c\x43reatePolicy\x12\x30.strmprivacy.api.policies.v1.CreatePolicyRequest\x1a\x31.strmprivacy.api.policies.v1.CreatePolicyResponse\x12s\n\x0cUpdatePolicy\x12\x30.strmprivacy.api.policies.v1.UpdatePolicyRequest\x1a\x31.strmprivacy.api.policies.v1.UpdatePolicyResponseBi\n\x1eio.strmprivacy.api.policies.v1P\x01ZEgithub.com/strmprivacy/api-definitions-go/v3/api/policies/v1;policiesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'strmprivacy.api.policies.v1.policies_v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036io.strmprivacy.api.policies.v1P\001ZEgithub.com/strmprivacy/api-definitions-go/v3/api/policies/v1;policies'
  _DELETEPOLICYREQUEST.fields_by_name['policy_id']._options = None
  _DELETEPOLICYREQUEST.fields_by_name['policy_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _CREATEPOLICYREQUEST.fields_by_name['policy']._options = None
  _CREATEPOLICYREQUEST.fields_by_name['policy']._serialized_options = b'\372B\005\212\001\002\020\001'
  _CREATEPOLICYRESPONSE.fields_by_name['policy']._options = None
  _CREATEPOLICYRESPONSE.fields_by_name['policy']._serialized_options = b'\340A\002'
  _UPDATEPOLICYREQUEST.fields_by_name['policy']._options = None
  _UPDATEPOLICYREQUEST.fields_by_name['policy']._serialized_options = b'\372B\005\212\001\002\020\001'
  _UPDATEPOLICYREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEPOLICYREQUEST.fields_by_name['update_mask']._serialized_options = b'\372B\005\212\001\002\020\001'
  _UPDATEPOLICYRESPONSE.fields_by_name['policy']._options = None
  _UPDATEPOLICYRESPONSE.fields_by_name['policy']._serialized_options = b'\340A\002'
  _GETPOLICYREQUEST.fields_by_name['policy_id']._options = None
  _GETPOLICYREQUEST.fields_by_name['policy_id']._serialized_options = b'\372B\010r\006\320\001\001\260\001\001'
  _LISTPOLICIESREQUEST._serialized_start=217
  _LISTPOLICIESREQUEST._serialized_end=238
  _LISTPOLICIESRESPONSE._serialized_start=240
  _LISTPOLICIESRESPONSE._serialized_end=327
  _DELETEPOLICYREQUEST._serialized_start=329
  _DELETEPOLICYREQUEST._serialized_end=389
  _DELETEPOLICYRESPONSE._serialized_start=391
  _DELETEPOLICYRESPONSE._serialized_end=413
  _CREATEPOLICYREQUEST._serialized_start=415
  _CREATEPOLICYREQUEST._serialized_end=507
  _CREATEPOLICYRESPONSE._serialized_start=509
  _CREATEPOLICYRESPONSE._serialized_end=597
  _UPDATEPOLICYREQUEST._serialized_start=600
  _UPDATEPOLICYREQUEST._serialized_end=763
  _UPDATEPOLICYRESPONSE._serialized_start=765
  _UPDATEPOLICYRESPONSE._serialized_end=853
  _GETPOLICYREQUEST._serialized_start=855
  _GETPOLICYREQUEST._serialized_end=915
  _GETPOLICYRESPONSE._serialized_start=917
  _GETPOLICYRESPONSE._serialized_end=997
  _POLICIESSERVICE._serialized_start=1000
  _POLICIESSERVICE._serialized_end=1593
# @@protoc_insertion_point(module_scope)
