-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 12, 2024 at 01:22 PM
-- Server version: 5.7.19
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pharma_info`
--

-- --------------------------------------------------------

--
-- Table structure for table `avail_med`
--

DROP TABLE IF EXISTS `avail_med`;
CREATE TABLE IF NOT EXISTS `avail_med` (
  `serial_number` int(11) NOT NULL AUTO_INCREMENT,
  `medicine_name` varchar(50) DEFAULT NULL,
  `rate` varchar(50) DEFAULT NULL,
  `avail_quant` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`serial_number`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `avail_med`
--

INSERT INTO `avail_med` (`serial_number`, `medicine_name`, `rate`, `avail_quant`) VALUES
(1, 'ACETAMINOPEN', '92', '100'),
(2, 'IBUPROFEN', '60', '80'),
(3, 'ASPIRIN', '78', '76'),
(4, 'AMOXICILLIN', '78', '74'),
(5, 'OMEPARAZOLE', '81', '94'),
(6, 'METFORMIN', '81', '88'),
(7, 'SIMVASTATIN', '98', '90'),
(8, 'LORATADINE', '38', '95'),
(9, 'DIPHENHYDRAMINE', '38', '95'),
(10, 'CETIRIZINE', '52', '98'),
(11, 'PREDNISONE', '72', '100'),
(12, 'LISINOPRIL', '62', '100'),
(13, 'RANITIDINE', '90', '99'),
(14, 'ALBUTEROL', '98', '100'),
(15, 'ATORVASTATINE', '48', '100');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
