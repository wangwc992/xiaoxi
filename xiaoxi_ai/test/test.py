from dotenv import load_dotenv, find_dotenv
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

_ = load_dotenv(find_dotenv())
model = "gpt-3.5-turbo"
model = "gpt-4-turbo"
model = "gpt-4o"
llm = ChatOpenAI(model=model)  # 默认是gpt-3.5-turbo

model_name = "BAAI/bge-large-zh-v1.5"
model_path = "D:\\LLM\\BAAI\\bge-large-zh-v1.5"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embedding = HuggingFaceEmbeddings(
    model_name=model_path,  # model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
def test1():
    template = PromptTemplate.from_file(template_file="../prompt/knowledge_prompt.txt")
    print("===Template===")
    print(template)
    print("===Prompt===")
    print(template.format(input='黑色幽默', reference_data='asdfdsaf'))


def test2():
    template = PromptTemplate.from_file(template_file="../prompt/pdf_ocr_prompt.txt")
    print("===Template===")
    print(template)
    print("===Prompt===")

    print(template.format(query='黑色幽默',
                          format_instructions={"format_instructions": ' parser.get_format_instructions()'}))


def test3():
    from langchain_community.embeddings import HuggingFaceEmbeddings

    model_name = "BAAI/bge-large-zh-v1.5"
    model_path = "D:\\LLM\\BAAI\\bge-large-zh-v1.5"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    hf = HuggingFaceEmbeddings(
        model_name=model_path,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    print(hf.embed_query("黑色幽默"))
    lit = ["黑色幽默","巴啦啦能量"]
    em = hf.embed_documents(lit)
    print(em)

def lect():
    _ = load_dotenv(find_dotenv())
    model = "gpt-3.5-turbo"
    llm = ChatOpenAI(model=model)  # 默认是gpt-3.5-turbo

    model_name = "BAAI/bge-large-zh-v1.5"
    model_path = "D:\\LLM\\BAAI\\bge-large-zh-v1.5"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    Embedding = HuggingFaceEmbeddings(
        model_name=model_path,  # model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    prompt = ChatPromptTemplate.from_template("请问{text}怎么样")
    # LCEL 表达式
    runnable = (
            {"text": RunnablePassthrough()} | prompt | llm | StrOutputParser()
    )
    print(runnable.invoke("悉尼大学"))

def function_calling():
    from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser
    from langchain_core.tools import tool

    @tool
    def multiply(first_int: int, second_int: int) -> int:
        """两个整数相乘"""
        return first_int * second_int

    tools = [multiply]
    # 带有分支的 LCEL
    llm_with_tools = llm.bind_tools(tools) | {
        "functions": JsonOutputToolsParser(),
        "text": StrOutputParser()
    } | llm

    result = llm_with_tools.invoke("1024乘16是多少")

    print(result)

if __name__ == '__main__':
    test1()
    # function_calling()
