'''CREATE TABLE `zn_school_deparment_admission_score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zsdp_id` int(11) NOT NULL COMMENT 'zh_school_department_project表id',
  `atar_score` decimal(6,2) DEFAULT NULL COMMENT 'ATAR分数',
  `ukalevel3_score` decimal(6,2) DEFAULT NULL COMMENT 'UKAlevel三科分数',
  `ukalevel3_score1` varchar(5) DEFAULT NULL COMMENT 'UKAlevel三科分数（一）',
  `ukalevel3_score2` varchar(5) DEFAULT NULL COMMENT 'UKAlevel三科分数（二）',
  `ukalevel3_score3` varchar(5) DEFAULT NULL COMMENT 'UKAlevel三科分数（三）',
  `ukalevel4_score` decimal(6,2) DEFAULT NULL COMMENT 'UKAlevel四科分数',
  `ib_score` decimal(6,2) DEFAULT NULL COMMENT 'IB分数',
  `sat_score` decimal(6,2) DEFAULT NULL COMMENT 'SAT分数',
  `act_score` decimal(6,2) DEFAULT NULL COMMENT 'ACT分数',
  `ap_score` decimal(6,2) DEFAULT NULL COMMENT 'AP分数',
  `ossd_score` decimal(6,2) DEFAULT NULL COMMENT 'OSSD分数',
  `bc_score` decimal(6,2) DEFAULT NULL COMMENT 'BC分数',
  `gaokao_score` char(4) DEFAULT NULL COMMENT 'GAOKAO分数',
  `c9_score` decimal(6,2) DEFAULT NULL COMMENT 'C9均分分数',
  `s985_score` decimal(6,2) DEFAULT NULL COMMENT '985均分分数',
  `s211_score` decimal(6,2) DEFAULT NULL COMMENT '211均分分数',
  `sn211_score` decimal(6,2) DEFAULT NULL COMMENT '非211均分分数',
  `b_accept_md_bg` tinyint(1) DEFAULT '1' COMMENT '是否接受跨专业/需要相关背景',
  `atar_ask` char(100) DEFAULT NULL COMMENT 'ATAR要求',
  `ukalevel3_ask` varchar(1000) DEFAULT NULL COMMENT 'UKAlevel三科要求',
  `ukalevel4_ask` varchar(1000) DEFAULT NULL COMMENT 'UKAlevel四科要求',
  `ib_ask` varchar(1000) DEFAULT NULL COMMENT 'IB要求',
  `sat_ask` char(100) DEFAULT NULL COMMENT 'SAT要求',
  `act_ask` char(100) DEFAULT NULL COMMENT 'ACT要求	',
  `ap_ask` char(100) DEFAULT NULL COMMENT 'AP要求',
  `ossd_ask` char(100) DEFAULT NULL COMMENT 'OSSD要求',
  `bc_ask` char(100) DEFAULT NULL COMMENT 'BC要求',
  `gaokao_ask` char(100) DEFAULT NULL COMMENT 'GAOKAO要求',
  `c9_ask` char(100) DEFAULT NULL COMMENT 'C9均分要求',
  `s985_ask` char(100) DEFAULT NULL COMMENT '985均分要求',
  `s211_ask` char(100) DEFAULT NULL COMMENT '211均分要求',
  `sn211_ask` char(100) DEFAULT NULL COMMENT '非211均分要求',
  `accept_md_bg` char(100) DEFAULT NULL COMMENT '是否接受跨专业/需要相关背景',
  `delete_status` int(1) DEFAULT '0',
  `create_by` int(11) NOT NULL COMMENT 'zh_school_department_project表id',
  `update_by` int(11) NOT NULL COMMENT 'zh_school_department_project表id',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idx_ukalevel3_score` (`ukalevel3_score`),
  KEY `idx_zsdp_id` (`zsdp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12819 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;'''

from datetime import datetime

