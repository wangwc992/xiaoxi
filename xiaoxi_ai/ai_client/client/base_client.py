from openai import OpenAI


class BaseClient:

    def __init__(self, api_key, base_url, model):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )
        self.model = model

    def get_completion_response(self, prompt, response_format="text", model=None):
        model = model or self.model
        messages = [{"role": "user", "content": prompt}]
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,  # 模型输出的随机性，0 表示随机性最小
            # 返回消息的格式，text 或 json_object
            response_format={"type": response_format},
        )
        return response

    def get_completion_content(self, prompt, response_format="text", model=None):
        model = model or self.model
        response = self.get_completion_response(prompt, response_format, model)
        return response.choices[0].message.content
