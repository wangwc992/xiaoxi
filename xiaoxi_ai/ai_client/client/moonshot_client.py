from xiaoxi_ai.ai_client.client.base_client import BaseClient


class DevAGiClient(BaseClient):
    def __init__(self, api_key="sk-jBtRO21VeFaB71cAHulig0ZqC0CyaFY0CKDp2aHcFVCSikPb",
                 base_url="https://api.moonshot.cn/v1", model="moonshot-v1-32k"):
        super().__init__(api_key, base_url, model)


if __name__ == '__main__':
    devAGiClient = DevAGiClient()
    print(devAGiClient.get_completion_content("你是什么模型"))
