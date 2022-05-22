-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 22, 2022 at 04:26 PM
-- Server version: 10.3.34-MariaDB-0ubuntu0.20.04.1
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask_site1`
--

-- --------------------------------------------------------

--
-- Table structure for table `cursuri`
--

CREATE TABLE `cursuri` (
  `id` int(11) NOT NULL,
  `id_materie` int(11) NOT NULL,
  `id_student` int(11) NOT NULL,
  `data` date NOT NULL,
  `ora` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cursuri`
--

INSERT INTO `cursuri` (`id`, `id_materie`, `id_student`, `data`, `ora`) VALUES
(1, 1, 1, '2022-05-16', '09:00:00'),
(2, 1, 2, '2022-05-16', '09:00:00'),
(3, 1, 1, '2022-05-16', '09:00:00'),
(4, 2, 2, '2022-05-16', '10:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `materii`
--

CREATE TABLE `materii` (
  `id` int(11) NOT NULL,
  `nume` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `materii`
--

INSERT INTO `materii` (`id`, `nume`) VALUES
(1, 'Matematica'),
(2, 'Fizica'),
(3, 'Informatica'),
(4, 'Istorie');

-- --------------------------------------------------------

--
-- Table structure for table `studenti`
--

CREATE TABLE `studenti` (
  `id` int(11) NOT NULL,
  `nume` varchar(45) NOT NULL,
  `prenume` varchar(45) NOT NULL,
  `comentarii` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studenti`
--

INSERT INTO `studenti` (`id`, `nume`, `prenume`, `comentarii`) VALUES
(1, 'Ionescu', 'Ion', 'Comentariu Ionescu Ion'),
(2, 'Georgescu', 'George', '*********'),
(3, 'Popescu', 'Petre', ''),
(4, 'Dumitrescu', 'Dumitru', ''),
(5, 'Mihaila', 'Mihai', ''),
(6, 'Nicolaescu', 'Nicolae', ''),
(7, 'Radulescu', 'Radu', 'rrrrr');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cursuri`
--
ALTER TABLE `cursuri`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_curs` (`id_materie`),
  ADD KEY `id_student` (`id_student`);

--
-- Indexes for table `materii`
--
ALTER TABLE `materii`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `studenti`
--
ALTER TABLE `studenti`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cursuri`
--
ALTER TABLE `cursuri`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `materii`
--
ALTER TABLE `materii`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `studenti`
--
ALTER TABLE `studenti`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cursuri`
--
ALTER TABLE `cursuri`
  ADD CONSTRAINT `cursuri_ibfk_1` FOREIGN KEY (`id_materie`) REFERENCES `materii` (`id`),
  ADD CONSTRAINT `cursuri_ibfk_2` FOREIGN KEY (`id_student`) REFERENCES `studenti` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
