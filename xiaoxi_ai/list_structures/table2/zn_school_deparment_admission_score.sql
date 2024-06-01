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

 Date: 30/05/2024 13:35:51
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zn_school_deparment_admission_score
-- ----------------------------
DROP TABLE IF EXISTS `zn_school_deparment_admission_score`;
CREATE TABLE `zn_school_deparment_admission_score`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zsdp_id` int(11) NOT NULL COMMENT 'zh_school_department_project表id',
  `atar_score` decimal(6, 2) NULL DEFAULT NULL COMMENT 'ATAR分数',
  `ukalevel3_score` decimal(6, 2) NULL DEFAULT NULL COMMENT 'UKAlevel三科分数',
  `ukalevel3_score1` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'UKAlevel三科分数（一）',
  `ukalevel3_score2` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'UKAlevel三科分数（二）',
  `ukalevel3_score3` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'UKAlevel三科分数（三）',
  `ukalevel4_score` decimal(6, 2) NULL DEFAULT NULL COMMENT 'UKAlevel四科分数',
  `ib_score` decimal(6, 2) NULL DEFAULT NULL COMMENT 'IB分数',
  `sat_score` decimal(6, 2) NULL DEFAULT NULL COMMENT 'SAT分数',
  `act_score` decimal(6, 2) NULL DEFAULT NULL COMMENT 'ACT分数',
  `ap_score` decimal(6, 2) NULL DEFAULT NULL COMMENT 'AP分数',
  `ossd_score` decimal(6, 2) NULL DEFAULT NULL COMMENT 'OSSD分数',
  `bc_score` decimal(6, 2) NULL DEFAULT NULL COMMENT 'BC分数',
  `gaokao_score` char(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'GAOKAO分数',
  `c9_score` decimal(6, 2) NULL DEFAULT NULL COMMENT 'C9均分分数',
  `s985_score` decimal(6, 2) NULL DEFAULT NULL COMMENT '985均分分数',
  `s211_score` decimal(6, 2) NULL DEFAULT NULL COMMENT '211均分分数',
  `sn211_score` decimal(6, 2) NULL DEFAULT NULL COMMENT '非211均分分数',
  `b_accept_md_bg` tinyint(1) NULL DEFAULT 1 COMMENT '是否接受跨专业/需要相关背景',
  `atar_ask` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'ATAR要求',
  `ukalevel3_ask` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'UKAlevel三科要求',
  `ukalevel4_ask` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'UKAlevel四科要求',
  `ib_ask` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'IB要求',
  `sat_ask` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'SAT要求',
  `act_ask` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'ACT要求	',
  `ap_ask` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'AP要求',
  `ossd_ask` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'OSSD要求',
  `bc_ask` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'BC要求',
  `gaokao_ask` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'GAOKAO要求',
  `c9_ask` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'C9均分要求',
  `s985_ask` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '985均分要求',
  `s211_ask` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '211均分要求',
  `sn211_ask` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '非211均分要求',
  `accept_md_bg` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '是否接受跨专业/需要相关背景',
  `delete_status` int(1) NULL DEFAULT 0,
  `create_by` int(11) NOT NULL COMMENT 'zh_school_department_project表id',
  `update_by` int(11) NOT NULL COMMENT 'zh_school_department_project表id',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  `update_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_ukalevel3_score`(`ukalevel3_score`) USING BTREE,
  INDEX `idx_zsdp_id`(`zsdp_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12817 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
