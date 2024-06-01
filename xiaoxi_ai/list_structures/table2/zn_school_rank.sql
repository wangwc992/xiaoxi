/*
 Navicat Premium Data Transfer

 Source Server         : 120.92.116.101
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : 120.92.116.101:9200
 Source Schema         : xxlxdb

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 30/05/2024 13:37:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zn_school_rank
-- ----------------------------
DROP TABLE IF EXISTS `zn_school_rank`;
CREATE TABLE `zn_school_rank`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) NULL DEFAULT NULL COMMENT '院校表ID',
  `world_rank_usnews` int(5) NULL DEFAULT NULL COMMENT '世界USNEWS排名',
  `world_rank_the` int(5) NULL DEFAULT NULL COMMENT '世界泰晤士高等教育排名',
  `world_rank_qs` int(5) NULL DEFAULT NULL COMMENT '世界QS排名',
  `local_rank_usnews` int(5) NULL DEFAULT NULL COMMENT '地区USNEWS排名',
  `local_rank_the` int(5) NULL DEFAULT NULL COMMENT '地区泰晤士高等教育排名',
  `local_rank_qs` int(5) NULL DEFAULT NULL COMMENT '地区QS排名',
  `delete_status` int(1) NULL DEFAULT 0 COMMENT '是否删除  0-未删除,1-已删除',
  `create_by` int(11) NOT NULL COMMENT '创建人',
  `update_by` int(11) NOT NULL COMMENT '更新人',
  `create_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人名称',
  `update_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '更新人名称',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `update_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `uk_school`(`school_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20011 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '院校排名表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
