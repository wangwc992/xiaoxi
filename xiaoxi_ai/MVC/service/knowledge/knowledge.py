import json
import time
import os
from langchain_core.prompts import PromptTemplate
from langfuse.decorators import observe, langfuse_context

import xiaoxi_ai.database.mysql.ai_chat_log_mapper as ai_chat_log_mapper
import xiaoxi_ai.common.text_utils.rank as rank
import xiaoxi_ai.database.mysql.ai_knowledge_mapper as ai_knowledge_mapper
from xiaoxi_ai.common.text_utils import html_dispose, text_util

from xiaoxi_ai.database.weaviate.knowledge_weaviate import KnowledgeWeaviate
import xiaoxi_ai.ai_client.client.langchain_client as langchain_client
from xiaoxi_ai.database.elasticsearch.knowledge_es import KnowledgeEs

knowledgeWeaviate = KnowledgeWeaviate()
esClient = KnowledgeEs()
langchain_client = langchain_client.LangChain()


class KnowledgeService:

    @observe()
    def completion(self, query):
        langfuse_context.update_current_trace(
            name="LangChainDemo",
            user_id="1001",
        )
        # 获取向量数据类表
        knowledge_weaviate_list = knowledgeWeaviate.search_hybrid(query, 20)
        print(knowledge_weaviate_list)
        # 获取es数据
        knowledge_es_list = esClient.search(query, 20)
        print(knowledge_es_list)
        # 合并排序
        rrf_list = rank.rrf([knowledge_weaviate_list, knowledge_es_list])
        n = min(10, len(rrf_list))
        reference_data = "\n\n".join([f"reference data{n + 1}: {rrf_list[n]['text']}"
                                      for n in range(n) if 'text' in rrf_list[n]])
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, '../../../prompt/knowledge_prompt.txt')
        template = PromptTemplate.from_file(file_path)
        prompt = template.format(input=query, reference_data=reference_data)
        print('l', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        ai_message = langchain_client.invoke_with_handler(prompt)
        print('l', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        response_metadata = ai_message.response_metadata
        token_usage = response_metadata['token_usage']
        ai_chat_log_mapper.insert_ai_chat_log(ai_message.id, response_metadata['model_name'], query, prompt,
                                              token_usage['prompt_tokens'], ai_message.content,
                                              token_usage['completion_tokens']
                                              , token_usage['total_tokens'])
        response = {
            "reference_data": reference_data,
            "ai_message": ai_message.content
        }

        # 将响应转换为 UTF-8 编码的 JSON 字符串
        response_json = json.dumps(response, ensure_ascii=False)

        return response_json

    def parsingUrl(self, url):
        soup = html_dispose.getSoup(url)
        title = soup.find('title').get_text() + " "
        reduced_structure = html_dispose.reduced_structure(soup)
        text = html_dispose.cleat_text(html_dispose.process_tags(reduced_structure))
        sentence_list = text_util.split_text_sentence(text, 300, 100)
        # text_list 里面有句子的长度大于600的，进行分割，并且在前面加上异常数据
        new_list = list()
        # sentence_list 里面有句子的长度不大于600的加到new_list里面，否则使用text_util.split_text_str，并且在前面加上异常数据，在加到new_list里面
        for sentence in sentence_list:
            if len(sentence) > 500:
                new_list.extend([f"可能是异常数据：{title}{s}" for s in text_util.split_text_str(sentence, 300, 100)])
            else:
                new_list.append(title + sentence)
        return new_list

    def addUrlData(self, data_list: list):
        result_list = []
        for item in data_list:
            if item.startswith("可能是异常数据"):
                continue
            aiKnowledgeDic = {"instruction": item, "output": " "}
            vec = langchain_client.embedding.embed_query(aiKnowledgeDic['instruction'])
            uuid = knowledgeWeaviate.insert_data(aiKnowledgeDic, vec)
            try:
                ai_knowledge_mapper.insert_ai_knowledge(uuid, "", "", item, "")
                result_list.append("成功")
            except:
                knowledgeWeaviate.delete_data_id(uuid)
                result_list.append("添加失败")
        return result_list

    def addBaseData(self, baseKnowledgeModel):
        result_list = []
        print(baseKnowledgeModel)
        # 打印类型
        print(type(baseKnowledgeModel))
        aiKnowledgeDic = {
            "instruction": baseKnowledgeModel.country + ' ' + baseKnowledgeModel.school + ' ' + baseKnowledgeModel.questions,
            "output": baseKnowledgeModel.answer}
        vec = langchain_client.embedding.embed_query(aiKnowledgeDic['instruction'])
        uuid = knowledgeWeaviate.insert_data(aiKnowledgeDic, vec)
        try:
            ai_knowledge_mapper.insert_ai_knowledge(uuid, baseKnowledgeModel.school, baseKnowledgeModel.country,
                                                    baseKnowledgeModel.questions, baseKnowledgeModel.answer)
            result_list.append("添加成功")
        except:
            knowledgeWeaviate.delete_data_id(uuid)
            result_list.append("添加失败")
        return result_list


if __name__ == '__main__':
    # knowledgeService = KnowledgeService()
    template = PromptTemplate.from_file(template_file="../../../prompt/knowledge_prompt.txt")
    print(template)
