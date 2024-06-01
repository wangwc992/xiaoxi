'''CREATE TABLE `service_confirm_school` (
  `id` varchar(20) NOT NULL COMMENT '定校编号',
  `service_id` varchar(11) NOT NULL COMMENT '服务流程ID',
  `member_id` bigint(12) DEFAULT NULL COMMENT '学生编号',
  `flow_id` varchar(40) NOT NULL COMMENT '合同编号',
  `service_confirm_type` tinyint(1) DEFAULT '0' COMMENT '申请服务类型(0:定校, 1:加申语言)',
  `school_id` int(11) NOT NULL COMMENT '学校ID',
  `school_chinese_name` varchar(200) DEFAULT NULL COMMENT '学校名称',
  `school_english_name` varchar(300) DEFAULT NULL COMMENT '学校英文名称',
  `choice_rank` tinyint(4) DEFAULT NULL COMMENT '同校志愿排序',
  `project_id` int(11) NOT NULL COMMENT '专业方向ID (项目ID)',
  `project_chinese_name` varchar(200) DEFAULT NULL COMMENT '项目中文名称',
  `project_english_name` varchar(300) DEFAULT NULL COMMENT '项目英文名称',
  `is_language` char(1) NOT NULL DEFAULT '0' COMMENT '是否配语言 0 否  1是',
  `start_date` date DEFAULT NULL COMMENT '配备语言：开学日期',
  `apply_week` varchar(20) DEFAULT NULL COMMENT '配备语言：申请周数',
  `other_remark` varchar(500) DEFAULT NULL COMMENT '配备语言：其他备注',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态 1可编辑 2待评估 3通过 4驳回  同一serviceId，状态一致',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `svc_status` tinyint(1) unsigned DEFAULT '125' COMMENT '服务状态 同service_node',
  `svc_status_name` varchar(50) DEFAULT '申请未提交' COMMENT '服务状态名称',
  `is_packaged` tinyint(1) DEFAULT '0' COMMENT '是否打包课程  1是  0否',
  `package_school_id` int(11) DEFAULT NULL COMMENT '打包课程：申请院校ID',
  `package_school_name` varchar(500) DEFAULT NULL COMMENT '打包课程：申请院校名称',
  `package_project_id` int(11) DEFAULT NULL COMMENT '打包课程：专业ID 自定义传 0',
  `package_project_name` varchar(500) DEFAULT NULL COMMENT '打包课程：专业名称',
  `package_degree` varchar(255) DEFAULT NULL COMMENT '打包课程：申请学位',
  `package_campus` varchar(100) DEFAULT NULL COMMENT '打包课程：校区',
  `package_semester` varchar(50) DEFAULT NULL COMMENT '打包课程：开学时间 yyyy-MM-01',
  `is_asny` tinyint(1) DEFAULT '0' COMMENT '是否同步文签：1是  0否',
  `asny_date` datetime DEFAULT NULL COMMENT '同步文签时间',
  `reviewer_id` int(11) DEFAULT NULL COMMENT '审核人ID',
  `reviewer_name` varchar(50) DEFAULT NULL COMMENT '审核人名称',
  `campus` varchar(100) DEFAULT NULL COMMENT '就读校区',
  `length_of_school` varchar(100) DEFAULT NULL COMMENT '学制',
  `length_of_unit` tinyint(4) DEFAULT NULL COMMENT '学制单位：1 周,2 月,3 年,4 学期',
  `semester` varchar(100) DEFAULT NULL COMMENT '开学时间',
  `is_fraction_reduction` tinyint(11) DEFAULT '0' COMMENT '是否需要减免学分 0否 1是',
  `country_id` varchar(100) DEFAULT NULL COMMENT '国家编号',
  `country_name` varchar(100) DEFAULT NULL COMMENT '国家名称',
  `academic_degree` varchar(200) DEFAULT NULL COMMENT '学位',
  `major_no` varchar(50) DEFAULT NULL COMMENT '专业编号',
  `majorlink` varchar(1000) DEFAULT NULL COMMENT '专业链接',
  `major_direction` varchar(100) DEFAULT NULL COMMENT '专业小方向',
  `reject_reason` varchar(500) DEFAULT NULL COMMENT '驳回愿意/修改意见',
  `reject_time` datetime DEFAULT NULL COMMENT '审核时间',
  `visa_apply_id` int(11) DEFAULT NULL COMMENT '文签申请id,仅用于手动同步文签系统上的数据',
  `examine_flag` tinyint(4) DEFAULT '0' COMMENT '文签审核学生信息 0未审核 1已审核',
  `delay_time` varchar(50) DEFAULT NULL COMMENT '申请延期时间',
  `offer_feedback` tinyint(4) DEFAULT NULL COMMENT '学生意愿, 接受offer时使用',
  `wish_detail` varchar(100) DEFAULT NULL COMMENT '学生意愿详情',
  `update_feedback_origin` varchar(2) DEFAULT NULL COMMENT '修改意愿来源 1-代理 2-学生',
  `reject_attach` text COMMENT '定校驳回附件',
  `isTransfer` int(11) DEFAULT '0' COMMENT '是否转案0:未转案 1:已转案',
  `trans_date` datetime DEFAULT NULL COMMENT '转案时间',
  `remarks_transfer` varchar(500) CHARACTER SET utf8 DEFAULT NULL COMMENT '转案备注',
  `package_school_english_name` varchar(500) DEFAULT NULL COMMENT '打包课程：申请院校英文名称',
  `package_project_english_name` varchar(500) DEFAULT NULL COMMENT '打包课程：专业英文名称',
  `package_major_no` varchar(50) DEFAULT NULL COMMENT '打包专业编号',
  `package_major_direction` varchar(100) DEFAULT NULL COMMENT '打包专业小方向',
  `except_later_time` varchar(20) DEFAULT NULL COMMENT '期望晚报道时间',
  `is_after_submit` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否加申1-是',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id` (`id`) USING BTREE,
  KEY `idx_flow_id` (`flow_id`),
  KEY `service_confirm_school_service_id_index` (`service_id`),
  KEY `idx_projectId_svsStatus` (`project_id`,`svc_status`),
  KEY `idx_svc_status` (`svc_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='定校信息';'''

