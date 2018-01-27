/*
 Navicat Premium Data Transfer

 Source Server         : 本机Mysql数据库
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 28/01/2018 00:53:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for test1
-- ----------------------------
DROP TABLE IF EXISTS `test1`;
CREATE TABLE `test1` (
  `id_name` varchar(20) COLLATE utf8_croatian_ci NOT NULL,
  `money` int(30) NOT NULL,
  PRIMARY KEY (`id_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_croatian_ci;

-- ----------------------------
-- Records of test1
-- ----------------------------
BEGIN;
INSERT INTO `test1` VALUES ('张三', 801);
INSERT INTO `test1` VALUES ('李四', 1401);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
