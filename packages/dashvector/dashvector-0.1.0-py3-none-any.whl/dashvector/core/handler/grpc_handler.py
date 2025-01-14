##
#   Copyright 2021 Alibaba, Inc. and its affiliates. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
##

# -*- coding: utf-8 -*-

import grpc

from dashvector.common.error import DashVectorCode, DashVectorException, DashVectorGRPCException
from dashvector.common.handler import RPCHandler, RPCResponse
from dashvector.common.status import Status
from dashvector.core.doc import DocBuilder
from dashvector.core.models.collection_meta_status import CollectionMeta, CollectionStats
from dashvector.core.models.create_collection_request import CreateCollectionRequest
from dashvector.core.models.create_partition_request import CreatePartitionRequest
from dashvector.core.models.delete_collection_request import DeleteCollectionRequest
from dashvector.core.models.delete_doc_request import DeleteDocRequest
from dashvector.core.models.delete_partition_request import DeletePartitionRequest
from dashvector.core.models.describe_collection_request import DescribeCollectionRequest
from dashvector.core.models.describe_partition_request import DescribePartitionRequest
from dashvector.core.models.fetch_doc_request import FetchDocRequest
from dashvector.core.models.get_version_request import GetVersionRequest
from dashvector.core.models.list_collections_request import ListCollectionsRequest
from dashvector.core.models.list_partitions_request import ListPartitionsRequest
from dashvector.core.models.partition_meta_status import PartitionStats
from dashvector.core.models.query_doc_request import QueryDocRequest
from dashvector.core.models.stats_collection_request import StatsCollectionRequest
from dashvector.core.models.stats_partition_request import StatsPartitionRequest
from dashvector.core.models.upsert_doc_request import UpsertDocRequest
from dashvector.core.proto import dashvector_pb2_grpc
from dashvector.version import __version__


