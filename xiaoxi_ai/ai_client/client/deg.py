from langchain_openai import ChatOpenAI

model = ChatOpenAI(api_key='sk-dEYVN5FywLxJXA7VihyJtmALJwJUYISKHvuFPn9UrboUfCU2', base_url='https://api.fe8.cn/v1',
                   model="gpt-3.5-turbo", temperature=0.3)  # 默认是gpt-3.5-turbo
chunks = []
for chunk in model.stream("what color is the sky?"):
    chunks.append(chunk)
    print(chunk.content, end="|", flush=True)