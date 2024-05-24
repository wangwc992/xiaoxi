import os
import django
from langfuse.decorators import observe, langfuse_context

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xiaoxi.settings_prod')  # 替换为你的settings文件路径
django.setup()
import warnings

warnings.filterwarnings("ignore")

from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import JsonOutputToolsParser
from xiaoxi_ai.tools.tools import *

_ = load_dotenv(find_dotenv())
llm = ChatOpenAI(model="gpt-4o")
# print(llm.invoke("李四的父母是谁？"))
tools = [
    search_student_info_tool
]
llm_with_tools = llm.bind_tools(tools) | {
    "functions": JsonOutputToolsParser(),
    "text": StrOutputParser()
}
result = llm_with_tools.invoke("李四的父母是谁？")

print(result)