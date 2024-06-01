import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from xiaoxi_ai.MVC.controller.knowledge.knowledge import knowledgeService
from xiaoxi_ai.MVC.model.knowledge.knowledge_model import BaseKnowledgeModel


# Create your views here.
def index(request):
    my_setting_value = settings.MY_SETTING
    # 使用 my_setting_value 执行逻辑
    print(f"The setting value is: {my_setting_value}", settings.MYSQL_HOST,
          settings.MYSQL_USER,
          settings.MYSQL_PASSWD,
          settings.MYSQL_DB)
    print(settings.SECRET_KEY)
    return render(request, 'aiClient.html')


def ask(request):
    model_name = request.headers.get('Model-Name', 'qianfan')
    response = knowledgeService.information_consultant(request.GET['text'], model_name)
    print(response)
    return HttpResponse(response)


def ParsingUrl(request):
    response = knowledgeService.parsingUrl(request.GET['url'])
    # 使用 \n\n 分割变成字符串
    response = "\n\n".join(response)
    return HttpResponse(response)


@csrf_exempt
def addBaseData(request):
    # 获取原始的请求体并解析 JSON 数据
    baseKnowledgeModel = BaseKnowledgeModel(**request.POST.dict())
    response = knowledgeService.addBaseData(baseKnowledgeModel)
    return HttpResponse(response)


@csrf_exempt
def addUrlData(request):
    questions = request.POST['questions']
    list = questions.split("\n\n")
    response = knowledgeService.addUrlData(list)
    return HttpResponse(response)
