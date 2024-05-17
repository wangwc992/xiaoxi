from xiaoxi_ai.database.elasticsearch import knowledge_es
from xiaoxi_ai.database.weaviate.knowledge_weaviate import KnowledgeWeaviate
from xiaoxi_ai.database.mysql import ai_knowledge_mapper
from xiaoxi_ai.common.text_utils.html_util import HtmlUtils


def insert_data():
    KnowledgeWeaviate().create_collection()
    es = knowledge_es.KnowledgeEs()
    # 获取mysql数据
    for i in range(1000):
        ai_knowledge_list = ai_knowledge_mapper.select_ai_knowledge_by_id(i * 2, 2)
        # 插入weaviate
        uuid_list = KnowledgeWeaviate().insert_data_batch(ai_knowledge_list)
        ai_knowledge_mapper.update_ai_knowledge_uuid(uuid_list)

# mysql数据洗入es
def mysql_to_es():
    es = knowledge_es.KnowledgeEs()
    # 获取mysql数据
    for i in range(1000):
        ai_knowledge_list = ai_knowledge_mapper.select_ai_knowledge_by_id(i * 300 + 3650, 300)
        # 插入es
        for ai_knowledge in ai_knowledge_list:
            print(ai_knowledge.id)
            es.insert_data(ai_knowledge.weaviate_id,
                           HtmlUtils.replace_link_with_url(ai_knowledge.country_name + ' ' + ai_knowledge.school_name + ' ' + ai_knowledge.question),
                           HtmlUtils.replace_link_with_url(ai_knowledge.answer))


if __name__ == '__main__':
    insert_data()