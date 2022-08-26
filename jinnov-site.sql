DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(80) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(128) NOT NULL,
  `salt` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL,
  `created_by` INT NOT NULL,
  `title` varchar(45) NOT NULL,
  `body` longtext NOT NULL,
  `attachements` longtext,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`created_by`) REFERENCES `admin` (`id`)
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `etude`;
CREATE TABLE `etude` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL,
  `customer_name` varchar(80) NOT NULL,
  `customer_link` varchar(80) NOT NULL,
  `body` longtext NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `membre`;
CREATE TABLE `membre` (
  `email` varchar(80) NOT NULL,
  `first_name` varchar(80) NOT NULL,
  `last_name` varchar(80) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `pole` varchar(45) NOT NULL,
  `poste` varchar(45) NOT NULL,
  `picture_path` varchar(80) NOT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `first_name_UNIQUE` (`first_name`),
  UNIQUE KEY `last_name_UNIQUE` (`last_name`),
  UNIQUE KEY `phone_number_UNIQUE` (`phone_number`),
  UNIQUE KEY `picture_path_UNIQUE` (`picture_path`)
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `user_path`;
CREATE TABLE `user_path` (
  `id` int NOT NULL AUTO_INCREMENT,
  `session_id` varchar(45) NOT NULL,
  `start_date` INT NOT NULL,
  `end_date` INT,
  `page` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4;
