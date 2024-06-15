import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xiaoxi.settings_prod')  # 替换为你的settings文件路径
django.setup()

from xiaoxi_ai.ai_client.client import langchain_client
from xiaoxi_ai.database.weaviate.weaviate_client import WeaviateClient

from xiaoxi_ai.MVC.service.school.school_service import School


def creatr():
    global school_id, school
    wea = WeaviateClient("School_project")
    wea.create_collection()
    wea.collections_list_all()
    embedding = langchain_client.LangChain().embedding
    school_service = School()
    school_ids = [32, 36, 34, 56, 55, 79, 92, 38, 98, 95]
    for school_id in school_ids:
        school_dic = school_service.getSchool(school_id)
        for school in school_dic:
            vector = embedding.embed_query(school['instruction'])
            print(wea.insert_data(school, vector))
        project_dic = school_service.getProject(school_id)
        print(project_dic)
        for project in project_dic:
            vector = embedding.embed_query(project['instruction'])
            print(wea.insert_data(project, vector))


def search1(text):
    wea = WeaviateClient("School_project")
    embedding = langchain_client.LangChain().embedding
    vector = embedding.embed_query(text)
    response = wea.search_near_vector(vector)
    print(response)


import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def json_file_add():
    global data
    wea = WeaviateClient("School_project")
    embedding = langchain_client.LangChain().embedding
    file_path = '系统功能介绍-0614.json'
    datas = read_json_file(file_path)
    for data in datas:
        vector = embedding.embed_query(data['instruction'])
        print(wea.insert_data(data, vector))


if __name__ == '__main__':
    search1("悉尼大学的好评")
