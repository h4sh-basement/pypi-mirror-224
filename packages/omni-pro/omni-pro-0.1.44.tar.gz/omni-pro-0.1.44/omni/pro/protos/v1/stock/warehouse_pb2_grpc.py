# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.stock import warehouse_pb2 as v1_dot_stock_dot_warehouse__pb2


class WarehouseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WarehouseCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.warehouse.WarehouseService/WarehouseCreate",
            request_serializer=v1_dot_stock_dot_warehouse__pb2.WarehouseCreateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_warehouse__pb2.WarehouseCreateResponse.FromString,
        )
        self.WarehouseRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.warehouse.WarehouseService/WarehouseRead",
            request_serializer=v1_dot_stock_dot_warehouse__pb2.WarehouseReadRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_warehouse__pb2.WarehouseReadResponse.FromString,
        )
        self.WarehouseUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.warehouse.WarehouseService/WarehouseUpdate",
            request_serializer=v1_dot_stock_dot_warehouse__pb2.WarehouseUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_warehouse__pb2.WarehouseUpdateResponse.FromString,
        )
        self.WarehouseDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.warehouse.WarehouseService/WarehouseDelete",
            request_serializer=v1_dot_stock_dot_warehouse__pb2.WarehouseDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_warehouse__pb2.WarehouseDeleteResponse.FromString,
        )


class WarehouseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WarehouseCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def WarehouseRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def WarehouseUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def WarehouseDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_WarehouseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "WarehouseCreate": grpc.unary_unary_rpc_method_handler(
            servicer.WarehouseCreate,
            request_deserializer=v1_dot_stock_dot_warehouse__pb2.WarehouseCreateRequest.FromString,
            response_serializer=v1_dot_stock_dot_warehouse__pb2.WarehouseCreateResponse.SerializeToString,
        ),
        "WarehouseRead": grpc.unary_unary_rpc_method_handler(
            servicer.WarehouseRead,
            request_deserializer=v1_dot_stock_dot_warehouse__pb2.WarehouseReadRequest.FromString,
            response_serializer=v1_dot_stock_dot_warehouse__pb2.WarehouseReadResponse.SerializeToString,
        ),
        "WarehouseUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.WarehouseUpdate,
            request_deserializer=v1_dot_stock_dot_warehouse__pb2.WarehouseUpdateRequest.FromString,
            response_serializer=v1_dot_stock_dot_warehouse__pb2.WarehouseUpdateResponse.SerializeToString,
        ),
        "WarehouseDelete": grpc.unary_unary_rpc_method_handler(
            servicer.WarehouseDelete,
            request_deserializer=v1_dot_stock_dot_warehouse__pb2.WarehouseDeleteRequest.FromString,
            response_serializer=v1_dot_stock_dot_warehouse__pb2.WarehouseDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.stock.warehouse.WarehouseService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class WarehouseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WarehouseCreate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.stock.warehouse.WarehouseService/WarehouseCreate",
            v1_dot_stock_dot_warehouse__pb2.WarehouseCreateRequest.SerializeToString,
            v1_dot_stock_dot_warehouse__pb2.WarehouseCreateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def WarehouseRead(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.stock.warehouse.WarehouseService/WarehouseRead",
            v1_dot_stock_dot_warehouse__pb2.WarehouseReadRequest.SerializeToString,
            v1_dot_stock_dot_warehouse__pb2.WarehouseReadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def WarehouseUpdate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.stock.warehouse.WarehouseService/WarehouseUpdate",
            v1_dot_stock_dot_warehouse__pb2.WarehouseUpdateRequest.SerializeToString,
            v1_dot_stock_dot_warehouse__pb2.WarehouseUpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def WarehouseDelete(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.stock.warehouse.WarehouseService/WarehouseDelete",
            v1_dot_stock_dot_warehouse__pb2.WarehouseDeleteRequest.SerializeToString,
            v1_dot_stock_dot_warehouse__pb2.WarehouseDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
