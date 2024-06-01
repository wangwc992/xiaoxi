'''CREATE TABLE `country_info` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL COMMENT '国家名称',
  `english_name` varchar(45) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL COMMENT '父级id',
  `logo` varchar(100) DEFAULT NULL COMMENT '国家图标',
  `is_show` int(1) DEFAULT NULL COMMENT '是否显示  1-是,2-否',
  `sort` int(11) DEFAULT '0' COMMENT '排序值',
  `advantage` varchar(1000) DEFAULT NULL COMMENT '国家优点',
  `weakness` varchar(1000) DEFAULT NULL COMMENT '国家缺点',
  `delete_status` int(1) DEFAULT '0' COMMENT '是否删除  0-未删除,1-已删除',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `create_by` varchar(45) DEFAULT NULL COMMENT '创建人',
  `update_by` varchar(45) DEFAULT NULL COMMENT '更新人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=202 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='国家信息表';'''

# 创建实体类
from typing import Optional
from langchain_core.pydantic_v1 import Field
from pydantic import BaseModel
from datetime import datetime

from xiaoxi_ai.database.mysql import mysql_connect


class CountryInfo(BaseModel):
    id: Optional[int] = Field(None, description="国家id")
    name: Optional[str] = Field(None, description="国家名称")
    english_name: Optional[str] = Field(None, description="国家英文名称")
    parent_id: Optional[int] = Field(None, description="父级id")
    logo: Optional[str] = Field(None, description="国家图标")
    is_show: Optional[int] = Field(None, description="是否显示  1-是,2-否")
    sort: Optional[int] = Field(None, description="排序值")
    advantage: Optional[str] = Field(None, description="国家优点")
    weakness: Optional[str] = Field(None, description="国家缺点")
    delete_status: Optional[int] = Field(None, description="是否删除  0-未删除,1-已删除")
    create_time: Optional[datetime] = Field(None, description="创建时间")
    update_time: Optional[datetime] = Field(None, description="更新时间")
    create_by: Optional[str] = Field(None, description="创建人")
    update_by: Optional[str] = Field(None, description="更新人")


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

    return CountryInfo(**result_dict)
