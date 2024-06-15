'''CREATE TABLE `zn_school_recruit_graduate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) DEFAULT NULL COMMENT '院校表ID',
  `recruit_type` int(1) DEFAULT NULL COMMENT '招生类型 1本科 2研究生',
  `introduction` text COMMENT '申请简介',
  `admission_rate` varchar(200) DEFAULT NULL COMMENT '录取率',
  `time_apply_deadline` varchar(300) DEFAULT NULL COMMENT '申请截止时间',
  `apply_amount` varchar(200) DEFAULT NULL COMMENT '申请人数',
  `semester` varchar(200) DEFAULT NULL COMMENT '申请学期',
  `time_offer` varchar(200) DEFAULT NULL COMMENT 'Offer发放时间',
  `fee_apply` varchar(200) DEFAULT NULL COMMENT '申请费用',
  `fee_tuition` varchar(300) DEFAULT NULL COMMENT '学费',
  `fee_book` varchar(200) DEFAULT NULL COMMENT '书本费',
  `fee_life` varchar(200) DEFAULT NULL COMMENT '生活费',
  `fee_traffic` varchar(200) DEFAULT NULL COMMENT '交通费',
  `fee_accommodation` varchar(200) DEFAULT NULL COMMENT '住宿费用',
  `fee_others` varchar(200) DEFAULT NULL COMMENT '其他费用',
  `fee_total` varchar(200) DEFAULT NULL COMMENT '总花费',
  `score_gpa` varchar(500) DEFAULT NULL COMMENT 'GPA成绩',
  `score_act` varchar(200) DEFAULT NULL COMMENT 'ACT成绩',
  `score_sat` varchar(200) DEFAULT NULL COMMENT 'SAT成绩',
  `score_sat2` varchar(200) DEFAULT NULL COMMENT 'SAT2成绩',
  `score_gre` varchar(200) DEFAULT NULL COMMENT 'GRE成绩',
  `score_gmat` varchar(200) DEFAULT NULL COMMENT 'GMAT成绩',
  `score_ielts` varchar(500) DEFAULT NULL COMMENT '雅思成绩',
  `score_toefl` varchar(500) DEFAULT NULL COMMENT '托福成绩',
  `score_native` varchar(200) DEFAULT NULL COMMENT 'native成绩',
  `score_others` varchar(500) DEFAULT NULL COMMENT '其他成绩',
  `scholarship` text COMMENT '奖学金',
  `material` text COMMENT '申请材料',
  `recruit_flow` text COMMENT '申请流程',
  `delete_status` int(1) DEFAULT '0' COMMENT '是否删除  0-未删除,1-已删除',
  `create_by` int(11) NOT NULL COMMENT '创建人',
  `update_by` int(11) NOT NULL COMMENT '更新人',
  `create_name` varchar(50) DEFAULT NULL COMMENT '创建人名称',
  `update_name` varchar(50) DEFAULT NULL COMMENT '更新人名称',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `application_fee_value` decimal(8,2) DEFAULT NULL COMMENT '申请费值',
  `currency_id` int(11) DEFAULT NULL COMMENT '币种id',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `uk_school` (`school_id`,`recruit_type`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16273 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='院校本研招生表';'''


from xiaoxi_ai.database.mysql import mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur


# 创建实体类
from typing import Optional, Dict, Any
from langchain_core.pydantic_v1 import Field

from pydantic import BaseModel
from datetime import datetime

class ZnSchoolRecruitGraduate(BaseModel):
    id: Optional[int] = Field(None, description="院校本研招生id")
    school_id: Optional[int] = Field(None, description="院校表ID")
    recruit_type: Optional[int] = Field(None, description="招生类型 1本科 2研究生")
    introduction: Optional[str] = Field(None, description="申请简介")
    admission_rate: Optional[str] = Field(None, description="录取率")
    time_apply_deadline: Optional[str] = Field(None, description="申请截止时间")
    apply_amount: Optional[str] = Field(None, description="申请人数")
    semester: Optional[str] = Field(None, description="申请学期")
    time_offer: Optional[str] = Field(None, description="Offer发放时间")
    fee_apply: Optional[str] = Field(None, description="申请费用")
    fee_tuition: Optional[str] = Field(None, description="学费")
    fee_book: Optional[str] = Field(None, description="书本费")
    fee_life: Optional[str] = Field(None, description="生活费")
    fee_traffic: Optional[str] = Field(None, description="交通费")
    fee_accommodation: Optional[str] = Field(None, description="住宿费用")
    fee_others: Optional[str] = Field(None, description="其他费用")
    fee_total: Optional[str] = Field(None, description="总花费")
    score_gpa: Optional[str] = Field(None, description="GPA成绩")
    score_act: Optional[str] = Field(None, description="ACT成绩")
    score_sat: Optional[str] = Field(None, description="SAT成绩")
    score_sat2: Optional[str] = Field(None, description="SAT2成绩")
    score_gre: Optional[str] = Field(None, description="GRE成绩")
    score_gmat: Optional[str] = Field(None, description="GMAT成绩")
    score_ielts: Optional[str] = Field(None, description="雅思成绩")
    score_toefl: Optional[str] = Field(None, description="托福成绩")
    score_native: Optional[str] = Field(None , description="native成绩")
    score_others: Optional[str] = Field(None, description="其他成绩")
    scholarship: Optional[str] = Field(None, description="奖学金")
    material: Optional[str] = Field(None, description="申请材料")
    recruit_flow: Optional[str] = Field(None, description="申请流程")
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
    mySQLConnectCur.execute('select * from zn_school_recruit_graduate where school_id=%s', (school_id,))
    result = mySQLConnectCur.fetchone()
    if result is None:
        return None
    # Get column names from cursor description
    column_names = [column[0] for column in mySQLConnectCur.description]
    # Convert result tuple to dictionary
    result_dict = dict(zip(column_names, result))
    # result_dict 变成 CountryInfo 对象
    return ZnSchoolRecruitGraduate(**result_dict)