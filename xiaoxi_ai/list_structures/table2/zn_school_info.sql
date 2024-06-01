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

 Date: 30/05/2024 13:35:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zn_school_info
-- ----------------------------
DROP TABLE IF EXISTS `zn_school_info`;
CREATE TABLE `zn_school_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL COMMENT '国家ID',
  `country_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '国家名称',
  `chinese_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '院校中文名',
  `english_name` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '院校英文名',
  `logo_url` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '院校logo',
  `cover_url` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '院校背景图',
  `market_tags` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '院校标签 逗号分隔',
  `city_path` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '院校位置',
  `website` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '官网地址',
  `spider_id` int(11) NOT NULL DEFAULT 0 COMMENT '爬虫ID',
  `delete_status` int(1) NOT NULL DEFAULT 0 COMMENT '是否删除  0-未删除,1-已删除',
  `create_by` int(11) NOT NULL COMMENT '填写人',
  `update_by` int(11) NOT NULL COMMENT '更新人',
  `create_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人名称',
  `update_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '更新人名称',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `update_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  `comment_tags` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '评价标签',
  `is_popular` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否热门院校  1：是  0否',
  `fans_base_total` int(11) NOT NULL DEFAULT 0 COMMENT '关注基数',
  `school_sort` int(11) NULL DEFAULT 0 COMMENT '院校排序',
  `fans_total` int(11) NULL DEFAULT 0 COMMENT '关注人数',
  `school_abbreviations` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '院校简称',
  `fee_dimension` tinyint(4) NULL DEFAULT NULL COMMENT '申请费支付方式1-按院校;2-按专业3-其他',
  `apply_cycle_algorithm` int(11) NULL DEFAULT NULL COMMENT '申请周期-算法统计(自然日)',
  `apply_cycle_manual` int(11) NULL DEFAULT NULL COMMENT '申请周期-人工填写(自然日)',
  `period` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `weight` int(11) NOT NULL DEFAULT 0 COMMENT '排序权重（23.7-24.1的申请数）',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `uk_spider`(`spider_id`) USING BTREE,
  INDEX `idx_cid`(`country_id`) USING BTREE,
  INDEX `idx_del_status`(`delete_status`) USING BTREE,
  INDEX `country_id_index`(`country_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11477 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
