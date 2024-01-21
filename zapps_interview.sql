-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.28-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for zapps_interview
CREATE DATABASE IF NOT EXISTS `zapps_interview` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `zapps_interview`;

-- Dumping structure for table zapps_interview.book_borrow
CREATE TABLE IF NOT EXISTS `book_borrow` (
  `idborrow` varchar(25) NOT NULL,
  `nama_peminjam` varchar(35) NOT NULL,
  `tanggal_pinjam` date NOT NULL,
  `deadline_pinjam` date DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `isBorrow` tinyint(1) DEFAULT NULL,
  `nisn_book` varchar(25) NOT NULL,
  `userid` int(11) NOT NULL,
  `violation_type` int(11) DEFAULT NULL,
  PRIMARY KEY (`idborrow`),
  KEY `nisn_book` (`nisn_book`),
  KEY `userid` (`userid`),
  KEY `book_borrow_ibfk_3` (`violation_type`),
  CONSTRAINT `book_borrow_ibfk_1` FOREIGN KEY (`nisn_book`) REFERENCES `book_stock` (`isbn`),
  CONSTRAINT `book_borrow_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `users` (`id`),
  CONSTRAINT `book_borrow_ibfk_3` FOREIGN KEY (`violation_type`) REFERENCES `violation_type` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table zapps_interview.book_borrow: ~3 rows (approximately)
INSERT INTO `book_borrow` (`idborrow`, `nama_peminjam`, `tanggal_pinjam`, `deadline_pinjam`, `quantity`, `isBorrow`, `nisn_book`, `userid`, `violation_type`) VALUES
	('B000', 'Febby Fauziah', '2024-01-21', '2024-01-24', 0, 0, '777668146', 8, 0),
	('B001', 'Rudi Ahmadi', '2024-01-21', '2024-01-23', 0, 0, '777668146', 7, 3),
	('B002', 'Rudi Ahmadi', '2024-01-21', '2024-01-24', 0, 0, '777668146', 7, 1);

-- Dumping structure for table zapps_interview.book_return
CREATE TABLE IF NOT EXISTS `book_return` (
  `idreturn` varchar(25) NOT NULL,
  `nama_pengembali` varchar(35) NOT NULL,
  `tanggal_kembali` date DEFAULT NULL,
  `isReturn` tinyint(1) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `nisn_book` varchar(25) NOT NULL,
  `userid` int(11) NOT NULL,
  `borrow` varchar(25) NOT NULL,
  PRIMARY KEY (`idreturn`),
  KEY `nisn_book` (`nisn_book`),
  KEY `userid` (`userid`),
  KEY `book_return_ibfk_3` (`borrow`),
  CONSTRAINT `book_return_ibfk_1` FOREIGN KEY (`nisn_book`) REFERENCES `book_stock` (`isbn`),
  CONSTRAINT `book_return_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `users` (`id`),
  CONSTRAINT `book_return_ibfk_3` FOREIGN KEY (`borrow`) REFERENCES `book_borrow` (`idborrow`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table zapps_interview.book_return: ~1 rows (approximately)
INSERT INTO `book_return` (`idreturn`, `nama_pengembali`, `tanggal_kembali`, `isReturn`, `quantity`, `nisn_book`, `userid`, `borrow`) VALUES
	('R000', 'Febby Fauziah', '2024-01-21', 1, 2, '777668146', 8, 'B000');

-- Dumping structure for table zapps_interview.book_stock
CREATE TABLE IF NOT EXISTS `book_stock` (
  `isbn` varchar(25) NOT NULL,
  `bookname` varchar(255) NOT NULL,
  `author` varchar(50) NOT NULL,
  `penerbit` varchar(50) NOT NULL,
  `category` varchar(15) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` float NOT NULL,
  PRIMARY KEY (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table zapps_interview.book_stock: ~5 rows (approximately)
INSERT INTO `book_stock` (`isbn`, `bookname`, `author`, `penerbit`, `category`, `quantity`, `price`) VALUES
	('1234567', 'Top Gear', 'Marks Bob', 'Auto', 'Automotive', 25, 55000),
	('609183768', 'Algoritma Pemrograman', 'Rinaldi Munir', 'Informatika', 'Pendidikan', 50, 35000),
	('7768103', 'Si cantik milik si pemberani', 'Aji Parama', 'Erlangga', 'dongeng', 20, 30000),
	('777668146', 'Rekayasa Pernagkat Lunak', 'Ridwan Hanif', 'Bina Informatika', 'Pendidikan', 48, 60000),
	('88661968', 'Akuntansi Dasar', 'Rina Oktaviani', 'Erlangga', 'Pendidikan', 40, 45000);

-- Dumping structure for table zapps_interview.book_violation
CREATE TABLE IF NOT EXISTS `book_violation` (
  `idviolation` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(35) NOT NULL,
  `biaya_denda` float NOT NULL,
  `quantity_denda` int(11) DEFAULT NULL,
  `borrowid` varchar(25) NOT NULL,
  `damged_level` int(11) DEFAULT NULL,
  `violationtypes` int(11) DEFAULT NULL,
  PRIMARY KEY (`idviolation`),
  KEY `book_violation_ibfk_1` (`borrowid`),
  KEY `book_violation_ibfk_2` (`damged_level`),
  KEY `book_violation_ibfk_3` (`violationtypes`),
  CONSTRAINT `book_violation_ibfk_1` FOREIGN KEY (`borrowid`) REFERENCES `book_borrow` (`idborrow`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `book_violation_ibfk_2` FOREIGN KEY (`damged_level`) REFERENCES `damage_level` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `book_violation_ibfk_3` FOREIGN KEY (`violationtypes`) REFERENCES `violation_type` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table zapps_interview.book_violation: ~2 rows (approximately)
INSERT INTO `book_violation` (`idviolation`, `nama`, `biaya_denda`, `quantity_denda`, `borrowid`, `damged_level`, `violationtypes`) VALUES
	(20, 'Rudi Ahmadi', 60000, 1, 'B001', NULL, 3),
	(21, 'Rudi Ahmadi', 36000, 1, 'B002', NULL, 1);

-- Dumping structure for table zapps_interview.damage_level
CREATE TABLE IF NOT EXISTS `damage_level` (
  `id` int(11) NOT NULL,
  `description` varchar(10) NOT NULL,
  `charged` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table zapps_interview.damage_level: ~4 rows (approximately)
INSERT INTO `damage_level` (`id`, `description`, `charged`) VALUES
	(0, 'Buku Hilan', 0),
	(1, 'Kecil', 0.8),
	(2, 'Sedang', 0.4),
	(3, 'Besar', 0.1);

-- Dumping structure for table zapps_interview.detail_users
CREATE TABLE IF NOT EXISTS `detail_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(25) NOT NULL,
  `adress` varchar(30) NOT NULL,
  `city` varchar(15) NOT NULL,
  `telephone` varchar(25) DEFAULT NULL,
  `usersid` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usersid` (`usersid`),
  CONSTRAINT `detail_users_ibfk_1` FOREIGN KEY (`usersid`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table zapps_interview.detail_users: ~2 rows (approximately)
INSERT INTO `detail_users` (`id`, `fullname`, `adress`, `city`, `telephone`, `usersid`) VALUES
	(1, 'Dita saraswati', 'JL Jati jajar 25 ', 'Depok', '087818696967', 5),
	(2, 'Dina Anjani', 'JL Jati jajar 25 ', 'Depok', '087818696967', 4);

-- Dumping structure for table zapps_interview.loggedusers
CREATE TABLE IF NOT EXISTS `loggedusers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `loggedin` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `loggedout` timestamp NULL DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userid` (`userid`),
  CONSTRAINT `loggedusers_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table zapps_interview.loggedusers: ~0 rows (approximately)

-- Dumping structure for table zapps_interview.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(25) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usertype` (`usertype`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`usertype`) REFERENCES `usertype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table zapps_interview.users: ~6 rows (approximately)
INSERT INTO `users` (`id`, `email`, `username`, `password`, `usertype`) VALUES
	(4, NULL, 'superadmin', '827ccb0eea8a706c4c34a16891f84e7b', 1),
	(5, 'ditasaras@gmail.com', 'staff', '827ccb0eea8a706c4c34a16891f84e7b', 2),
	(6, 'ramaparama9@gmail.com', 'ajiparamab', 'f1568dcd119893b46cdb7a527c0b0aa2', 3),
	(7, 'rudiahm@gmail.com', 'rudiahmadi', '7689f4e29db4a9dc7356cda3863d70c4', 3),
	(8, NULL, 'fbbyfauziah', '9768d23fca10303dd069a620fbc64d98', 3),
	(9, NULL, 'suryandarum', 'e184ae61160460ec94624cb9ed102da5', 3);

-- Dumping structure for table zapps_interview.usertype
CREATE TABLE IF NOT EXISTS `usertype` (
  `id` int(11) NOT NULL,
  `description` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table zapps_interview.usertype: ~2 rows (approximately)
INSERT INTO `usertype` (`id`, `description`) VALUES
	(1, 'superadmin'),
	(2, 'staff'),
	(3, 'member');

-- Dumping structure for table zapps_interview.violation_type
CREATE TABLE IF NOT EXISTS `violation_type` (
  `id` int(11) NOT NULL,
  `description` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table zapps_interview.violation_type: ~3 rows (approximately)
INSERT INTO `violation_type` (`id`, `description`) VALUES
	(0, 'bagus'),
	(1, 'rusak'),
	(2, 'telat'),
	(3, 'hilang');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