from xiaoxi_ai.database.mysql import mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur

# 创建实体类
from typing import Optional, Dict, Any
from langchain_core.pydantic_v1 import Field
from datetime import datetime
from pydantic import BaseModel


class ServiceConfirmSchool(BaseModel):
    id: Optional[str] = Field(None, description="定校编号")
    service_id: Optional[str] = Field(None, description="服务流程ID")
    member_id: Optional[int] = Field(None, description="学生编号")
    flow_id: Optional[str] = Field(None, description="合同编号")
    service_confirm_type: Optional[int] = Field(None, description="申请服务类型(0:定校, 1:加申语言)")
    school_id: Optional[int] = Field(None, description="学校ID")
    school_chinese_name: Optional[str] = Field(None, description="学校名称")
    school_english_name: Optional[str] = Field(None, description="学校英文名称")
    choice_rank: Optional[int] = Field(None, description="同校志愿排序")
    project_id: Optional[int] = Field(None, description="专业方向ID (项目ID)")
    project_chinese_name: Optional[str] = Field(None, description="项目中文名称")
    project_english_name: Optional[str] = Field(None, description="项目英文名称")
    is_language: Optional[str] = Field(None, description="是否配语言 0 否  1是")
    start_date: Optional[datetime] = Field(None, description="配备语言：开学日期")
    apply_week: Optional[str] = Field(None, description="配备语言：申请周数")
    other_remark: Optional[str] = Field(None, description="配备语言：其他备注")
    status: Optional[int] = Field(None, description="状态 1可编辑 2待评估 3通过 4驳回  同一serviceId，状态一致")
    create_time: Optional[datetime] = Field(None, description="创建时间")
    update_time: Optional[datetime] = Field(None, description="更新时间")
    svc_status: Optional[int] = Field(None, description="服务状态 同service_node")
    svc_status_name: Optional[str] = Field(None, description="服务状态名称")
    is_packaged: Optional[int] = Field(None, description="是否打包课程  1是  0否")
    package_school_id: Optional[int] = Field(None, description="打包课程：申请院校ID")
    package_school_name: Optional[str] = Field(None, description="打包课程：申请院校名称")
    package_project_id: Optional[int] = Field(None, description="打包课程：专业ID 自定义传 0")
    package_project_name: Optional[str] = Field(None, description="打包课程：专业名称")
    package_degree: Optional[str] = Field(None, description="打包课程：申请学位")
    package_campus: Optional[str] = Field(None, description="打包课程：校区")
    package_semester: Optional[str] = Field(None, description="打包课程：开学时间 yyyy-MM-01")
    is_asny: Optional[int] = Field(None, description="是否同步文签：1是  0否")
    asny_date: Optional[datetime] = Field(None, description="同步文签时间")
    reviewer_id: Optional[int] = Field(None, description="审核人ID")
    reviewer_name: Optional[str] = Field(None, description="审核人名称")
    campus: Optional[str] = Field(None, description="就读校区")
    length_of_school: Optional[str] = Field(None, description="学制")
    length_of_unit: Optional[int] = Field(None, description="学制单位：1 周,2 月,3 年,4 学期")
    semester: Optional[str] = Field(None, description="开学时间")
    is_fraction_reduction: Optional[int] = Field(None, description="是否需要减免学分 0否 1是")
    country_id: Optional[str] = Field(None, description="国家编号")
    country_name: Optional[str] = Field(None, description="国家名称")
    academic_degree: Optional[str] = Field(None, description="学位")
    major_no: Optional[str] = Field(None, description="专业编号")
    majorlink: Optional[str] = Field(None, description="专业链接")
    major_direction: Optional[str] = Field(None, description="专业小方向")
    reject_reason: Optional[str] = Field(None, description="驳回愿意/修改意见")
    reject_time: Optional[datetime] = Field(None, description="审核时间")
    visa_apply_id: Optional[int] = Field(None, description="文签申请id,仅用于手动同步文签系统上的数据")
    examine_flag: Optional[int] = Field(None, description="文签审核学生信息 0未审核 1已审核")
    delay_time: Optional[str] = Field(None, description="申请延期时间")
    offer_feedback: Optional[int] = Field(None, description="学生意愿, 接受offer时使用")
    wish_detail: Optional[str] = Field(None, description="学生意愿详情")
    update_feedback_origin: Optional[str] = Field(None, description="修改意愿来源 1-代理 2-学生")
    reject_attach: Optional[str] = Field(None, description="定校驳回附件")
    isTransfer: Optional[int] = Field(None, description="是否转案0:未转案 1:已转案")


def select_by_ids(ids):
    query = 'select * from service_confirm_school where id in (%s)' % ','.join(['%s'] * len(ids))
    mySQLConnectCur.execute(query, tuple(ids))
    # 打印SQL语句
    print("Executing query:", mySQLConnectCur.mogrify(query, ids))

    result = mySQLConnectCur.fetchall()
    if result is None:
        return None

    # Get column names from cursor description
    column_names = [column[0] for column in mySQLConnectCur.description]

    # Convert result tuple to dictionary
    result_dict = [dict(zip(column_names, row)) for row in result]
    # result_dict 变成 CountryInfo 对象
    return [ServiceConfirmSchool(**row) for row in result_dict]
