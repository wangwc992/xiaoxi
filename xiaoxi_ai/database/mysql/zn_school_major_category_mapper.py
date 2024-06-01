'''CREATE TABLE `zn_school_major_category` (
  `id` int(11) NOT NULL,
  `category_english_name` varchar(255) DEFAULT NULL COMMENT '分类英文名称',
  `zh_category_name` varchar(255) DEFAULT NULL COMMENT '分类中文名称',
  `html_code` varchar(20) NOT NULL COMMENT '分类代码',
  `category_level` int(2) NOT NULL COMMENT '分类级别',
  `parent_id` int(11) NOT NULL COMMENT '上级分类id',
  `deleted` int(1) NOT NULL DEFAULT '0',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='新版院校专业分类表';'''