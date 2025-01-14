# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/attachment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni.pro.protos.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19v1/stock/attachment.proto\x12$pro.omni.oms.api.v1.stock.attachment\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xb1\x01\n\nAttachment\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06\x64oc_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x06 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"}\n\x17\x41ttachmentCreateRequest\x12\x0e\n\x06\x64oc_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xab\x01\n\x18\x41ttachmentCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x44\n\nattachment\x18\x02 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.stock.attachment.Attachment"\xf3\x02\n\x15\x41ttachmentReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xe5\x01\n\x16\x41ttachmentReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x45\n\x0b\x61ttachments\x18\x03 \x03(\x0b\x32\x30.pro.omni.oms.api.v1.stock.attachment.Attachment"\x97\x01\n\x17\x41ttachmentUpdateRequest\x12\x44\n\nattachment\x18\x01 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.stock.attachment.Attachment\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xab\x01\n\x18\x41ttachmentUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x44\n\nattachment\x18\x02 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.stock.attachment.Attachment"]\n\x17\x41ttachmentDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"e\n\x18\x41ttachmentDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xe5\x04\n\x11\x41ttachmentService\x12\x93\x01\n\x10\x41ttachmentCreate\x12=.pro.omni.oms.api.v1.stock.attachment.AttachmentCreateRequest\x1a>.pro.omni.oms.api.v1.stock.attachment.AttachmentCreateResponse"\x00\x12\x8d\x01\n\x0e\x41ttachmentRead\x12;.pro.omni.oms.api.v1.stock.attachment.AttachmentReadRequest\x1a<.pro.omni.oms.api.v1.stock.attachment.AttachmentReadResponse"\x00\x12\x93\x01\n\x10\x41ttachmentUpdate\x12=.pro.omni.oms.api.v1.stock.attachment.AttachmentUpdateRequest\x1a>.pro.omni.oms.api.v1.stock.attachment.AttachmentUpdateResponse"\x00\x12\x93\x01\n\x10\x41ttachmentDelete\x12=.pro.omni.oms.api.v1.stock.attachment.AttachmentDeleteRequest\x1a>.pro.omni.oms.api.v1.stock.attachment.AttachmentDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.attachment_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_ATTACHMENT"]._serialized_start = 119
    _globals["_ATTACHMENT"]._serialized_end = 296
    _globals["_ATTACHMENTCREATEREQUEST"]._serialized_start = 298
    _globals["_ATTACHMENTCREATEREQUEST"]._serialized_end = 423
    _globals["_ATTACHMENTCREATERESPONSE"]._serialized_start = 426
    _globals["_ATTACHMENTCREATERESPONSE"]._serialized_end = 597
    _globals["_ATTACHMENTREADREQUEST"]._serialized_start = 600
    _globals["_ATTACHMENTREADREQUEST"]._serialized_end = 971
    _globals["_ATTACHMENTREADRESPONSE"]._serialized_start = 974
    _globals["_ATTACHMENTREADRESPONSE"]._serialized_end = 1203
    _globals["_ATTACHMENTUPDATEREQUEST"]._serialized_start = 1206
    _globals["_ATTACHMENTUPDATEREQUEST"]._serialized_end = 1357
    _globals["_ATTACHMENTUPDATERESPONSE"]._serialized_start = 1360
    _globals["_ATTACHMENTUPDATERESPONSE"]._serialized_end = 1531
    _globals["_ATTACHMENTDELETEREQUEST"]._serialized_start = 1533
    _globals["_ATTACHMENTDELETEREQUEST"]._serialized_end = 1626
    _globals["_ATTACHMENTDELETERESPONSE"]._serialized_start = 1628
    _globals["_ATTACHMENTDELETERESPONSE"]._serialized_end = 1729
    _globals["_ATTACHMENTSERVICE"]._serialized_start = 1732
    _globals["_ATTACHMENTSERVICE"]._serialized_end = 2345
# @@protoc_insertion_point(module_scope)
