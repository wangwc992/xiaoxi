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

 Date: 30/05/2024 13:38:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zn_school_major_category
-- ----------------------------
DROP TABLE IF EXISTS `zn_school_major_category`;
CREATE TABLE `zn_school_major_category`  (
  `id` int(11) NOT NULL,
  `category_english_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '分类英文名称',
  `zh_category_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '分类中文名称',
  `html_code` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '分类代码',
  `category_level` int(2) NOT NULL COMMENT '分类级别',
  `parent_id` int(11) NOT NULL COMMENT '上级分类id',
  `deleted` int(1) NOT NULL DEFAULT 0,
  `create_time` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0),
  `update_time` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '新版院校专业分类表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
