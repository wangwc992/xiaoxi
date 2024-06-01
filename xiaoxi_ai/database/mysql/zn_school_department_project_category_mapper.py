'''CREATE TABLE `zn_school_department_project_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zsdp_id` int(11) NOT NULL COMMENT 'zn_school_department_project id',
  `category_id` int(11) NOT NULL COMMENT 'zn_school_major_category id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21588 DEFAULT CHARSET=utf8mb4 COMMENT='新版院校专业分类关联表';'''