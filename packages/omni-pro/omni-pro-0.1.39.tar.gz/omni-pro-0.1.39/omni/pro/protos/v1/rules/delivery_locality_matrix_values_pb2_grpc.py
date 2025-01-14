# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.rules import (
    delivery_locality_matrix_values_pb2 as v1_dot_rules_dot_delivery__locality__matrix__values__pb2,
)


class DeliveryLocalityMatrixValuesServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeliveryLocalityMatrixValuesCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_locality_matrix_values.DeliveryLocalityMatrixValuesService/DeliveryLocalityMatrixValuesCreate",
            request_serializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesCreateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesCreateResponse.FromString,
        )
        self.DeliveryLocalityMatrixValuesRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_locality_matrix_values.DeliveryLocalityMatrixValuesService/DeliveryLocalityMatrixValuesRead",
            request_serializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesReadRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesReadResponse.FromString,
        )
        self.DeliveryLocalityMatrixValuesUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_locality_matrix_values.DeliveryLocalityMatrixValuesService/DeliveryLocalityMatrixValuesUpdate",
            request_serializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesUpdateResponse.FromString,
        )
        self.DeliveryLocalityMatrixValuesDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_locality_matrix_values.DeliveryLocalityMatrixValuesService/DeliveryLocalityMatrixValuesDelete",
            request_serializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesDeleteResponse.FromString,
        )


class DeliveryLocalityMatrixValuesServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DeliveryLocalityMatrixValuesCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryLocalityMatrixValuesRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryLocalityMatrixValuesUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryLocalityMatrixValuesDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DeliveryLocalityMatrixValuesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "DeliveryLocalityMatrixValuesCreate": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryLocalityMatrixValuesCreate,
            request_deserializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesCreateRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesCreateResponse.SerializeToString,
        ),
        "DeliveryLocalityMatrixValuesRead": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryLocalityMatrixValuesRead,
            request_deserializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesReadRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesReadResponse.SerializeToString,
        ),
        "DeliveryLocalityMatrixValuesUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryLocalityMatrixValuesUpdate,
            request_deserializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesUpdateRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesUpdateResponse.SerializeToString,
        ),
        "DeliveryLocalityMatrixValuesDelete": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryLocalityMatrixValuesDelete,
            request_deserializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesDeleteRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.delivery_locality_matrix_values.DeliveryLocalityMatrixValuesService",
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DeliveryLocalityMatrixValuesService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DeliveryLocalityMatrixValuesCreate(
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
            "/pro.omni.oms.api.v1.rules.delivery_locality_matrix_values.DeliveryLocalityMatrixValuesService/DeliveryLocalityMatrixValuesCreate",
            v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesCreateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesCreateResponse.FromString,
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
    def DeliveryLocalityMatrixValuesRead(
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
            "/pro.omni.oms.api.v1.rules.delivery_locality_matrix_values.DeliveryLocalityMatrixValuesService/DeliveryLocalityMatrixValuesRead",
            v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesReadRequest.SerializeToString,
            v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesReadResponse.FromString,
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
    def DeliveryLocalityMatrixValuesUpdate(
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
            "/pro.omni.oms.api.v1.rules.delivery_locality_matrix_values.DeliveryLocalityMatrixValuesService/DeliveryLocalityMatrixValuesUpdate",
            v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesUpdateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesUpdateResponse.FromString,
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
    def DeliveryLocalityMatrixValuesDelete(
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
            "/pro.omni.oms.api.v1.rules.delivery_locality_matrix_values.DeliveryLocalityMatrixValuesService/DeliveryLocalityMatrixValuesDelete",
            v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesDeleteRequest.SerializeToString,
            v1_dot_rules_dot_delivery__locality__matrix__values__pb2.DeliveryLocalityMatrixValuesDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
