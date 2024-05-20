import weaviate
from django.conf import settings

import xiaoxi_ai.ai_client.client.langchain_client as langchain_client

from weaviate.classes.config import Property, DataType, Configure
from weaviate.classes.query import HybridFusion, Filter, MetadataQuery, Move, Rerank

langchain_client = langchain_client.LangChain()


class WeaviateClient:
    client = weaviate.connect_to_custom(
        http_host=settings.WEAVIATE_HOST,
        http_port=8080,
        http_secure=False,
        grpc_host="localhost",
        grpc_port=50051,
        grpc_secure=False,
        headers={"X-Huggingface-Api-Key": "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"}
    )

    def __init__(self, collections_name):
        self.collections_name = collections_name
        self.collections = self.client.collections.get(collections_name)

    def collections_list_all(self):
        collections = self.client.collections.list_all()
        for collection in collections:
            print(collection)
        return collections

    def get_collection_config(self):
        articles_config = self.collections.config.get()
        print(articles_config)

    # 查询数据
    def search_hybrid(self, query):
        response = self.collections.query.hybrid(
            query=query,
            fusion_type=HybridFusion.RELATIVE_SCORE,
            target_vector="instruction",
            query_properties=["instruction", "output"],
            return_metadata=MetadataQuery(score=True, explain_score=True),
            limit=10,
        )
        return response

    # 关键字查询数据
    def search_bm25(self, query):
        response = self.collections.query.bm25(
            query=query,
            query_properties=["instruction"],
            return_metadata=MetadataQuery(score=True),
            limit=8
        )
        return response.objects

    # 查询数据
    def search_near_text(self, query):
        response = self.collections.query.near_text(
            query=query,
            limit=10,
            target_vector="instruction",
            return_metadata=MetadataQuery(distance=True)
        )
        return response.objects

    # 查询数据
    def search_near_vector(self, near_vector, limit=10):
        response = self.collections.query.near_vector(
            near_vector=near_vector,
            limit=limit,
            return_metadata=MetadataQuery(distance=True)
        )
        return response

    # 获取全部对象
    def search_all(self, limit):
        response = self.collections.query.fetch_objects(
            limit=limit
        )
        return response.objects

    def search_id(self, uuid):
        data_object = self.collections.query.fetch_object_by_id(uuid)
        print(data_object.properties)

    # 插入数据
    def insert_data_batch(self, aiKnowledgeDictList):
        uuid_list = list()
        for item in aiKnowledgeDictList:
            uuid = self.collections.data.insert(
                properties=item,
            )
            uuid_list.append(uuid)
        return uuid_list

    def insert_data(self, data, vecs):
        return self.collections.data.insert(properties=data, vector=vecs)

    # 更新数据
    def update_data(self, uuid, update_data):
        self.collections.data.update(
            uuid=uuid,
            properties={
                "output": update_data,
            }
        )

    # 删除数据
    def delete_data(self, where):
        self.collections.data.delete_many(
            where=Filter.by_property("title").like("*悉尼*"),
        )

    def delete_all_data(self):
        self.collections.data.delete_all()

    def delete_data_id(self, uuid):
        collection = self.collections.collections.get("EphemeralObject")
        collection.data.delete_by_id(uuid)


if __name__ == '__main__':
    weaviate_client = WeaviateClient("knoledge")
    weaviate_client.collections_list_all()
