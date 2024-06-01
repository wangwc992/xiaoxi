import uvicorn
import xiaoxi_ai.common.text_utils.html_dispose as html_dispose
import xiaoxi_ai.common.text_utils.text_util as text_util

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from xiaoxi_ai.MVC.model.knowledge.knowledge_model import BaseKnowledgeModel
from xiaoxi_ai.MVC.service.knowledge.knowledge import KnowledgeService

app = FastAPI()
router = APIRouter(prefix="/knowledge")
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

knowledgeService = KnowledgeService()


@app.get("/ask")
async def completion(text):
    response = knowledgeService.information_consultant(text)
    return response


@app.post("/ParsingUrl")
async def add_url(url: str):
    soup = html_dispose.getSoup(url)
    title = soup.find('title').get_text() + " "
    reduced_structure = html_dispose.reduced_structure(soup)
    text = html_dispose.cleat_text(html_dispose.process_tags(reduced_structure))
    sentence_list = text_util.split_text_sentence(text, 300, 100)
    # text_list 里面有句子的长度大于600的，进行分割，并且在前面加上异常数据
    new_list = list()
    # sentence_list 里面有句子的长度不大于600的加到new_list里面，否则使用text_util.split_text_str，并且在前面加上异常数据，在加到new_list里面
    for sentence in sentence_list:
        if len(sentence) > 500:
            new_list.extend([f"可能是异常数据：{title}{s}" for s in text_util.split_text_str(sentence, 300, 100)])
        else:
            new_list.append(title + sentence)
    return new_list


@app.post("/addBaseData")
async def addBaseData(baseKnowledgeModel: BaseKnowledgeModel):
    response = knowledgeService.addBaseData(baseKnowledgeModel)
    return response


@app.post("/addUrlData")
async def addUrlData(baseKnowledgeModel: BaseKnowledgeModel):
    list = baseKnowledgeModel.questions.split("\n\n")
    response = knowledgeService.addUrlData(list)
    return response


# 启动命令 允许外网访问
if __name__ == '__main__':
    uvicorn.run("MVC.controller.knowledge.knowledge:app", host="0.0.0.0", port=80)
