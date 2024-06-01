'''CREATE TABLE `school_china` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `name` varchar(100) NOT NULL COMMENT '学校名称',
  `level` tinyint(2) DEFAULT NULL COMMENT '办学层次  1本科  2专科',
  `is_top` tinyint(1) DEFAULT NULL COMMENT '是否双一流 0否  1是',
  `is211` tinyint(1) DEFAULT NULL COMMENT '是否211  0否  1是',
  `is985` tinyint(1) DEFAULT NULL COMMENT '是否985  0否  1是',
  `isC9` tinyint(1) DEFAULT NULL COMMENT '是否C9  0否  1是',
  `softRank` int(11) DEFAULT NULL COMMENT '软科排名',
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3123 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='中国院校表';'''

from typing import Optional
from langchain_core.pydantic_v1 import Field
from pydantic import BaseModel
from datetime import datetime

from xiaoxi_ai.database.mysql import mysql_connect

# 创建实体

class SchoolChina(BaseModel):
    id: Optional[int] = Field(None, description="id")
    name: str = Field(..., description="学校名称")
    level: Optional[int] = Field(None, description="办学层次  1本科  2专科")
    is_top: Optional[int] = Field(None, description="是否双一流 0否  1是")
    is211: Optional[int] = Field(None, description="是否211  0否  1是")
    is985: Optional[int] = Field(None, description="是否985  0否  1是")
    isC9: Optional[int] = Field(None, description="是否C9  0否  1是")
    softRank: Optional[int] = Field(None, description="软科排名")
    update_time: Optional[datetime] = Field(None, description="更新时间")

mySQLConnectCur = mysql_connect.MySQLConnect().cur

# 预编译的方式根据国家名称查询国家信息返回CountryInfo对象，如果没有查询到则返回None
def select_by_name(name):
    mySQLConnectCur.execute('select * from country_info where name=%s', (name,))
    result = mySQLConnectCur.fetchone()
    if result is None:
        return None

    # Get column names from cursor description
    column_names = [column[0] for column in mySQLConnectCur.description]

    # Convert result tuple to dictionary
    result_dict = dict(zip(column_names, result))
    # result_dict 变成 CountryInfo 对象

    return SchoolChina(**result_dict)