class GRPCHandler(RPCHandler):
    def __init__(self, *,
                 endpoint: str,
                 api_key: str = "",
                 timeout: float = 10.0):
        """
        endpoint: str
        """
        if not isinstance(endpoint, str):
            raise DashVectorException(
                code=DashVectorCode.InvalidArgument,
                reason=f"DashVectorSDK GRPCHandler endpoint Type({endpoint}) is Invalid")

        if len(endpoint) <= 0:
            raise DashVectorException(
                code=DashVectorCode.InvalidArgument,
                reason=f"DashVectorSDK GRPCHandler endpoint Empty")

        """
        api_key: str
        """
        if not isinstance(api_key, str):
            raise DashVectorException(
                code=DashVectorCode.InvalidArgument,
                reason=f"DashVectorSDK GRPCHandler api_key Type({api_key}) is Invalid")

        """
        timeout: float
        """
        if isinstance(timeout, float):
            pass
        elif isinstance(timeout, int):
            timeout = float(timeout)
        else:
            raise DashVectorException(
                code=DashVectorCode.InvalidArgument,
                reason=f"DashVectorSDK GRPCHandler timeout Type({timeout}) is Invalid")
        if timeout <= 0.000001:
            timeout = 365.5 * 86400

        super().__init__(endpoint=endpoint,
                         api_key=api_key,
                         timeout=timeout)

        self._channel = grpc.insecure_channel(self._endpoint)
        self._stub = dashvector_pb2_grpc.DashVectorServiceStub(self._channel)
        self._metadata = (("dashvector-auth-token", self._api_key),
                          ("dashvertor-client-version", __version__))

    @classmethod
    def _parse_request_id_from_exception(cls, e: grpc.RpcError):
        for metak, metav in e.trailing_metadata():
            if metak == "request-id":
                return metav
        return ""

    class _GRPCResponse(RPCResponse):
        def __init__(self,
                     future,
                     *,
                     req=None,
                     async_req=False,
                     attr_name=None):

            super().__init__(async_req=async_req)
            self._future = future
            self._attr_name = attr_name
            self._request = req
            self._response = None

        def get(self):
            if self._response is None:
                try:
                    self._response = self._future.result()
                except grpc.RpcError as e:
                    raise DashVectorGRPCException(
                        code=e.code(),
                        reason=e.details(),
                        request_id=GRPCHandler._parse_request_id_from_exception(e))
            if self._response is None:
                return None

            self._request_id = self._response.request_id
            self._code = self._response.code
            self._message = self._response.message
            if self._response.code == DashVectorCode.Success:
                self._parse_output()
            return self

        def _parse_output(self):
            if self._attr_name == "get_version":
                self._output = self._response.version
            elif self._attr_name == "describe_collection":
                self._output = CollectionMeta(self._response.output)
            elif self._attr_name in ("list_collections", "list_partitions"):
                self._output = list(self._response.output)
            elif self._attr_name == "stats_collection":
                self._output = CollectionStats(stats=self._response.output)
            elif self._attr_name == "describe_partition":
                if isinstance(self._request, DescribePartitionRequest):
                    self._output = Status.str(self._response.output)
            elif self._attr_name == "fetch_doc":
                result_docs = {}
                if isinstance(self._request, FetchDocRequest):
                    for doc_id, doc in self._response.output.items():
                        result_docs[doc_id] = DocBuilder.from_pb(
                            doc, self._request.collection_meta)
                self._output = result_docs
            elif self._attr_name == "query_doc":
                result_docs = []
                if isinstance(self._request, QueryDocRequest):
                    for doc in self._response.output:
                        result_docs.append(
                            DocBuilder.from_pb(
                                doc, self._request.collection_meta))
                self._output = result_docs
            elif self._attr_name == "stats_partition":
                if isinstance(self._request, StatsPartitionRequest):
                    self._output = PartitionStats(
                        self._request.partition_name,
                        self._response.output.total_doc_count)

    def create_collection(self,
                          create_request: CreateCollectionRequest,
                          *,
                          async_req: bool = False) -> RPCResponse:
        try:
            rebuild_timeout = self._timeout
            if rebuild_timeout < 30.0:
                rebuild_timeout = 30.0
            rsp = self._stub.create_collection.future(
                create_request.to_proto(),
                metadata=self._metadata,
                timeout=rebuild_timeout)
            return self._GRPCResponse(rsp, async_req=async_req)
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def delete_collection(self,
                          delete_request: DeleteCollectionRequest,
                          *,
                          async_req: bool = False) -> RPCResponse:
        try:
            rebuild_timeout = self._timeout
            if rebuild_timeout < 30.0:
                rebuild_timeout = 30.0
            rsp = self._stub.delete_collection.future(
                delete_request.to_proto(),
                metadata=self._metadata,
                timeout=rebuild_timeout)
            return self._GRPCResponse(rsp, async_req=async_req)
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def describe_collection(self,
                            describe_request: DescribeCollectionRequest,
                            *,
                            async_req: bool = False) -> RPCResponse:
        try:
            rsp = self._stub.describe_collection.future(
                describe_request.to_proto(), metadata=self._metadata, timeout=self._timeout)
            return self._GRPCResponse(
                rsp, async_req=async_req, attr_name='describe_collection')
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def list_collections(self,
                         *,
                         async_req: bool = False) -> RPCResponse:
        try:
            rsp = self._stub.list_collections.future(
                ListCollectionsRequest().to_proto(),
                metadata=self._metadata,
                timeout=self._timeout)
            return self._GRPCResponse(
                rsp, async_req=async_req, attr_name="list_collections")
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def stats_collection(self,
                         stats_request: StatsCollectionRequest,
                         *,
                         async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", stats_request.name),)
            rsp = self._stub.stats_collection.future(stats_request.to_proto(),
                                                     metadata=metadata,
                                                     timeout=self._timeout)
            return self._GRPCResponse(
                rsp, async_req=async_req, attr_name="stats_collection")
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def get_version(self,
                    *,
                    async_req: bool = False) -> RPCResponse:
        try:
            rsp = self._stub.get_version.future(GetVersionRequest().to_proto(),
                                                metadata=self._metadata,
                                                timeout=self._timeout)
            return self._GRPCResponse(
                rsp, async_req=async_req, attr_name="get_version")
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def insert_doc(self,
                   insert_request: UpsertDocRequest,
                   *,
                   async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", insert_request.collection_name),)
            rsp = self._stub.insert_doc.future(insert_request.to_proto(),
                                               metadata=metadata,
                                               timeout=self._timeout)
            return self._GRPCResponse(rsp, async_req=async_req)
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def update_doc(self,
                   update_request: UpsertDocRequest,
                   *,
                   async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", update_request.collection_name),)
            rsp = self._stub.update_doc.future(update_request.to_proto(),
                                               metadata=metadata,
                                               timeout=self._timeout)
            return self._GRPCResponse(rsp, async_req=async_req)
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def upsert_doc(self,
                   upsert_request: UpsertDocRequest,
                   *,
                   async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", upsert_request.collection_name),)
            rsp = self._stub.upsert_doc.future(upsert_request.to_proto(),
                                               metadata=metadata,
                                               timeout=self._timeout)
            return self._GRPCResponse(rsp, async_req=async_req)
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def delete_doc(self,
                   delete_request: DeleteDocRequest,
                   *,
                   async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", delete_request.collection_name),)
            rsp = self._stub.delete_doc.future(delete_request.to_proto(),
                                               metadata=metadata,
                                               timeout=self._timeout)
            return self._GRPCResponse(rsp, async_req=async_req)
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def fetch_doc(self,
                  fetch_request: FetchDocRequest,
                  *,
                  async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", fetch_request.collection_name),)
            rsp = self._stub.fetch_doc.future(fetch_request.to_proto(),
                                              metadata=metadata,
                                              timeout=self._timeout)
            return self._GRPCResponse(
                rsp,
                req=fetch_request,
                async_req=async_req,
                attr_name="fetch_doc")
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def query_doc(self,
                  query_request: QueryDocRequest,
                  *,
                  async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", query_request.collection_name),)
            rsp = self._stub.query_doc.future(query_request.to_proto(),
                                              metadata=metadata,
                                              timeout=self._timeout)
            return self._GRPCResponse(rsp, req=query_request,
                                      attr_name="query_doc",
                                      async_req=async_req)
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def create_partition(self,
                         create_request: CreatePartitionRequest,
                         *,
                         async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", create_request.collection_name),)
            rsp = self._stub.create_partition.future(create_request.to_proto(),
                                                     metadata=metadata,
                                                     timeout=self._timeout)
            return self._GRPCResponse(rsp, async_req=async_req)
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def describe_partition(self,
                           describe_request: DescribePartitionRequest,
                           *,
                           async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", describe_request.collection_name),)
            rsp = self._stub.describe_partition.future(
                describe_request.to_proto(), metadata=metadata, timeout=self._timeout)
            return self._GRPCResponse(
                rsp,
                async_req=async_req,
                req=describe_request,
                attr_name="describe_partition")
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def delete_partition(self,
                         delete_request: DeletePartitionRequest,
                         *,
                         async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", delete_request.collection_name),)
            rsp = self._stub.delete_partition.future(delete_request.to_proto(),
                                                     metadata=metadata,
                                                     timeout=self._timeout)
            return self._GRPCResponse(rsp, async_req=async_req)
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def list_partitions(self,
                        list_request: ListPartitionsRequest,
                        *,
                        async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", list_request.collection_name),)
            rsp = self._stub.list_partitions.future(list_request.to_proto(),
                                                    metadata=metadata,
                                                    timeout=self._timeout)
            return self._GRPCResponse(
                rsp, async_req=async_req, attr_name="list_partitions")
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def stats_partition(self,
                        stats_request: StatsPartitionRequest,
                        *,
                        async_req: bool = False) -> RPCResponse:
        try:
            metadata = self._metadata + \
                (("collection-name", stats_request.collection_name),)
            rsp = self._stub.stats_partition.future(stats_request.to_proto(),
                                                    metadata=metadata,
                                                    timeout=self._timeout)
            return self._GRPCResponse(
                rsp,
                req=stats_request,
                async_req=async_req,
                attr_name="stats_partition")
        except grpc.RpcError as e:
            raise DashVectorGRPCException(
                code=e.code(),
                reason=e.details(),
                request_id=self._parse_request_id_from_exception(e))

    def close(self) -> None:
        self._channel.close()
        return None
