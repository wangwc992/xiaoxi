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

 Date: 30/05/2024 13:37:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for service_confirm_school
-- ----------------------------
DROP TABLE IF EXISTS `service_confirm_school`;
CREATE TABLE `service_confirm_school`  (
  `id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '定校编号',
  `service_id` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '服务流程ID',
  `member_id` bigint(12) NULL DEFAULT NULL COMMENT '学生编号',
  `flow_id` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '合同编号',
  `service_confirm_type` tinyint(1) NULL DEFAULT 0 COMMENT '申请服务类型(0:定校, 1:加申语言)',
  `school_id` int(11) NOT NULL COMMENT '学校ID',
  `school_chinese_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '学校名称',
  `school_english_name` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '学校英文名称',
  `choice_rank` tinyint(4) NULL DEFAULT NULL COMMENT '同校志愿排序',
  `project_id` int(11) NOT NULL COMMENT '专业方向ID (项目ID)',
  `project_chinese_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '项目中文名称',
  `project_english_name` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '项目英文名称',
  `is_language` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0' COMMENT '是否配语言 0 否  1是',
  `start_date` date NULL DEFAULT NULL COMMENT '配备语言：开学日期',
  `apply_week` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '配备语言：申请周数',
  `other_remark` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '配备语言：其他备注',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态 1可编辑 2待评估 3通过 4驳回  同一serviceId，状态一致',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `svc_status` tinyint(1) UNSIGNED NULL DEFAULT 125 COMMENT '服务状态 同service_node',
  `svc_status_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '申请未提交' COMMENT '服务状态名称',
  `is_packaged` tinyint(1) NULL DEFAULT 0 COMMENT '是否打包课程  1是  0否',
  `package_school_id` int(11) NULL DEFAULT NULL COMMENT '打包课程：申请院校ID',
  `package_school_name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '打包课程：申请院校名称',
  `package_project_id` int(11) NULL DEFAULT NULL COMMENT '打包课程：专业ID 自定义传 0',
  `package_project_name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '打包课程：专业名称',
  `package_degree` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '打包课程：申请学位',
  `package_campus` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '打包课程：校区',
  `package_semester` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '打包课程：开学时间 yyyy-MM-01',
  `is_asny` tinyint(1) NULL DEFAULT 0 COMMENT '是否同步文签：1是  0否',
  `asny_date` datetime(0) NULL DEFAULT NULL COMMENT '同步文签时间',
  `reviewer_id` int(11) NULL DEFAULT NULL COMMENT '审核人ID',
  `reviewer_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '审核人名称',
  `campus` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '就读校区',
  `length_of_school` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '学制',
  `length_of_unit` tinyint(4) NULL DEFAULT NULL COMMENT '学制单位：1 周,2 月,3 年,4 学期',
  `semester` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '开学时间',
  `is_fraction_reduction` tinyint(11) NULL DEFAULT 0 COMMENT '是否需要减免学分 0否 1是',
  `country_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '国家编号',
  `country_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '国家名称',
  `academic_degree` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '学位',
  `major_no` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '专业编号',
  `majorlink` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '专业链接',
  `major_direction` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '专业小方向',
  `reject_reason` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '驳回愿意/修改意见',
  `reject_time` datetime(0) NULL DEFAULT NULL COMMENT '审核时间',
  `visa_apply_id` int(11) NULL DEFAULT NULL COMMENT '文签申请id,仅用于手动同步文签系统上的数据',
  `examine_flag` tinyint(4) NULL DEFAULT 0 COMMENT '文签审核学生信息 0未审核 1已审核',
  `delay_time` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '申请延期时间',
  `offer_feedback` tinyint(4) NULL DEFAULT NULL COMMENT '学生意愿, 接受offer时使用',
  `wish_detail` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '学生意愿详情',
  `update_feedback_origin` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '修改意愿来源 1-代理 2-学生',
  `reject_attach` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '定校驳回附件',
  `isTransfer` int(11) NULL DEFAULT 0 COMMENT '是否转案0:未转案 1:已转案',
  `trans_date` datetime(0) NULL DEFAULT NULL COMMENT '转案时间',
  `remarks_transfer` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '转案备注',
  `package_school_english_name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '打包课程：申请院校英文名称',
  `package_project_english_name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '打包课程：专业英文名称',
  `package_major_no` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '打包专业编号',
  `package_major_direction` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '打包专业小方向',
  `except_later_time` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '期望晚报道时间',
  `is_after_submit` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否加申1-是',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id`(`id`) USING BTREE,
  INDEX `idx_flow_id`(`flow_id`) USING BTREE,
  INDEX `service_confirm_school_service_id_index`(`service_id`) USING BTREE,
  INDEX `idx_projectId_svsStatus`(`project_id`, `svc_status`) USING BTREE,
  INDEX `idx_svc_status`(`svc_status`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '定校信息' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
