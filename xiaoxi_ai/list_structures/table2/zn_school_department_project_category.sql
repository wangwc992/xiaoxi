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

 Date: 30/05/2024 13:37:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zn_school_department_project_category
-- ----------------------------
DROP TABLE IF EXISTS `zn_school_department_project_category`;
CREATE TABLE `zn_school_department_project_category`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zsdp_id` int(11) NOT NULL COMMENT 'zn_school_department_project id',
  `category_id` int(11) NOT NULL COMMENT 'zn_school_major_category id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21583 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '新版院校专业分类关联表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
