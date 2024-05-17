from xiaoxi_ai.ai_client.client.base_client import BaseClient


class DevAGiClient(BaseClient):
    def __init__(self, api_key="sk-dEYVN5FywLxJXA7VihyJtmALJwJUYISKHvuFPn9UrboUfCU2",
                 base_url="https://api.fe8.cn/v1", model="gpt-3.5-turbo"):
        super().__init__(api_key, base_url, model)


if __name__ == '__main__':
    devAGiClient = DevAGiClient()
    print(devAGiClient.get_completion_content("请问悉尼大学什么时候可以申请免学分"))
