import os
import django
from langfuse.decorators import observe, langfuse_context

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xiaoxi.settings_dev')  # 替换为你的settings文件路径
django.setup()

from xiaoxi_ai.database.elasticsearch import knowledge_es
from xiaoxi_ai.database.weaviate.knowledge_weaviate import KnowledgeWeaviate
from xiaoxi_ai.database.mysql import ai_knowledge_mapper
from xiaoxi_ai.common.text_utils.html_util import HtmlUtils


@observe()
def insert_data():
    langfuse_context.update_current_trace(
        name="insert_data",
        user_id="wzr",
    )
    KnowledgeWeaviate().create_collection()
    es = knowledge_es.KnowledgeEs()
    # 获取mysql数据
    i = 0
    while True:
        ai_knowledge_list = ai_knowledge_mapper.select_ai_knowledge_by_id(i * 300, 10)
        if not ai_knowledge_list:
            break
        # 遍历出 weaviate_id 为空的数据
        for ai_knowledge in ai_knowledge_list:
            if ai_knowledge.weaviate_id is not None:
                ai_knowledge_list.remove(ai_knowledge)
        # 插入weaviate
        uuid_list = KnowledgeWeaviate().insert_data_batch(ai_knowledge_list)
        print(uuid_list)
        # 插入es
        for ai_knowledge in ai_knowledge_list:
            es.insert_data(ai_knowledge.weaviate_id,
                           HtmlUtils.replace_link_with_url(
                               ai_knowledge.country_name + ' ' + ai_knowledge.school_name + ' ' + ai_knowledge.question),
                           HtmlUtils.replace_link_with_url(ai_knowledge.answer))
        # 更新mysql数据
        ai_knowledge_mapper.update_ai_knowledge_uuid(uuid_list)
        i += 1


if __name__ == '__main__':
    insert_data()
