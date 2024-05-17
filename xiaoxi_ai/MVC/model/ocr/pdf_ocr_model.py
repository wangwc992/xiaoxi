from pydantic import BaseModel, Field, validator
from typing import Optional

class PdfOcrModel(BaseModel):
    type: str = Field(description="类型，限制在真实材料、成绩单、语言成绩、护照、在读证明、学位证、毕业证之内")
    name: str = Field(description="姓名")
    isSignature: str = Field(description="在用户输入的资料内，有 学生签名 这四个字的附近有学生的名字就是签名了，获取这个名字")
    signatureDate: str = Field(description="用户输入的资料内，有 签名日期 这四个字的附近的时间就是签名日期，获取这个日期")
    school: str = Field(description="学校")
    major: str = Field(description="入读学校的专业")
    student_number: str = Field(description="在校的学号")
    graduation_date: str = Field(description="毕业时间")
    full_time: str = Field(description="是否为全日制，回答限制在[是、否]")
    isChineseVersion: bool = Field(description="请检查提供的资料，判断其中是否包含中文版本。如果资料中包含任何中文文本，则将 isChineseVersion 设为 True；否则设为 False。请注意，中文版本可以包括中文字符、中文词汇或中文短语。请勿将包含英文或其他语言的资料误判为中文版本")
    isEnglishVersion: bool = Field(description="请检查提供的资料，判断其中是否包含英文版本。如果资料中包含任何英文文本，则将 isEnglishVersion 设为 True；否则设为 False。请注意，英文版本可以包括英文字符、英文词汇或英文短语。请勿将包含中文或其他语言的资料误判为英文版本。")

    # degree: str = Field(description="学位")
    # id: str = Field(description="身份证号")
    # passport: str = Field(description="护照号")
    # language: str = Field(description="语言")
    # reading: str = Field(description="阅读")
    # graduate: str = Field(description="毕业")
    # transcript: str = Field(description="成绩单")
    # real: str = Field(description="真实")
    # status: str = Field(description="状态")
    # other: str = Field(description="其他")
    # gender: str = Field(description="性别")
    # dateOfBirth: str = Field(description="出生日期")
    # enrollmentTime: str = Field(description="入学时间")
    # isChineseAndEnglishVersion: str = Field(description="中英文版本")


