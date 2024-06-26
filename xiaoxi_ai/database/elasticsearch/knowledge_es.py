import time

from langfuse.decorators import observe
from pydantic import BaseModel

from xiaoxi_ai.database.elasticsearch.elasticsearch_client import EsClient


class KnowledgeEsModel(BaseModel):
    uuid: str
    instruction: str
    output: str


class KnowledgeEs(EsClient):

    def __init__(self):
        super().__init__("ai_knowledge")

    @observe()
    def search(self, query, top_n=10):
        query = {"instruction": query}
        res = super().search_data(query, top_n)
        response_list = list()
        for hit in res:
            source = hit['_source']
            knowledgeEsModel = KnowledgeEsModel(uuid=source['uuid'], instruction=source['instruction'],
                                                output=source['output'])
            response_list.append(knowledgeEsModel)
        return response_list
