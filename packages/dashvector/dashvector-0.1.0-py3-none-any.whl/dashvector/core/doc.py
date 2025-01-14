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

from dataclasses import dataclass
from typing import Optional

from dashvector.common.types import *
from dashvector.core.models.collection_meta_status import CollectionMeta
from dashvector.core.proto import dashvector_pb2

__all__ = ["DocBuilder", "Doc"]


@dataclass(frozen=True)
class Doc(object):
    """
    A Doc Instance.

    Args:
        id (str): a primary key for a unique doc.
        vector (Union[List[Union[int, float]]): a vector for a doc.
        fields (Optional[Dict[str, Union[str, int, float, bool]]]): additional attributes of a doc. [optional]
        score (float): a correlation score when use doc query api, default is 0.0.

    Examples
        a_doc_with_float = Doc(id="a", vector=[0.1, 0.2])
        a_doc_with_int = Doc(id="a", vector=[1, 2])
        a_doc_with_fields = Doc(id="a", vector=[0.1, 0.2], fields={'price': 100, 'type': "dress"})
    """

    id: str
    vector: VectorValueType
    fields: Optional[FieldValueType] = None
    score: float = 0.0

    def __dict__(self):
        meta_dict = {}
        if self.id is not None:
            meta_dict['id'] = self.id
        if self.vector is not None:
            if isinstance(self.vector, np.ndarray):
                meta_dict['vector'] = self.vector.astype(np.float32).tolist()
            elif isinstance(self.vector, list):
                meta_dict['vector'] = self.vector
        if self.fields is not None:
            meta_dict['fields'] = self.fields
        if self.score is not None:
            meta_dict['score'] = self.score
        return meta_dict

    def __str__(self):
        return json.dumps(self.__dict__())

    def __repr__(self):
        return self.__str__()


@dataclass(frozen=True)
class HybridDoc(Doc):
    sparse_vector: Optional[SparseVector] = None

    def __dict__(self):
        meta_dict = super().__dict__()
        if self.sparse_vector is not None:
            meta_dict['sparse_values'] = self.sparse_vector.__dict__()
        return meta_dict

    def __str__(self):
        return json.dumps(self.__dict__())

    def __repr__(self):
        return self.__str__()


class DocBuilder(object):
    @staticmethod
    def from_pb(doc: dashvector_pb2.Doc, collection_meta: CollectionMeta):
        if not isinstance(doc, dashvector_pb2.Doc):
            raise DashVectorException(
                code=DashVectorCode.InvalidArgument,
                reason="DashVectorSDK Get Invalid Doc")
        if not isinstance(collection_meta, CollectionMeta):
            raise DashVectorException(
                code=DashVectorCode.InvalidArgument,
                reason="DashVectorSDK Get Invalid collection meta")

        id = doc.id
        score = round(doc.score, 4)
        vector_type = VectorType.get(collection_meta.dtype)
        dimension = collection_meta.dimension

        # vector
        vector = None
        if doc.HasField("vector"):
            vtype = doc.vector.WhichOneof('value_oneof')
            if vtype == "byte_vector":
                vector = list(
                    VectorType.convert_to_dtype(
                        doc.vector.byte_vector,
                        vector_type,
                        dimension))
                if bool(vector):
                    if isinstance(
                            vector[0],
                            bytes) and vector_type == VectorType.INT:
                        vector = [int(v) for v in vector]
                    if isinstance(
                            vector[0],
                            bytes) and vector_type == VectorType.FLOAT:
                        vector = [float(v) for v in vector]
            else:
                vector = list(doc.vector.float_vector.values)

        # fields
        fields = {}
        for field_name, field_value in doc.fields.items():
            ftype = field_value.WhichOneof('value_oneof')
            fields[field_name] = getattr(
                field_value, ftype) if ftype is not None else None

        # sparse_vector
        sparse_vector = None
        if doc.HasField("sparse_values"):
            indices = list(doc.sparse_values.indices)
            values = doc.sparse_values.values
            vtype = values.WhichOneof('value_oneof')
            if vtype == "byte_vector":
                values = list(
                    VectorType.convert_to_dtype(
                        values.byte_vector,
                        vector_type,
                        dimension))
            else:
                values = list(values.float_vector.values)
            sparse_vector = SparseVector(indices=indices, values=values)
        return HybridDoc(id=id,
                         score=score,
                         vector=vector,
                         fields=fields,
                         sparse_vector=sparse_vector)

    @staticmethod
    def from_dict(doc: dict, collection_meta: Optional[CollectionMeta] = None):
        if not isinstance(doc, dict):
            raise DashVectorException(
                code=DashVectorCode.InvalidArgument,
                reason="DashVectorSDK Get Invalid Doc")
        if not isinstance(collection_meta, CollectionMeta):
            raise DashVectorException(
                code=DashVectorCode.InvalidArgument,
                reason="DashVectorSDK Get Invalid collection meta")

        vector_type = VectorType.get(collection_meta.dtype)
        dimension = collection_meta.dimension

        # TODO 1. type 检查

        '''
        id: str
        '''
        id = doc.get("id")
        if not isinstance(id, str):
            raise DashVectorException(
                code=DashVectorCode.InvalidArgument,
                reason="DashVectorSDK Get Invalid Doc id and id must be str")

        '''
        vector: VectorValueType
        '''
        vector = doc.get("vector")
        if 'vector' in doc:
            if not isinstance(vector, list):
                raise DashVectorException(
                    code=DashVectorCode.InvalidArgument,
                    reason="DashVectorSDK Get Invalid Doc vector")
            if len(vector) != dimension:
                raise DashVectorException(
                    code=DashVectorCode.InvalidArgument,
                    reason="DashVectorSDK Get Invalid Doc vector and length is different from dimension")
            vtype = VectorType.get_vector_data_type(type(vector[0]))
            if vtype != vector_type:
                raise DashVectorException(
                    code=DashVectorCode.InvalidArgument,
                    reason="DashVectorSDK Get Invalid Doc vector type")

        '''
        fields: FieldDataType
        '''
        fields = doc.get("fields")

        '''
        score: float
        '''
        if 'score' in doc:
            score = round(float(doc['score']), 4)

        '''
        sparse_vector: SparseVector
        '''
        sparse_vector = None
        if "sparse_values" in doc:
            sparse_map = doc.get("sparse_vector")
            if isinstance(sparse_map, dict) \
                    and "indices" in sparse_vector \
                    and "values" in sparse_vector:
                sparse_vector = SparseVector(indices=sparse_map['indices'],
                                             values=sparse_map['values'])

        return HybridDoc(id, vector, fields, score,
                         sparse_vector=sparse_vector)
