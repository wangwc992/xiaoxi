import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from xiaoxi_ai.MVC.controller.knowledge.knowledge import knowledgeService
from xiaoxi_ai.MVC.model.knowledge.knowledge_model import BaseKnowledgeModel


# Create your views here.
def index(request):
    print('index')
    return render(request, 'aiClient.html')


def ask(request):
    response = knowledgeService.completion(request.GET['text'])
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
    data = json.loads(request.body.decode('utf-8'))
    baseKnowledgeModel = BaseKnowledgeModel(**data)
    response = knowledgeService.addBaseData(baseKnowledgeModel)
    return HttpResponse(response)


@csrf_exempt
def addUrlData(request):
    data = json.loads(request.body)
    questions = data['questions']
    list = questions.split("\n\n")
    response = knowledgeService.addUrlData(list)
    return HttpResponse(response)
