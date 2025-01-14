# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/picking_order.proto
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
    b'\n\x1cv1/sales/picking_order.proto\x12\'pro.omni.oms.api.v1.sales.picking.order\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xad\x01\n\x0cPickingOrder\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08order_id\x18\x02 \x01(\x05\x12\x12\n\npicking_id\x18\x03 \x01(\x05\x12*\n\x06\x61\x63tive\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x05 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"y\n\x19PickingOrderCreateRequest\x12\x10\n\x08order_id\x18\x01 \x01(\x05\x12\x12\n\npicking_id\x18\x02 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb5\x01\n\x1aPickingOrderCreateResponse\x12L\n\rpicking_order\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.sales.picking.order.PickingOrder\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf5\x02\n\x17PickingOrderReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xef\x01\n\x18PickingOrderReadResponse\x12M\n\x0epicking_orders\x18\x01 \x03(\x0b\x32\x35.pro.omni.oms.api.v1.sales.picking.order.PickingOrder\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x03 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData"\xa1\x01\n\x19PickingOrderUpdateRequest\x12L\n\rpicking_order\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.sales.picking.order.PickingOrder\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb5\x01\n\x1aPickingOrderUpdateResponse\x12L\n\rpicking_order\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.sales.picking.order.PickingOrder\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"_\n\x19PickingOrderDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb5\x01\n\x1aPickingOrderDeleteResponse\x12L\n\rpicking_order\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.sales.picking.order.PickingOrder\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x97\x05\n\x13PickingOrderService\x12\x9f\x01\n\x12PickingOrderCreate\x12\x42.pro.omni.oms.api.v1.sales.picking.order.PickingOrderCreateRequest\x1a\x43.pro.omni.oms.api.v1.sales.picking.order.PickingOrderCreateResponse"\x00\x12\x99\x01\n\x10PickingOrderRead\x12@.pro.omni.oms.api.v1.sales.picking.order.PickingOrderReadRequest\x1a\x41.pro.omni.oms.api.v1.sales.picking.order.PickingOrderReadResponse"\x00\x12\x9f\x01\n\x12PickingOrderUpdate\x12\x42.pro.omni.oms.api.v1.sales.picking.order.PickingOrderUpdateRequest\x1a\x43.pro.omni.oms.api.v1.sales.picking.order.PickingOrderUpdateResponse"\x00\x12\x9f\x01\n\x12PickingOrderDelete\x12\x42.pro.omni.oms.api.v1.sales.picking.order.PickingOrderDeleteRequest\x1a\x43.pro.omni.oms.api.v1.sales.picking.order.PickingOrderDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.sales.picking_order_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_PICKINGORDER"]._serialized_start = 125
    _globals["_PICKINGORDER"]._serialized_end = 298
    _globals["_PICKINGORDERCREATEREQUEST"]._serialized_start = 300
    _globals["_PICKINGORDERCREATEREQUEST"]._serialized_end = 421
    _globals["_PICKINGORDERCREATERESPONSE"]._serialized_start = 424
    _globals["_PICKINGORDERCREATERESPONSE"]._serialized_end = 605
    _globals["_PICKINGORDERREADREQUEST"]._serialized_start = 608
    _globals["_PICKINGORDERREADREQUEST"]._serialized_end = 981
    _globals["_PICKINGORDERREADRESPONSE"]._serialized_start = 984
    _globals["_PICKINGORDERREADRESPONSE"]._serialized_end = 1223
    _globals["_PICKINGORDERUPDATEREQUEST"]._serialized_start = 1226
    _globals["_PICKINGORDERUPDATEREQUEST"]._serialized_end = 1387
    _globals["_PICKINGORDERUPDATERESPONSE"]._serialized_start = 1390
    _globals["_PICKINGORDERUPDATERESPONSE"]._serialized_end = 1571
    _globals["_PICKINGORDERDELETEREQUEST"]._serialized_start = 1573
    _globals["_PICKINGORDERDELETEREQUEST"]._serialized_end = 1668
    _globals["_PICKINGORDERDELETERESPONSE"]._serialized_start = 1671
    _globals["_PICKINGORDERDELETERESPONSE"]._serialized_end = 1852
    _globals["_PICKINGORDERSERVICE"]._serialized_start = 1855
    _globals["_PICKINGORDERSERVICE"]._serialized_end = 2518
# @@protoc_insertion_point(module_scope)
