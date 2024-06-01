from typing import Optional, Dict, Any
from langchain_core.pydantic_v1 import BaseModel, Field



class IntelligentCalibration(BaseModel):
    grade_type: Optional[str] = Field(None, description="成绩类型, 高考、gpa")
    grade_score: Optional[float] = Field(None, description="学生的成绩")
    background_institution: Optional[str] = Field(None, description="学生的毕业/在读院校")
    IELTS_score: Optional[float] = Field(None, description="学生的雅思分数")
    TOEFL_score: Optional[float] = Field(None, description="学生的托福分数")
    country_name: Optional[str] = Field(None, description="留学的意向国家名称")
    academic_degree: Optional[str] = Field(None, description="留学的学位")
    school_name_zh: Optional[str] = Field(None, description="留学学校的中文名称")
    school_name_en: Optional[str] = Field(None, description="留学学校的英文名称")
    major_name_zh: Optional[str] = Field(None, description="留学专业的中文名称")
    major_name_en: Optional[str] = Field(None, description="留学专业的英文名称")
    # intent_country: Optional[str] = Field(None, description="留学意向的国家")
    first_class_major: Optional[str] = Field(None, description="留学一级专业")
    secondary_major: Optional[str] = Field(None, description="留学二级专业")
    qs_ranking: Optional[int] = Field(None, description="留学学校的QS世界排名")
    length_of_full: Optional[str] = Field(None, description="留学学校的学制")
    semester: Optional[str] = Field(None, description="留学学校的开学时间(月)")
    admission_probability: Optional[float] = Field(None, description="留学学校的录取概率")

    def is_enough_information(self):
        '''
            IntelligentCalibration里面的参数，根据学生提供的信息，
            grade_score，background_institution、country_name、academic_degree、school_name_en、major_name_en、intent_country
            至少需要提供不低于命中的三个信息
        '''
        info_fields = [self.grade_score, self.background_institution, self.country_name, self.academic_degree,
                       self.school_name_en, self.major_name_en]
        provided_info = [field for field in info_fields if field is not None]
        return len(provided_info) >= 3