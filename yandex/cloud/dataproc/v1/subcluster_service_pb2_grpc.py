# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.dataproc.v1 import subcluster_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__pb2
from yandex.cloud.dataproc.v1 import subcluster_service_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class SubclusterServiceStub(object):
  """A set of methods for managing Data Proc subclusters.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.dataproc.v1.SubclusterService/Get',
        request_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.GetSubclusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__pb2.Subcluster.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.dataproc.v1.SubclusterService/List',
        request_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.ListSubclustersRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.ListSubclustersResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.dataproc.v1.SubclusterService/Create',
        request_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.CreateSubclusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Update = channel.unary_unary(
        '/yandex.cloud.dataproc.v1.SubclusterService/Update',
        request_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.UpdateSubclusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.dataproc.v1.SubclusterService/Delete',
        request_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.DeleteSubclusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )


class SubclusterServiceServicer(object):
  """A set of methods for managing Data Proc subclusters.
  """

  def Get(self, request, context):
    """Returns the specified subcluster.

    To get the list of all available subclusters, make a [SubclusterService.List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Retrieves a list of subclusters in the specified cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates a subcluster in the specified cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Updates the specified subcluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes the specified subcluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SubclusterServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.GetSubclusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__pb2.Subcluster.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.ListSubclustersRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.ListSubclustersResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.CreateSubclusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.UpdateSubclusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.DeleteSubclusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.dataproc.v1.SubclusterService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
