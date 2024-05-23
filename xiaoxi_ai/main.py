import os
import django
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xiaoxi.settings_prod')  # 替换为你的settings文件路径
django.setup()

from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser
from xiaoxi_ai.tools.tools import *
_ = load_dotenv(find_dotenv())
llm = ChatOpenAI(model="gpt-3.5-turbo")
tools = [
    get_student_info
]
llm_with_tools = llm.bind_tools(tools) | {
    "functions": JsonOutputToolsParser(),
    "text": StrOutputParser()
}
result = llm_with_tools.invoke("李四的父母是谁？")

print(result)