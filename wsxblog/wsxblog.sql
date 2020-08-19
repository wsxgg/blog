-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: wsxblog
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1-log

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
-- Table structure for table `blogs_blogs`
--

DROP TABLE IF EXISTS `blogs_blogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogs_blogs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `author` varchar(30) NOT NULL,
  `img` varchar(100) DEFAULT NULL,
  `body` longtext NOT NULL,
  `abstract` longtext,
  `visiting` int(10) unsigned NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `modifyed_time` datetime(6) NOT NULL,
  `category_id` int(11) NOT NULL,
  `tags_id` int(11) NOT NULL,
  `is_top` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blogs_blogs_category_id_202287bd_fk_blogs_categorys_id` (`category_id`),
  KEY `blogs_blogs_tags_id_28ad2181_fk_blogs_tags_id` (`tags_id`),
  CONSTRAINT `blogs_blogs_category_id_202287bd_fk_blogs_categorys_id` FOREIGN KEY (`category_id`) REFERENCES `blogs_categorys` (`id`),
  CONSTRAINT `blogs_blogs_tags_id_28ad2181_fk_blogs_tags_id` FOREIGN KEY (`tags_id`) REFERENCES `blogs_tags` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogs_blogs`
--

LOCK TABLES `blogs_blogs` WRITE;
/*!40000 ALTER TABLE `blogs_blogs` DISABLE KEYS */;
INSERT INTO `blogs_blogs` VALUES (1,'first','都不是宝贝','group1/M00/00/00/wKiYnF6mc5CAK_oQAAIuKXqEzh48322699','第一个blog的正文','第一个的描述',6,'2020-04-27 05:54:24.353334','2020-04-28 05:20:38.679254',1,1,1),(2,'second','都不是宝贝','group1/M00/00/00/wKiYnF6mdUOAMQBNAALHDUBQnDs7508104','<p>第二篇了</p>','2222',7,'2020-04-27 06:01:39.912201','2020-04-28 05:20:37.256463',1,1,1),(3,'third','都不是宝贝','group1/M00/00/00/wKiYnF6meUyAclskAARVpBmvBVM0113443','33333','333333333',96,'2020-04-27 06:18:52.518868','2020-04-28 09:45:12.227445',1,1,1),(4,'forth','都不是宝贝','group1/M00/00/00/wKiYnF6meV2AGrTnAAHGDxD1_m40072242','<p>4444444</p>','4444444444',52,'2020-04-27 06:19:09.557588','2020-04-29 09:10:08.826573',1,1,1),(5,'第一个web','都不是宝贝','group1/M00/00/00/wKiYnF6mhPOAKkgvAAIuKXqEzh49760581','第一个web','11111',6,'2020-04-27 07:08:35.756858','2020-04-29 09:54:17.781701',1,2,1),(6,'linux01','都不是宝贝','group1/M00/00/00/wKiYnF6mjqGAJlEcAALHDUBQnDs7229563','linux01','linux01',6,'2020-04-27 07:49:53.581383','2020-04-28 05:16:34.556256',1,3,1),(7,'linux02','都不是宝贝','group1/M00/00/00/wKiYnF6mjrOAHVKVAALHDUBQnDs3850085','linux02','linux02',20,'2020-04-27 07:50:12.260115','2020-04-28 09:30:03.398178',1,3,1),(8,'linux03','都不是宝贝','group1/M00/00/00/wKiYnF6mjsiAEYmIAARVpBmvBVM4921979','<p>linux03</p>','linux03',40,'2020-04-27 07:50:32.763204','2020-04-29 09:55:42.696321',1,3,1),(9,'linux04','都不是宝贝','group1/M00/00/00/wKiYnF6mjtiAErnCAAIuKXqEzh41423480','linux04','linux04',18,'2020-04-27 07:50:49.249509','2020-04-28 05:20:35.887656',1,3,1),(10,'markdown','都不是宝贝','group1/M00/00/00/wKiYnF6nvWOAbBB6AAAtMvQAkZE1196770','---\r\n#一级标题1\r\n##二级标题\r\n---\r\n**关关雎鸠，在河之洲。窈窕淑女，君子好逑。**\r\n\r\n参差荇菜，左右流之。窈窕淑女，寤寐求之。\r\n#一级标题1\r\n#一级标题1\r\n##二级标题\r\n#一级标题1\r\n#一级标题1\r\n---\r\n+ 列表一\r\n+ 列表二\r\n    + 列表二-1\r\n    + 列表二-2\r\n---\r\n#一级标题2\r\n```python\r\ndef aa():\r\njkjk = 1\r\nhhhh = 2\r\n```\r\n---\r\n> HAHA\r\n>\r\n>>HAHA2\r\n>\r\n>haha\r\n---\r\n\r\n- [ ] 不勾选\r\n- [x] 勾选\r\n\r\n---\r\n\r\n```ruby\r\nrequire \'redcarpet\'\r\nmarkdown = Redcarpet.new(\"Hello World!\")\r\nputs markdown.to_html\r\n```\r\n---\r\n```python\r\ndef function():\r\nmarkdown = \"Hello World!\"\r\n```','没有描述',165,'2020-04-28 05:21:40.375586','2020-04-29 07:19:05.886633',1,2,1),(11,'linux05','都不是宝贝','group1/M00/00/00/wKiYnF6oEJ6AdjL7AAAVf1-JjlY2329201','linux05','linux05',0,'2020-04-28 11:16:46.896441','2020-04-28 11:16:46.896441',1,3,0),(12,'linux06','都不是宝贝','group1/M00/00/00/wKiYnF6oELGAF8psAAAtMvQAkZE1896750','linux06','linux06',0,'2020-04-28 11:17:06.182474','2020-04-28 11:17:06.182474',1,3,0),(13,'linux07','都不是宝贝','group1/M00/00/00/wKiYnF6oEYaAfWywAALHDUBQnDs9209886','linux07','linux07',0,'2020-04-28 11:20:39.154311','2020-04-28 11:20:39.154311',1,3,0),(14,'linux08','都不是宝贝','group1/M00/00/00/wKiYnF6oEZiAGk9gAAHGDxD1_m41633663','linux08','linux08',0,'2020-04-28 11:20:57.446446','2020-04-28 11:20:57.446446',1,3,0),(15,'linux09','都不是宝贝','group1/M00/00/00/wKiYnF6oEamAQZaqAAHGDxD1_m49769444','linux09','linux09',0,'2020-04-28 11:21:14.821056','2020-04-28 11:21:14.821056',1,3,0),(16,'linux10','都不是宝贝','group1/M00/00/00/wKiYnF6oEbyAdwy2AALHDUBQnDs3483372','linux10','linux10',0,'2020-04-28 11:21:33.224411','2020-04-28 11:21:33.224411',1,3,0),(17,'linux11','都不是宝贝','group1/M00/00/00/wKiYnF6oEcuAMe69AARVpBmvBVM9833299','linux11','linux11',0,'2020-04-28 11:21:48.866282','2020-04-28 11:21:48.866282',1,3,0);
/*!40000 ALTER TABLE `blogs_blogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogs_categorys`
--

DROP TABLE IF EXISTS `blogs_categorys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogs_categorys` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogs_categorys`
--

LOCK TABLES `blogs_categorys` WRITE;
/*!40000 ALTER TABLE `blogs_categorys` DISABLE KEYS */;
INSERT INTO `blogs_categorys` VALUES (1,'技术文档');
/*!40000 ALTER TABLE `blogs_categorys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogs_tags`
--

DROP TABLE IF EXISTS `blogs_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogs_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogs_tags`
--

LOCK TABLES `blogs_tags` WRITE;
/*!40000 ALTER TABLE `blogs_tags` DISABLE KEYS */;
INSERT INTO `blogs_tags` VALUES (1,'python'),(2,'web'),(3,'linux');
/*!40000 ALTER TABLE `blogs_tags` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-04 15:43:56
