-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2020. Nov 27. 16:07
-- Kiszolgáló verziója: 8.0.22
-- PHP verzió: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `szálloda`
--
CREATE DATABASE IF NOT EXISTS `szálloda` DEFAULT CHARACTER SET utf8 COLLATE utf8_hungarian_ci;
USE `szálloda`;

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `foglalás`
--

CREATE TABLE `foglalás` (
  `foglalásid` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  `ár` int NOT NULL,
  `mettől` date NOT NULL,
  `meddig` date NOT NULL,
  `személyi` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  `foglalás_időpontja` timestamp NOT NULL,
  `lemondhatóság` varchar(5) CHARACTER SET utf8 COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `foglalás`
--

INSERT INTO `foglalás` (`foglalásid`, `ár`, `mettől`, `meddig`, `személyi`, `foglalás_időpontja`, `lemondhatóság`) VALUES
('15', 45000, '2020-11-04', '2020-11-07', '464123RM', '2020-06-20 07:43:45', 'nem'),
('19', 9000, '2020-04-26', '2020-04-30', '765165XQ', '2020-03-15 12:54:27', 'igen'),
('22', 10500, '2020-08-11', '2020-08-14', '486435UE', '2020-06-14 16:41:51', 'nem'),
('34', 10000, '2021-01-03', '2021-01-13', '673563AP', '2020-11-22 18:56:29', 'igen'),
('40', 21000, '2020-06-12', '2020-06-15', '348530SA', '2020-06-03 14:12:03', 'igen'),
('57', 15000, '2020-07-15', '2020-07-18', '942348LU', '2020-06-12 13:29:41', 'nem'),
('61', 16000, '2020-08-09', '2020-08-11', '178624GB', '2020-02-13 11:38:21', 'igen'),
('78', 36000, '2020-12-20', '2020-12-23', '694207NI', '2020-12-03 07:00:32', 'nem'),
('95', 8000, '2020-02-10', '2020-02-11', '436841ER', '2019-12-26 20:58:38', 'igen');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szoba`
--

CREATE TABLE `szoba` (
  `szobaszám` int NOT NULL,
  `napidíj` int NOT NULL,
  `emelet` int NOT NULL,
  `tipusmegnevezés` varchar(30) COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `szoba`
--

INSERT INTO `szoba` (`szobaszám`, `napidíj`, `emelet`, `tipusmegnevezés`) VALUES
(1, 8000, 1, 'Családi'),
(2, 7000, 1, 'Csoportos'),
(3, 4000, 1, 'Egyedüli'),
(4, 15000, 1, 'Giga'),
(5, 3500, 2, 'Nappali'),
(6, 2000, 2, 'Olcsó'),
(7, 12000, 2, 'Prémium'),
(8, 20000, 2, 'VIP'),
(9, 5000, 3, 'Átlagos');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szobatípus`
--

CREATE TABLE `szobatípus` (
  `tipusmegnevezés` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  `internet` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  `méret` int NOT NULL,
  `ágyak száma` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `szobatípus`
--

INSERT INTO `szobatípus` (`tipusmegnevezés`, `internet`, `méret`, `ágyak száma`) VALUES
('Átlagos', 'lassú', 10, 2),
('Családi', 'gyors', 17, 4),
('Csoportos', 'gyors', 15, 3),
('Egyedüli', 'gyors', 12, 1),
('Éjszakai', 'lassú', 10, 2),
('Giga', 'nincs', 40, 10),
('Nappali', 'nincs', 5, 0),
('Olcsó', 'nincs', 8, 1),
('Prémium', 'gyors', 15, 2),
('VIP', 'gyors', 30, 2);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szobája`
--

CREATE TABLE `szobája` (
  `foglalásid` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  `szobaszám` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `szobája`
--

INSERT INTO `szobája` (`foglalásid`, `szobaszám`) VALUES
('22', 1),
('34', 2),
('19', 3),
('61', 4),
('40', 5),
('15', 6),
('78', 7),
('95', 8),
('57', 9);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `vendég`
--

CREATE TABLE `vendég` (
  `személyi` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  `szüldátum` date NOT NULL,
  `nem` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  `kor` int NOT NULL,
  `lakcím` varchar(80) COLLATE utf8_hungarian_ci NOT NULL,
  `vezetéknév` varchar(30) COLLATE utf8_hungarian_ci NOT NULL,
  `keresztnév` varchar(30) COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `vendég`
--

INSERT INTO `vendég` (`személyi`, `szüldátum`, `nem`, `kor`, `lakcím`, `vezetéknév`, `keresztnév`) VALUES
('178624GB', '1998-10-08', 'férfi', 22, 'Eger, Hunyadi u. 12.', 'Lukács', 'Gábor'),
('348530SA', '1985-01-25', 'férfi', 35, 'Sopron, Kossuth u. 15.', 'Lakatos', 'Gergely'),
('436841ER', '1997-05-17', 'nő', 23, 'Debrecen, Móra krt. 38.', 'Novák', 'Erzsébet'),
('464123RM', '2001-09-25', 'nő', 19, 'Vác, Otthon u. 3.', 'Kiss', 'Dóra'),
('486435UE', '1973-02-13', 'férfi', 47, 'Budapest, Ferenc krt. 17.', 'Tóth', 'Dezső'),
('673563AP', '1969-12-20', 'férfi', 50, 'Pécs, Aladár u. 1.', 'Bútoros', 'Tibor'),
('694207NI', '1990-08-22', 'nő', 30, 'Miskolc, Petőfi u. 38.', 'Orosz', 'Anna'),
('765165XQ', '1995-06-20', 'nő', 25, 'Székesfehérvár, Szabadság u. 24.', 'Varga', 'Ilona'),
('942348LU', '1999-07-13', 'férfi', 21, 'Győr, Német u. 32.', 'Szabó', 'István');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `étkezés`
--

CREATE TABLE `étkezés` (
  `tipusmegnevezés` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  `étkezés` varchar(50) CHARACTER SET utf8 COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `étkezés`
--

INSERT INTO `étkezés` (`tipusmegnevezés`, `étkezés`) VALUES
('Átlagos', 'Ebéd, Vacsora'),
('Családi', 'Reggeli, Ebéd, Vacsora'),
('Csoportos', 'Reggeli, Ebéd, Vacsora'),
('Egyedüli', 'Reggeli, Ebéd'),
('Éjszakai', 'Vacsora'),
('Giga', 'Svédasztal'),
('Nappali', 'Ebéd'),
('Olcsó', 'Ebéd'),
('Prémium', '0/24 Telefonos Kiszolgálás'),
('VIP', 'Arany Kaviár');

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `foglalás`
--
ALTER TABLE `foglalás`
  ADD PRIMARY KEY (`foglalásid`),
  ADD UNIQUE KEY `személyi` (`személyi`);

--
-- A tábla indexei `szoba`
--
ALTER TABLE `szoba`
  ADD PRIMARY KEY (`szobaszám`),
  ADD UNIQUE KEY `tipusmegnevezés` (`tipusmegnevezés`);

--
-- A tábla indexei `szobatípus`
--
ALTER TABLE `szobatípus`
  ADD PRIMARY KEY (`tipusmegnevezés`);

--
-- A tábla indexei `szobája`
--
ALTER TABLE `szobája`
  ADD PRIMARY KEY (`foglalásid`,`szobaszám`),
  ADD UNIQUE KEY `foglalásid` (`foglalásid`,`szobaszám`),
  ADD KEY `szobája_ibfk_2` (`szobaszám`);

--
-- A tábla indexei `vendég`
--
ALTER TABLE `vendég`
  ADD PRIMARY KEY (`személyi`);

--
-- A tábla indexei `étkezés`
--
ALTER TABLE `étkezés`
  ADD PRIMARY KEY (`tipusmegnevezés`,`étkezés`),
  ADD UNIQUE KEY `tipusmegnevezés` (`tipusmegnevezés`);

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `foglalás`
--
ALTER TABLE `foglalás`
  ADD CONSTRAINT `foglalás_ibfk_1` FOREIGN KEY (`személyi`) REFERENCES `vendég` (`személyi`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Megkötések a táblához `szoba`
--
ALTER TABLE `szoba`
  ADD CONSTRAINT `szoba_ibfk_1` FOREIGN KEY (`tipusmegnevezés`) REFERENCES `szobatípus` (`tipusmegnevezés`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Megkötések a táblához `szobája`
--
ALTER TABLE `szobája`
  ADD CONSTRAINT `szobája_ibfk_1` FOREIGN KEY (`foglalásid`) REFERENCES `foglalás` (`foglalásid`),
  ADD CONSTRAINT `szobája_ibfk_2` FOREIGN KEY (`szobaszám`) REFERENCES `szoba` (`szobaszám`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Megkötések a táblához `étkezés`
--
ALTER TABLE `étkezés`
  ADD CONSTRAINT `étkezés_ibfk_1` FOREIGN KEY (`tipusmegnevezés`) REFERENCES `szobatípus` (`tipusmegnevezés`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
