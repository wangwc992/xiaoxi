import requests


class GaoDeMap:
    __URL = 'https://restapi.amap.com/v5/place/text'
    search_poi = {
        "type": "function",
        "function": {
            "name": "get_location_coordinate",
            "description": "根据POI名称，获得POI的经纬度坐标",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "POI名称，必须是中文",
                    },
                    "city": {
                        "type": "string",
                        "description": "POI所在的城市名，必须是中文",
                    }
                },
                "required": ["location", "city"],
            }
        }
    }

    def __init__(self):
        self.name = '高德地图'

    def invoke(self, location: str, city: str):
        data = {
            "keywords": location,
            "city": city,
            "key": "36d496628b6e082993919ef8095e5d41"
        }
        response = requests.post(self.__URL, data=data)
        return response.json()


class GoogleSearch:
    __URL = 'https://www.googleapis.com/customsearch/v1'
    custom_search_tool = {
        "type": "function",
        "function": {
            "name": "google_custom_search",
            "description": "根据关键字搜索POI",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索关键字",
                    }
                },
                "required": ["query", "key"],
            }
        }
    }

    def __init__(self):
        self.name = '谷歌搜索'

    def invoke(self, query: str):
        data = {
            "q": query,
            "key": "AIzaSyDMB8sbN8UHU58ck0c7WlsjT5JtE8AZRvo",
            "cx": "413ba375f186946a9",
        }
        response = requests.get(self.__URL, params=data)
        return response.json()
