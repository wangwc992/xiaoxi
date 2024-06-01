'''CREATE TABLE `student_matriculate_case` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `visa_apply_info_id` int(11) NOT NULL COMMENT '文签系统申请信息表id',
  `service_confirm_school_id` varchar(50) DEFAULT NULL COMMENT '定校id，对应文签apply_info.xxlx_apply',
  `student_no` varchar(50) DEFAULT NULL COMMENT '学号',
  `case_title` varchar(255) DEFAULT '' COMMENT '案例标题',
  `ik_max_word` varchar(500) DEFAULT '' COMMENT '最大搜索字段',
  `student_name` varchar(255) DEFAULT '' COMMENT '学生姓名',
  `fictitious_name` varchar(255) DEFAULT '' COMMENT '虚拟姓名(x同学)',
  `offer_country_id` int(11) DEFAULT '0' COMMENT '申请国家id',
  `offer_country_name` varchar(255) DEFAULT '' COMMENT '申请国家名称',
  `offer_college_id` int(11) DEFAULT '0' COMMENT '录取院校id',
  `offer_college_name_en` varchar(255) DEFAULT '' COMMENT '录取院校名称',
  `offer_college_name_zh` varchar(255) DEFAULT '' COMMENT '录取院校英文名称',
  `offer_college_logo_url` varchar(500) DEFAULT '' COMMENT '录取院校logo url',
  `offer_college_background_url` varchar(500) DEFAULT '' COMMENT '录取院校背景url',
  `offer_degree_level_id` tinyint(3) DEFAULT '18' COMMENT '录取学位等级id(文签目标学位：2_中小学,3_本科,4_硕士,5_博士,9_专科,10_非学历,11_证书,12_副学士)',
  `offer_degree_name` varchar(255) DEFAULT '' COMMENT '录取学位名称',
  `offer_major_id` int(11) DEFAULT '0' COMMENT '录取专业id',
  `offer_major_name_zh` varchar(255) DEFAULT '' COMMENT '录取专业名称',
  `offer_major_name_en` varchar(255) DEFAULT '' COMMENT '录取专业名称英文',
  `offer_college_rank` int(11) DEFAULT '999' COMMENT '录取院校QPS排名',
  `course_start_time` datetime DEFAULT NULL COMMENT '开课日期',
  `education_school_name_zh` varchar(255) DEFAULT '' COMMENT '教育背景学校名称',
  `education_school_name_en` varchar(255) DEFAULT '' COMMENT '教育背景学校英文名称',
  `education_school_name_or` varchar(255) NOT NULL DEFAULT '' COMMENT '教育背景学校原始名称',
  `education_project_name` varchar(255) DEFAULT '' COMMENT '教育背景专业',
  `education_period_id` int(5) DEFAULT '6' COMMENT '教育背景学段id',
  `education_gpa` double(10,2) DEFAULT '0.00' COMMENT '教育背景GPA',
  `education_gpa_str` varchar(255) DEFAULT '' COMMENT '原教育背景GPA',
  `education_country_id` int(11) DEFAULT '-1' COMMENT '教育背景院校所在国家id(-1:文签同步，没有国家)',
  `education_country_name` varchar(255) DEFAULT '' COMMENT '教育背景校区所在国家',
  `education_begin_date` datetime DEFAULT NULL COMMENT '教育背景开始时间',
  `education_end_data` datetime DEFAULT NULL COMMENT '教育背景结束时间',
  `job_exp` tinyint(1) DEFAULT '0' COMMENT '工作经历',
  `offer_type` int(3) DEFAULT NULL COMMENT 'offer类型(1:无条件offer, 2:只有语言条件offer, 3:只有学术条件offer, 4:其他条件offer)',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `create_by` varchar(10) DEFAULT '1' COMMENT '操作人',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `update_by` varchar(10) DEFAULT '1' COMMENT '更新人',
  `delete_status` tinyint(1) DEFAULT '0' COMMENT '逻辑删除',
  `views` int(11) DEFAULT '0' COMMENT '分享数',
  `share_num` int(11) DEFAULT '0' COMMENT '分享数',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `index_start_time_id` (`course_start_time`,`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=47824 DEFAULT CHARSET=utf8mb4 COMMENT='学生案例库表';'''

from xiaoxi_ai.database.mysql import mysql_connect

mySQLConnectCur = mysql_connect.MySQLConnect().cur

# 创建实体类
from typing import Optional, Dict, Any
from langchain_core.pydantic_v1 import Field
from datetime import datetime
from langchain_core.pydantic_v1 import BaseModel

