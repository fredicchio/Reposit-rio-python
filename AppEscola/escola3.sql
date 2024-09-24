# Host: localhost  (Version: 5.5.5-10.4.32-MariaDB)
# Date: 2024-09-18 08:57:21
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "tbl_cidades"
#

DROP TABLE IF EXISTS `tbl_cidades`;
CREATE TABLE `tbl_cidades` (
  `CID_COD` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(255) DEFAULT NULL,
  `UF` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`CID_COD`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Data for table "tbl_cidades"
#


#
# Structure for table "tbl_cursos"
#

DROP TABLE IF EXISTS `tbl_cursos`;
CREATE TABLE `tbl_cursos` (
  `COD_CUR` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(255) DEFAULT NULL,
  `Valor` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`COD_CUR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Data for table "tbl_cursos"
#


#
# Structure for table "tbl_alunos"
#

DROP TABLE IF EXISTS `tbl_alunos`;
CREATE TABLE `tbl_alunos` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `CID_COD` int(11) NOT NULL DEFAULT 0,
  `CUR_COD` int(11) NOT NULL DEFAULT 0,
  `Nome` varchar(255) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telefone` varchar(255) DEFAULT NULL,
  `idade` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `CID_COD` (`CID_COD`,`CUR_COD`),
  KEY `CUR_COD` (`CUR_COD`),
  CONSTRAINT `tbl_alunos_ibfk_1` FOREIGN KEY (`CID_COD`) REFERENCES `tbl_cidades` (`CID_COD`),
  CONSTRAINT `tbl_alunos_ibfk_2` FOREIGN KEY (`CUR_COD`) REFERENCES `tbl_cursos` (`COD_CUR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Data for table "tbl_alunos"
#


#
# Structure for table "tbl_professores"
#

DROP TABLE IF EXISTS `tbl_professores`;
CREATE TABLE `tbl_professores` (
  `PRO_COD` int(11) NOT NULL AUTO_INCREMENT,
  `CID_COD` int(11) NOT NULL DEFAULT 0,
  `Nome` varchar(255) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telefone` varchar(255) DEFAULT NULL,
  `cpf` varchar(255) DEFAULT NULL,
  `idade` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`PRO_COD`),
  UNIQUE KEY `CID_COD` (`CID_COD`),
  CONSTRAINT `tbl_professores_ibfk_1` FOREIGN KEY (`CID_COD`) REFERENCES `tbl_cidades` (`CID_COD`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Data for table "tbl_professores"
#


#
# Structure for table "tbl_materias"
#

DROP TABLE IF EXISTS `tbl_materias`;
CREATE TABLE `tbl_materias` (
  `MAT_COD` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(255) DEFAULT NULL,
  `CUR_COD` int(11) NOT NULL DEFAULT 0,
  `PRO_COD` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`MAT_COD`),
  UNIQUE KEY `CUR_COD` (`CUR_COD`,`PRO_COD`),
  KEY `PRO_COD` (`PRO_COD`),
  CONSTRAINT `tbl_materias_ibfk_1` FOREIGN KEY (`PRO_COD`) REFERENCES `tbl_professores` (`PRO_COD`),
  CONSTRAINT `tbl_materias_ibfk_2` FOREIGN KEY (`CUR_COD`) REFERENCES `tbl_cursos` (`COD_CUR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Data for table "tbl_materias"
#


#
# Structure for table "tbl_aulas"
#

DROP TABLE IF EXISTS `tbl_aulas`;
CREATE TABLE `tbl_aulas` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `data` varchar(255) DEFAULT NULL,
  `sala` varchar(255) DEFAULT NULL,
  `MAT_COD` int(11) NOT NULL DEFAULT 0,
  `observacoes` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `MAT_COD` (`MAT_COD`),
  CONSTRAINT `tbl_aulas_ibfk_1` FOREIGN KEY (`MAT_COD`) REFERENCES `tbl_materias` (`MAT_COD`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Data for table "tbl_aulas"
#


#
# Structure for table "tbl_usuarios"
#

DROP TABLE IF EXISTS `tbl_usuarios`;
CREATE TABLE `tbl_usuarios` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Data for table "tbl_usuarios"
#

INSERT INTO `tbl_usuarios` VALUES (1,'admin','admin','1'),(2,'teste','frederico','12345678');