from xiaoxi_ai.database.mysql import mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur

# 创建实体类
from typing import Optional, Dict, Any
from langchain_core.pydantic_v1 import Field

from pydantic import BaseModel


class ZnSchoolDeparmentAdmissionScore(BaseModel):
    id: Optional[int] = Field(None, description="id")
    zsdp_id: Optional[int] = Field(None, description="zh_school_department_project表id")
    atar_score: Optional[float] = Field(None, description="ATAR分数")
    ukalevel3_score: Optional[float] = Field(None, description="UKAlevel三科分数")
    ukalevel3_score1: Optional[str] = Field(None, description="UKAlevel三科分数（一）")
    ukalevel3_score2: Optional[str] = Field(None, description="UKAlevel三科分数（二）")
    ukalevel3_score3: Optional[str] = Field(None, description="UKAlevel三科分数（三）")
    ukalevel4_score: Optional[float] = Field(None, description="UKAlevel四科分数")
    ib_score: Optional[float] = Field(None, description="IB分数")
    sat_score: Optional[float] = Field(None, description="SAT分数")
    act_score: Optional[float] = Field(None, description="ACT分数")
    ap_score: Optional[float] = Field(None, description="AP分数")
    ossd_score: Optional[float] = Field(None, description="OSSD分数")
    bc_score: Optional[float] = Field(None, description="BC分数")
    gaokao_score: Optional[str] = Field(None, description="GAOKAO分数")
    c9_score: Optional[float] = Field(None, description="C9均分分数")
    s985_score: Optional[float] = Field(None, description="985均分分数")
    s211_score: Optional[float] = Field(None, description="211均分分数")
    sn211_score: Optional[float] = Field(None, description="非211均分分数")
    b_accept_md_bg: Optional[bool] = Field(1, description="是否接受跨专业/需要相关背景")
    atar_ask: Optional[str] = Field(None, description="ATAR要求")
    ukalevel3_ask: Optional[str] = Field(None, description="UKAlevel三科要求")
    ukalevel4_ask: Optional[str] = Field(None, description="UKAlevel四科要求")
    ib_ask: Optional[str] = Field(None, description="IB要求")
    sat_ask: Optional[str] = Field(None, description="SAT要求")
    act_ask: Optional[str] = Field(None, description="ACT要求	")
    ap_ask: Optional[str] = Field(None, description="AP要求")
    ossd_ask: Optional[str] = Field(None, description="OSSD要求")
    bc_ask: Optional[str] = Field(None, description="BC要求")
    gaokao_ask: Optional[str] = Field(None, description="GAOKAO要求")
    c9_ask: Optional[str] = Field(None, description="C9均分要求")
    s985_ask: Optional[str] = Field(None, description="985均分要求")
    s211_ask: Optional[str] = Field(None, description="211均分要求")
    sn211_ask: Optional[str] = Field(None, description="非211均分要求")
    accept_md_bg: Optional[str] = Field(None, description="是否接受跨专业/需要相关背景")
    delete_status: Optional[int] = Field(0, description="是否删除  0-未删除,1-已删除")
    create_by: Optional[int] = Field(None, description="zh_school_department_project表id")
    update_by: Optional[int] = Field(None, description="zh_school_department_project表id")
    create_time: Optional[datetime] = Field(None, description="创建时间")
    update_time: Optional[datetime] = Field(None, description="更新时间")


def select_by_id(zsdp_id):
    mySQLConnectCur.execute('select * from zn_school_deparment_admission_score where zsdp_id=%s', (zsdp_id,))
    result = mySQLConnectCur.fetchone()
    if result is None:
        return None
    # Get column names from cursor description
    column_names = [column[0] for column in mySQLConnectCur.description]
    # Convert result tuple to dictionary
    result_dict = dict(zip(column_names, result))
    # result_dict 变成 CountryInfo 对象
    return ZnSchoolDeparmentAdmissionScore(**result_dict)
