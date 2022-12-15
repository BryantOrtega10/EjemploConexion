-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-11-2022 a las 01:10:07
-- Versión del servidor: 10.4.13-MariaDB
-- Versión de PHP: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rotonda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `adicion`
--

CREATE TABLE `adicion` (
  `id_adicion` bigint(20) UNSIGNED NOT NULL,
  `cantidad` float DEFAULT NULL,
  `fk_ingrediente` bigint(20) UNSIGNED NOT NULL,
  `maximo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `adicion`
--

INSERT INTO `adicion` (`id_adicion`, `cantidad`, `fk_ingrediente`, `maximo`) VALUES
(101, 1, 101, 10),
(213, 1, 13, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `admin_tecnico`
--

CREATE TABLE `admin_tecnico` (
  `id_admin_tecnico` bigint(20) UNSIGNED NOT NULL,
  `documento` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `apellido` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `fk_usuario` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `admin_tecnico`
--

INSERT INTO `admin_tecnico` (`id_admin_tecnico`, `documento`, `nombre`, `apellido`, `email`, `fk_usuario`) VALUES
(1, 'A111111111', 'TECNICO', 'NUMERO 1', 'tecnico1@correo.com', 9),
(2, 'B22222222', 'TECNICO', 'NUMERO DOS', 'tecnico2@correo.com', 10),
(3, 'C33333333', 'TECNICO', 'NUMERO TRES', 'tecnico2@correo.com', 11),
(4, 'D44444444', 'TECNICO', 'NUMERO CUATRO', 'tecnico2@correo.com', 12),
(5, 'E55555555', 'TECNICO', 'NUMERO CINCO', 'tecnico2@correo.com', 13);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

CREATE TABLE `carrito` (
  `id_carrito` bigint(20) UNSIGNED NOT NULL,
  `sub_total` bigint(20) UNSIGNED NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `fecha_finalizacion` timestamp NULL DEFAULT NULL,
  `estado` tinyint(3) UNSIGNED NOT NULL DEFAULT 0,
  `fk_cliente` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `carrito`
--

INSERT INTO `carrito` (`id_carrito`, `sub_total`, `fecha_creacion`, `fecha_finalizacion`, `estado`, `fk_cliente`) VALUES
(1, 21000, '2022-10-28 16:53:29', '2022-10-27 15:51:21', 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` bigint(20) UNSIGNED NOT NULL,
  `documento` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `apellido` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `foto` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `direccion` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `fk_usuario` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `documento`, `nombre`, `apellido`, `foto`, `direccion`, `email`, `fk_usuario`) VALUES
