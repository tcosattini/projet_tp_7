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

-- --------------------------------------------------------

--
-- Table structure for table `t_objet`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_objet` (
  `codobj` int NOT NULL AUTO_INCREMENT,
  `libobj` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Tailleobj` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `puobj` decimal(19,4) DEFAULT NULL,
  `Poidsobj` decimal(19,4) DEFAULT NULL,
  `indispobj` int DEFAULT NULL,
  `o_imp` int DEFAULT NULL,
  `o_aff` int DEFAULT NULL,
  `o_cartp` int DEFAULT NULL,
  `idcondit` int DEFAULT NULL,
  `points` int DEFAULT NULL,
  `o_ordre_aff` int DEFAULT NULL,
  `is_active` int NOT NULL,
  PRIMARY KEY (`codobj`)
) ENGINE=InnoDB AUTO_INCREMENT=176 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_communes`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_communes` (
  `id_commune` int NOT NULL AUTO_INCREMENT,
  `DEP` int unsigned DEFAULT NULL,
  `CP` varchar(5) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `COMMUNES` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id_commune`),
  CONSTRAINT `t_communes_chk_1` CHECK ((`DEP` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=21836 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_client`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_client` (
  `codcli` int NOT NULL AUTO_INCREMENT,
  `genrecli` varchar(8) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nomcli` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `prenomcli` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adresse1cli` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adresse2cli` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adresse3cli` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cpcli` varchar(5) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `villecli` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `telcli` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `emailcli` longtext COLLATE utf8mb4_general_ci,
  `portcli` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `newsletter` int DEFAULT NULL,
  `id_commune` int DEFAULT NULL,
  PRIMARY KEY (`codcli`),
  KEY `t_client_id_commune_ee177057_fk_t_communes_id_commune` (`id_commune`),
  CONSTRAINT `t_client_id_commune_ee177057_fk_t_communes_id_commune` FOREIGN KEY (`id_commune`) REFERENCES `t_communes` (`id_commune`)
) ENGINE=InnoDB AUTO_INCREMENT=5751 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_conditionnement`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_conditionnement` (
  `idcondit` int NOT NULL AUTO_INCREMENT,
  `libcondit` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `poidscondit` int DEFAULT NULL,
  `prixcond` decimal(19,4) DEFAULT NULL,
  `ordreimp` int DEFAULT NULL,
  PRIMARY KEY (`idcondit`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dept`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_dept` (
  `code_dept` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
  `nom_dept` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ordre_aff_dept` int DEFAULT NULL,
  PRIMARY KEY (`code_dept`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dtlcode`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_dtlcode` (
  `codcde` int DEFAULT NULL,
  `qte` int DEFAULT NULL,
  `Colis` int DEFAULT NULL,
  `Commentaire` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_dtl_commande` int NOT NULL AUTO_INCREMENT,
  `codobj` int DEFAULT NULL,
  PRIMARY KEY (`id_dtl_commande`),
  KEY `t_dtlcode_codobj_8a366611_fk_t_objet_codobj` (`codobj`),
  CONSTRAINT `t_dtlcode_codobj_8a366611_fk_t_objet_codobj` FOREIGN KEY (`codobj`) REFERENCES `t_objet` (`codobj`)
) ENGINE=InnoDB AUTO_INCREMENT=23228 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_enseigne`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_enseigne` (
  `id_enseigne` int NOT NULL AUTO_INCREMENT,
  `lb_enseigne` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ville_enseigne` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `dept_enseigne` int DEFAULT NULL,
  PRIMARY KEY (`id_enseigne`)
) ENGINE=InnoDB AUTO_INCREMENT=483 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_entcde`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_entcde` (
  `codcde` int NOT NULL AUTO_INCREMENT,
  `datcde` datetime(6) DEFAULT NULL,
  `timbrecli` double DEFAULT NULL,
  `timbrecde` double DEFAULT NULL,
  `Nbcolis` int unsigned DEFAULT NULL,
  `cheqcli` double DEFAULT NULL,
  `idcondit` int DEFAULT NULL,
  `cdeComt` longtext COLLATE utf8mb4_general_ci,
  `barchive` int DEFAULT NULL,
  `bstock` int DEFAULT NULL,
  `codcli` int DEFAULT NULL,
  `id_dtl_commande` int DEFAULT NULL,
  PRIMARY KEY (`codcde`),
  KEY `t_entcde_codcli_2fe584de_fk_t_client_codcli` (`codcli`),
  KEY `t_entcde_id_dtl_commande_ef7d5e56_fk_t_dtlcode_id_dtl_commande` (`id_dtl_commande`),
  CONSTRAINT `t_entcde_codcli_2fe584de_fk_t_client_codcli` FOREIGN KEY (`codcli`) REFERENCES `t_client` (`codcli`),
  CONSTRAINT `t_entcde_id_dtl_commande_ef7d5e56_fk_t_dtlcode_id_dtl_commande` FOREIGN KEY (`id_dtl_commande`) REFERENCES `t_dtlcode` (`id_dtl_commande`),
  CONSTRAINT `t_entcde_chk_1` CHECK ((`Nbcolis` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=9305 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_poids`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_poids` (
  `idpoids` int NOT NULL AUTO_INCREMENT,
  `valmin` double NOT NULL,
  `valtimbre` double DEFAULT NULL,
  PRIMARY KEY (`idpoids`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_poidsv`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_poidsv` (
  `idpoids` int NOT NULL AUTO_INCREMENT,
  `valmin` double NOT NULL,
  `valtimbre` double DEFAULT NULL,
  PRIMARY KEY (`idpoids`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_rel_cond`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_rel_cond` (
  `idrelcond` int NOT NULL AUTO_INCREMENT,
  `qteobjdeb` int DEFAULT NULL,
  `qteobjfin` int DEFAULT NULL,
  `codcond` int DEFAULT NULL,
  `codobj` int DEFAULT NULL,
  PRIMARY KEY (`idrelcond`),
  KEY `t_rel_cond_codcond_db43f01b_fk_t_conditionnement_idcondit` (`codcond`),
  KEY `t_rel_cond_codobj_66c6266c_fk_t_objet_codobj` (`codobj`),
  CONSTRAINT `t_rel_cond_codcond_db43f01b_fk_t_conditionnement_idcondit` FOREIGN KEY (`codcond`) REFERENCES `t_conditionnement` (`idcondit`),
  CONSTRAINT `t_rel_cond_codobj_66c6266c_fk_t_objet_codobj` FOREIGN KEY (`codobj`) REFERENCES `t_objet` (`codobj`)
) ENGINE=InnoDB AUTO_INCREMENT=213 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_role`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_role` (
  `code_role` int NOT NULL AUTO_INCREMENT,
  `lib_role` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`code_role`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_utilisateur`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_utilisateur` (
  `code_utilisateur` int NOT NULL AUTO_INCREMENT,
  `nom_utilisateur` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `prenom_utilisateur` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `couleur_fond_utilisateur` int DEFAULT NULL,
  `date_cde_utilisateur` datetime(6) DEFAULT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `code_role` int DEFAULT NULL,
  PRIMARY KEY (`code_utilisateur`),
  UNIQUE KEY `username` (`username`),
  KEY `t_utilisateur_code_role_a74656d6_fk_t_role_code_role` (`code_role`),
  CONSTRAINT `t_utilisateur_code_role_a74656d6_fk_t_role_code_role` FOREIGN KEY (`code_role`) REFERENCES `t_role` (`code_role`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
