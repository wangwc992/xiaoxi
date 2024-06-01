import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xiaoxi.settings_prod')  # 替换为你的settings文件路径
django.setup()

from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI


from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser
from xiaoxi_ai.tools.tools import *

_ = load_dotenv(find_dotenv())
llm = ChatOpenAI(model="gpt-3.5-turbo")
tools = [
    get_calibration_school
]
llm_with_tools = llm.bind_tools(tools) | {
    "functions": JsonOutputToolsParser(),
    "text": StrOutputParser()
}
result = llm_with_tools.invoke("我清华毕业想去英国的悉尼大学读研究生，专业是计算机科学，雅思7.5，GPA3.5，录取概率多少？")

for function in result['functions']:
    method_name = function['type']
    parameters = function['args']
    action = Action(name=method_name, args=parameters)
    exec_action(tools, action)
