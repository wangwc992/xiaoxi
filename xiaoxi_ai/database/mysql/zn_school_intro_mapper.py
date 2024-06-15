'''CREATE TABLE `zn_school_intro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) DEFAULT NULL COMMENT '院校表ID',
  `introduction` text COMMENT '院校简介',
  `international_ratio` varchar(200) DEFAULT NULL COMMENT '国际学生比例',
  `faculty_ratio` varchar(200) DEFAULT NULL COMMENT '师生比例',
  `boy_girl_ratio` varchar(200) DEFAULT NULL COMMENT '男女比例',
  `student_amount` varchar(200) DEFAULT NULL COMMENT '学生总数量',
  `undergraduate_amount` varchar(200) DEFAULT NULL COMMENT '本科生数量',
  `graduate_amount` varchar(200) DEFAULT NULL COMMENT '研究生数量',
  `employment_rate` varchar(200) DEFAULT NULL COMMENT '就业率',
  `employment_salary` varchar(200) DEFAULT NULL COMMENT '毕业薪资',
  `history` text COMMENT '院校历史',
  `location` text COMMENT '地理位置',
  `campus` text COMMENT '校园环境',
  `accommodation` text COMMENT '学校宿舍',
  `library` text COMMENT '图书馆',
  `installation` text COMMENT '学校设施',
  `admissions_office` text COMMENT '招生办信息',
  `covid_rule` text COMMENT '防疫信息',
  `video_url` varchar(255) DEFAULT NULL COMMENT '介绍视频url',
  `delete_status` int(1) DEFAULT '0' COMMENT '是否删除  0-未删除,1-已删除',
  `create_by` int(11) NOT NULL COMMENT '创建人',
  `update_by` int(11) NOT NULL COMMENT '更新人',
  `create_name` varchar(50) DEFAULT NULL COMMENT '创建人名称',
  `update_name` varchar(50) DEFAULT NULL COMMENT '更新人名称',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_school` (`school_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=20505 DEFAULT CHARSET=utf8mb4;'''

from datetime import datetime

from xiaoxi_ai.database.mysql import mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur


# 创建实体类
from typing import Optional, Dict, Any
from langchain_core.pydantic_v1 import Field

from pydantic import BaseModel


class ZnSchoolIntro(BaseModel):
    id: Optional[int] = Field(None, description="院校简介id")
    school_id: Optional[int] = Field(None, description="院校表ID")
    introduction: Optional[str] = Field(None, description="院校简介")
    international_ratio: Optional[str] = Field(None, description="国际学生比例")
    faculty_ratio: Optional[str] = Field(None, description="师生比例")
    boy_girl_ratio: Optional[str] = Field(None, description="男女比例")
    student_amount: Optional[str] = Field(None, description="学生总数量")
    undergraduate_amount: Optional[str] = Field(None, description="本科生数量")
    graduate_amount: Optional[str] = Field(None, description="研究生数量")
    employment_rate: Optional[str] = Field(None, description="就业率")
    employment_salary: Optional[str] = Field(None, description="毕业薪资")
    history: Optional[str] = Field(None, description="院校历史")
    location: Optional[str] = Field(None, description="地理位置")
    campus: Optional[str] = Field(None, description="校园环境")
    accommodation: Optional[str] = Field(None, description="学校宿舍")
    library: Optional[str] = Field(None, description="图书馆")
    installation: Optional[str] = Field(None, description="学校设施")
    admissions_office: Optional[str] = Field(None, description="招生办信息")
    covid_rule: Optional[str] = Field(None, description="防疫信息")
    video_url: Optional[str] = Field(None, description="介绍视频url")
    delete_status: Optional[int] = Field(0, description="是否删除  0-未删除,1-已删除")
    create_by: Optional[int] = Field(None, description="创建人")
    update_by: Optional[int] = Field(None, description="更新人")
    create_name: Optional[str] = Field(None, description="创建人名称")
    update_name: Optional[str] = Field(None, description="更新人名称")
    create_time: Optional[datetime] = Field(None, description="创建时间")
    update_time: Optional[datetime] = Field(None, description="更新时间")

def select_by_id(school_id):
    mySQLConnectCur.execute('select * from zn_school_intro where school_id=%s', (school_id,))
    result = mySQLConnectCur.fetchone()
    if result is None:
        return None

    # Get column names from cursor description
    column_names = [column[0] for column in mySQLConnectCur.description]

    # Convert result tuple to dictionary
    result_dict = dict(zip(column_names, result))
    # result_dict 变成 CountryInfo 对象
    return ZnSchoolIntro(**result_dict)

