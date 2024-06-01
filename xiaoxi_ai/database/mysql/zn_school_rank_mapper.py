'''CREATE TABLE `zn_school_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) DEFAULT NULL COMMENT '院校表ID',
  `world_rank_usnews` int(5) DEFAULT NULL COMMENT '世界USNEWS排名',
  `world_rank_the` int(5) DEFAULT NULL COMMENT '世界泰晤士高等教育排名',
  `world_rank_qs` int(5) DEFAULT NULL COMMENT '世界QS排名',
  `local_rank_usnews` int(5) DEFAULT NULL COMMENT '地区USNEWS排名',
  `local_rank_the` int(5) DEFAULT NULL COMMENT '地区泰晤士高等教育排名',
  `local_rank_qs` int(5) DEFAULT NULL COMMENT '地区QS排名',
  `delete_status` int(1) DEFAULT '0' COMMENT '是否删除  0-未删除,1-已删除',
  `create_by` int(11) NOT NULL COMMENT '创建人',
  `update_by` int(11) NOT NULL COMMENT '更新人',
  `create_name` varchar(50) DEFAULT NULL COMMENT '创建人名称',
  `update_name` varchar(50) DEFAULT NULL COMMENT '更新人名称',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_school` (`school_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=20011 DEFAULT CHARSET=utf8mb4 COMMENT='院校排名表';'''