(1, '1022397291', 'Bryant', 'Ortega', 'rutafoto.jpg', 'Calle de prueba 1234 # 123 - 45', 'bdortegav@correo.udistrital.edu.co', 1),
(2, '20191020025', 'David', 'Veloza', 'rutafoto.jpg', 'Calle de prueba 1234 # 123 - 45', 'bryant.ortega@gmail.com', 2),
(3, '20191020038', 'Oscar', 'Rojas', 'rutafoto.jpg', 'Calle de prueba 4321 # 432 - 11', 'correooscar@correo.com', 3),
(4, '20191020040', 'Daniel', 'Garay', 'rutafoto.jpg', 'Calle de prueba 8910 # 1213 - 11', 'correo_prueba1@correo.com', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horario`
--

CREATE TABLE `horario` (
  `id_horario` bigint(20) UNSIGNED NOT NULL,
  `dia` tinyint(4) DEFAULT NULL COMMENT 'Dias de la semana con 0 como domingo y 6 como sabado',
  `hora_inicio` tinyint(4) DEFAULT NULL,
  `minuto_inicio` tinyint(4) DEFAULT NULL,
  `hora_fin` tinyint(4) DEFAULT NULL,
  `minuto_fin` tinyint(4) DEFAULT NULL,
  `fk_restaurante` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `horario`
--

INSERT INTO `horario` (`id_horario`, `dia`, `hora_inicio`, `minuto_inicio`, `hora_fin`, `minuto_fin`, `fk_restaurante`) VALUES
(1, 0, 10, 0, 20, 0, 2),
(3, 1, 10, 0, 20, 0, 2),
(4, 2, 10, 0, 20, 0, 2),
(5, 3, 10, 0, 20, 0, 2),
(6, 4, 10, 0, 20, 0, 2),
(7, 5, 10, 0, 20, 0, 2),
(8, 6, 10, 0, 20, 0, 2),
(9, 0, 12, 0, 22, 0, 1),
(10, 1, 9, 0, 20, 0, 1),
(11, 2, 9, 0, 20, 0, 1),
(12, 3, 9, 0, 20, 0, 1),
(13, 4, 9, 0, 20, 0, 1),
(14, 5, 9, 0, 20, 0, 1),
(15, 6, 12, 0, 22, 0, 1),
(16, 0, 11, 0, 22, 0, 3),
(17, 1, 11, 0, 19, 0, 3),
(18, 2, 11, 0, 19, 0, 3),
(19, 3, 11, 0, 19, 0, 3),
(20, 4, 11, 0, 19, 0, 3),
(21, 5, 11, 0, 19, 0, 3),
(22, 6, 11, 0, 22, 0, 3),
(23, 0, 11, 0, 21, 0, 4),
(24, 1, 11, 0, 21, 0, 4),
(25, 2, 11, 0, 21, 0, 4),
(27, 1, 12, 0, 22, 60, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingrediente`
--

CREATE TABLE `ingrediente` (
  `id_ingrediente` bigint(20) UNSIGNED NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `foto` varchar(200) NOT NULL,
  `und_medida` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `ingrediente`
--

INSERT INTO `ingrediente` (`id_ingrediente`, `nombre`, `foto`, `und_medida`) VALUES
(1, 'pan', 'workinprogress', 'unidad'),
(2, 'queso', 'workinprogress', 'gramos'),
(3, 'carne', 'workinprogress', 'gramos'),
(4, 'tomate', 'workinprogress', 'gramos'),
(5, 'cebolla', 'workinprogress', 'gramos'),
(6, 'lechuga', 'workinprogress', 'gramos'),
(7, 'ketchup', 'workinprogress', 'gramos'),
(8, 'mayonesa', 'workinprogress', 'gramos'),
(9, 'mostaza', 'workinprogress', 'gramos'),
(10, 'papas', 'workinprogress', 'gramos'),
(11, 'coca-cola', 'workinprogress', 'gramos'),
(12, 'pollo', 'workinprogress', 'gramos'),
(13, 'tocineta', 'workinprogress', 'gramos'),
(14, 'pepinillos', 'workinprogress', 'gramos'),
(100, 'PASTA', 'pasta.jpg', 'gr'),
(101, 'ALBONDIGA', 'albondiga.jpg', 'unidad'),
(102, 'SALSA BOLOÑESA', 'albondiga.jpg', 'gr'),
(103, 'GASEOSA MANZANA POSTOBON 200ML', 'gaseosaManzana200.png', 'unidad'),
(104, 'GASEOSA PEPSI 200ML', 'gaseosaPepsi200.png', 'unidad'),
(105, 'GASEOSA COLOMBIANA POSTOBON 200ML', 'gaseosaColombiana200.png', 'unidad'),
(106, 'Patacones', 'reunion_14.png', 'Unidad');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingrediente_base`
--

CREATE TABLE `ingrediente_base` (
  `id_ingrediente_base` bigint(20) UNSIGNED NOT NULL,
  `cantidad` float DEFAULT NULL,
  `fk_ingrediente` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `ingrediente_base`
--

INSERT INTO `ingrediente_base` (`id_ingrediente_base`, `cantidad`, `fk_ingrediente`) VALUES
(1, 2, 1),
(2, 1, 2),
(4, 1, 4),
(7, 1, 7),
(8, 1, 8),
(101, 500, 100),
(102, 3, 101),
(103, 20, 102),
(104, 1, 103),
(105, 1, 104),
(106, 1, 105),
(203, 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingrediente_cambio`
--

CREATE TABLE `ingrediente_cambio` (
  `fk_ingrediente_base` bigint(20) UNSIGNED NOT NULL,
  `fk_ingrediente_cambio` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `ingrediente_cambio`
--

INSERT INTO `ingrediente_cambio` (`fk_ingrediente_base`, `fk_ingrediente_cambio`) VALUES
(2, 2),
(4, 4),
(7, 7),
(8, 8),
(104, 105),
(104, 106);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `item_carrito`
--

CREATE TABLE `item_carrito` (
  `id_item_carrito` bigint(20) UNSIGNED NOT NULL,
  `fk_carrito` bigint(20) UNSIGNED NOT NULL,
  `fk_menu` bigint(20) UNSIGNED NOT NULL,
  `fk_sede` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `item_carrito`
--

INSERT INTO `item_carrito` (`id_item_carrito`, `fk_carrito`, `fk_menu`, `fk_sede`) VALUES
(2001, 1, 1011, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `item_carrito_adicion`
--

CREATE TABLE `item_carrito_adicion` (
  `fk_item_carrito` bigint(20) UNSIGNED NOT NULL,
  `fk_adicion` bigint(20) UNSIGNED NOT NULL,
  `fk_producto` bigint(20) UNSIGNED NOT NULL,
  `cantidad` float NOT NULL,
  `precio` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `item_carrito_adicion`
--

INSERT INTO `item_carrito_adicion` (`fk_item_carrito`, `fk_adicion`, `fk_producto`, `cantidad`, `precio`) VALUES
(2001, 101, 101, 1, 1200);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `item_carrito_ingrediente_base`
--

CREATE TABLE `item_carrito_ingrediente_base` (
  `fk_item_carrito` bigint(20) UNSIGNED NOT NULL,
  `fk_ingrediente_base` bigint(20) UNSIGNED NOT NULL,
  `fk_producto` bigint(20) UNSIGNED NOT NULL,
  `cantidad` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `item_carrito_ingrediente_base`
--

INSERT INTO `item_carrito_ingrediente_base` (`fk_item_carrito`, `fk_ingrediente_base`, `fk_producto`, `cantidad`) VALUES
(2001, 1, 1003, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `item_carrito_producto`
--

CREATE TABLE `item_carrito_producto` (
  `fk_item_carrito` bigint(20) UNSIGNED NOT NULL,
  `fk_producto` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `menu`
--

CREATE TABLE `menu` (
  `id_menu` bigint(20) UNSIGNED NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `foto` varchar(200) NOT NULL,
  `precio` bigint(20) NOT NULL,
  `fk_restaurante` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `menu`
--

INSERT INTO `menu` (`id_menu`, `nombre`, `foto`, `precio`, `fk_restaurante`) VALUES
(101, 'COMBO PASTA BOLOÑESA', 'comboPastaBoloniesa.png', 22000, 3),
(1011, 'COMBO MCCOMBO', 'combomccombo.png', 25000, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `menu_producto`
--

CREATE TABLE `menu_producto` (
  `fk_menu` bigint(20) UNSIGNED NOT NULL,
  `fk_producto` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `menu_producto`
--

INSERT INTO `menu_producto` (`fk_menu`, `fk_producto`) VALUES
(101, 101),
(101, 102),
(1011, 1003);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE `pedido` (
  `idpedido` int(11) NOT NULL,
  `estado` tinyint(3) UNSIGNED NOT NULL DEFAULT 0 COMMENT '0 - Creado, 1 - En proceso de pago, 2- Pagado, 3- Cancelado',
  `metodo_pago` tinyint(4) NOT NULL DEFAULT 0,
  `total` bigint(20) UNSIGNED NOT NULL,
  `fk_carrito` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `pedido`
--

INSERT INTO `pedido` (`idpedido`, `estado`, `metodo_pago`, `total`, `fk_carrito`) VALUES
(91, 2, 0, 21000, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id_producto` bigint(20) UNSIGNED NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `precio` bigint(20) NOT NULL,
  `tipo` tinyint(3) UNSIGNED NOT NULL COMMENT '0- Entrada\n1- Plato Fuerte\n2- Postres\n3- Bebidas\n4- Acompañamientos',
  `foto` varchar(200) NOT NULL,
  `maximo_ingredientes_base` int(10) UNSIGNED NOT NULL,
  `aplica_maximo` tinyint(3) UNSIGNED NOT NULL COMMENT 'Campo estilo booleano',
  `minimo_ingredientes_base` int(10) UNSIGNED NOT NULL,
  `aplica_minimo` tinyint(3) UNSIGNED NOT NULL COMMENT 'Campo como boolean',
  `fk_restaurante` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id_producto`, `nombre`, `precio`, `tipo`, `foto`, `maximo_ingredientes_base`, `aplica_maximo`, `minimo_ingredientes_base`, `aplica_minimo`, `fk_restaurante`) VALUES
(101, 'PASTA BOLOÑESA', 20000, 1, 'pastaBoloniesa.jpg', 0, 0, 0, 0, 3),
(102, 'GASEOSA MANZANA 200 ML', 2500, 3, 'gaseosaManzana200.jpg', 0, 0, 0, 0, 3),
(1003, 'HAMBURGUESA MCNIFICA', 28000, 1, 'mcnifica.jpg', 9, 1, 2, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto_adicion`
--

CREATE TABLE `producto_adicion` (
  `fk_producto` bigint(20) UNSIGNED NOT NULL,
  `fk_adicion` bigint(20) UNSIGNED NOT NULL,
  `precio` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `producto_adicion`
--

INSERT INTO `producto_adicion` (`fk_producto`, `fk_adicion`, `precio`) VALUES
(101, 101, 5000),
(101, 213, 9900),
(1003, 213, 18000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto_ingrediente_base`
--

CREATE TABLE `producto_ingrediente_base` (
  `fk_producto` bigint(20) UNSIGNED NOT NULL,
  `fk_ingrediente_base` bigint(20) UNSIGNED NOT NULL,
  `auto_select` tinyint(4) NOT NULL COMMENT 'Cambio tipo booleano'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `producto_ingrediente_base`
--

INSERT INTO `producto_ingrediente_base` (`fk_producto`, `fk_ingrediente_base`, `auto_select`) VALUES
(101, 101, 1),
(101, 102, 1),
(101, 103, 1),
(1003, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `restaurante`
--

CREATE TABLE `restaurante` (
  `id_restaurante` bigint(20) UNSIGNED NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `logo` varchar(200) DEFAULT NULL,
  `en_servicio` tinyint(4) NOT NULL COMMENT 'Funciona como booleano 1 o 0',
  `especialidad` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `restaurante`
--

INSERT INTO `restaurante` (`id_restaurante`, `nombre`, `logo`, `en_servicio`, `especialidad`) VALUES
(1, 'MC DONALS', 'mcdonals.jpg', 0, 'HAMBURGUESAS'),
(2, 'EL CORRAL', 'elcorra.jpg', 0, 'HAMBURGUESAS'),
(3, 'SPOLLETO', 'spolleto.jpg', 0, 'PASTAS'),
(4, 'QBANO', 'qbano.jpg', 0, 'SANDWICH');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sede`
--

CREATE TABLE `sede` (
  `id_sede` bigint(20) UNSIGNED NOT NULL,
  `fk_restaurante` bigint(20) UNSIGNED NOT NULL,
  `fk_usuario` bigint(20) UNSIGNED NOT NULL,
  `direccion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `sede`
--

INSERT INTO `sede` (`id_sede`, `fk_restaurante`, `fk_usuario`, `direccion`) VALUES
(1, 1, 5, 'Calle 1 # 1 - 1'),
(2, 2, 6, 'Calle 2 # 2 - 2'),
(4, 1, 8, 'Calle 4 # 4 - 4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sede_ingrediente`
--

CREATE TABLE `sede_ingrediente` (
  `fk_sede` bigint(20) UNSIGNED NOT NULL,
  `fk_ingrediente` bigint(20) UNSIGNED NOT NULL,
  `stock` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `sede_ingrediente`
--

INSERT INTO `sede_ingrediente` (`fk_sede`, `fk_ingrediente`, `stock`) VALUES
(1, 13, 20);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` bigint(20) UNSIGNED NOT NULL,
  `user` varchar(100) NOT NULL COMMENT 'El usuario puede ser el correo electronico o uno asignado',
  `password` blob NOT NULL,
  `rol` tinyint(3) UNSIGNED NOT NULL COMMENT 'Puede adquirir los valores de: 1- SuperAdmin, 2- Administrador CCD, 3- Restaurante, 4- Cliente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `user`, `password`, `rol`) VALUES
(1, 'cliente_p1', 0x052a25a2c8c1193f69c288a9ae8b6e89, 4),
(2, 'cliente_p2', 0x052a25a2c8c1193f69c288a9ae8b6e89, 4),
(3, 'cliente_p3', 0x052a25a2c8c1193f69c288a9ae8b6e89, 4),
(4, 'cliente_p4', 0x052a25a2c8c1193f69c288a9ae8b6e89, 4),
(5, 'restaurante_p5', 0x052a25a2c8c1193f69c288a9ae8b6e89, 3),
(6, 'restaurante_p6', 0x052a25a2c8c1193f69c288a9ae8b6e89, 3),
(7, 'restaurante_p7', 0x052a25a2c8c1193f69c288a9ae8b6e89, 3),
(8, 'restaurante_p8', 0x052a25a2c8c1193f69c288a9ae8b6e89, 3),
(9, 'admin_p9', 0x052a25a2c8c1193f69c288a9ae8b6e89, 2),
(10, 'admin_p10', 0x052a25a2c8c1193f69c288a9ae8b6e89, 2),
(11, 'admin_p11', 0x052a25a2c8c1193f69c288a9ae8b6e89, 2),
(12, 'admin_p12', 0x052a25a2c8c1193f69c288a9ae8b6e89, 2),
(13, 'admin_p13', 0x052a25a2c8c1193f69c288a9ae8b6e89, 2),
(14, 'superadmin_p14', 0x052a25a2c8c1193f69c288a9ae8b6e89, 1),
(15, 'cliente_p5', 0x032a25a1c8c1193f69c287a9ae8b6e89, 4);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `adicion`
--
ALTER TABLE `adicion`
  ADD PRIMARY KEY (`id_adicion`),
  ADD UNIQUE KEY `id_adicion_UNIQUE` (`id_adicion`),
  ADD KEY `fk_ingrediente_base_ingrediente1_idx` (`fk_ingrediente`);

--
-- Indices de la tabla `admin_tecnico`
--
ALTER TABLE `admin_tecnico`
  ADD PRIMARY KEY (`id_admin_tecnico`),
  ADD UNIQUE KEY `idAdminTecnico_UNIQUE` (`id_admin_tecnico`),
  ADD UNIQUE KEY `fk_usuario_UNIQUE` (`fk_usuario`),
  ADD KEY `fk_admin_tecnico_usuario1_idx` (`fk_usuario`);

--
-- Indices de la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD PRIMARY KEY (`id_carrito`),
  ADD UNIQUE KEY `id_carrito_UNIQUE` (`id_carrito`),
  ADD KEY `fk_carrito_cliente1_idx` (`fk_cliente`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id_cliente`),
  ADD UNIQUE KEY `idcliente_UNIQUE` (`id_cliente`),
  ADD UNIQUE KEY `documento_UNIQUE` (`documento`),
  ADD UNIQUE KEY `fk_usuario_UNIQUE` (`fk_usuario`),
  ADD KEY `fk_cliente_usuario_idx` (`fk_usuario`);

--
-- Indices de la tabla `horario`
--
ALTER TABLE `horario`
  ADD PRIMARY KEY (`id_horario`),
  ADD UNIQUE KEY `id_horario_UNIQUE` (`id_horario`),
  ADD KEY `fk_horario_restaurante1_idx` (`fk_restaurante`);

--
-- Indices de la tabla `ingrediente`
--
ALTER TABLE `ingrediente`
  ADD PRIMARY KEY (`id_ingrediente`),
  ADD UNIQUE KEY `id_ingrediente_UNIQUE` (`id_ingrediente`);

--
-- Indices de la tabla `ingrediente_base`
--
ALTER TABLE `ingrediente_base`
  ADD PRIMARY KEY (`id_ingrediente_base`),
  ADD UNIQUE KEY `id_ingrediente_base_UNIQUE` (`id_ingrediente_base`),
  ADD KEY `fk_ingrediente_base_ingrediente1_idx` (`fk_ingrediente`);

--
-- Indices de la tabla `ingrediente_cambio`
--
ALTER TABLE `ingrediente_cambio`
  ADD PRIMARY KEY (`fk_ingrediente_base`,`fk_ingrediente_cambio`),
  ADD KEY `fk_ingrediente_has_ingrediente_base_ingrediente_base1_idx` (`fk_ingrediente_base`),
  ADD KEY `fk_ingrediente_cambio_ingrediente_base1_idx` (`fk_ingrediente_cambio`);

--
-- Indices de la tabla `item_carrito`
--
ALTER TABLE `item_carrito`
  ADD PRIMARY KEY (`id_item_carrito`),
  ADD UNIQUE KEY `id_item_carrito_UNIQUE` (`id_item_carrito`),
  ADD KEY `fk_carrito_has_menu_menu1_idx` (`fk_menu`),
  ADD KEY `fk_carrito_has_menu_carrito1_idx` (`fk_carrito`),
  ADD KEY `fk_item_carrito_sede1_idx` (`fk_sede`);

--
-- Indices de la tabla `item_carrito_adicion`
--
ALTER TABLE `item_carrito_adicion`
  ADD PRIMARY KEY (`fk_item_carrito`,`fk_adicion`,`fk_producto`),
  ADD KEY `fk_item_carrito_has_adicion_adicion1_idx` (`fk_adicion`),
  ADD KEY `fk_item_carrito_has_adicion_item_carrito1_idx` (`fk_item_carrito`),
  ADD KEY `fk_item_carrito_adicion_producto1_idx` (`fk_producto`);

--
-- Indices de la tabla `item_carrito_ingrediente_base`
--
ALTER TABLE `item_carrito_ingrediente_base`
  ADD PRIMARY KEY (`fk_item_carrito`,`fk_ingrediente_base`,`fk_producto`),
  ADD KEY `fk_item_carrito_has_ingrediente_base_ingrediente_base1_idx` (`fk_ingrediente_base`),
  ADD KEY `fk_item_carrito_has_ingrediente_base_item_carrito1_idx` (`fk_item_carrito`),
  ADD KEY `fk_item_carrito_ingrediente_base_producto1_idx` (`fk_producto`);

--
-- Indices de la tabla `item_carrito_producto`
--
ALTER TABLE `item_carrito_producto`
  ADD PRIMARY KEY (`fk_item_carrito`,`fk_producto`),
  ADD KEY `fk_producto` (`fk_producto`);

--
-- Indices de la tabla `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id_menu`),
  ADD UNIQUE KEY `idmenu_UNIQUE` (`id_menu`),
  ADD KEY `fk_menu_restaurante1_idx` (`fk_restaurante`);

--
-- Indices de la tabla `menu_producto`
--
ALTER TABLE `menu_producto`
  ADD PRIMARY KEY (`fk_menu`,`fk_producto`),
  ADD KEY `fk_menu_has_producto_producto1_idx` (`fk_producto`),
  ADD KEY `fk_menu_has_producto_menu1_idx` (`fk_menu`);

--
-- Indices de la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`idpedido`),
  ADD UNIQUE KEY `carrito_id_carrito_UNIQUE` (`fk_carrito`),
  ADD KEY `fk_pedido_carrito1_idx` (`fk_carrito`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`),
  ADD UNIQUE KEY `id_producto_UNIQUE` (`id_producto`),
  ADD KEY `fk_producto_restaurante1_idx` (`fk_restaurante`);

--
-- Indices de la tabla `producto_adicion`
--
ALTER TABLE `producto_adicion`
  ADD PRIMARY KEY (`fk_producto`,`fk_adicion`),
  ADD KEY `fk_producto_has_adicion_adicion1_idx` (`fk_adicion`),
  ADD KEY `fk_producto_has_adicion_producto1_idx` (`fk_producto`);

--
-- Indices de la tabla `producto_ingrediente_base`
--
ALTER TABLE `producto_ingrediente_base`
  ADD PRIMARY KEY (`fk_producto`,`fk_ingrediente_base`),
  ADD KEY `fk_producto_has_ingrediente_base_ingrediente_base1_idx` (`fk_ingrediente_base`),
  ADD KEY `fk_producto_has_ingrediente_base_producto1_idx` (`fk_producto`);

--
-- Indices de la tabla `restaurante`
--
ALTER TABLE `restaurante`
  ADD PRIMARY KEY (`id_restaurante`),
  ADD UNIQUE KEY `id_restaurante_UNIQUE` (`id_restaurante`);

--
-- Indices de la tabla `sede`
--
ALTER TABLE `sede`
  ADD PRIMARY KEY (`id_sede`),
  ADD UNIQUE KEY `id_sede_UNIQUE` (`id_sede`),
  ADD KEY `fk_restaurante_has_usuario_usuario1_idx` (`fk_usuario`),
  ADD KEY `fk_restaurante_has_usuario_restaurante1_idx` (`fk_restaurante`);

--
-- Indices de la tabla `sede_ingrediente`
--
ALTER TABLE `sede_ingrediente`
  ADD PRIMARY KEY (`fk_sede`,`fk_ingrediente`),
  ADD KEY `fk_sede_has_ingrediente_ingrediente1_idx` (`fk_ingrediente`),
  ADD KEY `fk_sede_has_ingrediente_sede1_idx` (`fk_sede`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `user_UNIQUE` (`user`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `adicion`
--
ALTER TABLE `adicion`
  MODIFY `id_adicion` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=214;

--
-- AUTO_INCREMENT de la tabla `admin_tecnico`
--
ALTER TABLE `admin_tecnico`
  MODIFY `id_admin_tecnico` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `carrito`
--
ALTER TABLE `carrito`
  MODIFY `id_carrito` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `horario`
--
ALTER TABLE `horario`
  MODIFY `id_horario` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `ingrediente`
--
ALTER TABLE `ingrediente`
  MODIFY `id_ingrediente` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=108;

--
-- AUTO_INCREMENT de la tabla `ingrediente_base`
--
ALTER TABLE `ingrediente_base`
  MODIFY `id_ingrediente_base` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=204;

--
-- AUTO_INCREMENT de la tabla `item_carrito`
--
ALTER TABLE `item_carrito`
  MODIFY `id_item_carrito` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2004;

--
-- AUTO_INCREMENT de la tabla `menu`
--
ALTER TABLE `menu`
  MODIFY `id_menu` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1012;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1005;

--
-- AUTO_INCREMENT de la tabla `restaurante`
--
ALTER TABLE `restaurante`
  MODIFY `id_restaurante` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `sede`
--
ALTER TABLE `sede`
  MODIFY `id_sede` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `adicion`
--
ALTER TABLE `adicion`
  ADD CONSTRAINT `fk_ingrediente_base_ingrediente10` FOREIGN KEY (`fk_ingrediente`) REFERENCES `ingrediente` (`id_ingrediente`);

--
-- Filtros para la tabla `admin_tecnico`
--
ALTER TABLE `admin_tecnico`
  ADD CONSTRAINT `fk_admin_tecnico_usuario1` FOREIGN KEY (`fk_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD CONSTRAINT `fk_carrito_cliente1` FOREIGN KEY (`fk_cliente`) REFERENCES `cliente` (`id_cliente`);

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `fk_cliente_usuario` FOREIGN KEY (`fk_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `horario`
--
ALTER TABLE `horario`
  ADD CONSTRAINT `fk_horario_restaurante1` FOREIGN KEY (`fk_restaurante`) REFERENCES `restaurante` (`id_restaurante`);

--
-- Filtros para la tabla `ingrediente_base`
--
ALTER TABLE `ingrediente_base`
  ADD CONSTRAINT `fk_ingrediente_base_ingrediente1` FOREIGN KEY (`fk_ingrediente`) REFERENCES `ingrediente` (`id_ingrediente`);

--
-- Filtros para la tabla `ingrediente_cambio`
--
ALTER TABLE `ingrediente_cambio`
  ADD CONSTRAINT `fk_ingrediente_cambio_ingrediente_base1` FOREIGN KEY (`fk_ingrediente_cambio`) REFERENCES `ingrediente_base` (`id_ingrediente_base`),
  ADD CONSTRAINT `fk_ingrediente_has_ingrediente_base_ingrediente_base1` FOREIGN KEY (`fk_ingrediente_base`) REFERENCES `ingrediente_base` (`id_ingrediente_base`);

--
-- Filtros para la tabla `item_carrito`
--
ALTER TABLE `item_carrito`
  ADD CONSTRAINT `fk_carrito_has_menu_carrito1` FOREIGN KEY (`fk_carrito`) REFERENCES `carrito` (`id_carrito`),
  ADD CONSTRAINT `fk_carrito_has_menu_menu1` FOREIGN KEY (`fk_menu`) REFERENCES `menu` (`id_menu`),
  ADD CONSTRAINT `fk_item_carrito_sede1` FOREIGN KEY (`fk_sede`) REFERENCES `sede` (`id_sede`);

--
-- Filtros para la tabla `item_carrito_adicion`
--
ALTER TABLE `item_carrito_adicion`
  ADD CONSTRAINT `fk_item_carrito_adicion_producto1` FOREIGN KEY (`fk_producto`) REFERENCES `producto` (`id_producto`),
  ADD CONSTRAINT `fk_item_carrito_has_adicion_adicion1` FOREIGN KEY (`fk_adicion`) REFERENCES `adicion` (`id_adicion`),
  ADD CONSTRAINT `fk_item_carrito_has_adicion_item_carrito1` FOREIGN KEY (`fk_item_carrito`) REFERENCES `item_carrito` (`id_item_carrito`);

--
-- Filtros para la tabla `item_carrito_ingrediente_base`
--
ALTER TABLE `item_carrito_ingrediente_base`
  ADD CONSTRAINT `fk_item_carrito_has_ingrediente_base_ingrediente_base1` FOREIGN KEY (`fk_ingrediente_base`) REFERENCES `ingrediente_base` (`id_ingrediente_base`),
  ADD CONSTRAINT `fk_item_carrito_has_ingrediente_base_item_carrito1` FOREIGN KEY (`fk_item_carrito`) REFERENCES `item_carrito` (`id_item_carrito`),
  ADD CONSTRAINT `fk_item_carrito_ingrediente_base_producto1` FOREIGN KEY (`fk_producto`) REFERENCES `producto` (`id_producto`);

--
-- Filtros para la tabla `item_carrito_producto`
--
ALTER TABLE `item_carrito_producto`
  ADD CONSTRAINT `item_carrito_producto_ibfk_1` FOREIGN KEY (`fk_item_carrito`) REFERENCES `item_carrito` (`id_item_carrito`),
  ADD CONSTRAINT `item_carrito_producto_ibfk_2` FOREIGN KEY (`fk_producto`) REFERENCES `producto` (`id_producto`);

--
-- Filtros para la tabla `menu`
--
ALTER TABLE `menu`
  ADD CONSTRAINT `fk_menu_restaurante1` FOREIGN KEY (`fk_restaurante`) REFERENCES `restaurante` (`id_restaurante`);

--
-- Filtros para la tabla `menu_producto`
--
ALTER TABLE `menu_producto`
  ADD CONSTRAINT `fk_menu_has_producto_menu1` FOREIGN KEY (`fk_menu`) REFERENCES `menu` (`id_menu`),
  ADD CONSTRAINT `fk_menu_has_producto_producto1` FOREIGN KEY (`fk_producto`) REFERENCES `producto` (`id_producto`);

--
-- Filtros para la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `fk_pedido_carrito1` FOREIGN KEY (`fk_carrito`) REFERENCES `carrito` (`id_carrito`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `fk_producto_restaurante1` FOREIGN KEY (`fk_restaurante`) REFERENCES `restaurante` (`id_restaurante`);

--
-- Filtros para la tabla `producto_adicion`
--
ALTER TABLE `producto_adicion`
  ADD CONSTRAINT `fk_producto_has_adicion_adicion1` FOREIGN KEY (`fk_adicion`) REFERENCES `adicion` (`id_adicion`),
  ADD CONSTRAINT `fk_producto_has_adicion_producto1` FOREIGN KEY (`fk_producto`) REFERENCES `producto` (`id_producto`);

--
-- Filtros para la tabla `producto_ingrediente_base`
--
ALTER TABLE `producto_ingrediente_base`
  ADD CONSTRAINT `fk_producto_has_ingrediente_base_ingrediente_base1` FOREIGN KEY (`fk_ingrediente_base`) REFERENCES `ingrediente_base` (`id_ingrediente_base`),
  ADD CONSTRAINT `fk_producto_has_ingrediente_base_producto1` FOREIGN KEY (`fk_producto`) REFERENCES `producto` (`id_producto`);

--
-- Filtros para la tabla `sede`
--
ALTER TABLE `sede`
  ADD CONSTRAINT `fk_restaurante_has_usuario_restaurante1` FOREIGN KEY (`fk_restaurante`) REFERENCES `restaurante` (`id_restaurante`),
  ADD CONSTRAINT `fk_restaurante_has_usuario_usuario1` FOREIGN KEY (`fk_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `sede_ingrediente`
--
ALTER TABLE `sede_ingrediente`
  ADD CONSTRAINT `fk_sede_has_ingrediente_ingrediente1` FOREIGN KEY (`fk_ingrediente`) REFERENCES `ingrediente` (`id_ingrediente`),
  ADD CONSTRAINT `fk_sede_has_ingrediente_sede1` FOREIGN KEY (`fk_sede`) REFERENCES `sede` (`id_sede`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
