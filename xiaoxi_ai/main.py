import os
import django
from langfuse.decorators import langfuse_context, observe

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xiaoxi.settings_prod')  # 替换为你的settings文件路径
django.setup()

from xiaoxi_ai.MVC.controller.knowledge.knowledge import knowledgeService
from xiaoxi_ai.ai_client.client.langchain_client import LangChain

from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser
from xiaoxi_ai.tools.tools import *
import xiaoxi_ai.ai_client.client.langchain_client as langchain_client

langchain_client = langchain_client.LangChain()


@observe()
def invoke_gpt(query):
    langfuse_context.update_current_trace(
        user_id="1001",
    )
    # model_name = request.headers.get('Model-Name', 'qianfan')
    # query = request.GET['text']
    model_name = 'gpt_4o'
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
    #
    # result = {'functions': [{'args': {
    #     'intelligentCalibration': {'background_institution': '帕奈尔中学', 'country_name': '澳洲',
    #                                'school_name_zh': '澳大利亚悉尼大学'}}, 'type': 'intelligentCalibration'}], 'text': ''}

    for function in result['functions']:
        method_name = function['type']
        parameters = function['args']
        action = Action(name=method_name, args=parameters)
        prompt = exec_action(tools, action)
        ai_message = langchain_client.invoke_with_handler(prompt, model_name)
        response= llm.invoke(ai_message)
    else:
        response = knowledgeService.information_consultant(query, model_name)

    print(response)


if __name__ == '__main__':
    invoke_gpt('悉尼大学的学费')
    # while True:
    #     user_input = input("输入： ")
    #     invoke_gpt(user_input)
