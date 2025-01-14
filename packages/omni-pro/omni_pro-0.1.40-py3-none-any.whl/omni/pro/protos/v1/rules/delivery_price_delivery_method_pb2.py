# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/delivery_price_delivery_method.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni.pro.protos.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n-v1/rules/delivery_price_delivery_method.proto\x12\x38pro.omni.oms.api.v1.rules.delivery_price_delivery_method\x1a\x11\x63ommon/base.proto"\xb1\x01\n\x1b\x44\x65liveryPriceDeliveryMethod\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x19\n\x11\x64\x65livery_price_id\x18\x02 \x01(\x05\x12\x1a\n\x12\x64\x65livery_method_id\x18\x03 \x01(\x05\x12\x0e\n\x06\x61\x63tive\x18\x04 \x01(\x08\x12?\n\x0cobject_audit\x18\x05 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x99\x01\n(DeliveryPriceDeliveryMethodCreateRequest\x12\x19\n\x11\x64\x65livery_price_id\x18\x01 \x01(\x05\x12\x1a\n\x12\x64\x65livery_method_id\x18\x02 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xf5\x01\n)DeliveryPriceDeliveryMethodCreateResponse\x12}\n\x1e\x64\x65livery_price_delivery_method\x18\x01 \x01(\x0b\x32U.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x84\x03\n&DeliveryPriceDeliveryMethodReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xae\x02\n\'DeliveryPriceDeliveryMethodReadResponse\x12}\n\x1e\x64\x65livery_price_delivery_method\x18\x01 \x03(\x0b\x32U.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethod\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xe1\x01\n(DeliveryPriceDeliveryMethodUpdateRequest\x12}\n\x1e\x64\x65livery_price_delivery_method\x18\x01 \x01(\x0b\x32U.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethod\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xf5\x01\n)DeliveryPriceDeliveryMethodUpdateResponse\x12}\n\x1e\x64\x65livery_price_delivery_method\x18\x01 \x01(\x0b\x32U.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"n\n(DeliveryPriceDeliveryMethodDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"v\n)DeliveryPriceDeliveryMethodDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xe2\x07\n"DeliveryPriceDeliveryMethodService\x12\xee\x01\n!DeliveryPriceDeliveryMethodCreate\x12\x62.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodCreateRequest\x1a\x63.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodCreateResponse"\x00\x12\xe8\x01\n\x1f\x44\x65liveryPriceDeliveryMethodRead\x12`.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodReadRequest\x1a\x61.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodReadResponse"\x00\x12\xee\x01\n!DeliveryPriceDeliveryMethodUpdate\x12\x62.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodUpdateRequest\x1a\x63.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodUpdateResponse"\x00\x12\xee\x01\n!DeliveryPriceDeliveryMethodDelete\x12\x62.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodDeleteRequest\x1a\x63.pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.delivery_price_delivery_method_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_DELIVERYPRICEDELIVERYMETHOD"]._serialized_start = 127
    _globals["_DELIVERYPRICEDELIVERYMETHOD"]._serialized_end = 304
    _globals["_DELIVERYPRICEDELIVERYMETHODCREATEREQUEST"]._serialized_start = 307
    _globals["_DELIVERYPRICEDELIVERYMETHODCREATEREQUEST"]._serialized_end = 460
    _globals["_DELIVERYPRICEDELIVERYMETHODCREATERESPONSE"]._serialized_start = 463
    _globals["_DELIVERYPRICEDELIVERYMETHODCREATERESPONSE"]._serialized_end = 708
    _globals["_DELIVERYPRICEDELIVERYMETHODREADREQUEST"]._serialized_start = 711
    _globals["_DELIVERYPRICEDELIVERYMETHODREADREQUEST"]._serialized_end = 1099
    _globals["_DELIVERYPRICEDELIVERYMETHODREADRESPONSE"]._serialized_start = 1102
    _globals["_DELIVERYPRICEDELIVERYMETHODREADRESPONSE"]._serialized_end = 1404
    _globals["_DELIVERYPRICEDELIVERYMETHODUPDATEREQUEST"]._serialized_start = 1407
    _globals["_DELIVERYPRICEDELIVERYMETHODUPDATEREQUEST"]._serialized_end = 1632
    _globals["_DELIVERYPRICEDELIVERYMETHODUPDATERESPONSE"]._serialized_start = 1635
    _globals["_DELIVERYPRICEDELIVERYMETHODUPDATERESPONSE"]._serialized_end = 1880
    _globals["_DELIVERYPRICEDELIVERYMETHODDELETEREQUEST"]._serialized_start = 1882
    _globals["_DELIVERYPRICEDELIVERYMETHODDELETEREQUEST"]._serialized_end = 1992
    _globals["_DELIVERYPRICEDELIVERYMETHODDELETERESPONSE"]._serialized_start = 1994
    _globals["_DELIVERYPRICEDELIVERYMETHODDELETERESPONSE"]._serialized_end = 2112
    _globals["_DELIVERYPRICEDELIVERYMETHODSERVICE"]._serialized_start = 2115
    _globals["_DELIVERYPRICEDELIVERYMETHODSERVICE"]._serialized_end = 3109
# @@protoc_insertion_point(module_scope)
