from django.conf import settings
from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.runnables import ConfigurableField
from langchain_openai import ChatOpenAI
from dotenv import find_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langfuse.decorators import langfuse_context
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from dotenv import load_dotenv
import os
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory

# 加载.env文件
_ = load_dotenv(find_dotenv())

# 加载.env文件
load_dotenv(".env")
OPENAI_MODEL_35 = os.getenv("OPENAI_MODEL_35")
OPENAI_MODEL_4o = os.getenv("OPENAI_MODEL_4o")

LLM_MODEL_PATH = settings.LLM_MODEL_PATH
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}


class LangChain:
    # 模型1
    qianfan = QianfanChatEndpoint(
        qianfan_ak='nhW0x9Tocm3ZvyhldiBw6gen',
        qianfan_sk='DS9MyuRcxcyn5fCUyFUqBkvs7ksYxTuX',
        model='ERNIE-3.5-8K',
        temperature=0.3,
    )
    qianfan_4 = QianfanChatEndpoint(
        qianfan_ak='92uPuxpuGvrPYQtDtKGs3rNV',
        qianfan_sk='gTcPd1eZUTT7ZK6zuvIsdS1M2rlpLSrB',
        model='ERNIE-4.0-8K',
        temperature=0.3,
    )
    gpt_3 = ChatOpenAI(model=OPENAI_MODEL_35, temperature=0.3)  # 默认是gpt-3.5-turbo
    gpt_4o = ChatOpenAI(model=OPENAI_MODEL_4o, temperature=0.3)  # 默认是gpt-3.5-turbo

    # 通过 configurable_alternatives 按指定字段选择模型
    llm = gpt_3.configurable_alternatives(
        ConfigurableField(id="llm"),
        default_key="gpt3.5",
        qianfan=qianfan,
        gpt_4o=gpt_4o,
        qianfan_4=qianfan_4,
        # claude=claude_model,
    )

    def invoke_with_handler(self, input, model_name="gpt3.5"):
        langfuse_context.update_current_trace(
            metadata={"model_name": model_name},
            # 添加模型名称的标签
            tags=[model_name]
        )
        langfuse_handler = langfuse_context.get_current_langchain_handler()
        ai_message = self.llm.with_config(
            configurable={"llm": model_name}
        ).invoke(input=input, config={"callbacks": [langfuse_handler]})
        return ai_message

    embedding = HuggingFaceEmbeddings(
        model_name=LLM_MODEL_PATH + "BAAI/bge-large-zh-v1.5",
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

    # 使用本地模型
    tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL_PATH + "BAAI/bge-reranker-large")
    model = AutoModelForSequenceClassification.from_pretrained(LLM_MODEL_PATH + "BAAI/bge-reranker-large")
    nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

    def reranker_list_str(self, user_query, search_results):
        '''
        大模型语言排序
        :param user_query:  查询的内容
        :param search_results:  排序列表
        :return:
        '''
        scores = [self.nlp(f"{user_query} {doc.properties['instruction']}")[0]['score'] for doc in search_results]

        # 按得分排序
        sorted_list = sorted(
            zip(scores, [doc.properties['instruction'] for doc in search_results]), key=lambda x: x[0], reverse=True)
        for score, doc in sorted_list:
            print(f"{score}\t{doc}\n")

    def reranker_model(self, user_query, model_list):
        search_results = [(doc.instruction) for doc in model_list]

        scores = [self.nlp(f"{user_query} {doc}")[0]['score'] for doc in search_results]

        # 按得分排序
        sorted_list = sorted(
            zip(scores, [doc for doc in search_results]), key=lambda x: x[0], reverse=True)

        sorted_dict = {doc: score for score, doc in sorted_list}

        model_list.sort(key=lambda x: sorted_dict.get(x.instruction, 0), reverse=True)
        return model_list


if __name__ == '__main__':
    langchain = LangChain()
    print(langchain.llm.invoke("请问悉尼大学什么时候可以申请免学分"))
    # print(langchain.embedding.embed_query("请问悉尼大学什么时候可以申请免学分"))
