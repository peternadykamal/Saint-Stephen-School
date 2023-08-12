-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: talmza_dev
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `talmza_dev`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `talmza_dev` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `talmza_dev`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add profile',7,'add_profile'),(26,'Can change profile',7,'change_profile'),(27,'Can delete profile',7,'delete_profile'),(28,'Can view profile',7,'view_profile'),(29,'Can add address',8,'add_address'),(30,'Can change address',8,'change_address'),(31,'Can delete address',8,'delete_address'),(32,'Can view address',8,'view_address'),(33,'Can add school level',9,'add_schoollevel'),(34,'Can change school level',9,'change_schoollevel'),(35,'Can delete school level',9,'delete_schoollevel'),(36,'Can view school level',9,'view_schoollevel'),(37,'Can add talmza level',10,'add_talmzalevel'),(38,'Can change talmza level',10,'change_talmzalevel'),(39,'Can delete talmza level',10,'delete_talmzalevel'),(40,'Can view talmza level',10,'view_talmzalevel'),(41,'Can add profile form log',11,'add_profileformlog'),(42,'Can change profile form log',11,'change_profileformlog'),(43,'Can delete profile form log',11,'delete_profileformlog'),(44,'Can view profile form log',11,'view_profileformlog'),(49,'Can add expenses profile form',12,'add_expensesprofileform'),(50,'Can change expenses profile form',12,'change_expensesprofileform'),(51,'Can delete expenses profile form',12,'delete_expensesprofileform'),(52,'Can view expenses profile form',12,'view_expensesprofileform'),(53,'Can add user permission tag',13,'add_userpermissiontag'),(54,'Can change user permission tag',13,'change_userpermissiontag'),(55,'Can delete user permission tag',13,'delete_userpermissiontag'),(56,'Can view user permission tag',13,'view_userpermissiontag'),(57,'view profile talmza level',7,'view_profile_talmza_level'),(58,'change profile talmza level',7,'change_profile_talmza_level'),(59,'view profile current talmza level',7,'view_profile_current_talmza_level_year'),(60,'change profile current talmza level',7,'change_profile_current_talmza_level_year'),(61,'Can add temp',14,'add_temp'),(62,'Can change temp',14,'change_temp'),(63,'Can delete temp',14,'delete_temp'),(64,'Can view temp',14,'view_temp');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$UQmrWAogdDcKBlPGg0dYrW$qL1mrp45R/R+q3aNPIX2RbwU+ZmZvF/7T4A/qTfC1+0=','2023-08-12 16:43:08.929850',1,'peter','','','peter@gmail.com',1,1,'2023-07-29 11:00:34.146586'),(2,'pbkdf2_sha256$600000$F7EvCOQhCLRHpcXjaEgmXm$798hduGVb8QT0jH0kzFOb07bXGUVDRElM1cfejtAxyc=','2023-08-12 16:43:30.719584',1,'19102929','','','kamalnadykamal@gmail.com',1,1,'2023-07-29 11:02:06.584175'),(8,'pbkdf2_sha256$600000$pDmbWAwJ9yoJw1ImNmKNFT$c1RX1OBcLVwejuKCzv5RxjqiIQxuV3RXeHfCoS2ioOM=',NULL,0,'2300008','','','',0,1,'2023-07-31 12:38:48.000000'),(9,'pbkdf2_sha256$600000$V6DP2mPRsGl1am19MzZevY$Ra1zjaLOO/ompkAe6YHlxFBrV/6HZyog84Ur16RizLc=',NULL,0,'2300009','','','',0,1,'2023-07-31 15:53:49.000000'),(12,'pbkdf2_sha256$600000$qTvMiherDrvOyLCbJtHyHZ$ipm+c8vZ0oeHNMcgnITaWDLekXgql5/X3XWDkAUx4AA=',NULL,0,'2300012','','','',0,1,'2023-07-31 15:59:50.000000'),(13,'pbkdf2_sha256$600000$cgtauUnYSCNPZZZIUMyD4c$YHTgSOxttCyy9mTIVVNckKDhFmEU7Kax5WDjBB3udrU=',NULL,0,'2300013','','','',0,1,'2023-07-31 16:01:47.000000'),(91,'pbkdf2_sha256$600000$VMsMLKH8YcXKq0QqInaz4U$vABVXa/7hGv+QdKjR9+Cpaf0+RZDKGd2IWhycSyBaEw=',NULL,0,'2300091','','','',0,1,'2023-08-06 13:36:11.796125'),(104,'pbkdf2_sha256$600000$w9pezStohAlWYNADy4R0W8$fzCBabENnHZF/Aozql8Y0QnlaUSoD9iXyPCr7XamYl4=',NULL,0,'2300104','','','',0,1,'2023-08-06 14:28:10.769723'),(105,'pbkdf2_sha256$600000$I1l7zC8TG1q6qjhXiEgkbO$+8mSkHHWDAzLTF8SBMG3JyCs44kmrEAKzgwN6UA0pOk=',NULL,0,'2300105','','','',0,1,'2023-08-08 07:10:32.198407'),(117,'pbkdf2_sha256$600000$fNCwYbqRjPF7hpoTefF0u2$x5yaGk2W7XZUxmo2T8ceD6IVvKeoq85L/Wp6iEHv270=',NULL,0,'2300117','','','',0,1,'2023-08-12 11:41:41.136182');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=428 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-07-29 19:34:22.720023','74f581f3-cca0-4506-beb3-95a8c938203a','المستوي الأول',1,'[{\"added\": {}}]',10,2),(2,'2023-07-29 19:34:32.549710','6b3aa176-2544-403e-8c05-a51fd36a4351','المستوي الثاني',1,'[{\"added\": {}}]',10,2),(3,'2023-07-29 19:34:44.034433','ba6c0d1e-e63d-4d27-a689-c55e65611bd6','المستوي الثالث',1,'[{\"added\": {}}]',10,2),(4,'2023-07-29 19:34:52.303763','362754ed-35c2-41e8-8cfc-adc7b1178191','المستوي الرابع',1,'[{\"added\": {}}]',10,2),(5,'2023-07-29 19:34:57.636517','74f581f3-cca0-4506-beb3-95a8c938203a','المستوي الأول',2,'[{\"changed\": {\"fields\": [\"Next level\"]}}]',10,2),(6,'2023-07-29 19:35:01.401490','6b3aa176-2544-403e-8c05-a51fd36a4351','المستوي الثاني',2,'[{\"changed\": {\"fields\": [\"Next level\"]}}]',10,2),(7,'2023-07-29 19:35:06.545951','ba6c0d1e-e63d-4d27-a689-c55e65611bd6','المستوي الثالث',2,'[{\"changed\": {\"fields\": [\"Next level\"]}}]',10,2),(8,'2023-07-29 19:35:11.430845','74f581f3-cca0-4506-beb3-95a8c938203a','المستوي الأول',2,'[]',10,2),(9,'2023-07-29 19:38:24.499167','410faf62-e732-4eb4-99bd-0ad117730406','الصف اقل من حضانة # 0',1,'[{\"added\": {}}]',9,2),(10,'2023-07-29 19:38:32.184219','d0b12a75-71bc-40e4-94ed-9745a604bef3','الصف حضانة # 1',1,'[{\"added\": {}}]',9,2),(11,'2023-07-29 19:38:41.746720','af153d90-953b-48e6-b8d8-ffa6e2a32320','الصف الابتدائي # 2',1,'[{\"added\": {}}]',9,2),(12,'2023-07-29 19:39:11.022150','750700e2-0aa9-462f-83a8-de322f87cc7e','الصف الإعدادي # 4',1,'[{\"added\": {}}]',9,2),(13,'2023-07-29 19:40:28.482587','c8fa8e83-73f0-45e5-a820-5e2c7d919239','الصف ثانوي # 5',1,'[{\"added\": {}}]',9,2),(14,'2023-07-29 19:40:33.402224','410faf62-e732-4eb4-99bd-0ad117730406','الصف اقل من حضانة # 0',2,'[{\"changed\": {\"fields\": [\"Next level\"]}}]',9,2),(15,'2023-07-29 19:40:37.914760','d0b12a75-71bc-40e4-94ed-9745a604bef3','الصف حضانة # 1',2,'[{\"changed\": {\"fields\": [\"Next level\"]}}]',9,2),(16,'2023-07-29 19:40:47.810226','af153d90-953b-48e6-b8d8-ffa6e2a32320','الصف الابتدائي # 2',2,'[{\"changed\": {\"fields\": [\"Next level\"]}}]',9,2),(17,'2023-07-29 19:40:55.971084','750700e2-0aa9-462f-83a8-de322f87cc7e','الصف الإعدادي # 3',2,'[{\"changed\": {\"fields\": [\"Level number\", \"Next level\"]}}]',9,2),(18,'2023-07-29 19:41:04.968520','c8fa8e83-73f0-45e5-a820-5e2c7d919239','الصف ثانوي # 4',2,'[{\"changed\": {\"fields\": [\"Level number\"]}}]',9,2),(19,'2023-07-29 20:03:26.425101','0b23ec22-3483-4227-884e-177432bc0b1f','الصف جامعة # 5',1,'[{\"added\": {}}]',9,2),(20,'2023-07-29 20:03:37.411143','07889dac-ae48-48b8-8d2b-683ee35d8ab2','الصف خريج # 6',1,'[{\"added\": {}}]',9,2),(21,'2023-07-29 20:03:48.246703','c8fa8e83-73f0-45e5-a820-5e2c7d919239','الصف ثانوي # 4',2,'[{\"changed\": {\"fields\": [\"Next level\"]}}]',9,2),(22,'2023-07-29 20:03:53.042036','0b23ec22-3483-4227-884e-177432bc0b1f','الصف جامعة # 5',2,'[{\"changed\": {\"fields\": [\"Next level\"]}}]',9,2),(23,'2023-07-29 20:03:53.089038','0b23ec22-3483-4227-884e-177432bc0b1f','الصف جامعة # 5',2,'[]',9,2),(24,'2023-07-29 20:05:28.913793','410faf62-e732-4eb4-99bd-0ad117730406','الصف اقل من حضانة # 0',2,'[{\"changed\": {\"fields\": [\"Number of years\"]}}]',9,2),(25,'2023-07-29 20:05:48.171696','bccd9679-1e53-421b-92b5-5358b3f0342f','None',1,'[{\"added\": {}}]',8,2),(26,'2023-07-29 20:05:53.911485','bccd9679-1e53-421b-92b5-5358b3f0342f','None',3,'',8,2),(27,'2023-07-29 20:05:57.872557','175dd702-ffe8-4842-896c-5de4031eed2f','None',1,'[{\"added\": {}}]',8,2),(28,'2023-07-29 20:06:12.053802','175dd702-ffe8-4842-896c-5de4031eed2f','None',3,'',8,2),(29,'2023-07-30 17:14:58.501101','3','test',1,'[{\"added\": {}}]',4,2),(30,'2023-07-30 17:15:11.170505','3','test',3,'',4,2),(31,'2023-07-30 17:33:13.141088','5','test',1,'[{\"added\": {}}]',4,2),(32,'2023-07-30 17:38:14.991441','df0213f0-2fa5-411b-ab1c-60a6eba82877',' test',3,'',7,2),(33,'2023-07-30 18:10:57.793987','6','2300006',1,'[{\"added\": {}}]',4,2),(34,'2023-07-30 18:11:11.752291','6','test',2,'[]',4,2),(35,'2023-07-30 18:11:45.139297','6','test',3,'',4,2),(36,'2023-07-30 18:11:57.031499','7','2300007',1,'[{\"added\": {}}]',4,2),(37,'2023-07-30 18:12:12.096381','7','2300007',3,'',4,2),(38,'2023-07-31 11:28:35.303510','0da9610f-a92a-4c9e-a6b0-26fde2ba6fcc','',1,'[{\"added\": {}}]',8,2),(39,'2023-07-31 11:28:42.100111','0da9610f-a92a-4c9e-a6b0-26fde2ba6fcc','',3,'',8,2),(40,'2023-07-31 11:30:07.751158','2e3f9832-b2f1-4c5c-ab9b-f5659b34ae75','مبنا: لوتس, شارع: جميلة ابو حريد, فرع من: يقوت الحموي, الطابق: 7, رقم الشقة: 704, الحي: السيوف, تفاصيل إضافية: بجوار ماركت مصباح',1,'[{\"added\": {}}]',8,2),(41,'2023-07-31 12:38:49.352824','8','2300008',1,'[{\"added\": {}}]',4,2),(42,'2023-07-31 12:38:55.538025','8','2300008',2,'[]',4,2),(43,'2023-07-31 12:53:33.029299','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عماد 2300008',2,'[{\"changed\": {\"fields\": [\"Name\", \"Birthdate\", \"Talmza level\", \"School level\", \"Address\", \"Gender\", \"Phone number\", \"Father phone number\", \"Mother phone number\", \"Mobile follow up on WhatsApp\", \"ConfessionFather\", \"Deaconess\"]}}]',7,2),(44,'2023-07-31 13:07:33.300983','32e4d997-c061-4018-8a06-02e2cf0aef57','المستوي اقل من تمهيدي # 0',1,'[{\"added\": {}}]',10,2),(45,'2023-07-31 13:07:56.194056','d2be3f99-4708-4d55-bee7-49c24094c125','المستوي تمهيدي # 1',1,'[{\"added\": {}}]',10,2),(46,'2023-07-31 13:08:10.292198','362754ed-35c2-41e8-8cfc-adc7b1178191','المستوي الرابع # 5',2,'[{\"changed\": {\"fields\": [\"Level number\"]}}]',10,2),(47,'2023-07-31 13:08:41.342963','74f581f3-cca0-4506-beb3-95a8c938203a','المستوي الأول # 2',2,'[{\"changed\": {\"fields\": [\"Level number\"]}}]',10,2),(48,'2023-07-31 13:08:46.148405','6b3aa176-2544-403e-8c05-a51fd36a4351','المستوي الثاني # 3',2,'[{\"changed\": {\"fields\": [\"Level number\"]}}]',10,2),(49,'2023-07-31 13:08:52.430896','ba6c0d1e-e63d-4d27-a689-c55e65611bd6','المستوي الثالث # 4',2,'[{\"changed\": {\"fields\": [\"Level number\"]}}]',10,2),(50,'2023-07-31 13:09:05.444248','32e4d997-c061-4018-8a06-02e2cf0aef57','المستوي اقل من تمهيدي # 0',2,'[{\"changed\": {\"fields\": [\"Next level\"]}}]',10,2),(51,'2023-07-31 13:09:15.652426','d2be3f99-4708-4d55-bee7-49c24094c125','المستوي تمهيدي # 1',2,'[{\"changed\": {\"fields\": [\"Next level\"]}}]',10,2),(52,'2023-07-31 14:33:13.137694','d2be3f99-4708-4d55-bee7-49c24094c125','المستوي تمهيدي # 1',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',10,2),(53,'2023-07-31 14:33:34.620031','d2be3f99-4708-4d55-bee7-49c24094c125','المستوي تمهيدي # 1',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',10,2),(54,'2023-07-31 14:33:43.721198','d2be3f99-4708-4d55-bee7-49c24094c125','المستوي تمهيدي # 1',2,'[]',10,2),(55,'2023-07-31 14:33:48.699559','74f581f3-cca0-4506-beb3-95a8c938203a','المستوي الأول # 2',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',10,2),(56,'2023-07-31 14:33:52.905483','6b3aa176-2544-403e-8c05-a51fd36a4351','المستوي الثاني # 3',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',10,2),(57,'2023-07-31 14:33:57.798548','ba6c0d1e-e63d-4d27-a689-c55e65611bd6','المستوي الثالث # 4',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',10,2),(58,'2023-07-31 14:34:02.538374','362754ed-35c2-41e8-8cfc-adc7b1178191','المستوي الرابع # 5',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',10,2),(59,'2023-07-31 14:34:32.756550','d0b12a75-71bc-40e4-94ed-9745a604bef3','الصف حضانة # 1',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',9,2),(60,'2023-07-31 14:35:37.886622','af153d90-953b-48e6-b8d8-ffa6e2a32320','# 2 الصف الابتدائي',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',9,2),(61,'2023-07-31 14:35:41.909980','750700e2-0aa9-462f-83a8-de322f87cc7e','# 3 الصف الإعدادي',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',9,2),(62,'2023-07-31 14:35:47.264909','c8fa8e83-73f0-45e5-a820-5e2c7d919239','# 4 الصف ثانوي',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',9,2),(63,'2023-07-31 14:35:55.591252','0b23ec22-3483-4227-884e-177432bc0b1f','# 5 الصف جامعة',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',9,2),(64,'2023-07-31 14:37:06.551892','07889dac-ae48-48b8-8d2b-683ee35d8ab2','# 6 الصف خريج',2,'[{\"changed\": {\"fields\": [\"Prevues level\"]}}]',9,2),(65,'2023-07-31 14:42:24.834552','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عماد 2300008',2,'[{\"changed\": {\"fields\": [\"Talmza level\"]}}]',7,2),(66,'2023-07-31 14:44:05.331595','32e4d997-c061-4018-8a06-02e2cf0aef57','# 0 المستوي اقل من تمهيدي',2,'[]',10,2),(67,'2023-07-31 14:45:13.030050','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عماد 2300008',2,'[{\"changed\": {\"fields\": [\"CurrentTalmzaLevelYear\"]}}]',7,2),(68,'2023-07-31 14:45:36.051116','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عماد 2300008',2,'[{\"changed\": {\"fields\": [\"Talmza level\", \"CurrentTalmzaLevelYear\"]}}]',7,2),(69,'2023-07-31 14:52:07.287484','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عماد 2300008',2,'[{\"changed\": {\"fields\": [\"Talmza level\"]}}]',7,2),(70,'2023-07-31 15:01:13.956629','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عماد 2300008',2,'[{\"changed\": {\"fields\": [\"School level\", \"CurrentSchoolLevelYear\"]}}]',7,2),(71,'2023-07-31 15:52:28.137358','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عمادX 2300008',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',7,2),(72,'2023-07-31 15:53:49.445600','9','2300009',1,'[{\"added\": {}}]',4,2),(73,'2023-07-31 15:53:51.969847','9','2300009',2,'[]',4,2),(74,'2023-07-31 15:59:22.951569','b8e42c89-a886-4ec6-9f96-095c6c29f573','مبنا: لوتس, شارع: جميلة ابو حريد, متفرع من: يقوت الحموي, الطابق: 7, رقم الشقة: 704, الحي: السيوف, تفاصيل إضافية: بجوار ماركت مصباح',1,'[{\"added\": {}}]',8,2),(75,'2023-07-31 15:59:36.366111','b27d3b20-9f9c-4b81-bc38-de70d4996bbb','جورج سدقي متحت عبدالغفورX 2300009',2,'[{\"changed\": {\"fields\": [\"Name\", \"Birthdate\", \"Talmza level\", \"CurrentTalmzaLevelYear\", \"School level\", \"CurrentSchoolLevelYear\", \"Address\", \"Gender\", \"Phone number\", \"Father phone number\", \"Mother phone number\", \"Mobile follow up on WhatsApp\", \"ConfessionFather\", \"Deaconess\"]}}]',7,2),(76,'2023-07-31 15:59:51.027618','12','2300012',1,'[{\"added\": {}}]',4,2),(77,'2023-07-31 15:59:53.234359','12','2300012',2,'[]',4,2),(78,'2023-07-31 16:01:08.260313','c76010b9-a1bd-4239-9140-7c1115789b85','مبنا: لوتس, شارع: جميلة ابو حريد, متفرع من: يقوت الحموي, الطابق: 7, رقم الشقة: 704, الحي: السيوف, تفاصيل إضافية: بجوار ماركت مصباح',1,'[{\"added\": {}}]',8,2),(79,'2023-07-31 16:01:35.429593','30438371-1291-4ebd-9a94-23b19ae7b180','مينا عماد بيشوي فتحيX 2300012',2,'[{\"changed\": {\"fields\": [\"Name\", \"Birthdate\", \"Talmza level\", \"CurrentTalmzaLevelYear\", \"School level\", \"Address\", \"Gender\", \"Phone number\", \"Father phone number\", \"Mother phone number\", \"Mobile follow up on WhatsApp\", \"ConfessionFather\", \"Deaconess\"]}}]',7,2),(80,'2023-07-31 16:01:47.384099','13','2300013',1,'[{\"added\": {}}]',4,2),(81,'2023-07-31 16:01:49.483348','13','2300013',2,'[]',4,2),(82,'2023-07-31 16:03:02.079794','72e74c5f-e753-4852-8ad8-7fd2d76783dd','مبنا: لوتس, شارع: جميلة ابو حريد, متفرع من: يقوت الحموي, الطابق: 7, رقم الشقة: 704, الحي: السيوف, تفاصيل إضافية: بجوار ماركت مصباح',1,'[{\"added\": {}}]',8,2),(83,'2023-07-31 16:03:29.845994','a9ae08e4-16a0-4237-af3b-c872f789ee79','ريتا جمال ملاك شربات 2300013',2,'[{\"changed\": {\"fields\": [\"Name\", \"Birthdate\", \"Talmza level\", \"School level\", \"Address\", \"Gender\", \"Phone number\", \"Father phone number\", \"Mother phone number\", \"Mobile follow up on WhatsApp\", \"ConfessionFather\", \"Deaconess\"]}}]',7,2),(84,'2023-07-31 17:22:01.288369','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عمادX 2300008',2,'[{\"changed\": {\"fields\": [\"Talmza level\"]}}]',7,2),(85,'2023-07-31 17:22:06.758950','b27d3b20-9f9c-4b81-bc38-de70d4996bbb','جورج سدقي متحت عبدالغفورX 2300009',2,'[{\"changed\": {\"fields\": [\"Talmza level\"]}}]',7,2),(86,'2023-07-31 17:28:49.167138','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عمادX 2300008',2,'[{\"changed\": {\"fields\": [\"School level\"]}}]',7,2),(87,'2023-07-31 17:28:57.316720','b27d3b20-9f9c-4b81-bc38-de70d4996bbb','جورج سدقي متحت عبدالغفورX 2300009',2,'[{\"changed\": {\"fields\": [\"School level\"]}}]',7,2),(88,'2023-07-31 17:29:09.160173','30438371-1291-4ebd-9a94-23b19ae7b180','مينا عماد بيشوي فتحيX 2300012',2,'[]',7,2),(89,'2023-07-31 17:29:15.835877','a9ae08e4-16a0-4237-af3b-c872f789ee79','ريتا جمال ملاك شربات 2300013',2,'[]',7,2),(90,'2023-07-31 17:38:02.978062','b27d3b20-9f9c-4b81-bc38-de70d4996bbb','جورج سدقي متحت عبدالغفورX 2300009',2,'[{\"changed\": {\"fields\": [\"CurrentSchoolLevelYear\"]}}]',7,2),(91,'2023-07-31 19:22:33.679994','14','2300014',1,'[{\"added\": {}}]',4,2),(92,'2023-07-31 19:22:35.483888','14','2300014',2,'[]',4,2),(93,'2023-07-31 19:22:51.952278','14','delete',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(94,'2023-07-31 20:54:29.658021','ee026d8d-40b2-419c-8d4e-ff08049b7c9d','مبنا: لوتس, شارع: جميلة ابو حريد, متفرع من: يقوت الحموي, الطابق: 7, رقم الشقة: 704, الحي: السيوف, تفاصيل إضافية: بجوار ماركت مصباح',1,'[{\"added\": {}}]',8,2),(95,'2023-07-31 21:21:00.873477','7a44d4d7-2685-41c3-9551-282b5f825ba4','شادي جرجس صموئيل فتحي delete',3,'',7,2),(96,'2023-07-31 21:24:04.339679','14','delete',3,'',4,2),(97,'2023-07-31 21:44:42.046483','15','2300015',1,'[{\"added\": {}}]',4,2),(98,'2023-07-31 21:44:51.178638','15','delete',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(99,'2023-08-02 17:45:19.582684','ba6c0d1e-e63d-4d27-a689-c55e65611bd6',' المستوي الثالث',2,'[{\"changed\": {\"fields\": [\"Number of years\"]}}]',10,2),(100,'2023-08-02 17:47:32.590643','ba6c0d1e-e63d-4d27-a689-c55e65611bd6',' المستوي الثالث',2,'[{\"changed\": {\"fields\": [\"Number of years\"]}}]',10,2),(101,'2023-08-02 17:59:49.605144','2b86e0bd-2981-44a1-950c-b5d9ac3fc793','شfsdafادي جرجdsfس صموئيل فتحي 2300017',3,'',7,2),(102,'2023-08-02 18:02:33.508043','fcdf4cd1-9b9b-41ca-a106-fb27775d4cbe','شfsdafادي جرجdsfس صموئيل فتحي 2300018',3,'',7,2),(103,'2023-08-02 18:04:08.726149','accba649-247b-4887-b195-28933ea3f1c2','شfsdafادي جرجdsfس صموئيل فتحي 2300019',3,'',7,2),(104,'2023-08-02 18:16:39.586586','f39811bf-5045-4f78-955b-a420dcfb04eb','شfsdafادي جرجdsfس صموئيل فتحي 2300020',3,'',7,2),(105,'2023-08-02 18:16:53.382383','8bec9845-2109-4e43-9baa-aece8a3312b7','شfsdafادي جرجdsfس صموئيل فتحي 2300021',3,'',7,2),(106,'2023-08-02 18:16:57.857718','c8d0e2b8-8542-4ee8-b549-703796f9ff41','شادي جرجس صموئيل فتحي 2300016',3,'',7,2),(107,'2023-08-02 18:19:04.719097','bcbb71d5-8bfc-49eb-9d0e-26fe1ce94aa4','شfsdafادي جرجdsfس صموئيل فتحي 2300022',3,'',7,2),(108,'2023-08-02 18:19:57.779992','6f3f9905-020f-43df-b1f5-1b3aaeddfe86','شادي جرجس صموئيل فتحي 2300023',3,'',7,2),(109,'2023-08-02 18:30:34.694342','97c0b3b1-f62d-46ff-aae4-69aebde6c42b','شادي جرجس صموئيل فتحي 2300024',3,'',7,2),(110,'2023-08-02 18:36:39.254296','2d40d7f4-c901-4aff-a521-53ad9d5a42a0','شادي جرجس صموئيل فتحي 2300025',3,'',7,2),(111,'2023-08-02 18:36:55.017180','a0bbb6e2-566e-4c44-9e81-680af28bed7a','شادي جرجس صموئيل فتحي 2300026',3,'',7,2),(112,'2023-08-02 18:44:56.609669','7484f3e4-db37-4adc-80b9-44017d8857e0','شادي جرجس صموئيل فتحي 2300027',3,'',7,2),(113,'2023-08-02 18:45:13.649528','193ed2f4-4eb0-4e6a-84fa-42749f86a8f7','شادي جرجس صموئيل فتحي 2300028',3,'',7,2),(114,'2023-08-02 18:52:10.678605','ecad7a32-78a7-41f8-8341-0aea237239c5','شادي جرجس صموئيل فتحي 2300029',3,'',7,2),(115,'2023-08-02 18:55:00.512453','9a7ddc6b-6bcb-47d8-853b-98640624927c','شادي جرجس صموئيل فتحي 2300032',3,'',7,2),(116,'2023-08-02 19:04:52.553187','7b35b037-2cbd-4ce8-932a-f36609c44c6d','شادي حنين جرجس بخيت 2300033',3,'',7,2),(117,'2023-08-02 19:18:24.832070','80bd76a1-0561-436f-b760-0ac3d79fe6e7','شادي حنين جرجس بخيت 2300034',3,'',7,2),(118,'2023-08-03 05:49:48.271896','4a913c80-c1cc-4736-9db7-34ca9598a9be','شادي حنين جرجس بخيت 2300035',3,'',7,2),(119,'2023-08-03 05:52:46.994968','3aecca48-a951-43d4-afed-06e7fa14bd9c','',3,'',8,2),(120,'2023-08-03 05:52:46.997969','390b64b0-649a-4235-80de-3fafb4b86808','مبنا: لوتس, شارع: جميلة ابو حريد, الطابق: 7',3,'',8,2),(121,'2023-08-03 05:52:46.999969','12949550-8440-44ed-9e5f-c63ecaf5a9c7','مبنا: لوتس, الحي: السيوف',3,'',8,2),(122,'2023-08-03 05:52:47.001969','0ed25d0a-e554-49e4-b3b1-93c28bf236b3','',3,'',8,2),(123,'2023-08-03 05:52:55.878150','cebc7207-10d8-4bd2-a1c3-8d3e5c10ccba','مبنا: لوتس, شارع: جميلة ابو حريد, الطابق: 7, تفاصيل إضافية: قرب من مصباح ماركت',3,'',8,2),(124,'2023-08-03 05:53:18.508469','95e8f119-dc7d-4515-893d-2e74c9203558','شادي حنين جرجس بخيت 2300036',3,'',7,2),(125,'2023-08-03 05:59:15.735589','e9f074f3-94b1-449e-abcc-75847d26ad60','شادي حنين جرجس بخيت 2300037',3,'',7,2),(126,'2023-08-03 06:01:11.760650','d39ae40e-3f2a-422c-848c-ce8833624403','شادي حنين جرجس بخيت 2300038',3,'',7,2),(127,'2023-08-03 06:01:38.437421','9702751f-7e86-4383-abf7-951096d84d49','شادي حنين جرجس بخيت 2300040',3,'',7,2),(128,'2023-08-03 06:03:09.143060','4f9d1439-2b2b-481d-ab57-9299fec8e444','شادي حنين جرجس بخيت 2300041',3,'',7,2),(129,'2023-08-03 06:04:07.847358','0970185e-fe94-4a9b-a84c-892e7c176a79','شادي حنين جرجس بخيت 2300042',3,'',7,2),(130,'2023-08-03 06:04:59.792356','bf1440af-e1af-432b-945b-6fa526cec126','',3,'',8,2),(131,'2023-08-03 06:04:59.796329','bedac24f-db7a-4d69-95bd-1b7e0674c45f','',3,'',8,2),(132,'2023-08-03 06:04:59.797328','ad4212d1-5b3e-4460-bba6-9cd2cbe653c4','',3,'',8,2),(133,'2023-08-03 06:04:59.799335','91ace698-d897-4b7d-9758-b65fdfc36e64','',3,'',8,2),(134,'2023-08-03 06:04:59.800327','79f84655-d1d8-490a-bf35-d19b5a2670c4','',3,'',8,2),(135,'2023-08-03 06:04:59.801327','453cb5f1-b2a5-4757-abc9-8a54132f1317','',3,'',8,2),(136,'2023-08-03 06:08:29.989246','eea74f63-cbf1-4bb8-9940-5ed883b882e1','شادي حنين جرجس بخيت 2300043',3,'',7,2),(137,'2023-08-03 06:09:12.660897','c46b556a-a18a-484a-ab2a-e07a08b171a5','',3,'',8,2),(138,'2023-08-03 06:09:12.663906','5435cfe3-f72f-4088-aaa1-3751fd32c807','',3,'',8,2),(139,'2023-08-03 06:09:22.357753','e9228885-597d-4afe-ae19-7018b5a2b913','شادي حنين جرجس بخيت 2300044',3,'',7,2),(140,'2023-08-03 06:11:31.971758','cecfb58a-4703-4a50-915c-31a08e7ab9c0','شادي حنين جرجس بخيت 2300045',3,'',7,2),(141,'2023-08-03 06:12:29.826045','7b7a6050-82c8-4cea-8378-6a2e69ba773a','',3,'',8,2),(142,'2023-08-03 06:12:36.329345','0c6cc897-5191-43f0-b3db-37a5e98567a5','شادي حنين جرجس بخيت 2300047',3,'',7,2),(143,'2023-08-03 06:13:51.229622','ae9d1153-68ee-49fd-a6b4-9ab41f599d4f','شادي حنين جرجس بخيت 2300048',3,'',7,2),(144,'2023-08-03 06:14:29.410358','7d301db0-c4bf-4245-be85-b991097087e3','شادي حنين جرجس بخيت 2300049',3,'',7,2),(145,'2023-08-03 11:53:27.313721','04909c46-fb3b-42bd-ad90-602c5be332a0','شادي حنين جرجس بخيت 2300050',3,'',7,2),(146,'2023-08-03 11:55:46.093138','e4f2e03b-ad08-46a3-ad7e-e09f83b46932','مبنا: لوتس, شارع: جميلة ابو حريد, الطابق: 7',3,'',8,2),(147,'2023-08-03 11:57:18.424116','adbea4e7-14ad-4943-a79f-bf9e197ce9d9','مبنا: لوتس, شارع: جميلة ابو حريد, الطابق: 7',3,'',8,2),(148,'2023-08-03 12:12:26.428896','2200db73-3d80-4719-9793-6c91be61ffb2','2023 شادي حنين جرجس بخيت دفع 20 جنيهات',3,'',12,2),(154,'2023-08-03 12:13:43.337468','f78ec86a-f8c5-4cd5-994d-e716b9b9fd92','شادي حنين جرجس بخيت',3,'',7,2),(155,'2023-08-03 12:14:32.960882','30','2300030',3,'',4,2),(156,'2023-08-03 12:14:32.963885','31','2300031',3,'',4,2),(157,'2023-08-03 12:14:32.965846','39','2300039',3,'',4,2),(158,'2023-08-03 12:14:32.966847','46','2300046',3,'',4,2),(159,'2023-08-03 12:14:32.967847','51','2300051',3,'',4,2),(160,'2023-08-03 12:15:16.985067','30','2300030',3,'',4,2),(161,'2023-08-03 12:15:21.223794','31','2300031',3,'',4,2),(162,'2023-08-03 12:15:24.929029','39','2300039',3,'',4,2),(163,'2023-08-03 12:15:29.171488','46','2300046',3,'',4,2),(166,'2023-08-03 12:17:38.268073','b749bf16-d8b3-4463-98b9-17bd23e8a4a8','شادي حنين جرجس بخيت 2300051',3,'',7,2),(167,'2023-08-03 12:19:03.941084','6580fba5-aedd-43a2-9602-64491a3655a4','شادي حنين جرجس بخيت 2300052',3,'',7,2),(168,'2023-08-03 12:19:18.852369','15','delete',3,'',4,2),(169,'2023-08-03 12:20:50.255376','f1fd1c48-8bbc-4976-a03b-89663055ea0f','2023 None دفع 20 جنيهات',3,'',12,2),(170,'2023-08-03 12:20:50.258391','b7bfc550-2d6f-48c0-a905-7aead3cf7dd0','2023 None دفع 20 جنيهات',3,'',12,2),(171,'2023-08-03 12:24:39.762378','ee37d082-5a61-4b26-9050-5259294b7189','2023 شادي حنين جرجس بخيت 2300053 دفع 20 جنيهات',3,'',12,2),(172,'2023-08-03 12:24:47.490756','c77da837-3261-49db-abff-1673b5b91308','شادي حنين جرجس بخيت 2300053',3,'',7,2),(173,'2023-08-03 12:26:25.751597','893e9b99-397b-417e-8ef5-a1c221101b77','شادي حنين جرجس بخيت 2300054',3,'',7,2),(174,'2023-08-03 12:26:31.716890','51e4ae19-e273-4b2f-a1c9-b5cefdb42787','2023 None دفع 20 جنيهات',3,'',12,2),(175,'2023-08-03 12:33:20.711482','6b9ea7a9-11b5-41ed-98db-75a916c3937f','2023 شادي حنين جرجس بخيت 2300055 دفع 21 جنيهات',3,'',12,2),(176,'2023-08-03 12:33:33.435264','5f0e4ed3-013e-4fe0-a48b-34d16323e6d4','شادي حنين جرجس بخيت 2300055',3,'',7,2),(177,'2023-08-03 12:55:05.458037','cd36bc1c-3bfc-4940-867a-76979ef75408','شادي حنين جرجس بخيت 2300056',3,'',7,2),(178,'2023-08-03 12:55:10.745422','b19f1f31-32b1-4220-98d7-0c10d5cbd507','2023 None دفع 22 جنيهات',3,'',12,2),(179,'2023-08-03 12:57:14.362248','2b6dc740-5236-4978-8a3c-f497c939669c','2023 شادي حنين جرجس بخيت 2300057 دفع 23 جنيهات',3,'',12,2),(180,'2023-08-03 12:57:19.979875','4eddc229-8e8f-42df-9862-46aa471fb613','شادي حنين جرجس بخيت 2300057',3,'',7,2),(181,'2023-08-03 12:58:25.080868','b67e0e9a-8955-463e-b301-1a70e0d64be2','شادي حنين جرجس بخيت 2300058',3,'',7,2),(182,'2023-08-03 12:58:47.025985','03ee5863-e375-46e0-a2c2-25748cb2ced6','شادي حنين جرجس بخيت 2300059',3,'',7,2),(183,'2023-08-03 12:59:47.433620','36e0b945-13ce-4a83-877e-d3b160567bae','شادي حنين عبيد بخيت 2300060',3,'',7,2),(184,'2023-08-03 12:59:54.058143','f1bcfc29-a274-455e-abe5-a5cbbebfaba0','2023 None دفع 24 جنيهات',3,'',12,2),(185,'2023-08-03 12:59:54.060118','bb954410-f854-470b-bce4-5149b7733069','2023 None دفع 24 جنيهات',3,'',12,2),(186,'2023-08-03 12:59:54.061667','674dea99-8027-45cd-a11c-b5d303fc78eb','2023 None دفع 20 جنيهات',3,'',12,2),(187,'2023-08-03 13:01:50.248096','29472398-9732-48f6-bf4f-9c6560c27b8c','2023 شادي حنين جرجس بخيت 2300061 دفع 20 جنيهات',3,'',12,2),(188,'2023-08-03 13:01:55.959159','c54cfa1e-53e9-43c8-9d24-8f2403cb5ecf','شادي حنين جرجس بخيت 2300061',3,'',7,2),(189,'2023-08-03 13:03:16.556675','3a2a8fd0-dcb3-49be-8a68-eb808728a57f','شادي حنين جرجس بخيت 2300062',3,'',7,2),(190,'2023-08-03 13:03:24.334796','787101ff-6294-4ab2-9877-a43b29768b0a','2023 None دفع 10 جنيهات',3,'',12,2),(191,'2023-08-03 13:06:33.729838','aa5b75e9-c17a-480a-9e2e-fbcfaf215e76','2023 شادي حنين جرجس بخيت 2300063 دفع 20 جنيهات',3,'',12,2),(192,'2023-08-03 13:06:42.247328','35a1d96b-881c-4af2-bd1d-d493a639014e','شادي حنين جرجس بخيت 2300063',3,'',7,2),(193,'2023-08-03 13:08:11.719760','189d2f1b-171b-4b17-b233-bc77f8dc39bb','شادي حنين جرجس بخيت 2300064',3,'',7,2),(194,'2023-08-03 13:08:17.552710','7917402f-5e7d-4313-88a7-bb72ae68babf','2023 None دفع 20 جنيهات',3,'',12,2),(195,'2023-08-03 13:14:22.078862','03767479-d7c5-4e81-ad78-9600508391d5','2023 شادي حنين جرجس بخيت 2300065 دفع 20 جنيهات',3,'',12,2),(196,'2023-08-03 13:14:27.215465','16eb8d96-5ad7-4d48-a946-f397abeb6c91','شادي حنين جرجس بخيت 2300065',3,'',7,2),(197,'2023-08-03 13:15:51.328778','7343acbc-a1ad-4e28-84d1-de47e4fd429f','شادي حنين جرجس بخيت 2300066',3,'',7,2),(198,'2023-08-03 13:15:56.881774','4bc2fcac-79bb-4e64-b65b-34a1bfc5d0a7','2023 None دفع 20 جنيهات',3,'',12,2),(199,'2023-08-03 13:18:13.317727','5ceea6eb-0803-44fb-b064-1d2c43bf8d10','2023 شادي حنين جرجس بخيت 2300067 دفع 10 جنيهات',3,'',12,2),(200,'2023-08-03 13:18:20.271004','cca4c463-ca85-48d1-a1ad-cd2505f80088','شادي حنين جرجس بخيت 2300067',3,'',7,2),(201,'2023-08-03 16:17:54.007260','e363de5f-0c56-481d-8cab-e6afbf27ff0c','شادي حنين جرجس بخيت 2300068',2,'[{\"changed\": {\"fields\": [\"School level\"]}}]',7,1),(202,'2023-08-03 16:36:52.722673','5ca02f8e-d3fe-4b3b-97aa-312a0456ab3f','مبنا: لوتس, شارع: جميلة ابو حريد, الطابق: 7',1,'[{\"added\": {}}]',8,1),(203,'2023-08-03 16:37:34.187506','e363de5f-0c56-481d-8cab-e6afbf27ff0c','شادي حنين جرجس بخيت 2300068',2,'[{\"changed\": {\"fields\": [\"Address\"]}}]',7,1),(204,'2023-08-03 16:44:59.657722','e363de5f-0c56-481d-8cab-e6afbf27ff0c','شادي حنين جرجس بخيت 2300068',2,'[{\"changed\": {\"fields\": [\"Deaconess\"]}}]',7,1),(205,'2023-08-03 16:45:50.295532','e363de5f-0c56-481d-8cab-e6afbf27ff0c','شادي حنين جرجس بخيت 2300068',2,'[{\"changed\": {\"fields\": [\"Confession father\"]}}]',7,1),(206,'2023-08-03 16:47:14.220455','e363de5f-0c56-481d-8cab-e6afbf27ff0c','شادي حنين جرجس بخيت 2300068',2,'[{\"changed\": {\"fields\": [\"Talmza level\"]}}]',7,1),(207,'2023-08-03 18:00:45.479474','e363de5f-0c56-481d-8cab-e6afbf27ff0c','شادي حنين جرجس بخيت 2300068',2,'[{\"changed\": {\"fields\": [\"Phone number\", \"Father phone number\", \"Mother phone number\", \"Mobile follow up on WhatsApp\"]}}]',7,1),(208,'2023-08-03 18:01:20.577201','5ca02f8e-d3fe-4b3b-97aa-312a0456ab3f','مبنا: لوتس, شارع: جميلة ابو حريد, متفرع من: يقوت الحموي, الطابق: 7',2,'[{\"changed\": {\"fields\": [\"Branches from\"]}}]',8,1),(209,'2023-08-03 18:01:43.854571','5ca02f8e-d3fe-4b3b-97aa-312a0456ab3f','مبنا: لوتس, شارع: جميلة ابو حريد, متفرع من: يقوت الحموي, الطابق: 7, رقم الشقة: 704, الحي: السيوف, تفاصيل إضافية: بجوار ماركت مصباح',2,'[{\"changed\": {\"fields\": [\"Apartment number\", \"District\", \"Additional details\"]}}]',8,1),(210,'2023-08-03 18:02:06.778431','e363de5f-0c56-481d-8cab-e6afbf27ff0c','شادي حنين جرجس بخيت 2300068',2,'[{\"changed\": {\"fields\": [\"Profile image\"]}}]',7,1),(211,'2023-08-03 18:02:20.609467','e363de5f-0c56-481d-8cab-e6afbf27ff0c','شادي حنين جرجس بخيت 2300068',2,'[{\"changed\": {\"fields\": [\"Gender\"]}}]',7,1),(212,'2023-08-03 18:47:50.880821','e363de5f-0c56-481d-8cab-e6afbf27ff0c','شادي حنين جرجس بخيت 2300068',2,'[{\"changed\": {\"fields\": [\"Current talmza level year\", \"Current school level year\"]}}]',7,1),(213,'2023-08-03 18:49:16.095304','e363de5f-0c56-481d-8cab-e6afbf27ff0c','شادي حنين جرجس بخيت 2300068',2,'[{\"changed\": {\"fields\": [\"Current school level year\"]}}]',7,1),(214,'2023-08-03 19:00:48.735324','4b1508b0-c4f1-4fed-9f7c-3d8b9665906f','2023 شادي حنين جرجس بخيت 2300068 دفع 23 جنيهات',2,'[{\"changed\": {\"fields\": [\"Amount of money payed\"]}}]',12,1),(218,'2023-08-04 04:27:51.218995','8cf13337-86e5-4465-9771-986cf1f0f417','مريا نادي كمال سيدهم',3,'',7,1),(219,'2023-08-04 04:40:33.913376','e363de5f-0c56-481d-8cab-e6afbf27ff0c','شادي جرجس جرجس بخيت 2300068',3,'',7,1),(220,'2023-08-04 04:40:38.662825','e4e9e37e-6791-43ca-b70d-cec54f741024','يحيا نادي كمال سيدهم 2300070',3,'',7,1),(221,'2023-08-04 04:40:49.270464','67d51a6f-b14e-4f08-b8a1-b0a6e233088c','مريا نادي كمال سيدهم 2300069',3,'',7,1),(222,'2023-08-04 04:41:11.231159','a9ae08e4-16a0-4237-af3b-c872f789ee79','ريتا جمال ملاك شرباتX 2300013',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',7,1),(223,'2023-08-05 08:55:14.619287','009a3ab0-6225-4a8a-b1b3-c78ef44b59ea','',1,'[{\"added\": {}}]',8,2),(224,'2023-08-05 08:57:12.640782','02c21865-fca2-4ab5-b360-10af0f546e59','كمال نادي كمال سيدهم 19102929',2,'[{\"changed\": {\"fields\": [\"Birthdate\", \"Talmza level\", \"School level\", \"Address\", \"Gender\", \"Deaconess\"]}}]',7,2),(225,'2023-08-05 17:09:49.772815','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',1,'[{\"added\": {}}]',13,2),(226,'2023-08-05 17:10:57.338531','ffae898d-feed-4f55-a668-2d601e666f66','مريم سامى صادق مسعد 2300071',3,'',7,2),(227,'2023-08-05 17:10:57.369529','cbc39be9-18d8-4e5b-9daf-cbd70950022b','ghk kamal sedhom abdelshahed 2300076',3,'',7,2),(228,'2023-08-05 17:10:57.372532','bbf8e49a-eff3-4a5b-a421-6fac13c1bf09','pp kamal sedhom abdelshahed 2300077',3,'',7,2),(229,'2023-08-05 17:10:57.376531','b48dcf46-6c5e-4d74-b3eb-3cce2477ac21','fataa7 kamal sedhom abdelshahed 2300073',3,'',7,2),(230,'2023-08-05 17:10:57.379532','9a5b4b4f-9120-4e5b-81da-fc57a2dbaa73',';;; kamal sedhom abdelshahed 2300074',3,'',7,2),(231,'2023-08-05 17:10:57.382533','3f2bdf83-8d1f-4d33-89a1-5fef9b431b07','dsa kamal sedhom abdelshahed 2300075',3,'',7,2),(232,'2023-08-05 17:10:57.386530','1353ef37-5794-42b0-be47-bf1c60e744c1','oo kamal sedhom abdelshahed 2300072',3,'',7,2),(233,'2023-08-05 17:14:21.255423','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',13,2),(234,'2023-08-05 17:19:56.792415','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',1,'[{\"added\": {}}]',13,2),(235,'2023-08-06 07:16:51.728932','d2be3f99-4708-4d55-bee7-49c24094c125','تمهيدي',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',10,2),(236,'2023-08-06 07:16:55.021892','d2be3f99-4708-4d55-bee7-49c24094c125','تمهيدي',2,'[]',10,2),(237,'2023-08-06 07:17:07.424347','74f581f3-cca0-4506-beb3-95a8c938203a','الأول',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',10,2),(238,'2023-08-06 07:17:14.960032','74f581f3-cca0-4506-beb3-95a8c938203a','الأول',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',10,2),(239,'2023-08-06 07:17:30.718320','6b3aa176-2544-403e-8c05-a51fd36a4351','الثاني',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',10,2),(240,'2023-08-06 07:17:42.851491','ba6c0d1e-e63d-4d27-a689-c55e65611bd6','الثالث',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',10,2),(241,'2023-08-06 07:17:48.534700','362754ed-35c2-41e8-8cfc-adc7b1178191','الرابع',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',10,2),(242,'2023-08-06 07:18:01.282175','d0b12a75-71bc-40e4-94ed-9745a604bef3','حضانة',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',9,2),(243,'2023-08-06 07:18:09.030260','af153d90-953b-48e6-b8d8-ffa6e2a32320','الابتدائي',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',9,2),(244,'2023-08-06 07:18:22.595482','750700e2-0aa9-462f-83a8-de322f87cc7e','الإعدادي',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',9,2),(245,'2023-08-06 07:18:28.064590','c8fa8e83-73f0-45e5-a820-5e2c7d919239','ثانوي',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',9,2),(246,'2023-08-06 07:18:36.166825','0b23ec22-3483-4227-884e-177432bc0b1f','جامعة',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',9,2),(247,'2023-08-06 07:18:43.124981','07889dac-ae48-48b8-8d2b-683ee35d8ab2','خريج',2,'[{\"changed\": {\"fields\": [\"Previous level\"]}}]',9,2),(248,'2023-08-06 07:20:42.025254','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[{\"changed\": {\"fields\": [\"Previous Tag\"]}}]',13,2),(249,'2023-08-06 07:20:46.842058','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',2,'[{\"changed\": {\"fields\": [\"Next Tag\"]}}]',13,2),(250,'2023-08-06 08:14:55.449672','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[{\"changed\": {\"fields\": [\"Child\"]}}]',13,2),(251,'2023-08-06 08:14:59.388969','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',2,'[{\"changed\": {\"fields\": [\"Parent\"]}}]',13,2),(252,'2023-08-06 08:38:33.509075','b4103c25-e176-4f42-99e0-9110aa409a75','new tag 3',3,'',13,2),(253,'2023-08-06 08:38:36.457193','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[{\"changed\": {\"fields\": [\"Is top\"]}}]',13,2),(254,'2023-08-06 08:39:23.314622','6984a8f5-6095-4055-b615-fd4c7e40f5c6','new tag 2',2,'[{\"changed\": {\"fields\": [\"Is buttom\"]}}]',13,2),(255,'2023-08-06 08:39:28.509397','6984a8f5-6095-4055-b615-fd4c7e40f5c6','new tag 2',2,'[]',13,2),(256,'2023-08-06 11:54:26.684125','9e7d0b56-2998-49b1-8a12-92397ea1ca27','new tag 3',3,'',13,2),(257,'2023-08-06 11:55:13.831597','7243233a-f5c1-4147-9c63-873823d57cdd','new tag 3',3,'',13,2),(258,'2023-08-06 12:01:56.678747','5591e424-aed6-4474-ae4b-ecf09e07361f','new tag 3',3,'',13,2),(259,'2023-08-06 12:03:10.407011','964aa0e7-2967-4971-95ea-ccaf6108f127','new tag 3',3,'',13,2),(260,'2023-08-06 12:03:14.023508','6984a8f5-6095-4055-b615-fd4c7e40f5c6','new tag 2',3,'',13,2),(261,'2023-08-06 12:03:19.016293','15a702f2-7fa2-4455-8ed7-26c57016217c','new tag',3,'',13,2),(262,'2023-08-06 12:03:23.417715','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[{\"changed\": {\"fields\": [\"Child\", \"Is top\"]}}]',13,2),(263,'2023-08-06 12:03:28.472403','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',2,'[{\"changed\": {\"fields\": [\"Parent\", \"Is buttom\"]}}]',13,2),(264,'2023-08-06 12:03:31.448435','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[]',13,2),(265,'2023-08-06 12:07:35.424314','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عمادX 2300008',2,'[]',7,2),(266,'2023-08-06 12:07:40.620279','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عمادX 2300008',2,'[{\"changed\": {\"fields\": [\"User permission tags\"]}}]',7,2),(267,'2023-08-06 12:08:03.054673','c2973b75-0642-46c3-8a4e-6eac95f4b4cc','بيتر نادي كمال سيدهم peter',2,'[{\"changed\": {\"fields\": [\"Birthdate\", \"Talmza level\", \"School level\", \"Gender\", \"Deaconess\", \"User permission tags\"]}}]',7,2),(268,'2023-08-06 12:08:08.298615','b27d3b20-9f9c-4b81-bc38-de70d4996bbb','جورج سدقي متحت عبدالغفورX 2300009',2,'[{\"changed\": {\"fields\": [\"User permission tags\"]}}]',7,2),(269,'2023-08-06 12:08:11.967555','a9ae08e4-16a0-4237-af3b-c872f789ee79','ريتا جمال ملاك شرباتX 2300013',2,'[{\"changed\": {\"fields\": [\"User permission tags\"]}}]',7,2),(270,'2023-08-06 12:08:15.532467','30438371-1291-4ebd-9a94-23b19ae7b180','مينا عماد بيشوي فتحيX 2300012',2,'[{\"changed\": {\"fields\": [\"User permission tags\"]}}]',7,2),(271,'2023-08-06 12:08:19.620976','02c21865-fca2-4ab5-b360-10af0f546e59','كمال نادي كمال سيدهم 19102929',2,'[{\"changed\": {\"fields\": [\"User permission tags\"]}}]',7,2),(272,'2023-08-06 12:29:00.558276','78','2300078',1,'[{\"added\": {}}]',4,2),(273,'2023-08-06 12:29:04.422332','78','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(274,'2023-08-06 12:29:41.580265','543db37d-de66-4b9e-a4c1-ba14f93f8024','',1,'[{\"added\": {}}]',8,2),(275,'2023-08-06 12:31:19.775248','d8631d2d-58c9-4bfb-b73d-e380fbac28f2','رdasddsafsdfasdfasdf test',1,'[{\"added\": {}}]',7,2),(276,'2023-08-06 12:31:50.331750','d8631d2d-58c9-4bfb-b73d-e380fbac28f2','رdasddsafsdfasdfasdf test',3,'',7,2),(277,'2023-08-06 12:32:09.504593','79','2300079',1,'[{\"added\": {}}]',4,2),(278,'2023-08-06 12:32:13.399755','79','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(279,'2023-08-06 12:32:28.700836','a2a86efa-f90a-45bf-bcea-09ba51c6555e','fast test',1,'[{\"added\": {}}]',7,2),(280,'2023-08-06 12:34:54.424525','a2a86efa-f90a-45bf-bcea-09ba51c6555e','fast test',3,'',7,2),(281,'2023-08-06 12:35:07.735194','80','2300080',1,'[{\"added\": {}}]',4,2),(282,'2023-08-06 12:35:37.225827','80','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(283,'2023-08-06 12:35:57.909730','645adca6-df9d-4c21-8772-17d43068082c','',1,'[{\"added\": {}}]',8,2),(284,'2023-08-06 12:36:02.939055','7ce36de4-1599-414a-8d9c-950c04bd9f1a','asdasd test',1,'[{\"added\": {}}]',7,2),(285,'2023-08-06 12:36:52.912764','7ce36de4-1599-414a-8d9c-950c04bd9f1a','asdasd test',3,'',7,2),(286,'2023-08-06 12:37:03.002942','81','2300081',1,'[{\"added\": {}}]',4,2),(287,'2023-08-06 12:37:08.597418','81','tesrtt',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(288,'2023-08-06 12:37:21.749593','7c79a2a2-13e1-497d-a1ac-888a1efbeaa3','',1,'[{\"added\": {}}]',8,2),(289,'2023-08-06 12:37:26.519911','9aaab648-f2f7-4f9d-8626-5814acba63ad','koko tesrtt',1,'[{\"added\": {}}]',7,2),(290,'2023-08-06 12:38:28.983667','9aaab648-f2f7-4f9d-8626-5814acba63ad','koko tesrtt',3,'',7,2),(291,'2023-08-06 12:38:37.409086','82','2300082',1,'[{\"added\": {}}]',4,2),(292,'2023-08-06 12:38:57.753651','83','2300083',1,'[{\"added\": {}}]',4,2),(293,'2023-08-06 12:39:01.407066','83','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(294,'2023-08-06 12:39:22.848570','9d69b280-f354-4c9a-a6a9-141b3628744c','',1,'[{\"added\": {}}]',8,2),(295,'2023-08-06 12:39:30.135520','497bdc5e-a2e9-4740-9e59-fc10d9937dd7','test test',1,'[{\"added\": {}}]',7,2),(296,'2023-08-06 12:41:11.425575','497bdc5e-a2e9-4740-9e59-fc10d9937dd7','test test',3,'',7,2),(297,'2023-08-06 12:41:26.012113','82','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(298,'2023-08-06 12:41:41.699036','02fe4570-fd59-4cc5-90b3-e0ee1577d5f4','',1,'[{\"added\": {}}]',8,2),(299,'2023-08-06 12:42:51.482333','07a32efd-2852-47ac-bb34-f23ecff20c1e','شادي test',1,'[{\"added\": {}}]',7,2),(300,'2023-08-06 12:43:08.193214','07a32efd-2852-47ac-bb34-f23ecff20c1e','شادي test',3,'',7,2),(301,'2023-08-06 12:43:58.634499','84','2300084',1,'[{\"added\": {}}]',4,2),(302,'2023-08-06 12:44:02.176866','84','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(303,'2023-08-06 12:44:20.177618','79596409-cb2f-4831-91c9-981bc82bf8c4','',1,'[{\"added\": {}}]',8,2),(304,'2023-08-06 12:44:23.708611','863f34d8-eaf7-4d6c-a4cd-db6d80192c96','das test',1,'[{\"added\": {}}]',7,2),(305,'2023-08-06 12:48:06.067001','863f34d8-eaf7-4d6c-a4cd-db6d80192c96','das test',3,'',7,2),(306,'2023-08-06 12:48:20.794923','85','2300085',1,'[{\"added\": {}}]',4,2),(307,'2023-08-06 12:48:24.565088','85','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(308,'2023-08-06 12:48:38.065105','7fe57c86-44b5-4595-bcae-003e87418999','',1,'[{\"added\": {}}]',8,2),(309,'2023-08-06 12:48:41.557554','e29358cc-e31b-4789-bc5e-dcd7e318f570','tes test',1,'[{\"added\": {}}]',7,2),(310,'2023-08-06 12:49:09.657934','e29358cc-e31b-4789-bc5e-dcd7e318f570','tes test',3,'',7,2),(311,'2023-08-06 12:49:17.346405','86','2300086',1,'[{\"added\": {}}]',4,2),(312,'2023-08-06 12:49:21.109542','86','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(313,'2023-08-06 12:49:35.467819','14b820c2-84fc-4454-acf8-133a642aa031','',1,'[{\"added\": {}}]',8,2),(314,'2023-08-06 12:50:02.230469','5888e40d-db8f-40ee-9398-7399f4f352ec','',1,'[{\"added\": {}}]',8,2),(315,'2023-08-06 12:53:12.894897','06aa97c5-dacc-4d26-8347-b9299bf9b613','sads test',1,'[{\"added\": {}}]',7,2),(316,'2023-08-06 13:14:55.063685','06aa97c5-dacc-4d26-8347-b9299bf9b613','sads test',3,'',7,2),(317,'2023-08-06 13:15:08.608249','87','2300087',1,'[{\"added\": {}}]',4,2),(318,'2023-08-06 13:15:13.490296','87','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(319,'2023-08-06 13:15:27.494578','053fe957-1c4e-4843-b14c-eec7f5ed8abf','',1,'[{\"added\": {}}]',8,2),(320,'2023-08-06 13:15:48.830828','9e57fd4f-d75f-480d-8b27-bebe083bc2d6','شادي test',1,'[{\"added\": {}}]',7,2),(321,'2023-08-06 13:20:47.856616','9e57fd4f-d75f-480d-8b27-bebe083bc2d6','شادي test',2,'[]',7,2),(322,'2023-08-06 13:25:31.152633','9e57fd4f-d75f-480d-8b27-bebe083bc2d6','شادي test',3,'',7,2),(323,'2023-08-06 13:25:50.068900','88','2300088',1,'[{\"added\": {}}]',4,2),(324,'2023-08-06 13:25:54.796464','88','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(325,'2023-08-06 13:26:11.877634','e1842579-8696-43c1-91fe-20565c88eb5b','',1,'[{\"added\": {}}]',8,2),(326,'2023-08-06 13:26:26.533793','c93c452e-7d0c-4bbe-8f7e-8b6835eac3be','شادي test',1,'[{\"added\": {}}]',7,2),(327,'2023-08-06 13:28:59.046005','c93c452e-7d0c-4bbe-8f7e-8b6835eac3be','شادي test',3,'',7,2),(328,'2023-08-06 13:29:13.346551','89','2300089',1,'[{\"added\": {}}]',4,2),(329,'2023-08-06 13:29:17.467912','89','fd',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(330,'2023-08-06 13:29:31.180507','35849951-e77d-4703-9245-d470f51f4abf','',1,'[{\"added\": {}}]',8,2),(331,'2023-08-06 13:29:36.231960','08affc4a-40c4-4d6c-9db2-29b6ba7504f1','شادي fd',1,'[{\"added\": {}}]',7,2),(332,'2023-08-06 13:34:30.846981','08affc4a-40c4-4d6c-9db2-29b6ba7504f1','شادي fd',3,'',7,2),(333,'2023-08-06 13:34:41.066738','90','2300090',1,'[{\"added\": {}}]',4,2),(334,'2023-08-06 13:34:46.760357','90','asf',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(335,'2023-08-06 13:35:07.854101','397a21b4-83b8-4b00-8626-4e9fb2c58246','',1,'[{\"added\": {}}]',8,2),(336,'2023-08-06 13:35:12.855133','0ce7494d-57d2-4c1a-a6cc-44db17ac9927','sad asf',1,'[{\"added\": {}}]',7,2),(337,'2023-08-06 13:36:03.142295','0ce7494d-57d2-4c1a-a6cc-44db17ac9927','sad asf',3,'',7,2),(338,'2023-08-06 13:36:12.290933','91','2300091',1,'[{\"added\": {}}]',4,2),(339,'2023-08-06 13:36:12.354934','92','2300092',1,'[{\"added\": {}}]',4,2),(340,'2023-08-06 13:36:26.332497','650ebcef-fef1-42b2-84c7-67c46fb8e408','',1,'[{\"added\": {}}]',8,2),(341,'2023-08-06 13:37:19.571058','b066d705-2759-4084-9c2c-1d058723d1b0','شادي 2300092',1,'[{\"added\": {}}]',7,2),(342,'2023-08-06 13:41:00.847677','b066d705-2759-4084-9c2c-1d058723d1b0','شادي 2300092',3,'',7,2),(343,'2023-08-06 13:41:20.788567','93','2300093',1,'[{\"added\": {}}]',4,2),(344,'2023-08-06 13:41:24.946121','93','asdas',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(345,'2023-08-06 13:41:40.347420','265d6ac0-2391-4906-b18d-9886ef746963','',1,'[{\"added\": {}}]',8,2),(346,'2023-08-06 13:41:44.503392','be95fc11-2745-4ff4-aab7-f2743b26a597','شادي asdas',1,'[{\"added\": {}}]',7,2),(347,'2023-08-06 13:44:26.838891','be95fc11-2745-4ff4-aab7-f2743b26a597','شادي asdas',3,'',7,2),(348,'2023-08-06 13:44:38.640328','94','2300094',1,'[{\"added\": {}}]',4,2),(349,'2023-08-06 13:44:41.936151','94','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(350,'2023-08-06 13:44:57.361357','47177871-389c-4698-b106-b5c39b8ef32b','',1,'[{\"added\": {}}]',8,2),(351,'2023-08-06 13:45:00.193405','9b29ca91-1ef1-4526-b725-ab8bfd325da3','شادي test',1,'[{\"added\": {}}]',7,2),(352,'2023-08-06 13:47:08.943977','9b29ca91-1ef1-4526-b725-ab8bfd325da3','شادي test',3,'',7,2),(353,'2023-08-06 13:47:18.300702','95','2300095',1,'[{\"added\": {}}]',4,2),(354,'2023-08-06 13:47:22.264661','95','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(355,'2023-08-06 13:47:35.853754','744ff960-e413-4254-9689-62db1ee80c79','',1,'[{\"added\": {}}]',8,2),(356,'2023-08-06 13:48:10.119880','4f77969b-a5de-4a2f-ae49-4db898af738a','شادي test',1,'[{\"added\": {}}]',7,2),(357,'2023-08-06 13:51:56.012582','4f77969b-a5de-4a2f-ae49-4db898af738a','شادي test',3,'',7,2),(358,'2023-08-06 13:52:05.424423','96','2300096',1,'[{\"added\": {}}]',4,2),(359,'2023-08-06 13:52:08.971806','96','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(360,'2023-08-06 13:52:20.500008','1a4e2d3a-3836-4777-9fea-7912a4d2c5fe','',1,'[{\"added\": {}}]',8,2),(361,'2023-08-06 14:02:14.123128','21dd9861-1051-45c7-abb6-070120bcbf55','شادي test',1,'[{\"added\": {}}]',7,2),(362,'2023-08-06 14:09:23.361203','1','Temp object (1)',1,'[{\"added\": {}}]',14,2),(363,'2023-08-06 14:11:07.833442','21dd9861-1051-45c7-abb6-070120bcbf55','شادي test',3,'',7,2),(364,'2023-08-06 14:11:15.981350','97','2300097',1,'[{\"added\": {}}]',4,2),(365,'2023-08-06 14:11:20.950736','97','test',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,2),(366,'2023-08-06 14:12:02.860389','1ec7a7ff-ddce-4447-ad29-a10834d635ac','',1,'[{\"added\": {}}]',8,2),(367,'2023-08-06 14:12:07.741459','c225b2d2-57c4-4aee-a9f7-65a95c49d80e','شادي test',1,'[{\"added\": {}}]',7,2),(368,'2023-08-06 14:17:34.343123','c225b2d2-57c4-4aee-a9f7-65a95c49d80e','شادي test',3,'',7,2),(369,'2023-08-06 14:19:50.033299','2d6b1c24-e9fd-456f-befc-a8da4e4b821d','شادي حنين جرجس بخيت 2300098',3,'',7,2),(370,'2023-08-06 14:20:51.527380','883f5da5-1f5e-44dc-846a-abf1cb9b4883','شادي جرجس جرجس بخيت 2300099',3,'',7,2),(371,'2023-08-06 14:22:28.704477','c0d060e4-eac4-4712-93dc-6091bba6eb73','شادي جرجس جرجس بخيت 2300100',3,'',7,2),(372,'2023-08-06 14:22:55.480969','806fe50a-57cf-4866-9bfb-be7dfb767100','شادي جرجس جرجس بخيت 2300101',3,'',7,2),(373,'2023-08-06 14:24:12.978908','11f19381-4a88-4a79-9730-8c584f34dc64','شادي حنين جرجس سيدهم 2300102',3,'',7,2),(374,'2023-08-06 14:27:38.189732','60194232-73ef-4f23-bc23-796a9f8b31b1','شادي جرجس جرجس بخيت 2300103',3,'',7,2),(375,'2023-08-06 18:01:09.446137','e997367a-c32a-41a8-afe8-13e70da4e72d','tag 1',1,'[{\"added\": {}}]',13,2),(376,'2023-08-06 18:01:18.797403','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[{\"changed\": {\"fields\": [\"Child\"]}}]',13,2),(377,'2023-08-06 18:01:22.246130','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',2,'[{\"changed\": {\"fields\": [\"Parent\"]}}]',13,2),(378,'2023-08-06 18:01:40.288203','e997367a-c32a-41a8-afe8-13e70da4e72d','tag 1',2,'[{\"changed\": {\"fields\": [\"Parent\"]}}]',13,2),(379,'2023-08-06 18:01:51.507104','ea057173-1291-411c-8225-0d973454245f','tag 2',1,'[{\"added\": {}}]',13,2),(380,'2023-08-06 18:01:58.770487','c965449d-97e5-480b-95b6-80ba3cd02781','tag 3',1,'[{\"added\": {}}]',13,2),(381,'2023-08-06 18:02:13.983587','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[{\"changed\": {\"fields\": [\"Child\"]}}]',13,2),(382,'2023-08-06 18:02:31.165622','e997367a-c32a-41a8-afe8-13e70da4e72d','tag 1',2,'[{\"changed\": {\"fields\": [\"Child\"]}}]',13,2),(383,'2023-08-06 18:02:42.738920','ea057173-1291-411c-8225-0d973454245f','tag 2',2,'[{\"changed\": {\"fields\": [\"Child\"]}}]',13,2),(384,'2023-08-06 18:02:56.087386','ea057173-1291-411c-8225-0d973454245f','tag 2',2,'[]',13,2),(385,'2023-08-06 18:03:00.327207','c965449d-97e5-480b-95b6-80ba3cd02781','tag 3',2,'[{\"changed\": {\"fields\": [\"Child\"]}}]',13,2),(386,'2023-08-06 18:03:04.549907','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',2,'[{\"changed\": {\"fields\": [\"Parent\"]}}]',13,2),(387,'2023-08-07 08:00:28.354400','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[{\"changed\": {\"fields\": [\"Child\"]}}]',13,2),(388,'2023-08-07 08:08:29.955463','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[{\"changed\": {\"fields\": [\"Child\"]}}]',13,2),(389,'2023-08-07 08:08:37.283603','e997367a-c32a-41a8-afe8-13e70da4e72d','tag 1',2,'[{\"changed\": {\"fields\": [\"Child\"]}}]',13,2),(390,'2023-08-07 08:08:44.871744','ea057173-1291-411c-8225-0d973454245f','tag 2',2,'[]',13,2),(391,'2023-08-07 08:08:58.235066','c965449d-97e5-480b-95b6-80ba3cd02781','tag 3',2,'[{\"changed\": {\"fields\": [\"Child\"]}}]',13,2),(392,'2023-08-07 08:09:02.670178','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',2,'[]',13,2),(393,'2023-08-07 08:09:22.707062','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',2,'[]',13,2),(394,'2023-08-07 08:14:52.334119','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',2,'[]',13,2),(395,'2023-08-07 08:14:59.035132','c965449d-97e5-480b-95b6-80ba3cd02781','tag 3',2,'[]',13,2),(396,'2023-08-07 08:15:05.293412','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[]',13,2),(397,'2023-08-07 08:15:10.175602','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[]',13,2),(398,'2023-08-07 08:15:19.227143','ea057173-1291-411c-8225-0d973454245f','tag 2',2,'[]',13,2),(399,'2023-08-07 08:15:26.571653','c965449d-97e5-480b-95b6-80ba3cd02781','tag 3',2,'[]',13,2),(400,'2023-08-07 08:15:29.205481','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',2,'[]',13,2),(401,'2023-08-07 08:21:22.042710','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[]',13,2),(402,'2023-08-07 08:21:43.341075','e997367a-c32a-41a8-afe8-13e70da4e72d','tag 1',2,'[{\"changed\": {\"fields\": [\"Parent\", \"Child\"]}}]',13,2),(403,'2023-08-07 08:21:47.763628','ea057173-1291-411c-8225-0d973454245f','tag 2',2,'[]',13,2),(404,'2023-08-07 08:21:58.628352','c965449d-97e5-480b-95b6-80ba3cd02781','tag 3',2,'[{\"changed\": {\"fields\": [\"Parent\", \"Child\"]}}]',13,2),(405,'2023-08-07 08:22:01.519512','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',2,'[]',13,2),(406,'2023-08-07 11:34:22.005006','ea057173-1291-411c-8225-0d973454245f','tag 2',3,'',13,2),(407,'2023-08-07 11:34:30.993006','e997367a-c32a-41a8-afe8-13e70da4e72d','tag 1',3,'',13,2),(408,'2023-08-07 11:34:40.622403','c965449d-97e5-480b-95b6-80ba3cd02781','tag 3',3,'',13,2),(409,'2023-08-09 14:01:45.699561','885c0378-966a-408e-a35a-09c8cf6f3c79','peter nady kamal sedhom',3,'',7,1),(410,'2023-08-09 14:04:05.806675','9de7422d-7fc0-4ff6-a2fe-aa155ed505a3','peter nady kamal sedhom',3,'',7,1),(411,'2023-08-09 14:07:23.411890','fb9c9f1e-c5ec-464f-b122-d8192ad506d4','peter nady kamal sedhom',3,'',7,1),(412,'2023-08-09 14:12:30.217586','127455e1-9a3d-4a61-b331-91749c528b67','peter nady kamal sedhom',3,'',7,1),(413,'2023-08-09 14:12:53.415050','0b9f06a9-5fc5-4967-9a05-630ff952cefc','peter nady kamal sedhom',3,'',7,1),(415,'2023-08-10 07:06:14.387934','2a7008c7-46bf-4847-a594-97632e3b97a9','peter nady kamal sedhom',3,'',7,1),(416,'2023-08-10 07:08:14.085413','ff4e6b7e-7803-47b4-9e77-b0fe2c2aeed6','peter nady kamal sedhom',3,'',7,1),(417,'2023-08-10 07:26:09.003216','ffd58727-3ceb-4d6d-b100-5fa3ef868475','peter nady kamal sedhom',3,'',7,1),(418,'2023-08-10 07:27:03.440686','cbf65978-8710-4829-861c-df27c16a9a79','peter nady kamal sedhom',3,'',7,1),(419,'2023-08-10 07:53:56.604374','be9108ae-91ae-4cfa-a6b8-635d364278af','peter nady kamal sedhom',3,'',7,1),(420,'2023-08-10 07:58:27.372132','1d2cc99b-dead-46d0-847d-dba4241be896','peter nady kamal sedhom',3,'',7,1),(421,'2023-08-10 10:18:37.723643','a907ef5f-4c11-41bc-9648-355f7d23111d','مخدوم',2,'[{\"changed\": {\"fields\": [\"Parent\"]}}]',13,1),(422,'2023-08-10 10:19:02.092465','fb109f48-aea3-495a-a9e7-6cd671dfceb8','admin',2,'[{\"changed\": {\"fields\": [\"Child\", \"Is top\"]}}]',13,1),(423,'2023-08-10 10:24:55.334096','213dec12-eda1-4155-a75a-30408deee609','tag2',3,'',13,1),(424,'2023-08-10 11:27:47.840258','f60e1fa0-676d-4f11-8e74-0ddb2307f68f','شادي جرجس جرجس بخيت',2,'[{\"changed\": {\"fields\": [\"User permission tags\"]}}]',7,1),(425,'2023-08-10 11:32:45.173259','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عمادX',2,'[{\"changed\": {\"fields\": [\"User permission tags\"]}}]',7,1),(426,'2023-08-10 11:33:21.981870','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عمادX',2,'[]',7,1),(427,'2023-08-10 11:44:51.418088','d4dd0583-4502-4033-a612-56088cfc53ec','جرجس عبيد محمود عمادX',2,'[{\"changed\": {\"fields\": [\"User permission tags\"]}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(8,'users','address'),(12,'users','expensesprofileform'),(7,'users','profile'),(11,'users','profileformlog'),(9,'users','schoollevel'),(10,'users','talmzalevel'),(14,'users','temp'),(13,'users','userpermissiontag');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-07-29 10:13:37.727109'),(2,'auth','0001_initial','2023-07-29 10:13:38.099222'),(3,'admin','0001_initial','2023-07-29 10:13:38.191266'),(4,'admin','0002_logentry_remove_auto_add','2023-07-29 10:13:38.199266'),(5,'admin','0003_logentry_add_action_flag_choices','2023-07-29 10:13:38.209232'),(6,'contenttypes','0002_remove_content_type_name','2023-07-29 10:13:38.281228'),(7,'auth','0002_alter_permission_name_max_length','2023-07-29 10:13:38.328266'),(8,'auth','0003_alter_user_email_max_length','2023-07-29 10:13:38.359264'),(9,'auth','0004_alter_user_username_opts','2023-07-29 10:13:38.371264'),(10,'auth','0005_alter_user_last_login_null','2023-07-29 10:13:38.425287'),(11,'auth','0006_require_contenttypes_0002','2023-07-29 10:13:38.427267'),(12,'auth','0007_alter_validators_add_error_messages','2023-07-29 10:13:38.437265'),(13,'auth','0008_alter_user_username_max_length','2023-07-29 10:13:38.484265'),(14,'auth','0009_alter_user_last_name_max_length','2023-07-29 10:13:38.530687'),(15,'auth','0010_alter_group_name_max_length','2023-07-29 10:13:38.555656'),(16,'auth','0011_update_proxy_permissions','2023-07-29 10:13:38.566691'),(17,'auth','0012_alter_user_first_name_max_length','2023-07-29 10:13:38.629672'),(18,'sessions','0001_initial','2023-07-29 10:13:38.661673'),(19,'users','0001_initial','2023-07-29 18:36:08.718542'),(20,'users','0002_remove_profile_user','2023-07-29 18:39:26.804117'),(21,'users','0003_delete_profile','2023-07-29 19:11:46.898714'),(22,'users','0004_initial','2023-07-29 19:12:16.679224'),(23,'users','0005_alter_profile_birthdate','2023-07-29 19:12:50.339489'),(24,'users','0006_profile_address','2023-07-29 19:13:16.166744'),(25,'users','0007_profile_currentschoollevelyear_and_more','2023-07-29 19:13:59.748387'),(26,'users','0008_talmzalevel_schoollevel_profile_school_level_and_more','2023-07-29 19:33:20.927710'),(27,'users','0009_profileformlog_masreefprofileform','2023-07-29 19:58:30.521562'),(28,'users','0010_alter_schoollevel_number_of_years','2023-07-29 20:03:13.712618'),(29,'users','0011_rename_fatherphonenumber_profile_father_phone_number_and_more','2023-07-30 17:01:35.410476'),(30,'users','0012_alter_profile_birthdate','2023-07-30 17:33:04.811527'),(31,'users','0013_rename_masreefprofileform_expensesprofileform','2023-07-31 11:38:51.057615'),(32,'users','0014_alter_profile_deaconess','2023-07-31 13:26:39.658959'),(33,'users','0015_alter_address_additional_details_and_more','2023-07-31 13:32:54.833476'),(34,'users','0016_alter_schoollevel_level_name_and_more','2023-07-31 13:33:53.255996'),(35,'users','0017_schoollevel_prevues_level_talmzalevel_prevues_level_and_more','2023-07-31 14:32:33.362767'),(36,'users','0018_alter_schoollevel_options_alter_talmzalevel_options_and_more','2023-07-31 17:58:46.957258'),(37,'users','0019_rename_confessionfather_profile_confession_father_and_more','2023-07-31 20:28:22.494134'),(38,'users','0020_alter_profile_school_level_and_more','2023-08-02 05:54:11.140255'),(39,'users','0021_alter_profile_current_school_level_year_and_more','2023-08-02 18:35:58.412745'),(40,'users','0022_alter_profile_current_talmza_level_year_and_more','2023-08-03 15:51:41.360881'),(41,'users','0023_alter_profile_gender','2023-08-03 15:52:10.871535'),(42,'users','0024_userpermissiontag','2023-08-05 16:36:51.521057'),(43,'users','0002_custom_permissions','2023-08-05 18:07:57.009060'),(44,'users','0003_remove_schoollevel_prevues_level_and_more','2023-08-06 07:03:36.226891'),(45,'users','0004_remove_profile_user_permission_tags','2023-08-06 07:09:07.150465'),(46,'users','0005_profile_user_permission_tags','2023-08-06 07:20:26.104248'),(47,'users','0006_remove_userpermissiontag_next_tag_and_more','2023-08-06 08:13:05.154978'),(48,'users','0007_userpermissiontag_is_buttom_userpermissiontag_is_top','2023-08-06 08:38:14.674633'),(49,'users','0008_temp_alter_profile_user_permission_tags_and_more','2023-08-06 14:08:24.690201'),(50,'users','0009_remove_profile_temps_delete_temp','2023-08-06 14:14:33.184076'),(51,'users','0004_alter_userpermissiontag_child_and_more','2023-08-07 08:00:09.806970'),(52,'users','0003_adding_school_levels','2023-08-09 02:14:33.541510'),(53,'users','0005_alter_profile_current_talmza_level_year_and_more','2023-08-09 02:22:34.665745'),(54,'users','0006_load_schoollevel_data','2023-08-09 02:32:32.554445'),(55,'users','0007_load_talmzalevel_data','2023-08-09 02:39:39.132381'),(56,'users','0003_load_schoollevel_data','2023-08-09 05:00:32.396829'),(57,'users','0004_load_talmzalevel_data','2023-08-09 05:00:33.347213'),(58,'users','0005_profile_user_permission_tags_userpermissiontag_child_and_more','2023-08-09 05:05:37.168905');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8h3bj7jt01c6gwm1kjhfg4zk1lmsgz6y','.eJxVjMEOwiAQRP-FsyGlyAIevfsNhN0FqRpISnsy_rtt0oPOcd6beYsQ16WEtac5TCwuYhSn3w4jPVPdAT9ivTdJrS7zhHJX5EG7vDVOr-vh_h2U2Mu2Nm7MbkuOMDCRdqwQwCuH1mUP7DOiBcV5QOWtRnBJG3NOpCkSGhCfL-SzOCo:1qSye0:Pwa-Df6L3ZOJ-MWNjZE5IMDoaJNPKon49JM3lRSSS4E','2023-08-21 11:43:28.798825'),('ak2roxip9tx6vdcp2ypj2xcw1i8dqqx5','.eJxVjMsOwiAURP-FtSE8hEKX7v0GwuWCRQ0YaBON8d9tky50ljNnzps4v8yTW3psLiMZiSCH3w58uMWyDXj15VJpqGVuGeiG0H3t9Fwx3k87-yeYfJ_WtzIimTXJa4YhSIMctLbcwGCS1WgTwKA5JgbcDhK0iVKpYwwy-ABKb9Iee8-1uPh85PYio1BWMMYo-3wBkpBA9w:1qUri6:ApKwKFaVjpDsldOjV5KBJ85LqeyGqFWj8ZjLdENnxPw','2023-09-11 16:43:30.723563'),('kpfwskxovhjdfpgfcwwg5dak73e10rb6','.eJxVjMEOwiAQRP-FsyGlyAIevfsNhN0FqRpISnsy_rtt0oPOcd6beYsQ16WEtac5TCwuYhSn3w4jPVPdAT9ivTdJrS7zhHJX5EG7vDVOr-vh_h2U2Mu2Nm7MbkuOMDCRdqwQwCuH1mUP7DOiBcV5QOWtRnBJG3NOpCkSGhCfL-SzOCo:1qTGp8:MOF1PsOSClnP5QBLKE8uQ7JYMlXwJyrPiL9AcxS-G-c','2023-08-22 07:08:10.562210'),('l42evn1cwba28gofdoem82rchip7dxuj','.eJxVjMsOwiAURP-FtSE8hEKX7v0GwuWCRQ0YaBON8d9tky50ljNnzps4v8yTW3psLiMZiSCH3w58uMWyDXj15VJpqGVuGeiG0H3t9Fwx3k87-yeYfJ_WtzIimTXJa4YhSIMctLbcwGCS1WgTwKA5JgbcDhK0iVKpYwwy-ABKb9Iee8-1uPh85PYio1BWMMYo-3wBkpBA9w:1qUmol:7vWGB0Uf4CygdUJlfMxBGZLsw0hn4vO5ORDLdt7hcUg','2023-09-11 11:30:03.571430'),('lwsfo96ls0bg9sx1rkogxgvnrzuogmqo','.eJxVjkEOwiAURO_C2pAPSClduvcM5AMfixowpU00xrtrTRe6nfdmMk_mcJlHtzSaXI5sYILtfjOP4UJlBfGM5VR5qGWesuerwjfa-LFGuh42929gxDZ-2uAFoAkSKGifegFSdUqoZFH3lNDE5HsppMSgSavOQjLRe63J7IX14fuqUWu5Fkf3W54ebJDaSgDg8HoDh9VAuQ:1qTbUD:QNtIyNEmKs3BJyNZGatBp9A_tJhvyz54YbQ30CziO24','2023-09-08 05:11:57.711275'),('nb74798icn9ea26gxfwhvxgg7wiyhvjs','.eJxVjkEOwiAURO_C2pAPSClduvcM5AMfixowpU00xrtrTRe6nfdmMk_mcJlHtzSaXI5sYILtfjOP4UJlBfGM5VR5qGWesuerwjfa-LFGuh42929gxDZ-2uAFoAkSKGifegFSdUqoZFH3lNDE5HsppMSgSavOQjLRe63J7IX14fuqUWu5Fkf3W54ebJDaSgDg8HoDh9VAuQ:1qUrhk:-EyMDesjTCAg4Ur-dS0viSjrZN5afVWW70Vg9BOvyIQ','2023-09-11 16:43:08.934329'),('p0rcbqxpzi0c5fsxngth1cypx1lwk2se','.eJxVjMEOwiAQRP-FsyGlyAIevfsNhN0FqRpISnsy_rtt0oPOcd6beYsQ16WEtac5TCwuYhSn3w4jPVPdAT9ivTdJrS7zhHJX5EG7vDVOr-vh_h2U2Mu2Nm7MbkuOMDCRdqwQwCuH1mUP7DOiBcV5QOWtRnBJG3NOpCkSGhCfL-SzOCo:1qSyQH:S897lvlO8IG16qJZmPZ516H3tkIN1H5G5HYaxGsJF1s','2023-08-21 11:29:17.444960'),('rdv42t9d8p5bv8n33v0jbgujc4iss4wm','.eJxVjMEOwiAQRP-FsyGlyAIevfsNhN0FqRpISnsy_rtt0oPOcd6beYsQ16WEtac5TCwuYhSn3w4jPVPdAT9ivTdJrS7zhHJX5EG7vDVOr-vh_h2U2Mu2Nm7MbkuOMDCRdqwQwCuH1mUP7DOiBcV5QOWtRnBJG3NOpCkSGhCfL-SzOCo:1qSybU:-BZ9uB_9e4l7zUZsx8FkXmVVoFjnasDxBJTi03SNV-g','2023-08-21 11:40:52.547373'),('s8dgglr9veo3x7vj5uvbo7wq6g3jgcc8','.eJxVjkEOwiAURO_C2pAPSClduvcM5AMfixowpU00xrtrTRe6nfdmMk_mcJlHtzSaXI5sYILtfjOP4UJlBfGM5VR5qGWesuerwjfa-LFGuh42929gxDZ-2uAFoAkSKGifegFSdUqoZFH3lNDE5HsppMSgSavOQjLRe63J7IX14fuqUWu5Fkf3W54ebJDaSgDg8HoDh9VAuQ:1qUiqM:ESsDtju0mvrwl-R22rN8VvEUvfUujoRTaV6ytUFVMsU','2023-09-11 07:15:26.178277'),('se8bffh38w8lu0x5dd18xkvx29r6h1cr','.eJxVjEEOwiAQRe_C2hAGpIBL9z0DmYFBqoYmpV0Z765NutDtf-_9l4i4rTVunZc4ZXERIE6_G2F6cNtBvmO7zTLNbV0mkrsiD9rlOGd-Xg_376Bir99aESh0SStOlooHpc1gwJSA1nNBlwt5DVpjsmzNEFRxmchadmcIlEC8P-DAN-w:1qPhrS:y_2ERsBCwP17jBZA15IVLnCdEH7NoTOjnyzoyAr6kbM','2023-08-12 11:11:50.142824'),('t2bztviys8gq3v3f2zas797vahcqpka8','.eJxVjMsOwiAURP-FtSE8hEKX7v0GwuWCRQ0YaBON8d9tky50ljNnzps4v8yTW3psLiMZiSCH3w58uMWyDXj15VJpqGVuGeiG0H3t9Fwx3k87-yeYfJ_WtzIimTXJa4YhSIMctLbcwGCS1WgTwKA5JgbcDhK0iVKpYwwy-ABKb9Iee8-1uPh85PYio1BWMMYo-3wBkpBA9w:1qSeYr:k4GDzXkgj1BxT6g5O1uxoQJsbzLHy8IVKIcNSejWIQI','2023-09-05 14:16:49.008873');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_address`
--

DROP TABLE IF EXISTS `users_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_address` (
  `building` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `street` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `branches_from` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `floor` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `apartment_number` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `residential_complexes` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `district` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `additional_details` longtext COLLATE utf8mb4_unicode_ci,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_address`
--

LOCK TABLES `users_address` WRITE;
/*!40000 ALTER TABLE `users_address` DISABLE KEYS */;
INSERT INTO `users_address` VALUES (NULL,NULL,NULL,NULL,NULL,NULL,NULL,'','009a3ab062254a8ab1b3c78ef44b59ea'),('yuilgkjygyuk','عبدالفتاح كريم','','4','','  ghfghfyh','','','0f3f0b104296416a84d843475da48dd8'),(NULL,NULL,NULL,NULL,NULL,NULL,NULL,'','14b820c284fc4454acf8133a642aa031'),('لوتس','جميلة ابو حريد','يقوت الحموي','7','704',NULL,'السيوف','بجوار ماركت مصباح','2e3f9832b2f14c5cab9bf5659b34ae75'),('','','','','','','','','64af433f731349f990f99ea0b298a261'),('','','','','','','','','70af8ad7ae184fe09c7bac0393df8f17'),('لوتس','جميلة ابو حريد','يقوت الحموي','7','704',NULL,'السيوف','بجوار ماركت مصباح','72e74c5fe75348528ad87fd2d76783dd'),('لوتس','جميلة ابو حريد','يقوت الحموي','7','704',NULL,'السيوف','بجوار ماركت مصباح','b8e42c89a8864ec69f96095c6c29f573'),('لوتس','جميلة ابو حريد','يقوت الحموي','7','704',NULL,'السيوف','بجوار ماركت مصباح','c76010b9a1bd423991407c1115789b85'),('لوتس','جميلة ابو حريد','يقوت الحموي','7','704',NULL,'السيوف','بجوار ماركت مصباح','ee026d8d40b2419c8d4eff08049b7c9d'),('','','','','','','','','ef964a9ec0ed429f82445054ee008e41');
/*!40000 ALTER TABLE `users_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_expensesprofileform`
--

DROP TABLE IF EXISTS `users_expensesprofileform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_expensesprofileform` (
  `year` varchar(4) COLLATE utf8mb4_unicode_ci NOT NULL,
  `amount_of_money_payed` int NOT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_for_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_masreefprofile_created_for_id_e247de89_fk_users_pro` (`created_for_id`),
  CONSTRAINT `users_masreefprofile_created_for_id_e247de89_fk_users_pro` FOREIGN KEY (`created_for_id`) REFERENCES `users_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_expensesprofileform`
--

LOCK TABLES `users_expensesprofileform` WRITE;
/*!40000 ALTER TABLE `users_expensesprofileform` DISABLE KEYS */;
INSERT INTO `users_expensesprofileform` VALUES ('2023',35,'0a0b4cbaad5d4189bb6df139f669b87b',NULL),('2023',5,'0b5a2b4ee69f416aafbaf3723f66463a',NULL),('2023',10,'14180b0c25bf4b05ac650fbca7cd621c',NULL),('2023',5,'17d032065a6c41838e88eb71affd4817',NULL),('2023',35,'20163d659dab46f59581cef70fb07dfa',NULL),('2023',5,'2539f78240be47c38decf4547a3fc9d3',NULL),('2023',35,'3a6a94c9871d49af80263b1aca6f4dab',NULL),('2023',5,'3ad95b016aba40bd872ab13eba949da9',NULL),('2023',26,'4b1508b0c4f14fed9f7c3d8b9665906f',NULL),('2023',35,'4bee3106641348e8b015df46574893ec',NULL),('2023',5,'4d3af4a2d1b2462a87e0d42c9d4c9c50',NULL),('2023',5,'4dbeed1480a04e699a15aee68963daaa',NULL),('2023',30,'55b9ec9d0cb040dc823115854fe41a31',NULL),('2023',10,'5f0b856cf5474f4e90de32b6ac326a68',NULL),('2023',5,'669a2d66090e4c61bd6c84312de55bca',NULL),('2023',30,'6d1f8f5955c5406a95b8d31623907c80','af111cdde220479889f77ca2b27129f1'),('2023',10,'72f270c119a949dca9badbd7c10f72f3','f60e1fa0676d4f118e740ddb2307f68f'),('2023',35,'7d643251c28e44b8a2c26e4b772fe0f1',NULL),('2023',10,'82259ce9327c46ca85105246f2218f8a',NULL),('2023',5,'8bd7d2165581467bb30e2c827dc21f06',NULL),('2023',10,'9e83e152de0f41c8bedb6bb25c240f1b',NULL),('2023',10,'a229985db6a748e9ae0215b18fd8a5e6',NULL),('2023',30,'a8a8340c6f2f4c0cb9e1c3eedf193bf3',NULL),('2023',20,'c0970c0338d64bee8b4f85ccca452c07',NULL),('2023',22,'db6e30bcb00e4888b91b4e286cb8ad43',NULL),('2023',35,'e80df91e64ab4629ab5410e7b7fe49bf',NULL),('2023',5,'f5a737ef46f94e9d83a918a9a92802ac',NULL),('2023',10,'f802cebbc00f4233b04a1baec6b645bc',NULL),('2023',5,'fa85d21c794c48868640774347d48637','2d2fdf12e1b44e2e9f632725930be080'),('2023',20,'ffad7764166a4d7a82e672b4836fa579',NULL);
/*!40000 ALTER TABLE `users_expensesprofileform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_profile`
--

DROP TABLE IF EXISTS `users_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_profile` (
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `birthdate` date DEFAULT NULL,
  `job` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gender` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone_number` varchar(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `father_phone_number` varchar(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mobile_follow_up_on_WhatsApp` varchar(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `confession_father` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `church` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `deaconess` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `profile_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int DEFAULT NULL,
  `address_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `current_school_level_year` int DEFAULT NULL,
  `current_talmza_level_year` int DEFAULT NULL,
  `school_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `talmza_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mother_phone_number` varchar(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `address_id` (`address_id`),
  KEY `users_profile_school_level_id_d8a42a43_fk_users_schoollevel_id` (`school_level_id`),
  KEY `users_profile_talmza_level_id_6eb92185_fk_users_talmzalevel_id` (`talmza_level_id`),
  CONSTRAINT `users_profile_address_id_bb4c9ea7_fk_users_address_id` FOREIGN KEY (`address_id`) REFERENCES `users_address` (`id`),
  CONSTRAINT `users_profile_school_level_id_d8a42a43_fk_users_schoollevel_id` FOREIGN KEY (`school_level_id`) REFERENCES `users_schoollevel` (`id`),
  CONSTRAINT `users_profile_talmza_level_id_6eb92185_fk_users_talmzalevel_id` FOREIGN KEY (`talmza_level_id`) REFERENCES `users_talmzalevel` (`id`),
  CONSTRAINT `users_profile_user_id_2112e78d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_profile`
--

LOCK TABLES `users_profile` WRITE;
/*!40000 ALTER TABLE `users_profile` DISABLE KEYS */;
INSERT INTO `users_profile` VALUES ('كمال نادي كمال سيدهم','2001-09-24',NULL,'M',NULL,NULL,NULL,NULL,'كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال','أغس','images/user-default.png','02c21865fca24ab5b36010af0f546e59',2,'009a3ab062254a8ab1b3c78ef44b59ea',1,1,'0b23ec2234834227884e177432bc0b1f','362754ed35c241e88cfcadc7b1178191',NULL),('test test test test','2014-05-05',NULL,'M',NULL,NULL,NULL,NULL,'كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال','غير','images/profiles/IMG_1988.png','2d2fdf12e1b44e2e9f632725930be080',117,'64af433f731349f990f99ea0b298a261',1,1,'410faf62e7324eb499bd0ad117730406','32e4d997c06140188a0602e2cf0aef57',NULL),('مينا عماد بيشوي فتحيX','2016-07-12',NULL,'M','01234567890','01234567890','01234567890','ابونا بولا','كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال','أغس','images/user-default.png','3043837112914ebd9a9423b19ae7b180',12,'c76010b9a1bd423991407c1115789b85',1,2,'0b23ec2234834227884e177432bc0b1f','362754ed35c241e88cfcadc7b1178191','01234567890'),('ريتا جمال ملاك شرباتX','2016-07-12',NULL,'F','01234567890','01234567890','01234567890','ابونا بولا','كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال','إبس','images/user-default.png','a9ae08e416a04237af3bc872f789ee79',13,'72e74c5fe75348528ad87fd2d76783dd',1,1,'410faf62e7324eb499bd0ad117730406','32e4d997c06140188a0602e2cf0aef57','01234567890'),('bjbk jikhukjiopjio opopjop kol;\'jkiol','2015-02-10',NULL,'M','01222906083',NULL,NULL,'ابونا كاراس','كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال','أغس','images/user-default.png','af111cdde220479889f77ca2b27129f1',105,'0f3f0b104296416a84d843475da48dd8',3,2,'af153d90953b48e6b8d8ffa6e2a32320','74f581f3cca04506beb395a8c938203a',NULL),('جورج سدقي متحت عبدالغفورX','2016-07-12',NULL,'M','01234567890','01234567890','01234567890','ابونا رويس','كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال','غير','images/user-default.png','b27d3b209f9c4b81bc38de70d4996bbb',9,'b8e42c89a8864ec69f96095c6c29f573',6,2,'af153d90953b48e6b8d8ffa6e2a32320','74f581f3cca04506beb395a8c938203a','01234567890'),('بيتر نادي كمال سيدهم','2001-09-24',NULL,'M',NULL,NULL,NULL,NULL,'كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال','غير','images/user-default.png','c2973b75064246c38a4e6eac95f4b4cc',1,NULL,1,1,'750700e20aa9462f83a8de322f87cc7e','32e4d997c06140188a0602e2cf0aef57',NULL),('جرجس عبيد محمود عمادX','2016-02-16',NULL,'M','01234567890','01234567890','01234567890','ابونا كاراس','كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال','غير','images/user-default.png','d4dd058345024033a61256088cfc53ec',8,'2e3f9832b2f14c5cab9bf5659b34ae75',1,1,'af153d90953b48e6b8d8ffa6e2a32320','74f581f3cca04506beb395a8c938203a','01234567890'),('شادي جرجس جرجس بخيت','2016-03-03',NULL,'M',NULL,NULL,NULL,NULL,'كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال','غير','images/user-default.png','f60e1fa0676d4f118e740ddb2307f68f',104,'ef964a9ec0ed429f82445054ee008e41',1,1,'410faf62e7324eb499bd0ad117730406','32e4d997c06140188a0602e2cf0aef57',NULL);
/*!40000 ALTER TABLE `users_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_profile_user_permission_tags`
--

DROP TABLE IF EXISTS `users_profile_user_permission_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_profile_user_permission_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `profile_id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `userpermissiontag_id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_profile_user_permi_profile_id_userpermissio_2061b2a2_uniq` (`profile_id`,`userpermissiontag_id`),
  KEY `users_profile_user_p_userpermissiontag_id_03708b2d_fk_users_use` (`userpermissiontag_id`),
  CONSTRAINT `users_profile_user_p_profile_id_f3aaca1d_fk_users_pro` FOREIGN KEY (`profile_id`) REFERENCES `users_profile` (`id`),
  CONSTRAINT `users_profile_user_p_userpermissiontag_id_03708b2d_fk_users_use` FOREIGN KEY (`userpermissiontag_id`) REFERENCES `users_userpermissiontag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_profile_user_permission_tags`
--

LOCK TABLES `users_profile_user_permission_tags` WRITE;
/*!40000 ALTER TABLE `users_profile_user_permission_tags` DISABLE KEYS */;
INSERT INTO `users_profile_user_permission_tags` VALUES (6,'02c21865fca24ab5b36010af0f546e59','a907ef5f4c1141bc9648355f7d23111d'),(54,'2d2fdf12e1b44e2e9f632725930be080','a907ef5f4c1141bc9648355f7d23111d'),(5,'3043837112914ebd9a9423b19ae7b180','a907ef5f4c1141bc9648355f7d23111d'),(4,'a9ae08e416a04237af3bc872f789ee79','a907ef5f4c1141bc9648355f7d23111d'),(39,'af111cdde220479889f77ca2b27129f1','a907ef5f4c1141bc9648355f7d23111d'),(3,'b27d3b209f9c4b81bc38de70d4996bbb','a907ef5f4c1141bc9648355f7d23111d'),(2,'c2973b75064246c38a4e6eac95f4b4cc','a907ef5f4c1141bc9648355f7d23111d'),(53,'d4dd058345024033a61256088cfc53ec','72433fa4c4624c57bbc983a0ec7ed2f9'),(52,'d4dd058345024033a61256088cfc53ec','fb109f48aea3495aa9e76cd671dfceb8'),(38,'f60e1fa0676d4f118e740ddb2307f68f','a907ef5f4c1141bc9648355f7d23111d'),(50,'f60e1fa0676d4f118e740ddb2307f68f','fb109f48aea3495aa9e76cd671dfceb8');
/*!40000 ALTER TABLE `users_profile_user_permission_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_profileformlog`
--

DROP TABLE IF EXISTS `users_profileformlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_profileformlog` (
  `log_date` datetime(6) NOT NULL,
  `category_action` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_by_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_for_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_profileformlog_created_by_id_fd9a3cf0_fk_users_profile_id` (`created_by_id`),
  KEY `users_profileformlog_created_for_id_8b57fbf7_fk_users_profile_id` (`created_for_id`),
  CONSTRAINT `users_profileformlog_created_by_id_fd9a3cf0_fk_users_profile_id` FOREIGN KEY (`created_by_id`) REFERENCES `users_profile` (`id`),
  CONSTRAINT `users_profileformlog_created_for_id_8b57fbf7_fk_users_profile_id` FOREIGN KEY (`created_for_id`) REFERENCES `users_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_profileformlog`
--

LOCK TABLES `users_profileformlog` WRITE;
/*!40000 ALTER TABLE `users_profileformlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_profileformlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_schoollevel`
--

DROP TABLE IF EXISTS `users_schoollevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_schoollevel` (
  `level_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `level_number` int NOT NULL,
  `number_of_years` int DEFAULT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `next_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `previous_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `next_level_id` (`next_level_id`),
  UNIQUE KEY `previous_level_id` (`previous_level_id`),
  CONSTRAINT `users_schoollevel_next_level_id_06148425_fk_users_schoollevel_id` FOREIGN KEY (`next_level_id`) REFERENCES `users_schoollevel` (`id`),
  CONSTRAINT `users_schoollevel_previous_level_id_d9478edc_fk_users_sch` FOREIGN KEY (`previous_level_id`) REFERENCES `users_schoollevel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_schoollevel`
--

LOCK TABLES `users_schoollevel` WRITE;
/*!40000 ALTER TABLE `users_schoollevel` DISABLE KEYS */;
INSERT INTO `users_schoollevel` VALUES ('خريج',6,NULL,'07889dacae4848b88d2b683ee35d8ab2',NULL,'07889dacae4848b88d2b683ee35d8ab2'),('جامعة',5,NULL,'0b23ec2234834227884e177432bc0b1f','07889dacae4848b88d2b683ee35d8ab2','c8fa8e8373f045e5a8205e2c7d919239'),('اقل من حضانة',0,NULL,'410faf62e7324eb499bd0ad117730406','d0b12a7571bc40e494ed9745a604bef3',NULL),('الإعدادي',3,3,'750700e20aa9462f83a8de322f87cc7e','c8fa8e8373f045e5a8205e2c7d919239','af153d90953b48e6b8d8ffa6e2a32320'),('الابتدائي',2,6,'af153d90953b48e6b8d8ffa6e2a32320','750700e20aa9462f83a8de322f87cc7e','d0b12a7571bc40e494ed9745a604bef3'),('ثانوي',4,3,'c8fa8e8373f045e5a8205e2c7d919239','0b23ec2234834227884e177432bc0b1f','750700e20aa9462f83a8de322f87cc7e'),('حضانة',1,2,'d0b12a7571bc40e494ed9745a604bef3','af153d90953b48e6b8d8ffa6e2a32320','410faf62e7324eb499bd0ad117730406');
/*!40000 ALTER TABLE `users_schoollevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_talmzalevel`
--

DROP TABLE IF EXISTS `users_talmzalevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_talmzalevel` (
  `level_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `level_number` int NOT NULL,
  `number_of_years` int NOT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `next_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `previous_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `next_level_id` (`next_level_id`),
  UNIQUE KEY `previous_level_id` (`previous_level_id`),
  CONSTRAINT `users_talmzalevel_next_level_id_8904d407_fk_users_talmzalevel_id` FOREIGN KEY (`next_level_id`) REFERENCES `users_talmzalevel` (`id`),
  CONSTRAINT `users_talmzalevel_previous_level_id_62d68e96_fk_users_tal` FOREIGN KEY (`previous_level_id`) REFERENCES `users_talmzalevel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_talmzalevel`
--

LOCK TABLES `users_talmzalevel` WRITE;
/*!40000 ALTER TABLE `users_talmzalevel` DISABLE KEYS */;
INSERT INTO `users_talmzalevel` VALUES ('اقل من تمهيدي',0,1,'32e4d997c06140188a0602e2cf0aef57','d2be3f9947084d55bee749c24094c125',NULL),('الرابع',5,2,'362754ed35c241e88cfcadc7b1178191',NULL,'ba6c0d1ee63d4d27a689c55e65611bd6'),('الثاني',3,2,'6b3aa1762544403e8c05a51fd36a4351','ba6c0d1ee63d4d27a689c55e65611bd6','74f581f3cca04506beb395a8c938203a'),('الأول',2,2,'74f581f3cca04506beb395a8c938203a','6b3aa1762544403e8c05a51fd36a4351','d2be3f9947084d55bee749c24094c125'),('الثالث',4,2,'ba6c0d1ee63d4d27a689c55e65611bd6','362754ed35c241e88cfcadc7b1178191','6b3aa1762544403e8c05a51fd36a4351'),('تمهيدي',1,2,'d2be3f9947084d55bee749c24094c125','74f581f3cca04506beb395a8c938203a','32e4d997c06140188a0602e2cf0aef57');
/*!40000 ALTER TABLE `users_talmzalevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userpermissiontag`
--

DROP TABLE IF EXISTS `users_userpermissiontag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_userpermissiontag` (
  `tag_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `child_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `parent_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_buttom` tinyint(1) NOT NULL,
  `is_top` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tag_name` (`tag_name`),
  KEY `users_userpermissiontag_child_id_f3612627` (`child_id`),
  KEY `users_userpermissiontag_parent_id_ead25f1f` (`parent_id`),
  CONSTRAINT `users_userpermission_child_id_f3612627_fk_users_use` FOREIGN KEY (`child_id`) REFERENCES `users_userpermissiontag` (`id`),
  CONSTRAINT `users_userpermission_parent_id_ead25f1f_fk_users_use` FOREIGN KEY (`parent_id`) REFERENCES `users_userpermissiontag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userpermissiontag`
--

LOCK TABLES `users_userpermissiontag` WRITE;
/*!40000 ALTER TABLE `users_userpermissiontag` DISABLE KEYS */;
INSERT INTO `users_userpermissiontag` VALUES ('tag3','5ef1ed41bfbe4375935488a549ca91ab','72433fa4c4624c57bbc983a0ec7ed2f9','bb9bb7df95174c91a735c529a61ab49c',0,0),('tag4','72433fa4c4624c57bbc983a0ec7ed2f9','a907ef5f4c1141bc9648355f7d23111d','5ef1ed41bfbe4375935488a549ca91ab',0,0),('مخدوم','a907ef5f4c1141bc9648355f7d23111d',NULL,'72433fa4c4624c57bbc983a0ec7ed2f9',1,0),('tag2','bb9bb7df95174c91a735c529a61ab49c','5ef1ed41bfbe4375935488a549ca91ab','fb109f48aea3495aa9e76cd671dfceb8',0,0),('admin','fb109f48aea3495aa9e76cd671dfceb8','bb9bb7df95174c91a735c529a61ab49c',NULL,0,1);
/*!40000 ALTER TABLE `users_userpermissiontag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userpermissiontag_permissions`
--

DROP TABLE IF EXISTS `users_userpermissiontag_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_userpermissiontag_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userpermissiontag_id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userpermissiontag__userpermissiontag_id_per_5418b27a_uniq` (`userpermissiontag_id`,`permission_id`),
  KEY `users_userpermission_permission_id_226f4916_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_userpermission_permission_id_226f4916_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_userpermission_userpermissiontag_id_27f209a8_fk_users_use` FOREIGN KEY (`userpermissiontag_id`) REFERENCES `users_userpermissiontag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userpermissiontag_permissions`
--

LOCK TABLES `users_userpermissiontag_permissions` WRITE;
/*!40000 ALTER TABLE `users_userpermissiontag_permissions` DISABLE KEYS */;
INSERT INTO `users_userpermissiontag_permissions` VALUES (28,'a907ef5f4c1141bc9648355f7d23111d',16),(30,'a907ef5f4c1141bc9648355f7d23111d',28),(25,'a907ef5f4c1141bc9648355f7d23111d',32),(26,'a907ef5f4c1141bc9648355f7d23111d',36),(27,'a907ef5f4c1141bc9648355f7d23111d',40),(29,'a907ef5f4c1141bc9648355f7d23111d',52),(22,'fb109f48aea3495aa9e76cd671dfceb8',13),(23,'fb109f48aea3495aa9e76cd671dfceb8',14),(24,'fb109f48aea3495aa9e76cd671dfceb8',15),(21,'fb109f48aea3495aa9e76cd671dfceb8',16),(1,'fb109f48aea3495aa9e76cd671dfceb8',25),(2,'fb109f48aea3495aa9e76cd671dfceb8',26),(3,'fb109f48aea3495aa9e76cd671dfceb8',27),(4,'fb109f48aea3495aa9e76cd671dfceb8',28),(5,'fb109f48aea3495aa9e76cd671dfceb8',29),(6,'fb109f48aea3495aa9e76cd671dfceb8',30),(7,'fb109f48aea3495aa9e76cd671dfceb8',31),(8,'fb109f48aea3495aa9e76cd671dfceb8',32),(9,'fb109f48aea3495aa9e76cd671dfceb8',41),(10,'fb109f48aea3495aa9e76cd671dfceb8',42),(11,'fb109f48aea3495aa9e76cd671dfceb8',43),(12,'fb109f48aea3495aa9e76cd671dfceb8',44),(13,'fb109f48aea3495aa9e76cd671dfceb8',49),(14,'fb109f48aea3495aa9e76cd671dfceb8',50),(15,'fb109f48aea3495aa9e76cd671dfceb8',51),(16,'fb109f48aea3495aa9e76cd671dfceb8',52),(17,'fb109f48aea3495aa9e76cd671dfceb8',53),(18,'fb109f48aea3495aa9e76cd671dfceb8',54),(19,'fb109f48aea3495aa9e76cd671dfceb8',55),(20,'fb109f48aea3495aa9e76cd671dfceb8',56);
/*!40000 ALTER TABLE `users_userpermissiontag_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-12 19:59:42
