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

 Date: 30/05/2024 13:35:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zn_school_department_project
-- ----------------------------
DROP TABLE IF EXISTS `zn_school_department_project`;
CREATE TABLE `zn_school_department_project`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) NOT NULL COMMENT '院校表ID',
  `campus_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '校区id 已废 见中间表 zn_school_project_campus',
  `campus_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '校区名称',
  `depart_id` int(11) NOT NULL COMMENT '院系表ID',
  `depart_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '院系名称',
  `course_code` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '课程编码',
  `chinese_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '项目中文名',
  `english_name` varchar(600) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '项目英文名',
  `introduction` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '项目介绍',
  `degree_level` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '学位等级',
  `degree_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '学位名称',
  `degree_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '学位类型',
  `length_of_full` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '全日制学制',
  `length_of_schoolings` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '时间-年月日，学制时间',
  `length_of_part` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '非全日制学制',
  `semester` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '开学时间',
  `time_apply_deadline` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '申请截止时间',
  `time_offer` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'Offer发放时间',
  `time_offer_deadline` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'Offer发放截止时间',
  `science_requirement` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '学术要求',
  `major_link` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '专业链接',
  `fee_apply` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '申请费用',
  `fee_tuition` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '学费',
  `fee_book` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '书本费',
  `fee_life` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '生活费',
  `fee_traffic` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '交通费',
  `fee_accommodation` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '住宿费用',
  `fee_others` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '其他费用',
  `fee_total` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '总花费',
  `score_gpa` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'GPA成绩',
  `score_act` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'ACT成绩',
  `score_sat` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'SAT成绩',
  `score_sat2` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'SAT2成绩',
  `score_gre` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'GRE成绩',
  `score_gmat` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'GMAT成绩',
  `score_ielts` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '雅思成绩',
  `score_ielts_total` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '雅思总分',
  `score_toefl` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '托福成绩',
  `score_toefl_total` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '托福总分',
  `score_native` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'native成绩',
  `score_others` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '其他成绩',
  `material` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '申请材料',
  `admission_elements` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '申请要点',
  `reduce_status` bigint(1) NULL DEFAULT 0 COMMENT '是否减免 1是0否',
  `reduce_condition` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '减免条件',
  `spider_id` int(11) NULL DEFAULT NULL COMMENT '爬虫ID',
  `delete_status` int(1) NULL DEFAULT 0 COMMENT '是否删除  0-未删除,1-已删除',
  `create_by` int(11) NOT NULL COMMENT '创建人',
  `update_by` int(11) NOT NULL COMMENT '更新人',
  `create_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人名称',
  `update_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '更新人名称',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `update_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  `attention_total` int(10) NOT NULL DEFAULT 0 COMMENT '关注总数',
  `score` decimal(3, 1) NULL DEFAULT NULL COMMENT '评分',
  `market_tags` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '标签',
  `orderby` int(10) NOT NULL DEFAULT 0 COMMENT '排序',
  `application_fee_value` decimal(8, 2) NULL DEFAULT NULL COMMENT '申请费值',
  `currency_id` int(11) NULL DEFAULT NULL COMMENT '币种id',
  `small_direction` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '专业小方向',
  `project_abbreviations` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '专业简称',
  `opening_month` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '开学月份',
  `org_id` int(11) NULL DEFAULT NULL COMMENT '洗数据保留原始表id',
  `career_opportunities` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '职业规划',
  `cricos_code` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '澳洲专用',
  `weight` bigint(20) NOT NULL DEFAULT 0 COMMENT '排序权重（23.7-24.1申请数）',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_school`(`school_id`) USING BTREE,
  INDEX `idx_depart`(`depart_id`) USING BTREE,
  INDEX `uk_spider`(`spider_id`) USING BTREE,
  INDEX `idx_order`(`orderby`) USING BTREE,
  INDEX `idx_del_status`(`delete_status`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 209340 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '院校院系招生项目表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
