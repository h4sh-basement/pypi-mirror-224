# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/carrier.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni.pro.protos.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16v1/stock/carrier.proto\x12!pro.omni.oms.api.v1.stock.carrier\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9e\x01\n\x07\x43\x61rrier\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12*\n\x06\x61\x63tive\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x05 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"j\n\x14\x43\x61rrierCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15\x43\x61rrierCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12;\n\x07\x63\x61rrier\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.carrier.Carrier"\xf0\x02\n\x12\x43\x61rrierReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd9\x01\n\x13\x43\x61rrierReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12<\n\x08\x63\x61rriers\x18\x03 \x03(\x0b\x32*.pro.omni.oms.api.v1.stock.carrier.Carrier"\x8b\x01\n\x14\x43\x61rrierUpdateRequest\x12;\n\x07\x63\x61rrier\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.carrier.Carrier\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15\x43\x61rrierUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12;\n\x07\x63\x61rrier\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.carrier.Carrier"Z\n\x14\x43\x61rrierDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"b\n\x15\x43\x61rrierDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xa5\x04\n\x0e\x43\x61rrierService\x12\x84\x01\n\rCarrierCreate\x12\x37.pro.omni.oms.api.v1.stock.carrier.CarrierCreateRequest\x1a\x38.pro.omni.oms.api.v1.stock.carrier.CarrierCreateResponse"\x00\x12~\n\x0b\x43\x61rrierRead\x12\x35.pro.omni.oms.api.v1.stock.carrier.CarrierReadRequest\x1a\x36.pro.omni.oms.api.v1.stock.carrier.CarrierReadResponse"\x00\x12\x84\x01\n\rCarrierUpdate\x12\x37.pro.omni.oms.api.v1.stock.carrier.CarrierUpdateRequest\x1a\x38.pro.omni.oms.api.v1.stock.carrier.CarrierUpdateResponse"\x00\x12\x84\x01\n\rCarrierDelete\x12\x37.pro.omni.oms.api.v1.stock.carrier.CarrierDeleteRequest\x1a\x38.pro.omni.oms.api.v1.stock.carrier.CarrierDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.carrier_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_CARRIER"]._serialized_start = 146
    _globals["_CARRIER"]._serialized_end = 304
    _globals["_CARRIERCREATEREQUEST"]._serialized_start = 306
    _globals["_CARRIERCREATEREQUEST"]._serialized_end = 412
    _globals["_CARRIERCREATERESPONSE"]._serialized_start = 415
    _globals["_CARRIERCREATERESPONSE"]._serialized_end = 574
    _globals["_CARRIERREADREQUEST"]._serialized_start = 577
    _globals["_CARRIERREADREQUEST"]._serialized_end = 945
    _globals["_CARRIERREADRESPONSE"]._serialized_start = 948
    _globals["_CARRIERREADRESPONSE"]._serialized_end = 1165
    _globals["_CARRIERUPDATEREQUEST"]._serialized_start = 1168
    _globals["_CARRIERUPDATEREQUEST"]._serialized_end = 1307
    _globals["_CARRIERUPDATERESPONSE"]._serialized_start = 1310
    _globals["_CARRIERUPDATERESPONSE"]._serialized_end = 1469
    _globals["_CARRIERDELETEREQUEST"]._serialized_start = 1471
    _globals["_CARRIERDELETEREQUEST"]._serialized_end = 1561
    _globals["_CARRIERDELETERESPONSE"]._serialized_start = 1563
    _globals["_CARRIERDELETERESPONSE"]._serialized_end = 1661
    _globals["_CARRIERSERVICE"]._serialized_start = 1664
    _globals["_CARRIERSERVICE"]._serialized_end = 2213
# @@protoc_insertion_point(module_scope)
