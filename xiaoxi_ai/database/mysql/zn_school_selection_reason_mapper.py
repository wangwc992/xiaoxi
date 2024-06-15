'''CREATE TABLE `zn_school_selection_reason` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) DEFAULT NULL COMMENT '院校表ID',
  `selection_reason` text COMMENT '择校理由',
  `feature` text COMMENT '学校特色',
  `strong_majors` text COMMENT '强势专业',
  `hot_majors` text COMMENT '热门专业',
  `department_major` text COMMENT '院系设置',
  `teaching` text COMMENT '教学特色',
  `evaluation_bad` text COMMENT '差评项',
  `evaluation_good` text COMMENT '好评项',
  `delete_status` int(1) DEFAULT '0' COMMENT '是否删除  0-未删除,1-已删除',
  `create_by` int(11) NOT NULL COMMENT '创建人',
  `update_by` int(11) NOT NULL COMMENT '更新人',
  `create_name` varchar(50) DEFAULT NULL COMMENT '创建人名称',
  `update_name` varchar(50) DEFAULT NULL COMMENT '更新人名称',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_school` (`school_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=20114 DEFAULT CHARSET=utf8mb4;'''

from datetime import datetime

from xiaoxi_ai.database.mysql import mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur


# 创建实体类
from typing import Optional, Dict, Any
from langchain_core.pydantic_v1 import Field

from pydantic import BaseModel


class ZnSchoolSelectionReason(BaseModel):
    id: Optional[int] = Field(None, description="择校理由id")
    school_id: Optional[int] = Field(None, description="院校表ID")
    selection_reason: Optional[str] = Field(None, description="择校理由")
    feature: Optional[str] = Field(None, description="学校特色")
    strong_majors: Optional[str] = Field(None, description="强势专业")
    hot_majors: Optional[str] = Field(None, description="热门专业")
    department_major: Optional[str] = Field(None, description="院系设置")
    teaching: Optional[str] = Field(None, description="教学特色")
    evaluation_bad: Optional[str] = Field(None, description="差评项")
    evaluation_good: Optional[str] = Field(None, description="好评项")
    delete_status: Optional[int] = Field(0, description="是否删除  0-未删除,1-已删除")
    create_by: Optional[int] = Field(None, description="创建人")
    update_by: Optional[int] = Field(None, description="更新人")
    create_name: Optional[str] = Field(None, description="创建人名称")
    update_name: Optional[str] = Field(None, description="更新人名称")
    create_time: Optional[datetime] = Field(None, description="创建时间")
    update_time: Optional[datetime] = Field(None, description="更新时间")

def select_by_id(school_id):
    mySQLConnectCur.execute('select * from zn_school_selection_reason where school_id=%s', (school_id,))
    result = mySQLConnectCur.fetchone()
    if result is None:
        return None

    # Get column names from cursor description
    column_names = [column[0] for column in mySQLConnectCur.description]

    # Convert result tuple to dictionary
    result_dict = dict(zip(column_names, result))

    return ZnSchoolSelectionReason(**result_dict)
