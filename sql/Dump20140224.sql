CREATE DATABASE  IF NOT EXISTS `sensecambrowser` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `sensecambrowser`;
-- MySQL dump 10.13  Distrib 5.5.35, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: sensecambrowser
-- ------------------------------------------------------
-- Server version	5.5.35-0ubuntu0.12.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `annotater_annotationaction`
--

DROP TABLE IF EXISTS `annotater_annotationaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `annotater_annotationaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `concept_id` int(11) NOT NULL,
  `annotate_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `annotater_annotationaction_6340c63c` (`user_id`),
  KEY `annotater_annotationaction_8a386586` (`concept_id`),
  CONSTRAINT `user_id_refs_id_d54d2a02` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `concept_id_refs_id_a4c56212` FOREIGN KEY (`concept_id`) REFERENCES `annotater_annotationterm` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `annotater_annotationaction`
--

LOCK TABLES `annotater_annotationaction` WRITE;
/*!40000 ALTER TABLE `annotater_annotationaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `annotater_annotationaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `annotater_annotationterm`
--

DROP TABLE IF EXISTS `annotater_annotationterm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `annotater_annotationterm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `concept` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `add_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `concept` (`concept`),
  UNIQUE KEY `category` (`category`),
  KEY `annotater_annotationterm_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_baa215dd` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `annotater_annotationterm`
--

