import json
import django
import os

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xiaoxi.settings_prod')  # 替换为你的settings文件路径
django.setup()

from langfuse.decorators import langfuse_context, observe
from xiaoxi_ai.database.mysql import ai_chat_log_mapper

from xiaoxi_ai.ai_client.client.langchain_client import LangChain

from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser
from xiaoxi_ai.tools.tools import *
import xiaoxi_ai.ai_client.client.langchain_client as langchain_client
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from xiaoxi_ai.database.redis.redis_client import r
import pickle

langchain_client = langchain_client.LangChain()


def get_chat_history(user_id):
    chat_history_data = r.get(user_id)
    if chat_history_data:
        chat_history = pickle.loads(chat_history_data)
        return chat_history
    else:
        return ChatMessageHistory()  # 如果没有记录则返回一个新的 ChatMessageHistory 对象


# 存储 ChatMessageHistory 对象到 Redis
def save_chat_history(user_id, chat_history):
    chat_history_data = pickle.dumps(chat_history)
    r.set(user_id, chat_history_data)


@observe()
def invoke_gpt(query: str, model_name: str) -> str:
    langfuse_context.update_current_trace(
        user_id="1001",
    )
    user_id = 1001
    chat_history = get_chat_history(user_id)
    print(chat_history.messages)

    query = query
    llm = LangChain().gpt_4o
    tools = [
        intelligent_calibration,
        information_consultant
    ]
    llm_with_tools = llm.bind_tools(tools) | {
        "functions": JsonOutputToolsParser(),
        "text": StrOutputParser()
    }
    result = llm_with_tools.invoke(query)
    print(result)
    ai_message = result['text']
    reference_data = ''

    for function in result['functions']:
        method_name = function['type']
        parameters = function['args']
        action = Action(name=method_name, args=parameters)
        prompt_dic = exec_action(tools, action)

        prompt = ChatPromptTemplate.from_messages(
            [
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template(prompt_dic["prompt"]),
            ]
        ).partial(
            chat_history=chat_history.messages
        )
        resource = langchain_client.invoke_with_handler(prompt.format(), model_name, chat_history)

        response_metadata = resource.response_metadata
        token_usage = response_metadata['token_usage']
        ai_chat_log_mapper.insert_ai_chat_log(resource.id, response_metadata['model_name'], query, prompt_dic,
                                              token_usage['prompt_tokens'], resource.content,
                                              token_usage['completion_tokens']
                                              , token_usage['total_tokens'])
        ai_message = resource.content
        reference_data = prompt_dic["reference_data"]

    response = {
        "reference_data": reference_data,
        "ai_message": ai_message
    }
    chat_history.add_user_message(query)
    chat_history.add_ai_message(ai_message)
    save_chat_history(user_id, chat_history)
    # 将响应转换为 UTF-8 编码的 JSON 字符串
    response_json = json.dumps(response, ensure_ascii=False)

    return response_json


if __name__ == '__main__':
    invoke_gpt('悉尼大学的学费',"gpt_3.5")
    # while True:
    #     user_input = input("输入： ")
    #     invoke_gpt(user_input, "gpt_4o")
