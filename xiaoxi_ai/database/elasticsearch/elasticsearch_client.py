from django.conf import settings
from elasticsearch7.client import Elasticsearch


class EsClient:
    es = Elasticsearch(
        hosts=[settings.ES_HOST],  # 服务地址与端口
        # http_auth=("elastic", "FKaB1Jpz0Rlw0l6G"),  # 用户名，密码
    )

    def __init__(self, index_name):
        self.index_name = index_name

    def search_data(self, query, top_n=10):
        # ES 的查询语言
        search_query = {
            "query": {
                "match": query
            }
        }
        res = self.es.search(index=self.index_name, size=top_n, **search_query)
        return res["hits"]["hits"]

    def insert_data(self, uuid, instruction, output):
        document = {
            "uuid": uuid,
            "instruction": instruction,
            "output": output
        }
        res = self.es.index(index=self.index_name, id=uuid, document=document)
        return res

    def delete_all_data(self):
        query = {"query": {"match_all": {}}}
        res = self.es.delete_by_query(index=self.index_name, body=query)
        return res


if __name__ == "__main__":
    esClient = esClient("ai_knowledge")
    keyword_search_results = esClient.search_data("悉尼")
    print(keyword_search_results)
