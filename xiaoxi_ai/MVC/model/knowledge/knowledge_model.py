from pydantic import BaseModel


class BaseKnowledgeModel(BaseModel):
    school: str
    country: str
    questions: str
    answer: str


class UrlKnowledgeModel(BaseModel):
    school: str
    country: str
    paragraph: str
