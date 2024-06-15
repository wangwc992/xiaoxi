'''CREATE TABLE `zn_school_recruit_art` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) DEFAULT NULL COMMENT '院校表ID',
  `strong_majors` varchar(500) DEFAULT NULL COMMENT '优势专业',
  `admission_rate` varchar(200) DEFAULT NULL COMMENT '录取率',
  `fee_apply` varchar(200) DEFAULT NULL COMMENT '申请费用',
  `fee_tuition` varchar(200) DEFAULT NULL COMMENT '学费',
  `fee_book` varchar(200) DEFAULT NULL COMMENT '书本费',
  `fee_life` varchar(200) DEFAULT NULL COMMENT '生活费',
  `fee_traffic` varchar(200) DEFAULT NULL COMMENT '交通费',
  `fee_accommodation` varchar(200) DEFAULT NULL COMMENT '住宿费用',
  `fee_others` varchar(200) DEFAULT NULL COMMENT '其他费用',
  `fee_total` varchar(200) DEFAULT NULL COMMENT '总花费',
  `graduate_majors` text COMMENT '研究生专业',
  `graduate_score_ielts` varchar(200) DEFAULT NULL COMMENT '研究生雅思成绩',
  `graduate_score_toefl` varchar(200) DEFAULT NULL COMMENT '研究生托福成绩',
  `graduate_requirements` text COMMENT '研究生申请要求',
  `graduate_works_requirement` text COMMENT '研究生作品集要求',
  `graduate_apply_deadline` varchar(200) DEFAULT NULL COMMENT '研究生申请截止日期',
  `undergraduate_majors` text COMMENT '本科专业',
  `undergraduate_score_ielts` varchar(200) DEFAULT NULL COMMENT '本科雅思成绩',
  `undergraduate_score_toefl` varchar(200) DEFAULT NULL COMMENT '本科托福成绩',
  `undergraduate_requirements` text COMMENT '本科申请要求',
  `undergraduate_works_requirement` text COMMENT '本科作品集要求',
  `undergraduate_apply_deadline` varchar(200) DEFAULT NULL COMMENT '本科申请截止日期',
  `difficulty_name` varchar(20) DEFAULT NULL COMMENT '申请难度',
  `apply_experience` text COMMENT '申请经验',
  `alumni` text COMMENT '明星校友',
  `delete_status` int(1) DEFAULT '0' COMMENT '是否删除  0-未删除,1-已删除',
  `create_by` int(11) NOT NULL COMMENT '创建人',
  `update_by` int(11) NOT NULL COMMENT '更新人',
  `create_name` varchar(50) DEFAULT NULL COMMENT '创建人名称',
  `update_name` varchar(50) DEFAULT NULL COMMENT '更新人名称',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `application_fee_value` decimal(8,2) DEFAULT NULL COMMENT '申请费值',
  `currency_id` int(11) DEFAULT NULL COMMENT '币种id',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_school` (`school_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=837 DEFAULT CHARSET=utf8mb4 COMMENT='院校艺术生招生表';'''
from datetime import datetime

from xiaoxi_ai.database.mysql import mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur


# 创建实体类
from typing import Optional, Dict, Any
from langchain_core.pydantic_v1 import Field

from pydantic import BaseModel


class ZnSchoolRecruitArt(BaseModel):
    id: Optional[int] = Field(None, description="院校艺术生招生id")
    school_id: Optional[int] = Field(None, description="院校表ID")
    strong_majors: Optional[str] = Field(None, description="优势专业")
    admission_rate: Optional[str] = Field(None, description="录取率")
    fee_apply: Optional[str] = Field(None, description="申请费用")
    fee_tuition: Optional[str] = Field(None, description="学费")
    fee_book: Optional[str] = Field(None, description="书本费")
    fee_life: Optional[str] = Field(None, description="生活费")
    fee_traffic: Optional[str] = Field(None, description="交通费")
    fee_accommodation: Optional[str] = Field(None, description="住宿费用")
    fee_others: Optional[str] = Field(None, description="其他费用")
    fee_total: Optional[str] = Field(None, description="总花费")
    graduate_majors: Optional[str] = Field(None, description="研究生专业")
    graduate_score_ielts: Optional[str] = Field(None, description="研究生雅思成绩")
    graduate_score_toefl: Optional[str] = Field(None, description="研究生托福成绩")
    graduate_requirements: Optional[str] = Field(None, description="研究生申请要求")
    graduate_works_requirement: Optional[str] = Field(None, description="研究生作品集要求")
    graduate_apply_deadline: Optional[str] = Field(None, description="研究生申请截止日期")
    undergraduate_majors: Optional[str] = Field(None, description="本科专业")
    undergraduate_score_ielts: Optional[str] = Field(None, description="本科雅思成绩")
    undergraduate_score_toefl: Optional[str] = Field(None, description="本科托福成绩")
    undergraduate_requirements: Optional[str] = Field(None, description="本科申请要求")
    undergraduate_works_requirement: Optional[str] = Field(None, description="本科作品集要求")
    undergraduate_apply_deadline: Optional[str] = Field(None, description="本科申请截止日期")
    difficulty_name: Optional[str] = Field(None, description="申请难度")
    apply_experience: Optional[str] = Field(None, description="申请经验")
    alumni: Optional[str] = Field(None, description="明星校友")
    delete_status: Optional[int] = Field(0, description="是否删除  0-未删除,1-已删除")
    create_by: Optional[int] = Field(None, description="创建人")
    update_by: Optional[int] = Field(None, description="更新人")
    create_name: Optional[str] = Field(None, description="创建人名称")
    update_name: Optional[str] = Field(None, description="更新人名称")
    create_time: Optional[datetime] = Field(None, description="创建时间")
    update_time: Optional[datetime] = Field(None, description="更新时间")
    application_fee_value: Optional[float] = Field(None, description="申请费值")
    currency_id: Optional[int] = Field(None, description="币种id")

def select_by_id(school_id):
    mySQLConnectCur.execute('select * from zn_school_recruit_art where school_id=%s', (school_id,))
    result = mySQLConnectCur.fetchone()
    if result is None:
        return None
    # Get column names from cursor description
    column_names = [column[0] for column in mySQLConnectCur.description]
    # Convert result tuple to dictionary
    result_dict = dict(zip(column_names, result))
    # result_dict 变成 CountryInfo 对象
    return ZnSchoolRecruitArt(**result_dict)