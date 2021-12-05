-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-12-2021 a las 07:51:51
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `reto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `Documento` varchar(15) NOT NULL,
  `Nombres` varchar(60) NOT NULL,
  `Apellidos` varchar(60) NOT NULL,
  `Edad` int(11) DEFAULT NULL,
  `Dirección` varchar(100) DEFAULT NULL,
  `Sexo` varchar(20) DEFAULT NULL,
  `Peso` int(11) NOT NULL,
  `Estatura` int(11) NOT NULL,
  `Fumador` varchar(5) NOT NULL,
  `dieta` varchar(5) NOT NULL,
  `PesoEstatura` int(11) NOT NULL,
  `Estado` varchar(20) NOT NULL,
  `Prioridad` varchar(10) NOT NULL,
  `Riesgo` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`Documento`, `Nombres`, `Apellidos`, `Edad`, `Dirección`, `Sexo`, `Peso`, `Estatura`, `Fumador`, `dieta`, `PesoEstatura`, `Estado`, `Prioridad`, `Riesgo`) VALUES
('091274932472', 'Calros Andres', 'Padilla', 60, 'Fuquene', 'Masculino', 70, 175, '10', 'Si', 2, 'Pendiente', '7', 9.5),
('123456789', 'Juan David', 'Paez Forero', 27, 'Fuquene', 'Masculino', 70, 175, 'no', 'Si', 2, 'Atendido', '2', 0.54),
('43432212312', 'Calros Andres', 'Paez Forero', 32, 'Fuquene', 'Masculino', 65, 150, 'No', 'No', 2, 'Pendiente', '2', 0.64),
('543543432423', 'Marco Antonio', 'Padilla', 27, 'Fuquene', 'Masculino', 50, 150, 'No', 'No', 2, 'Pendiente', '2', 0.54),
('74423222', 'Calros Andres', 'Padilla', 32, 'Fuquene', 'Masculino', 50, 150, '5', 'No', 2, 'Atendido', '3.25', 1.04);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`Documento`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
