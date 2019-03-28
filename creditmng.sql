-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 15, 2019 at 07:43 PM
-- Server version: 5.1.36
-- PHP Version: 5.3.0


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `creditmng`
--

-- --------------------------------------------------------

--
-- Table structure for table `trans`
--

CREATE TABLE IF NOT EXISTS `trans` (
  `uaccno1` varchar(100) NOT NULL,
  `uaccno2` varchar(100) NOT NULL,
  `ucredit` int(10) NOT NULL,
  `tdate` date NOT NULL
) TYPE=MyISAM;

--
-- Dumping data for table `trans`
--

INSERT INTO `trans` (`uaccno1`, `uaccno2`, `ucredit`, `tdate`) VALUES
('GRIP000222', 'GRIP000013', 50, '2019-03-09');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `uid` int(10) NOT NULL,
  `unm` varchar(50) NOT NULL,
  `uemail` varchar(100) NOT NULL,
  `udob` date NOT NULL,
  `uadd` varchar(100) NOT NULL,
  `ucredit` int(10) NOT NULL DEFAULT '0',
  `uaccno` varchar(50) NOT NULL,
  PRIMARY KEY (`uaccno`),
  UNIQUE KEY `uaccno` (`uaccno`),
  UNIQUE KEY `uaccno_2` (`uaccno`),
  UNIQUE KEY `uaccno_3` (`uaccno`)
) TYPE=MyISAM ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`uid`, `unm`, `uemail`, `udob`, `uadd`, `ucredit`, `uaccno`) VALUES
(1, 'harsh mahajan', 'harshmahajan95@gmail.com', '1995-03-14', 'vaishali nagar, near bada bazaar, indore', 3000, 'GRIP000001'),
(2, 'rahul jain', 'jain93@yahoo.com', '1994-10-17', 'vijay nagar chennai', 4000, 'GRIP000123'),
(3, 'vishesh nakul', 'nakul12345@gmail.com', '1997-03-10', 'imam bada, vadodra', 12000, 'GRIP000012'),
(4, 'mahesh agnihotri', 'agnihotri121@gmail.com', '1994-03-07', '53-B raja colony jalgaon', 3500, 'GRIP000312'),
(5, 'venkat bsr', 'venkatbsr111@yahoo.com', '1995-06-27', 't. nagar chennai', 5900, 'GRIP000124'),
(6, 'lalit bhagat', 'bhagat98@gmail.com', '1997-08-14', 'sentax colony khandwa', 5500, 'GRIP000222'),
(7, 'shubham mali', 'shubham121198@gmail.com', '1998-11-12', 'phool bazaar khandwa', 6910, 'GRIP000223'),
(8, 'anoop bhawalkar', 'pawni141211@gmail.com', '1994-01-25', 'limbodi indore', 9590, 'GRIP000002'),
(9, 'chetan joshi', 'chetanjoshi97@yahoo.com', '1995-09-21', 'central colony vadodra', 7050, 'GRIP000013'),
(10, 'girish barkale', 'girish97@gmail.com', '1994-12-13', 'koliwada jalgaon', 9820, 'GRIP000313');
