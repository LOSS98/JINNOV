DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(80) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(128) NOT NULL,
  `salt` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `membre`;
CREATE TABLE `membre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(80) NOT NULL,
  `first_name` varchar(80) NOT NULL,
  `last_name` varchar(80) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `pole` varchar(45) NOT NULL,
  `poste` varchar(45) NOT NULL,
  `picture_path` varchar(80) NOT NULL,
  `active` TINYINT,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` INT NOT NULL,
  `created_by` INT NOT NULL,
  `title` varchar(45) NOT NULL,
  `body` longtext NOT NULL,
  `image`longtext NOT NULL,
  `attachements` longtext,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`created_by`) REFERENCES `membre` (`id`)
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `etude`;
CREATE TABLE `etude` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` INT NOT NULL,
  `created_by` INT NOT NULL,
  `customer_name` varchar(80) NOT NULL,
  `customer_link` varchar(80) NOT NULL,
  `body` longtext NOT NULL,
<<<<<<< HEAD
=======
  `image`longtext NOT NULL,
  `attachements` longtext,
>>>>>>> origin/feat-6
  PRIMARY KEY (`id`),
  FOREIGN KEY (`created_by`) REFERENCES `membre` (`id`)
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `user_path`;
CREATE TABLE `user_path` (
  `id` int NOT NULL AUTO_INCREMENT,
  `session_id` varchar(45) NOT NULL,
  `start_date` INT NOT NULL,
  `end_date` INT NOT NULL,
  `page` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4;
