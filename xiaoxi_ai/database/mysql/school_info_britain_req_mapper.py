'''CREATE TABLE `school_info_britain_req` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) DEFAULT NULL COMMENT '英国学校id',
  `school_english_name` varchar(300) DEFAULT NULL COMMENT '英国学校名称',
  `project_id` int(11) DEFAULT NULL COMMENT '专业id',
  `pro_english_name` varchar(200) DEFAULT NULL COMMENT '专业名称',
  `china_school_id` int(11) NOT NULL COMMENT '中国大学id',
  `china_chinese_name` varchar(200) DEFAULT NULL COMMENT '中国大学名称',
  `gpa_req` decimal(6,2) DEFAULT NULL COMMENT '百分制GPA要求',
  `delete_status` int(1) DEFAULT '0' COMMENT '是否删除  0-未删除,1-已删除',
  `create_by` int(11) NOT NULL DEFAULT '1' COMMENT '创建人',
  `update_by` int(11) NOT NULL DEFAULT '1' COMMENT '更新人',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `index_update` (`school_id`,`project_id`,`china_school_id`) USING BTREE,
  KEY `index_gpaReq` (`gpa_req`) USING BTREE,
  KEY `index_gpaReq_projectId` (`gpa_req`,`project_id`) USING BTREE,
  KEY `idx_china_school_id` (`china_school_id`) USING BTREE,
  KEY `idx_project_id` (`project_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2217966 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='英国大学专业对中国学校均分要求表';'''

from typing import Optional, Dict, Any
from langchain_core.pydantic_v1 import BaseModel, Field
from xiaoxi_ai.database.mysql import mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur


# 创建实体类

class SchoolInfoBritainReq:
    id: Optional[int] = Field(None, description="英国大学专业对中国学校均分要求表id")
    school_id: Optional[int] = Field(None, description="英国学校id")
    school_english_name: Optional[str] = Field(None, description="英国学校名称")
    project_id: Optional[int] = Field(None, description="专业id")
    pro_english_name: Optional[str] = Field(None, description="专业名称")
    china_school_id: Optional[int] = Field(None, description="中国大学id")
    china_chinese_name: Optional[str] = Field(None, description="中国大学名称")
    gpa_req: Optional[float] = Field(None, description="百分制GPA要求")
    delete_status: Optional[int] = Field(None, description="是否删除  0-未删除,1-已删除")
    create_by: Optional[int] = Field(None, description="创建人")
    update_by: Optional[int] = Field(None, description="更新人")
    create_time: Optional[str] = Field(None, description="创建时间")
    update_time: Optional[str] = Field(None, description="更新时间")


# 预编译 根据英国学校id和专业id和中国大学id查询学校信息，返回SchoolInfoBritainReq对象，如果没有查询到则返回None，school_id, project_id, china_school_id可能为空，不为空的时候才拼接sql
def select_by_model(schoolInfoBritainReq:SchoolInfoBritainReq):
    sql = 'select * from school_info_britain_req where 1=1'
    params = []
    if schoolInfoBritainReq.school_id is not None:
        sql += ' and school_id=%s'
        params.append(schoolInfoBritainReq.school_id)
    if schoolInfoBritainReq.project_id is not None:
        sql += ' and project_id=%s'
        params.append(schoolInfoBritainReq.project_id)
    if schoolInfoBritainReq.china_school_id is not None:
        sql += ' and china_school_id=%s'
        params.append(schoolInfoBritainReq.china_school_id)
    if schoolInfoBritainReq.gpa_req is not None:
        sql += ' and gpa_req >=%s'
        params.append(schoolInfoBritainReq.gpa_req)
    mySQLConnectCur.execute(sql, tuple(params))
    result = mySQLConnectCur.fetchall()
    if result is None:
        return None
    return [SchoolInfoBritainReq(*res) for res in result]


