DELETE FROM reservas
WHERE laboratorio = 'Sala 1' AND data_reserva = '2024-07-31' AND '7' BETWEEN HOUR(primeiro_horario) AND HOUR(ultimo_horario)

truncate reservas


create table reservas
(
	 id INT PRIMARY KEY AUTO_INCREMENT,
           laboratorio TEXT,
           pessoa TEXT,
           primeiro_horario TEXT,
           ultimo_horario TEXT,
           data_reserva TEXT
);

create table usuarios
(
	id INT PRIMARY KEY AUTO_INCREMENT,
	usuario text,
	nome text
);

























SELECT * FROM tbl_agendamento;

SELECT HOUR(primeiro_horario), HOUR(ultimo_horario) FROM reservas WHERE data_reserva = %s and laboratorio = %s




DROP TABLE if exists  `tbl_agendamento`;
CREATE TABLE `tbl_agendamento` (
           id INT PRIMARY KEY AUTO_INCREMENT,
           laboratorio TEXT,
           pessoa TEXT,
           primeiro_horario TEXT,
           ultimo_horario TEXT,
           data_reserva TEXT
					 )
	
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_agendamento
#

LOCK TABLES `tbl_agendamento` WRITE;
/*!40000 ALTER TABLE `tbl_agendamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_agendamento` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_cadastro
#

DROP TABLE IF EXISTS `tbl_cadastro`;
CREATE TABLE `tbl_cadastro` (
  `cad_cod` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`cad_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_cadastro
#

LOCK TABLES `tbl_cadastro` WRITE;
/*!40000 ALTER TABLE `tbl_cadastro` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_cadastro` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_cargo
#

DROP TABLE IF EXISTS `tbl_cargo`;
CREATE TABLE `tbl_cargo` (
  `car_cod` int(11) NOT NULL AUTO_INCREMENT,
  `car_marcaProduto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`car_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_cargo
#

LOCK TABLES `tbl_cargo` WRITE;
/*!40000 ALTER TABLE `tbl_cargo` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_cargo` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_categorias
#

DROP TABLE IF EXISTS `tbl_categorias`;
CREATE TABLE `tbl_categorias` (
  `cat_cod` int(11) NOT NULL AUTO_INCREMENT,
  `cat_categoria` varchar(255) DEFAULT NULL,
  `cat_descrição` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cat_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_categorias
#

LOCK TABLES `tbl_categorias` WRITE;
/*!40000 ALTER TABLE `tbl_categorias` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_categorias` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_chefe
#

DROP TABLE IF EXISTS `tbl_chefe`;
CREATE TABLE `tbl_chefe` (
  `che_cod` int(11) NOT NULL AUTO_INCREMENT,
  `che_matrículas` varchar(255) DEFAULT NULL,
  `che_nome` varchar(255) DEFAULT NULL,
  `che_cpf` varchar(255) DEFAULT NULL,
  `che_perfil` varchar(255) DEFAULT NULL,
  `che_telefone` varchar(255) DEFAULT NULL,
  `che_celular` varchar(255) DEFAULT NULL,
  `che_email` varchar(255) DEFAULT NULL,
  `che_im` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`che_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_chefe
#

LOCK TABLES `tbl_chefe` WRITE;
/*!40000 ALTER TABLE `tbl_chefe` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_chefe` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_cidades
#

DROP TABLE IF EXISTS `tbl_cidades`;
CREATE TABLE `tbl_cidades` (
  `cid_cod` int(11) NOT NULL AUTO_INCREMENT,
  `cid_nome` varchar(255) DEFAULT NULL,
  `est_idEstado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cid_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_cidades
#

LOCK TABLES `tbl_cidades` WRITE;
/*!40000 ALTER TABLE `tbl_cidades` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_cidades` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_departamento
#

DROP TABLE IF EXISTS `tbl_departamento`;
CREATE TABLE `tbl_departamento` (
  `dep_cod` int(11) NOT NULL AUTO_INCREMENT,
  `dep_ID` varchar(255) DEFAULT NULL,
  `dep_detalhes` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`dep_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_departamento
#

LOCK TABLES `tbl_departamento` WRITE;
/*!40000 ALTER TABLE `tbl_departamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_departamento` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_detalheemp
#

DROP TABLE IF EXISTS `tbl_detalheemp`;
CREATE TABLE `tbl_detalheemp` (
  `det_cod` int(11) NOT NULL AUTO_INCREMENT,
  `det_IDEmpresa` varchar(255) DEFAULT NULL,
  `det_IDNpatri` varchar(255) DEFAULT NULL,
  `det_obs` varchar(255) DEFAULT NULL,
  `det_situação` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`det_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_detalheemp
#

LOCK TABLES `tbl_detalheemp` WRITE;
/*!40000 ALTER TABLE `tbl_detalheemp` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_detalheemp` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_empréstimo
#

DROP TABLE IF EXISTS `tbl_empréstimo`;
CREATE TABLE `tbl_empréstimo` (
  `emp_cod` int(11) NOT NULL AUTO_INCREMENT,
  `emp_IDEmpresa` varchar(255) DEFAULT NULL,
  `emp_IDLocatario` varchar(255) DEFAULT NULL,
  `emp_autorização` varchar(255) DEFAULT NULL,
  `emp_levarPara` varchar(255) DEFAULT NULL,
  `emp_obs` varchar(255) DEFAULT NULL,
  `emp_dataRetiro` varchar(255) DEFAULT NULL,
  `emp_previsãoDevolução` varchar(255) DEFAULT NULL,
  `emp_dataDevolução` varchar(255) DEFAULT NULL,
  `emp_uso` varchar(255) DEFAULT NULL,
  `emp_status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`emp_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_empréstimo
#

LOCK TABLES `tbl_empréstimo` WRITE;
/*!40000 ALTER TABLE `tbl_empréstimo` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_empréstimo` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_equipamento
#

DROP TABLE IF EXISTS `tbl_equipamento`;
CREATE TABLE `tbl_equipamento` (
  `equ_cod` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`equ_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_equipamento
#

LOCK TABLES `tbl_equipamento` WRITE;
/*!40000 ALTER TABLE `tbl_equipamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_equipamento` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_equipe
#

DROP TABLE IF EXISTS `tbl_equipe`;
CREATE TABLE `tbl_equipe` (
  `equ_cod` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`equ_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_equipe
#

LOCK TABLES `tbl_equipe` WRITE;
/*!40000 ALTER TABLE `tbl_equipe` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_equipe` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_estado
#

DROP TABLE IF EXISTS `tbl_estado`;
CREATE TABLE `tbl_estado` (
  `est_cod` int(11) NOT NULL AUTO_INCREMENT,
  `est_idEstado` varchar(2) DEFAULT NULL,
  `est_nome` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`est_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_estado
#

LOCK TABLES `tbl_estado` WRITE;
/*!40000 ALTER TABLE `tbl_estado` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_estado` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_estoque
#

DROP TABLE IF EXISTS `tbl_estoque`;
CREATE TABLE `tbl_estoque` (
  `est_cod` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`est_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_estoque
#

LOCK TABLES `tbl_estoque` WRITE;
/*!40000 ALTER TABLE `tbl_estoque` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_estoque` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_estoqueentrada
#

DROP TABLE IF EXISTS `tbl_estoqueentrada`;
CREATE TABLE `tbl_estoqueentrada` (
  `estE_cod` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`estE_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_estoqueentrada
#

LOCK TABLES `tbl_estoqueentrada` WRITE;
/*!40000 ALTER TABLE `tbl_estoqueentrada` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_estoqueentrada` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_estoquesaída
#

DROP TABLE IF EXISTS `tbl_estoquesaída`;
CREATE TABLE `tbl_estoquesaída` (
  `estS_cod` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`estS_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_estoquesaída
#

LOCK TABLES `tbl_estoquesaída` WRITE;
/*!40000 ALTER TABLE `tbl_estoquesaída` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_estoquesaída` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_fornecedor
#

DROP TABLE IF EXISTS `tbl_fornecedor`;
CREATE TABLE `tbl_fornecedor` (
  `for_cod` int(11) NOT NULL AUTO_INCREMENT,
  `for_ramoAtual` varchar(255) DEFAULT NULL,
  `for_nomeEmpresa` varchar(255) DEFAULT NULL,
  `for_razãosocial` varchar(255) DEFAULT NULL,
  `for_CPF` varchar(255) DEFAULT NULL,
  `for_CNPJ` varchar(255) DEFAULT NULL,
  `for_endereco` varchar(255) DEFAULT NULL,
  `for_fone` varchar(255) DEFAULT NULL,
  `for_celular` varchar(255) DEFAULT NULL,
  `for_email` varchar(255) DEFAULT NULL,
  `for_representante` varchar(255) DEFAULT NULL,
  `for_vendedor` varchar(255) DEFAULT NULL,
  `for_PJ` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`for_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_fornecedor
#

LOCK TABLES `tbl_fornecedor` WRITE;
/*!40000 ALTER TABLE `tbl_fornecedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_fornecedor` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_imagem
#

DROP TABLE IF EXISTS `tbl_imagem`;
CREATE TABLE `tbl_imagem` (
  `ima_cod` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ima_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_imagem
#

LOCK TABLES `tbl_imagem` WRITE;
/*!40000 ALTER TABLE `tbl_imagem` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_imagem` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_impressoras
#

DROP TABLE IF EXISTS `tbl_impressoras`;
CREATE TABLE `tbl_impressoras` (
  `imp_cod` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`imp_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_impressoras
#

LOCK TABLES `tbl_impressoras` WRITE;
/*!40000 ALTER TABLE `tbl_impressoras` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_impressoras` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_local
#

DROP TABLE IF EXISTS `tbl_local`;
CREATE TABLE `tbl_local` (
  `loc_cod` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`loc_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_local
#

LOCK TABLES `tbl_local` WRITE;
/*!40000 ALTER TABLE `tbl_local` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_local` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_mantsaída
#

DROP TABLE IF EXISTS `tbl_mantsaída`;
CREATE TABLE `tbl_mantsaída` (
  `manS_cod` int(11) NOT NULL AUTO_INCREMENT,
  `manS_IDSaida` varchar(255) DEFAULT NULL,
  `manS_IDEstoque` varchar(255) DEFAULT NULL,
  `manS_qtdeSaida` varchar(255) DEFAULT NULL,
  `manS_local` varchar(255) DEFAULT NULL,
  `manS_solicitante` varchar(255) DEFAULT NULL,
  `manS_NPatri` varchar(255) DEFAULT NULL,
  `manS_data` varchar(255) DEFAULT NULL,
  `manS_obs` varchar(255) DEFAULT NULL,
  `manS_IM` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`manS_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_mantsaída
#

LOCK TABLES `tbl_mantsaída` WRITE;
/*!40000 ALTER TABLE `tbl_mantsaída` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_mantsaída` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_manutenção
#

DROP TABLE IF EXISTS `tbl_manutenção`;
CREATE TABLE `tbl_manutenção` (
  `man_cod` int(11) NOT NULL AUTO_INCREMENT,
  `man_marca` varchar(255) DEFAULT NULL,
  `man_modelo` varchar(255) DEFAULT NULL,
  `man_numeroSerie` varchar(255) DEFAULT NULL,
  `man_dataInsta` varchar(255) DEFAULT NULL,
  `man_nomePapercut` varchar(255) DEFAULT NULL,
  `man_nomeID` varchar(255) DEFAULT NULL,
  `man_LocalUso` varchar(255) DEFAULT NULL,
  `man_IPconfiguração` varchar(255) DEFAULT NULL,
  `man_historicoGeral` varchar(255) DEFAULT NULL,
  `man_foto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`man_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_manutenção
#

LOCK TABLES `tbl_manutenção` WRITE;
/*!40000 ALTER TABLE `tbl_manutenção` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_manutenção` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_matentrada
#

DROP TABLE IF EXISTS `tbl_matentrada`;
CREATE TABLE `tbl_matentrada` (
  `manE_cod` int(11) NOT NULL AUTO_INCREMENT,
  `manE_entrada` varchar(255) DEFAULT NULL,
  `manE_IDEstoque` varchar(255) DEFAULT NULL,
  `manE_qtde` int(11) DEFAULT NULL,
  `manE_data` varchar(255) DEFAULT NULL,
  `manE_fornecedor` varchar(255) DEFAULT NULL,
  `manE_objetivoMaterial` varchar(255) DEFAULT NULL,
  `manE_IM` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`manE_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_matentrada
#

LOCK TABLES `tbl_matentrada` WRITE;
/*!40000 ALTER TABLE `tbl_matentrada` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_matentrada` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_material
#

DROP TABLE IF EXISTS `tbl_material`;
CREATE TABLE `tbl_material` (
  `mat_cod` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`mat_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_material
#

LOCK TABLES `tbl_material` WRITE;
/*!40000 ALTER TABLE `tbl_material` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_material` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_matestoque
#

DROP TABLE IF EXISTS `tbl_matestoque`;
CREATE TABLE `tbl_matestoque` (
  `manEs_cod` int(11) NOT NULL AUTO_INCREMENT,
  `manEs_IDEstoque` varchar(255) DEFAULT NULL,
  `manEs_produto` varchar(255) DEFAULT NULL,
  `manEs_marcaProduto` varchar(255) DEFAULT NULL,
  `manEs_modeloProduto` varchar(255) DEFAULT NULL,
  `manEs_estMax` varchar(255) DEFAULT NULL,
  `manEs_IM` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`manEs_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_matestoque
#

LOCK TABLES `tbl_matestoque` WRITE;
/*!40000 ALTER TABLE `tbl_matestoque` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_matestoque` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_matmarca
#

DROP TABLE IF EXISTS `tbl_matmarca`;
CREATE TABLE `tbl_matmarca` (
  `matM_cod` int(11) NOT NULL AUTO_INCREMENT,
  `matM_marcaProduto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`matM_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_matmarca
#

LOCK TABLES `tbl_matmarca` WRITE;
/*!40000 ALTER TABLE `tbl_matmarca` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_matmarca` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_matmodelo
#

DROP TABLE IF EXISTS `tbl_matmodelo`;
CREATE TABLE `tbl_matmodelo` (
  `matMo_cod` int(11) NOT NULL AUTO_INCREMENT,
  `matMo_modelo` varchar(255) DEFAULT NULL,
  `matMo_detalhes` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`matMo_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_matmodelo
#

LOCK TABLES `tbl_matmodelo` WRITE;
/*!40000 ALTER TABLE `tbl_matmodelo` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_matmodelo` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_mattipo
#

DROP TABLE IF EXISTS `tbl_mattipo`;
CREATE TABLE `tbl_mattipo` (
  `matT_cod` int(11) NOT NULL AUTO_INCREMENT,
  `matT_produto` varchar(255) DEFAULT NULL,
  `matT_detalhes` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`matT_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_mattipo
#

LOCK TABLES `tbl_mattipo` WRITE;
/*!40000 ALTER TABLE `tbl_mattipo` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_mattipo` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_pessoacad
#

DROP TABLE IF EXISTS `tbl_pessoacad`;
CREATE TABLE `tbl_pessoacad` (
  `pes_cod` int(11) NOT NULL AUTO_INCREMENT,
  `pes_nome` varchar(255) DEFAULT NULL,
  `pes_cpf` int(11) DEFAULT NULL,
  `pes_perfil` varchar(255) DEFAULT NULL,
  `pes_telefone` varchar(255) DEFAULT NULL,
  `pes_celular` varchar(255) DEFAULT NULL,
  `pes_email` varchar(255) DEFAULT NULL,
  `pes_obs` varchar(255) DEFAULT NULL,
  `pes_foto` varchar(255) DEFAULT NULL,
  `pes_status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pes_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_pessoacad
#

LOCK TABLES `tbl_pessoacad` WRITE;
/*!40000 ALTER TABLE `tbl_pessoacad` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_pessoacad` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_ramo
#

DROP TABLE IF EXISTS `tbl_ramo`;
CREATE TABLE `tbl_ramo` (
  `ram_cod` int(11) NOT NULL AUTO_INCREMENT,
  `ram_atuação` varchar(255) DEFAULT NULL,
  `ram_obsdetalhes` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ram_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_ramo
#

LOCK TABLES `tbl_ramo` WRITE;
/*!40000 ALTER TABLE `tbl_ramo` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_ramo` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_status
#

DROP TABLE IF EXISTS `tbl_status`;
CREATE TABLE `tbl_status` (
  `sta_cod` int(11) NOT NULL AUTO_INCREMENT,
  `sta_status` varchar(255) DEFAULT NULL,
  `sta_detalhes` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sta_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_status
#

LOCK TABLES `tbl_status` WRITE;
/*!40000 ALTER TABLE `tbl_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_status` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_supentrada
#

DROP TABLE IF EXISTS `tbl_supentrada`;
CREATE TABLE `tbl_supentrada` (
  `supE_cod` int(11) NOT NULL AUTO_INCREMENT,
  `supE_IDEstoque` varchar(255) DEFAULT NULL,
  `supE_qtdeEntrada` varchar(255) DEFAULT NULL,
  `supE_fornecedor` varchar(255) DEFAULT NULL,
  `supE_obs` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`supE_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_supentrada
#

LOCK TABLES `tbl_supentrada` WRITE;
/*!40000 ALTER TABLE `tbl_supentrada` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_supentrada` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_supestoque
#

DROP TABLE IF EXISTS `tbl_supestoque`;
CREATE TABLE `tbl_supestoque` (
  `supEs_cod` int(11) NOT NULL AUTO_INCREMENT,
  `supEs_suprimento` varchar(255) DEFAULT NULL,
  `supEs_estqMax` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`supEs_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_supestoque
#

LOCK TABLES `tbl_supestoque` WRITE;
/*!40000 ALTER TABLE `tbl_supestoque` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_supestoque` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_suprimentos
#

DROP TABLE IF EXISTS `tbl_suprimentos`;
CREATE TABLE `tbl_suprimentos` (
  `sup_cod` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`sup_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_suprimentos
#

LOCK TABLES `tbl_suprimentos` WRITE;
/*!40000 ALTER TABLE `tbl_suprimentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_suprimentos` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_supsaída
#

DROP TABLE IF EXISTS `tbl_supsaída`;
CREATE TABLE `tbl_supsaída` (
  `supS_cod` int(11) NOT NULL AUTO_INCREMENT,
  `supS_qtdeSaida` varchar(255) DEFAULT NULL,
  `supS_impressora` varchar(255) DEFAULT NULL,
  `supS_solicitante` varchar(255) DEFAULT NULL,
  `supS_dataSaida` varchar(255) DEFAULT NULL,
  `supS_obs` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`supS_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_supsaída
#

LOCK TABLES `tbl_supsaída` WRITE;
/*!40000 ALTER TABLE `tbl_supsaída` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_supsaída` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_técnico
#

DROP TABLE IF EXISTS `tbl_técnico`;
CREATE TABLE `tbl_técnico` (
  `tec_cod` int(11) NOT NULL AUTO_INCREMENT,
  `tec_nome` varchar(255) DEFAULT NULL,
  `tec_formacao` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`tec_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_técnico
#

LOCK TABLES `tbl_técnico` WRITE;
/*!40000 ALTER TABLE `tbl_técnico` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_técnico` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tbl_usuário
#

DROP TABLE IF EXISTS `tbl_usuário`;
CREATE TABLE `tbl_usuário` (
  `usu_cod` int(11) NOT NULL AUTO_INCREMENT,
  `usu_usuario` varchar(255) DEFAULT NULL,
  `usu_senha` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`usu_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tbl_usuário
#

LOCK TABLES `tbl_usuário` WRITE;
/*!40000 ALTER TABLE `tbl_usuário` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_usuário` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tblclientes
#

DROP TABLE IF EXISTS `tblclientes`;
CREATE TABLE `tblclientes` (
  `cli_cod` int(11) NOT NULL AUTO_INCREMENT,
  `cli_nome` varchar(200) DEFAULT NULL,
  `cli_endereco` varchar(200) DEFAULT NULL,
  `cli_bairro` varchar(200) DEFAULT NULL,
  `cli_cpf` int(11) DEFAULT NULL,
  PRIMARY KEY (`cli_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table tblclientes
#

LOCK TABLES `tblclientes` WRITE;
/*!40000 ALTER TABLE `tblclientes` DISABLE KEYS */;
/*!40000 ALTER TABLE `tblclientes` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table usuario
#

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
  `usu_cod` int(11) NOT NULL AUTO_INCREMENT,
  `usu_nome` varchar(50) DEFAULT NULL,
  `usu_usuario` varchar(255) DEFAULT NULL,
  `usu_email` varchar(50) DEFAULT NULL,
  `usu_cpf` varchar(11) DEFAULT NULL,
  `usu_cidade` varchar(255) DEFAULT NULL,
  `usu_senha` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`usu_cod`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Dumping data for table usuario
#

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Thawanny Martins Dos Anjos Silva','ThataS2','thata@gmail.com','78914715912','Itumbiara','asdfghjkl');
INSERT INTO `usuario` VALUES (2,'Frederico Alixame Di Chiacchio','FRicks96','fredericoa.chiacchio@gmail.com','46698920886','Itumbiara','12345678');
INSERT INTO `usuario` VALUES (3,'Lucas Almeida Santos','Luaas','lucasalmeida@gmail.com','15975325846','Itumbiara','qwertyuiop');
INSERT INTO `usuario` VALUES (4,'Thawanny Martins D','Thata52','thata@gmail.com','78914715912','Itumbiara','12345678');
INSERT INTO `usuario` VALUES (5,'Frederico Alxaime Di','Fricks96','fredericoa.chiacchio','46588920886','Itumbiara','12345678');
INSERT INTO `usuario` VALUES (6,'Lucas Almeida Sant','Luuas','lucasalmeida@gmail','15975325846','Itumbiara','qwertyuiop');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
