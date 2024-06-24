import time

from langfuse.decorators import observe
from pydantic import BaseModel
from weaviate.classes.config import Property, DataType, Configure
from weaviate.collections.classes.grpc import HybridFusion, MetadataQuery

from xiaoxi_ai.common.text_utils.html_util import HtmlUtils
from xiaoxi_ai.database.weaviate.weaviate_client import WeaviateClient
import xiaoxi_ai.ai_client.client.langchain_client as langchain_client

from typing import Optional


class KnowledgeWeaviateModel(BaseModel):
    uuid: Optional[str]
    instruction: str
    output: str


class KnowledgeWeaviate(WeaviateClient):
    langChain = langchain_client.LangChain()

    def __init__(self):
        super().__init__("AiKnowledge")
        self.collections_name = "AiKnowledge"

    def create_collection(self):
        if not self.client.collections.exists(self.collections_name):
            self.client.collections.create(
                self.collections_name,
                properties=[
                    Property(name="instruction", data_type=DataType.TEXT),
                    Property(name="input", data_type=DataType.TEXT),
                    Property(name="output", data_type=DataType.TEXT),
                ],
                vector_index_config=Configure.VectorIndex.hnsw()
            )

    def create_model_collection(self):
        '''
        创建collection,带矢量化模块的
        :return:
        '''
        model_name = langchain_client.LLM_MODEL_PATH + "BAAI/bge-large-zh-v1.5"
        self.client.collections.create(
            self.collections_name,
            properties=[  # Define properties
                Property(name="instruction", data_type=DataType.TEXT),
                Property(name="output", data_type=DataType.TEXT),
            ],

            vectorizer_config=[
                # Set a named vector
                Configure.NamedVectors.text2vec_huggingface(  # Set the vectorizer
                    name="instruction",  # Set a named vector
                    source_properties=["instruction"],  # Set the source property(ies)
                    model=model_name,  # Set the model,可以不写
                    vector_index_config=Configure.VectorIndex.hnsw(),  # Set the vector index configuration（default）
                ),
                Configure.NamedVectors.text2vec_huggingface(
                    name="output",
                    source_properties=["instruction"],
                    model=model_name,
                    vector_index_config=Configure.VectorIndex.hnsw(),
                )
            ],
        )

    def insert_data_batch(self, aiKnowledgeDictList):
        knowledge_weaviate_model_list = [{"instruction": HtmlUtils.replace_link_with_url(
            ai_knowledge.country_name + ' ' + ai_knowledge.school_name + ' ' + ai_knowledge.question),
            "output": HtmlUtils.replace_link_with_url(ai_knowledge.answer)}
            for ai_knowledge in aiKnowledgeDictList]
        documents = [doc['instruction'] for doc in knowledge_weaviate_model_list]
        doc_vecs = self.langChain.embedding.embed_documents(documents)
        uuid_list = []
        with self.collections.batch.dynamic() as batch:
            for i, data_row in enumerate(knowledge_weaviate_model_list):
                uuid = batch.add_object(
                    properties=data_row,
                    vector=doc_vecs[i]
                )
                uuid_list.append({'uuid': str(uuid), 'id': aiKnowledgeDictList[i].id})
        return uuid_list

    @observe()
    def search_hybrid(self, query, limit):
        response = self.collections.query.hybrid(
            query=query,
            fusion_type=HybridFusion.RELATIVE_SCORE,
            # target_vector="instruction",
            vector=self.langChain.embedding.embed_query(query),
            query_properties=["instruction", "output"],
            return_metadata=MetadataQuery(score=True, explain_score=True),
            limit=limit,
        )
        response_list = []
        for o in response.objects:
            knowledge_weaviate_model = KnowledgeWeaviateModel(uuid=str(o.uuid), instruction=o.properties['instruction'],
                                                              output=o.properties['output'])
            response_list.append(knowledge_weaviate_model)
        # 重排序
        # print('r',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # response_list = self.langChain.reranker_model(query, response_list)
        # print('r',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        return response_list

    def search_near_vector(self, query, limit=20):
        vec_list = self.langChain.embedding.embed_query(query)
        response = super().search_near_vector(vec_list, limit)
        response_list = []
        for o in response.objects:
            knowledge_weaviate_model = KnowledgeWeaviateModel(uuid=str(o.uuid), instruction=o.properties['instruction'],
                                                              output=o.properties['output'])
            response_list.append(knowledge_weaviate_model)
        # 重排序
        # response_list = self.langChain.reranker_model(query, response_list)
        return response_list

    def delete_data_id(self, uuid):
        self.collections.data.delete_by_id(uuid)


if __name__ == '__main__':
    knowledgeWeaviate = KnowledgeWeaviate()
    print(knowledgeWeaviate.search_hybrid("悉尼大学申请免学分", 10))
