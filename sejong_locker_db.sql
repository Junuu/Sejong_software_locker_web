-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: sejong
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `locker_info`
--

DROP TABLE IF EXISTS `locker_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locker_info` (
  `row` int NOT NULL,
  `column` int NOT NULL,
  `section` varchar(10) NOT NULL,
  `locker_statement` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locker_info`
--

LOCK TABLES `locker_info` WRITE;
/*!40000 ALTER TABLE `locker_info` DISABLE KEYS */;
INSERT INTO `locker_info` VALUES (1,2,'A','usable'),(1,3,'A','usable'),(1,4,'A','disable'),(1,8,'A','disable'),(1,5,'A','usable'),(1,6,'A','usable'),(1,7,'A','usable'),(1,9,'A','usable'),(1,10,'A','usable'),(2,1,'A','usable'),(2,2,'A','usable'),(2,3,'A','usable'),(2,4,'A','disable'),(2,5,'A','usable'),(2,6,'A','usable'),(2,7,'A','usable'),(2,8,'A','usable'),(2,9,'A','usable'),(2,10,'A','usable'),(3,1,'A','usable'),(3,2,'A','usable'),(3,3,'A','usable'),(3,4,'A','usable'),(3,5,'A','usable'),(3,6,'A','usable'),(3,7,'A','usable'),(3,8,'A','usable'),(3,9,'A','usable'),(3,10,'A','usable'),(4,1,'A','usable'),(4,2,'A','usable'),(4,3,'A','usable'),(4,4,'A','usable'),(4,5,'A','usable'),(4,6,'A','usable'),(4,7,'A','disable'),(4,8,'A','disable'),(4,9,'A','disable'),(4,10,'A','usable'),(5,1,'A','usable'),(5,2,'A','usable'),(5,3,'A','usable'),(5,4,'A','usable'),(5,5,'A','usable'),(5,6,'A','usable'),(5,7,'A','usable'),(5,8,'A','usable'),(5,9,'A','usable'),(5,10,'A','disable'),(6,1,'A','usable'),(6,2,'A','usable'),(6,3,'A','usable'),(6,4,'A','usable'),(6,5,'A','usable'),(6,6,'A','disable'),(6,7,'A','usable'),(6,8,'A','usable'),(6,9,'A','usable'),(6,10,'A','usable'),(1,1,'A','usable'),(1,1,'B','usable'),(1,2,'B','usable'),(1,3,'B','usable'),(1,4,'B','usable'),(1,5,'B','usable'),(1,6,'B','usable'),(1,7,'B','usable'),(1,8,'B','usable'),(1,9,'B','usable'),(1,10,'B','usable'),(2,1,'B','usable'),(2,2,'B','usable'),(2,3,'B','usable'),(2,4,'B','usable'),(2,5,'B','usable'),(2,6,'B','usable'),(2,7,'B','usable'),(2,8,'B','disable'),(2,9,'B','usable'),(2,10,'B','usable'),(3,1,'B','usable'),(3,2,'B','usable'),(3,3,'B','usable'),(3,4,'B','usable'),(3,5,'B','usable'),(3,6,'B','usable'),(3,7,'B','disable'),(3,8,'B','disable'),(3,9,'B','usable'),(3,10,'B','usable'),(4,1,'B','usable'),(4,2,'B','usable'),(4,3,'B','usable'),(4,4,'B','usable'),(4,5,'B','usable'),(4,6,'B','usable'),(4,7,'B','usable'),(4,8,'B','usable'),(4,9,'B','usable'),(4,10,'B','usable'),(5,1,'B','usable'),(5,2,'B','usable'),(5,3,'B','usable'),(5,4,'B','usable'),(5,5,'B','usable'),(5,6,'B','usable'),(5,7,'B','disable'),(5,8,'B','usable'),(5,9,'B','usable'),(5,10,'B','usable'),(6,1,'B','usable'),(6,2,'B','usable'),(6,3,'B','usable'),(6,4,'B','usable'),(6,5,'B','usable'),(6,6,'B','usable'),(6,7,'B','disable'),(6,8,'B','disable'),(6,9,'B','disable'),(6,10,'B','usable'),(1,1,'C','usable'),(1,2,'C','usable'),(1,3,'C','usable'),(1,4,'C','usable'),(1,5,'C','usable'),(1,6,'C','usable'),(2,1,'C','usable'),(2,2,'C','usable'),(2,3,'C','usable'),(2,4,'C','usable'),(2,5,'C','usable'),(2,6,'C','usable'),(3,1,'C','usable'),(3,2,'C','usable'),(3,3,'C','usable'),(3,4,'C','usable'),(3,5,'C','usable'),(3,6,'C','disable'),(4,1,'C','disable'),(4,2,'C','disable'),(4,3,'C','usable'),(4,4,'C','disable'),(4,5,'C','usable'),(4,6,'C','usable'),(5,1,'C','usable'),(5,2,'C','usable'),(5,3,'C','usable'),(5,4,'C','usable'),(5,5,'C','usable'),(5,6,'C','usable'),(6,1,'C','usable'),(6,2,'C','usable'),(6,3,'C','usable'),(6,4,'C','usable'),(6,5,'C','usable'),(6,6,'C','usable'),(1,1,'D','usable'),(1,2,'D','usable'),(1,3,'D','usable'),(1,4,'D','usable'),(1,5,'D','usable'),(1,6,'D','usable'),(2,1,'D','usable'),(2,2,'D','usable'),(2,3,'D','usable'),(2,4,'D','disable'),(2,5,'D','usable'),(2,6,'D','usable'),(3,1,'D','usable'),(3,2,'D','usable'),(3,3,'D','disable'),(3,4,'D','usable'),(3,5,'D','disable'),(3,6,'D','disable'),(4,1,'D','usable'),(4,2,'D','usable'),(4,3,'D','usable'),(4,4,'D','usable'),(4,5,'D','disable'),(4,6,'D','usable'),(5,1,'D','disable'),(5,2,'D','usable'),(5,3,'D','usable'),(5,4,'D','usable'),(5,5,'D','disable'),(5,6,'D','usable'),(6,1,'D','usable'),(6,2,'D','usable'),(6,3,'D','usable'),(6,4,'D','usable'),(6,5,'D','usable'),(6,6,'D','usable'),(1,1,'E','usable'),(1,2,'E','usable'),(1,3,'E','disable'),(1,4,'E','usable'),(1,5,'E','usable'),(1,6,'E','usable'),(2,1,'E','usable'),(2,2,'E','disable'),(2,3,'E','disable'),(2,4,'E','usable'),(2,5,'E','usable'),(2,6,'E','disable'),(3,1,'E','usable'),(3,2,'E','usable'),(3,3,'E','disable'),(3,4,'E','usable'),(3,5,'E','usable'),(3,6,'E','usable'),(4,1,'E','disable'),(4,2,'E','usable'),(4,3,'E','disable'),(4,4,'E','disable'),(4,5,'E','disable'),(4,6,'E','usable'),(5,1,'E','usable'),(5,2,'E','usable'),(5,3,'E','usable'),(5,4,'E','usable'),(5,5,'E','usable'),(5,6,'E','usable'),(6,1,'E','usable'),(6,2,'E','usable'),(6,3,'E','usable'),(6,4,'E','disable'),(6,5,'E','usable'),(6,6,'E','usable');
/*!40000 ALTER TABLE `locker_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_info` (
  `School_ID` varchar(30) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `locker_in_use` tinyint NOT NULL DEFAULT '0',
  `locker_section` varchar(45) DEFAULT NULL,
  `locker_num` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`School_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-19 17:14:46
