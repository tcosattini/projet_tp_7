-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: fromagerie_com
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Base de données : `fromagerie_com`
--

USE `fromagerie_com`;

-- --------------------------------------------------------

--
-- Droping all Tables in the right order
--

--
-- Droping django' auto-generated tables
--

DROP TABLE IF EXISTS `auth_group_permissions`;
DROP TABLE IF EXISTS `auth_permission`;
DROP TABLE IF EXISTS `auth_group`;
DROP TABLE IF EXISTS `django_admin_log`;
DROP TABLE IF EXISTS `django_content_type`;
DROP TABLE IF EXISTS `django_migrations`;
DROP TABLE IF EXISTS `django_session`;

--
-- Droping application' tables
--

DROP TABLE IF EXISTS `t_utilisateur`;
DROP TABLE IF EXISTS `t_rel_cond`;
DROP TABLE IF EXISTS `t_entcde`;
DROP TABLE IF EXISTS `t_dtlcode`;
DROP TABLE IF EXISTS `t_client`;
DROP TABLE IF EXISTS `t_poidsv`;
DROP TABLE IF EXISTS `t_poids`;
DROP TABLE IF EXISTS `t_role`;
DROP TABLE IF EXISTS `t_enseigne`;
DROP TABLE IF EXISTS `t_objet`;
DROP TABLE IF EXISTS `t_dept`;
DROP TABLE IF EXISTS `t_conditionnement`;
DROP TABLE IF EXISTS `t_communes`;

--
-- Dumping routines for database 'fromagerie_com'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-10 11:59:38
