# ai_client: 这是放AI客户端的目录。

# common: 这是一个包含项目中使用的公共实用程序和辅助函数的模块。

# controller: 这个模块控制应用程序中的数据流，并与视图交互以渲染最终输出。

# database: 这个模块处理所有数据库操作，如连接、查询和管理数据。

# embedding: 这个模块用于将输入数据转换为AI模型可以处理的格式。

# function_callingLLM: 这个模块负责调用LLM（语言模型）函数。

# prompt: 这个模块用于处理和处理用户提示。

# service: 这个模块提供了在应用程序中使用的服务，如API服务。

# venv: 这是安装项目依赖项的虚拟环境。

# .env: 这个文件包含在项目中使用的环境变量。保护这个文件的安全非常重要，不应将其推送到公共仓库。

# 包的安装

# 为了安装项目的依赖项，我们需要创建一个虚拟环境并激活它。然后，我们可以使用以下命令安装项目的依赖项：

    pip3.12 install openai: 安装openAi的包
    pip3.12 install --upgrade langchain: 安装langchain的包
    pip3.12 install --upgrade langchain-openai: 安装langchain-openai的包
    pip3.12 install --upgrade langchain_community: 安装langchain_community的包
    pip3.12 install python-dotenv langchain-openai: 安装python-dotenv的包,degAGI
    pip3.12 install transformers: 安装transformers的包,用于调用transformers模型
    pip3.12 install sentence_transformers # 安装sentence_transformers的包,用于将输入数据转换为AI模型可以处理的格式
    pip3.12 install -U weaviate-client: 安装weaviate-client的包,用于调用LLM（语言模型）函数,操作weaviate向量数据库
    pip3.12 install elasticsearch7: 安装elasticsearch的包,用于操作elasticsearch数据库
    pip3.12 install mysqlclient: 安装mysqlclient的包,用于操作mysql数据库
    pip3.12 install nltk
    pip3.12 install fastapi