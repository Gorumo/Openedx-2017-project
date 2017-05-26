-- mysql -u root -p CCDB < CCDB.sql

CREATE DATABASE IF NOT EXISTS `CCDB` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `CCDB`;


-- Структура таблицы `Concepts`
--

CREATE TABLE IF NOT EXISTS `Concepts` (
  `concept_id` int(10) NOT NULL AUTO_INCREMENT,
  `concept_URI` varchar(120) CHARACTER SET latin1 NOT NULL,
  `field_id` int(10) NOT NULL,
  `concept_label` varchar(120) CHARACTER SET latin1 NOT NULL,
  `concept_description` varchar(250) CHARACTER SET latin1 NOT NULL,
  PRIMARY KEY (`concept_id`),
  UNIQUE KEY `concept_id` (`concept_id`),
  UNIQUE KEY `concept_label` (`concept_label`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `Concept_Content_Manager`
--

CREATE TABLE IF NOT EXISTS `Concept_Content_Manager` (
  `id_m` int(10) NOT NULL AUTO_INCREMENT,
  `block_id` int(10) NOT NULL DEFAULT '0',
  `concept_id` int(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_m`),
  UNIQUE KEY `id_m` (`id_m`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `Fields`
--

CREATE TABLE IF NOT EXISTS `Fields` (
  `field_id` int(10) NOT NULL AUTO_INCREMENT,
  `field_label` varchar(120) CHARACTER SET latin1 NOT NULL,
  PRIMARY KEY (`field_id`),
  UNIQUE KEY `field_id` (`field_id`),
  UNIQUE KEY `field_label` (`field_label`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