class StudentMatriculateCase(BaseModel):
    id: Optional[int] = Field(None, description="主键id")
    visa_apply_info_id: Optional[int] = Field(None, description="文签系统申请信息表id")
    service_confirm_school_id: Optional[str] = Field(None, description="定校id，对应文签apply_info.xxlx_apply")
    student_no: Optional[str] = Field(None, description="学号")
    case_title: Optional[str] = Field(None, description="案例标题")
    ik_max_word: Optional[str] = Field(None, description="最大搜索字段")
    student_name: Optional[str] = Field(None, description="学生姓名")
    fictitious_name: Optional[str] = Field(None, description="虚拟姓名(x同学)")
    offer_country_id: Optional[int] = Field(None, description="申请国家id")
    offer_country_name: Optional[str] = Field(None, description="申请国家名称")
    offer_college_id: Optional[int] = Field(None, description="录取院校id")
    offer_college_name_en: Optional[str] = Field(None, description="录取院校名称")
    offer_college_name_zh: Optional[str] = Field(None, description="录取院校英文名称")
    offer_college_logo_url: Optional[str] = Field(None, description="录取院校logo url")
    offer_college_background_url: Optional[str] = Field(None, description="录取院校背景url")
    offer_degree_level_id: Optional[int] = Field(None, description="录取学位等级id(文签目标学位：2_中小学,3_本科,4_硕士,5_博士,9_专科,10_非学历,11_证书,12_副学士)")
    offer_degree_name: Optional[str] = Field(None, description="录取学位名称")
    offer_major_id: Optional[int] = Field(None, description="录取专业id")
    offer_major_name_zh: Optional[str] = Field(None, description="录取专业名称")
    offer_major_name_en: Optional[str] = Field(None, description="录取专业名称英文")
    offer_college_rank: Optional[int] = Field(None, description="录取院校QPS排名")
    course_start_time: Optional[datetime] = Field(None, description="开课日期")
    education_school_name_zh: Optional[str] = Field(None, description="教育背景学校名称")
    education_school_name_en: Optional[str] = Field(None, description="教育背景学校英文名称")
    education_school_name_or: Optional[str] = Field(None, description="教育背景学校原始名称")
    education_project_name: Optional[str] = Field(None, description="教育背景专业")
    education_period_id: Optional[int] = Field(None, description="教育背景学段id")
    education_gpa: Optional[float] = Field(None, description="教育背景GPA")
    education_gpa_str: Optional[str] = Field(None, description="原教育背景GPA")
    education_country_id: Optional[int] = Field(None, description="教育背景院校所在国家id(-1:文签同步，没有国家)")
    education_country_name: Optional[str] = Field(None, description="教育背景校区所在国家")
    education_begin_date: Optional[datetime] = Field(None, description="教育背景开始时间")
    education_end_data: Optional[datetime] = Field(None, description="教育背景结束时间")
    job_exp: Optional[int] = Field(None, description="工作经历")
    offer_type: Optional[int] = Field(None, description="offer类型(1:无条件offer, 2:只有语言条件offer, 3:只有学术条件offer, 4:其他条件offer)")
    create_time: Optional[datetime] = Field(None, description="创建时间")
    create_by: Optional[str] = Field(None, description="操作人")
    update_time: Optional[datetime] = Field(None, description="修改时间")
    update_by: Optional[str] = Field(None, description="更新人")
    delete_status: Optional[int] = Field(None, description="逻辑删除")
    views: Optional[int] = Field(None, description="分享数")
    share_num: Optional[int] = Field(None, description="分享数")

# 预编译的方式根据StudentMatriculateCase实例每一个属性查询学生案例信息，返回StudentMatriculateCase对象，如果没有查询到则返回None

def select_by_student_matriculate_case(case: StudentMatriculateCase) -> list[StudentMatriculateCase]:
    # Prepare SQL query
    query = "SELECT * FROM student_matriculate_case WHERE "
    values = []
    for field, value in case.dict().items():
        if value is not None:
            if field == 'education_gpa':
                query += f"{field} >= %s AND "
            else:
                query += f"{field} = %s AND "
            values.append(value)
    query = query.rstrip(" AND ")
    # 打印SQL语句
    print("Executing query:", mySQLConnectCur.mogrify(query, values))
    # Execute the query
    mySQLConnectCur.execute(query, tuple(values))

    # Fetch the result
    result = mySQLConnectCur.fetchall()
    if result is None:
        return None

    # Get column names from cursor description
    column_names = [column[0] for column in mySQLConnectCur.description]

    # Convert result tuple to dictionary
    result_dict = [dict(zip(column_names, row)) for row in result]
    # result_dict 变成 CountryInfo 对象
    return [StudentMatriculateCase(**row) for row in result_dict]


