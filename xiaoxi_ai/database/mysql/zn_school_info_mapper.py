'''CREATE TABLE `zn_school_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL COMMENT '国家ID',
  `country_name` varchar(20) DEFAULT NULL COMMENT '国家名称',
  `chinese_name` varchar(200) DEFAULT NULL COMMENT '院校中文名',
  `english_name` varchar(300) DEFAULT NULL COMMENT '院校英文名',
  `logo_url` varchar(300) DEFAULT NULL COMMENT '院校logo',
  `cover_url` varchar(300) DEFAULT NULL COMMENT '院校背景图',
  `market_tags` varchar(500) DEFAULT NULL COMMENT '院校标签 逗号分隔',
  `city_path` varchar(200) DEFAULT NULL COMMENT '院校位置',
  `website` varchar(200) DEFAULT NULL COMMENT '官网地址',
  `spider_id` int(11) NOT NULL DEFAULT '0' COMMENT '爬虫ID',
  `delete_status` int(1) NOT NULL DEFAULT '0' COMMENT '是否删除  0-未删除,1-已删除',
  `create_by` int(11) NOT NULL COMMENT '填写人',
  `update_by` int(11) NOT NULL COMMENT '更新人',
  `create_name` varchar(50) DEFAULT NULL COMMENT '创建人名称',
  `update_name` varchar(50) DEFAULT NULL COMMENT '更新人名称',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `comment_tags` varchar(200) DEFAULT NULL COMMENT '评价标签',
  `is_popular` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否热门院校  1：是  0否',
  `fans_base_total` int(11) NOT NULL DEFAULT '0' COMMENT '关注基数',
  `school_sort` int(11) DEFAULT '0' COMMENT '院校排序',
  `fans_total` int(11) DEFAULT '0' COMMENT '关注人数',
  `school_abbreviations` varchar(255) DEFAULT '' COMMENT '院校简称',
  `fee_dimension` tinyint(4) DEFAULT NULL COMMENT '申请费支付方式1-按院校;2-按专业3-其他',
  `apply_cycle_algorithm` int(11) DEFAULT NULL COMMENT '申请周期-算法统计(自然日)',
  `apply_cycle_manual` int(11) DEFAULT NULL COMMENT '申请周期-人工填写(自然日)',
  `period` varchar(20) DEFAULT NULL,
  `weight` int(11) NOT NULL DEFAULT '0' COMMENT '排序权重（23.7-24.1的申请数）',
  PRIMARY KEY (`id`),
  KEY `uk_spider` (`spider_id`) USING BTREE,
  KEY `idx_cid` (`country_id`) USING BTREE,
  KEY `idx_del_status` (`delete_status`) USING BTREE,
  KEY `country_id_index` (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11477 DEFAULT CHARSET=utf8mb4;'''

from xiaoxi_ai.database.mysql import mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur

# 创建实体类
from typing import Optional, Dict, Any
from langchain_core.pydantic_v1 import Field
from datetime import datetime
from pydantic import BaseModel


class ZnSchoolInfo(BaseModel):
    id: Optional[int] = Field(None, description="院校id")
    country_id: Optional[int] = Field(None, description="国家ID")
    country_name: Optional[str] = Field(None, description="国家名称")
    chinese_name: Optional[str] = Field(None, description="院校中文名")
    english_name: Optional[str] = Field(None, description="院校英文名")
    logo_url: Optional[str] = Field(None, description="院校logo")
    cover_url: Optional[str] = Field(None, description="院校背景图")
    market_tags: Optional[str] = Field(None, description="院校标签 逗号分隔")
    city_path: Optional[str] = Field(None, description="院校位置")
    website: Optional[str] = Field(None, description="官网地址")
    spider_id: Optional[int] = Field(None, description="爬虫ID")
    delete_status: Optional[int] = Field(None, description="是否删除  0-未删除,1-已删除")
    create_by: Optional[int] = Field(None, description="填写人")
    update_by: Optional[int] = Field(None, description="更新人")
    create_name: Optional[str] = Field(None, description="创建人名称")
    update_name: Optional[str] = Field(None, description="更新人名称")
    create_time: Optional[datetime] = Field(None, description="创建时间")
    update_time: Optional[datetime] = Field(None, description="更新时间")
    comment_tags: Optional[str] = Field(None, description="评价标签")
    is_popular: Optional[int] = Field(None, description="是否热门院校  1：是  0否")
    fans_base_total: Optional[int] = Field(None, description="关注基数")
    school_sort: Optional[int] = Field(None, description="院校排序")
    fans_total: Optional[int] = Field(None, description="关注人数")
    school_abbreviations: Optional[str] = Field(None, description="院校简称")
    fee_dimension: Optional[int] = Field(None, description="申请费支付方式1-按院校;2-按专业3-其他")
    apply_cycle_algorithm: Optional[int] = Field(None, description="申请周期-算法统计(自然日)")
    apply_cycle_manual: Optional[int] = Field(None, description="申请周期-人工填写(自然日)")
    period: Optional[str] = Field(None, description="")
    weight: Optional[int] = Field(None, description="排序权重（23.7-24.1的申请数）")


# 预编译的方式根据学校名称模糊查询学校信息，返回zn_school_info对象，如果没有查询到则返回None
def select_by_name(name):
    mySQLConnectCur.execute('select * from zn_school_info where chinese_name like %s or english_name like %s ',
                            ('%' + name + '%', '%' + name + '%',))
    result = mySQLConnectCur.fetchone()
    if result is None:
        return None

    # Get column names from cursor description
    column_names = [column[0] for column in mySQLConnectCur.description]

    # Convert result tuple to dictionary
    result_dict = dict(zip(column_names, result))
    # result_dict 变成 CountryInfo 对象

    return ZnSchoolInfo(**result_dict)


# 预编译 根据学校的id列表查询学校信息，返回zn_school_info对象列表，如果没有查询到则返回None
def select_by_ids(ids):
    sql = 'select * from zn_school_info where id in (%s)' % ','.join(['%s'] * len(ids))
    mySQLConnectCur.execute(sql, tuple(ids))
    result = mySQLConnectCur.fetchall()
    if result is None:
        return None

    # Get column names from cursor description
    column_names = [column[0] for column in mySQLConnectCur.description]

    # Convert result tuple to dictionary
    result_dict = [dict(zip(column_names, row)) for row in result]
    # result_dict 变成 CountryInfo 对象
    return [ZnSchoolInfo(**row) for row in result_dict]


def select_by_id(school_id):
    mySQLConnectCur.execute('select * from zn_school_info where id=%s', (school_id,))
    result = mySQLConnectCur.fetchone()
    if result is None:
        return None

    # Get column names from cursor description
    column_names = [column[0] for column in mySQLConnectCur.description]

    # Convert result tuple to dictionary
    result_dict = dict(zip(column_names, result))
    # result_dict 变成 CountryInfo 对象

    return ZnSchoolInfo(**result_dict)