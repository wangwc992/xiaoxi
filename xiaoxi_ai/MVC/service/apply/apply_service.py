class ApplyService:
    def __init__(self):
        pass


class ApplyTools:
    def __init__(self):
        pass

    def get_apply_info(self, service_id, apply_id, student_name):
        '''
            SQL query extracting info to answer the user's question.
            SQL should be written using this database schema:
            {database_schema_string}
            The query should be returned in plain text, not in JSON.
            The query should only contain grammars supported by SQLite.
        '''
    service_confirm_school = '''`service_confirm_school` (
                                    `id` varchar(20) NOT NULL COMMENT '定校编号',
                                    `service_id` varchar(11) NOT NULL COMMENT '服务流程ID',
                                    `flow_id` varchar(40) NOT NULL COMMENT '合同编号',
                                    `service_confirm_type` tinyint(1) DEFAULT '0' COMMENT '申请服务类型(0:定校, 1:加申语言)',
                                    `school_id` int(11) NOT NULL COMMENT '学校ID',
                                    `school_chinese_name` varchar(200) DEFAULT NULL COMMENT '学校名称',
                                    `school_english_name` varchar(300) DEFAULT NULL COMMENT '学校英文名称',
                                    `choice_rank` tinyint(4) DEFAULT NULL COMMENT '同校志愿排序',
                                    `project_id` int(11) NOT NULL COMMENT '专业方向ID (项目ID)',
                                    `project_chinese_name` varchar(200) DEFAULT NULL COMMENT '项目中文名称',
                                    `project_english_name` varchar(300) DEFAULT NULL COMMENT '项目英文名称'
                                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='定校信息';
                                 '''
    service_master = '''`service_master` (
                            `id` varchar(11) NOT NULL COMMENT '服务流程ID',
                            `user_real_name` varchar(40) DEFAULT NULL COMMENT '学生实名',
                            `adviser_name` varchar(40) DEFAULT NULL COMMENT '顾问姓名'
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='定校服务进程表';
                    '''
    apply_main = '''`apply_main` (
                        `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
                        `service_id` varchar(20) DEFAULT NULL COMMENT '服务编号',
                    ) ENGINE=InnoDB AUTO_INCREMENT=47381 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='申请材料-主表';
                '''
    apply_education = '''`apply_education` (
                              `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
                              `main_id` int(11) NOT NULL COMMENT 'main_id',
                              `begin_date` date DEFAULT NULL COMMENT '开始时间',
                              `end_data` date DEFAULT NULL COMMENT '结束时间',
                              `school_name` varchar(100) DEFAULT NULL COMMENT '学校名称',
                              `project_name` varchar(100) DEFAULT '' COMMENT '专业信息',
                              `degree` varchar(50) DEFAULT NULL COMMENT '学位',
                              `gpa` varchar(255) DEFAULT NULL COMMENT 'GPA',
                              `country_name` varchar(200) DEFAULT '' COMMENT '校区所在国家',
                          ) ENGINE=InnoDB AUTO_INCREMENT=30777 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='申请材料-教育信息表';
                  '''