LOCK TABLES `annotater_annotationterm` WRITE;
/*!40000 ALTER TABLE `annotater_annotationterm` DISABLE KEYS */;
/*!40000 ALTER TABLE `annotater_annotationterm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add migration history',7,'add_migrationhistory'),(20,'Can change migration history',7,'change_migrationhistory'),(21,'Can delete migration history',7,'delete_migrationhistory'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(25,'Can add user interaction',9,'add_userinteraction'),(26,'Can change user interaction',9,'change_userinteraction'),(27,'Can delete user interaction',9,'delete_userinteraction'),(28,'Can add sensor type',10,'add_sensortype'),(29,'Can change sensor type',10,'change_sensortype'),(30,'Can delete sensor type',10,'delete_sensortype'),(31,'Can add album',11,'add_album'),(32,'Can change album',11,'change_album'),(33,'Can delete album',11,'delete_album'),(34,'Can add image',12,'add_image'),(35,'Can change image',12,'change_image'),(36,'Can delete image',12,'delete_image'),(37,'Can add sensor',13,'add_sensor'),(38,'Can change sensor',13,'change_sensor'),(39,'Can delete sensor',13,'delete_sensor'),(40,'Can add sensor file',14,'add_sensorfile'),(41,'Can change sensor file',14,'change_sensorfile'),(42,'Can delete sensor file',14,'delete_sensorfile'),(43,'Can add event',15,'add_event'),(44,'Can change event',15,'change_event'),(45,'Can delete event',15,'delete_event'),(46,'Can add event image',16,'add_eventimage'),(47,'Can change event image',16,'change_eventimage'),(48,'Can delete event image',16,'delete_eventimage'),(49,'Can add annotation term',17,'add_annotationterm'),(50,'Can change annotation term',17,'change_annotationterm'),(51,'Can delete annotation term',17,'delete_annotationterm'),(52,'Can add annotation action',18,'add_annotationaction'),(53,'Can change annotation action',18,'change_annotationaction'),(54,'Can delete annotation action',18,'delete_annotationaction'),(55,'Can add user profile',19,'add_userprofile'),(56,'Can change user profile',19,'change_userprofile'),(57,'Can delete user profile',19,'delete_userprofile'),(58,'Can add registration profile',20,'add_registrationprofile'),(59,'Can change registration profile',20,'change_registrationprofile'),(60,'Can delete registration profile',20,'delete_registrationprofile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$10000$AEDEi1w45BJ5$7NcEH14yV8SFcFd56Msg5Y7jDt0eu/ekMkPmA861ZJg=','2014-02-24 23:24:02',1,'marissa','','','',1,1,'2014-02-24 23:17:12');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-02-24 23:20:02',1,10,'1','SensorType object',1,''),(2,'2014-02-24 23:20:52',1,10,'2','SensorType object',1,''),(3,'2014-02-24 23:21:18',1,10,'3','SensorType object',1,''),(4,'2014-02-24 23:21:28',1,10,'4','SensorType object',1,''),(5,'2014-02-24 23:21:39',1,10,'5','SensorType object',1,''),(6,'2014-02-24 23:22:23',1,10,'5','SensorType object',2,'No fields changed.'),(7,'2014-02-24 23:22:36',1,10,'6','SensorType object',1,''),(8,'2014-02-24 23:22:51',1,10,'7','SensorType object',1,''),(9,'2014-02-24 23:23:10',1,10,'8','SensorType object',1,''),(10,'2014-02-24 23:24:15',1,10,'9','SensorType object',1,''),(11,'2014-02-24 23:24:25',1,10,'10','SensorType object',1,''),(12,'2014-02-24 23:24:32',1,10,'11','SensorType object',1,''),(13,'2014-02-24 23:24:54',1,10,'12','SensorType object',1,''),(14,'2014-02-24 23:25:15',1,10,'13','SensorType object',1,''),(15,'2014-02-24 23:25:34',1,10,'14','SensorType object',1,''),(16,'2014-02-24 23:26:20',1,10,'15','SensorType object',1,''),(17,'2014-02-24 23:26:30',1,10,'16','SensorType object',1,''),(18,'2014-02-24 23:26:38',1,10,'17','SensorType object',1,''),(19,'2014-02-24 23:27:12',1,10,'18','SensorType object',1,''),(20,'2014-02-24 23:27:35',1,10,'19','SensorType object',1,''),(21,'2014-02-24 23:27:48',1,10,'20','SensorType object',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'migration history','south','migrationhistory'),(8,'log entry','admin','logentry'),(9,'user interaction','sensecam','userinteraction'),(10,'sensor type','fileuploader','sensortype'),(11,'album','fileuploader','album'),(12,'image','fileuploader','image'),(13,'sensor','fileuploader','sensor'),(14,'sensor file','fileuploader','sensorfile'),(15,'event','eventseg','event'),(16,'event image','eventseg','eventimage'),(17,'annotation term','annotater','annotationterm'),(18,'annotation action','annotater','annotationaction'),(19,'user profile','registration','userprofile'),(20,'registration profile','registration','registrationprofile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('js43tivmgaqik3jlmextq5rrgp2x7qba','ZWU4NjA2YjRiMmEwNzNhMmVjNzg2YTczMzFhZDE5MWFmMWVlZWQyMjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==','2014-03-10 23:24:02'),('lbenn3glob9g02zzuuyb6juzd01yhhz7','ZWU4NjA2YjRiMmEwNzNhMmVjNzg2YTczMzFhZDE5MWFmMWVlZWQyMjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==','2014-03-10 23:18:29');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eventseg_event`
--

DROP TABLE IF EXISTS `eventseg_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `eventseg_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `start_at` datetime NOT NULL,
  `end_at` datetime NOT NULL,
  `location` varchar(1000) NOT NULL,
  `sensor_num` int(11) NOT NULL,
  `pic_num` int(11) NOT NULL,
  `keyframe` varchar(1000) NOT NULL,
  `shared` tinyint(1) NOT NULL,
  `favourite` tinyint(1) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `eventseg_event_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_31f4f414` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventseg_event`
--

LOCK TABLES `eventseg_event` WRITE;
/*!40000 ALTER TABLE `eventseg_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `eventseg_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eventseg_eventimage`
--

DROP TABLE IF EXISTS `eventseg_eventimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `eventseg_eventimage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image_id` int(11) NOT NULL,
  `event_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `eventseg_eventimage_06df7330` (`image_id`),
  KEY `eventseg_eventimage_a41e20fe` (`event_id`),
  CONSTRAINT `image_id_refs_id_b63a3c71` FOREIGN KEY (`image_id`) REFERENCES `fileuploader_image` (`id`),
  CONSTRAINT `event_id_refs_id_aa1f18a2` FOREIGN KEY (`event_id`) REFERENCES `eventseg_event` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventseg_eventimage`
--

LOCK TABLES `eventseg_eventimage` WRITE;
/*!40000 ALTER TABLE `eventseg_eventimage` DISABLE KEYS */;
/*!40000 ALTER TABLE `eventseg_eventimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fileuploader_album`
--

DROP TABLE IF EXISTS `fileuploader_album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fileuploader_album` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `duration_sec` int(11) NOT NULL,
  `capture_date` date NOT NULL,
  `uploaded_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fileuploader_album_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_78a5cea7` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fileuploader_album`
--

LOCK TABLES `fileuploader_album` WRITE;
/*!40000 ALTER TABLE `fileuploader_album` DISABLE KEYS */;
/*!40000 ALTER TABLE `fileuploader_album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fileuploader_image`
--

DROP TABLE IF EXISTS `fileuploader_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fileuploader_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `album_id` int(11) NOT NULL,
  `file` varchar(100) NOT NULL,
  `year` varchar(4) NOT NULL,
  `month` varchar(2) NOT NULL,
  `capture_at` datetime NOT NULL,
  `uploaded_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fileuploader_image_6340c63c` (`user_id`),
  KEY `fileuploader_image_6781e42a` (`album_id`),
  CONSTRAINT `user_id_refs_id_f2889ec5` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `album_id_refs_id_fe72f2fe` FOREIGN KEY (`album_id`) REFERENCES `fileuploader_album` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fileuploader_image`
--

LOCK TABLES `fileuploader_image` WRITE;
/*!40000 ALTER TABLE `fileuploader_image` DISABLE KEYS */;
/*!40000 ALTER TABLE `fileuploader_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fileuploader_sensor`
--

DROP TABLE IF EXISTS `fileuploader_sensor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fileuploader_sensor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `img_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL,
  `capture_at` datetime NOT NULL,
  `uploaded_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fileuploader_sensor_6340c63c` (`user_id`),
  KEY `fileuploader_sensor_b7ec2b54` (`img_id`),
  KEY `fileuploader_sensor_403d8ff3` (`type_id`),
  CONSTRAINT `img_id_refs_id_f8c14aff` FOREIGN KEY (`img_id`) REFERENCES `fileuploader_image` (`id`),
  CONSTRAINT `type_id_refs_id_532f2afa` FOREIGN KEY (`type_id`) REFERENCES `fileuploader_sensortype` (`id`),
  CONSTRAINT `user_id_refs_id_746e4da3` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fileuploader_sensor`
--

LOCK TABLES `fileuploader_sensor` WRITE;
/*!40000 ALTER TABLE `fileuploader_sensor` DISABLE KEYS */;
/*!40000 ALTER TABLE `fileuploader_sensor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fileuploader_sensorfile`
--

DROP TABLE IF EXISTS `fileuploader_sensorfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fileuploader_sensorfile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `file` varchar(100) NOT NULL,
  `uploaded_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fileuploader_sensorfile_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_c177f714` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fileuploader_sensorfile`
--

LOCK TABLES `fileuploader_sensorfile` WRITE;
/*!40000 ALTER TABLE `fileuploader_sensorfile` DISABLE KEYS */;
/*!40000 ALTER TABLE `fileuploader_sensorfile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fileuploader_sensortype`
--

DROP TABLE IF EXISTS `fileuploader_sensortype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fileuploader_sensortype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `abbreviation` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `abbreviation` (`abbreviation`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fileuploader_sensortype`
--

LOCK TABLES `fileuploader_sensortype` WRITE;
/*!40000 ALTER TABLE `fileuploader_sensortype` DISABLE KEYS */;
INSERT INTO `fileuploader_sensortype` VALUES (1,'size','sz'),(2,'proprietary','p'),(3,'accelerometer_x','accx'),(4,'accelerometer_y','accy'),(5,'accelerometer_z','accz'),(6,'magnetometer_x','magx'),(7,'magnetometer_y','magy'),(8,'magnetometer_z','magz'),(9,'red','red'),(10,'green','green'),(11,'blue','blue'),(12,'luminance','lum'),(13,'temperature','tem'),(14,'gps_status','g'),(15,'latitude','lat'),(16,'longitude','lon'),(17,'altitude','alt'),(18,'gps_groud_speed','gs'),(19,'gps_horizontal_error','herr'),(20,'gps_vertical_error','verr');
/*!40000 ALTER TABLE `fileuploader_sensortype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration_registrationprofile`
--

DROP TABLE IF EXISTS `registration_registrationprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registration_registrationprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `activation_key` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_954d2985` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration_registrationprofile`
--

LOCK TABLES `registration_registrationprofile` WRITE;
/*!40000 ALTER TABLE `registration_registrationprofile` DISABLE KEYS */;
/*!40000 ALTER TABLE `registration_registrationprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration_userprofile`
--

DROP TABLE IF EXISTS `registration_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registration_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `url` varchar(200) NOT NULL,
  `company` varchar(50) NOT NULL,
  `birthday` datetime NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `profile_img` varchar(100) NOT NULL,
  `weight` decimal(5,2) DEFAULT NULL,
  `height` decimal(5,2) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_1ce26a54` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration_userprofile`
--

LOCK TABLES `registration_userprofile` WRITE;
/*!40000 ALTER TABLE `registration_userprofile` DISABLE KEYS */;
/*!40000 ALTER TABLE `registration_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensecam_userinteraction`
--

DROP TABLE IF EXISTS `sensecam_userinteraction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sensecam_userinteraction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creator_id` int(11) NOT NULL,
  `itact_type` int(11) NOT NULL,
  `message` varchar(100) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sensecam_userinteraction_ad376f8d` (`creator_id`),
  CONSTRAINT `creator_id_refs_id_9dda6343` FOREIGN KEY (`creator_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensecam_userinteraction`
--

LOCK TABLES `sensecam_userinteraction` WRITE;
/*!40000 ALTER TABLE `sensecam_userinteraction` DISABLE KEYS */;
/*!40000 ALTER TABLE `sensecam_userinteraction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-02-24 23:32:28
