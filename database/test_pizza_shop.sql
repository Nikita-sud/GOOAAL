-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: test_pizza_shop
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `active_order`
--

DROP TABLE IF EXISTS `active_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `active_order` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `time_started` datetime DEFAULT NULL,
  `estimated_finish` datetime DEFAULT NULL,
  `finished` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `active_order`
--

LOCK TABLES `active_order` WRITE;
/*!40000 ALTER TABLE `active_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `active_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `city` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4096 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES (1,'city'),(2,'Appingedam'),(3,'Bierum'),(4,'Borgsweer'),(5,'Delfzijl'),(6,'Farmsum'),(7,'Godlinze'),(8,'Holwierde'),(9,'Krewerd'),(10,'Losdorp'),(11,'Meedhuizen'),(12,'Spijk'),(13,'Termunten'),(14,'Termunterzijl'),(15,'Wagenborgen'),(16,'Woldendorp'),(17,'Garmerwolde'),(18,'Glimmen'),(19,'Groningen'),(20,'Haren'),(21,'Lellens'),(22,'Meerstad'),(23,'Noordlaren'),(24,'Onnen'),(25,'Sint Annen'),(26,'Ten Boer'),(27,'Ten Post'),(28,'Thesinge'),(29,'Winneweer'),(30,'Woltersum'),(31,'Adorp'),(32,'Baflo'),(33,'Bedum'),(34,'Den Andel'),(35,'Eemshaven'),(36,'Eenrum'),(37,'Eppenhuizen'),(38,'Hornhuizen'),(39,'Houwerzijl'),(40,'Kantens'),(41,'Kloosterburen'),(42,'Lauwersoog'),(43,'Leens'),(44,'Mensingeweer'),(45,'Noordwolde'),(46,'Oldenzijl'),(47,'Onderdendam'),(48,'Oosternieland'),(49,'Oudeschip'),(50,'Pieterburen'),(51,'Rasquert'),(52,'Roodeschool'),(53,'Rottum'),(54,'Saaxumhuizen'),(55,'Sauwerd'),(56,'Schouwerzijl'),(57,'Stitswerd'),(58,'Tinallinge'),(59,'Uithuizen'),(60,'Uithuizermeeden'),(61,'Ulrum'),(62,'Usquert'),(63,'Vierhuizen'),(64,'Warffum'),(65,'Warfhuizen'),(66,'Wehe-den Hoorn'),(67,'Westernieland'),(68,'Wetsinge'),(69,'Winsum'),(70,'Zandeweer'),(71,'Zoutkamp'),(72,'Zuidwolde'),(73,'Zuurdijk'),(74,'\'t Zandt'),(75,'Eenum'),(76,'Garrelsweer'),(77,'Garsthuizen'),(78,'Huizinge'),(79,'Leermens'),(80,'Loppersum'),(81,'Middelstum'),(82,'Oosterwijtwerd'),(83,'Startenhuizen Lopper'),(84,'Stedum'),(85,'Toornwerd'),(86,'Westeremden'),(87,'Westerwijtwerd'),(88,'Wirdum'),(89,'Zeerijp'),(90,'Zijldijk'),(91,'Foxhol'),(92,'Froombosch'),(93,'Harkstede'),(94,'Hellum'),(95,'Hoogezand'),(96,'Kiel-Windeweer'),(97,'Kolham'),(98,'Kropswolde'),(99,'Lageland'),(100,'Luddeweer'),(101,'Meeden'),(102,'Muntendam'),(103,'Noordbroek'),(104,'Overschild'),(105,'Sappemeer'),(106,'Scharmer'),(107,'Schildwolde'),(108,'Siddeburen'),(109,'Slochteren'),(110,'Steendam'),(111,'Tjuchem'),(112,'Tripscompagnie'),(113,'Waterhuizen'),(114,'Westerbroek'),(115,'Woudbloem'),(116,'Zuidbroek'),(117,'\'t Waar'),(118,'Bad Nieuweschans'),(119,'Beerta'),(120,'Blauwestad'),(121,'Drieborg'),(122,'Finsterwolde'),(123,'Heiligerlee'),(124,'Midwolda'),(125,'Nieuw Beerta'),(126,'Nieuw Scheemda'),(127,'Nieuwolda'),(128,'Oudezijl'),(129,'Scheemda'),(130,'Westerlee'),(131,'Winschoten'),(132,'Nieuwe Pekela'),(133,'Oude Pekela'),(134,'Alteveer'),(135,'Mussel'),(136,'Musselkanaal'),(137,'Onstwedde'),(138,'Stadskanaal'),(139,'Vledderveen'),(140,'Borgercompagnie'),(141,'Veendam'),(142,'Wildervank'),(143,'Aduard'),(144,'Boerakker'),(145,'Briltil'),(146,'De Wilp'),(147,'Den Ham'),(148,'Den Horn'),(149,'Doezum'),(150,'Enumatil'),(151,'Ezinge'),(152,'Feerwerd'),(153,'Garnwerd'),(154,'Grijpskerk'),(155,'Grootegast'),(156,'Jonkersvaart'),(157,'Kommerzijl'),(158,'Kornhorn'),(159,'Lauwerzijl'),(160,'Leek'),(161,'Lettelbert'),(162,'Lucaswolde'),(163,'Lutjegast'),(164,'Marum'),(165,'Midwolde'),(166,'Niebert'),(167,'Niehove'),(168,'Niekerk'),(169,'Niezijl'),(170,'Noordhorn'),(171,'Noordwijk'),(172,'Nuis'),(173,'Oldehove'),(174,'Oldekerk'),(175,'Oostwold'),(176,'Opende'),(177,'Pieterzijl'),(178,'Saaksum'),(179,'Sebaldeburen'),(180,'Tolbert'),(181,'Visvliet'),(182,'Zevenhuizen'),(183,'Zuidhorn'),(184,'Bellingwolde'),(185,'Blijham'),(186,'Bourtange'),(187,'Oudeschans'),(188,'Sellingen'),(189,'Ter Apel'),(190,'Ter Apelkanaal'),(191,'Veelerveen'),(192,'Vlagtwedde'),(193,'Vriescheloo'),(194,'Wedde'),(195,'Augustinusga'),(196,'Boelenslaan'),(197,'Buitenpost'),(198,'Drogeham'),(199,'Gerkesklooster'),(200,'Harkema'),(201,'Kootstertille'),(202,'Stroobos'),(203,'Surhuisterveen'),(204,'Surhuizum'),(205,'Twijzel'),(206,'Twijzelerheide'),(207,'Ballum'),(208,'Buren'),(209,'Hollum'),(210,'BroeksterwР вЂњРЎС›l'),(211,'DamwР вЂњРЎС›ld'),(212,'De Falom'),(213,'De Westereen'),(214,'Driezum'),(215,'FeanwР вЂњРЎС›lden'),(216,'Readtsjerk'),(217,'Rinsumageast'),(218,'SibrandahР вЂњР’В»s'),(219,'WР вЂњРЎС›lterswР вЂ'),(220,'Akmarijp'),(221,'Oudemirdum'),(222,'Bakhuizen'),(223,'Balk'),(224,'Bantega'),(225,'Boornzwaag'),(226,'Broek'),(227,'Delfstrahuizen'),(228,'Dijken'),(229,'Doniaga'),(230,'Elahuizen'),(231,'Echten'),(232,'Echtenerbrug'),(233,'Eesterga'),(234,'Follega'),(235,'Goingarijp'),(236,'Harich'),(237,'Haskerhorne'),(238,'Idskenhuizen'),(239,'Joure'),(240,'Kolderwolde'),(241,'Langweer'),(242,'Legemeer'),(243,'Lemmer'),(244,'Mirns'),(245,'Nijehaske'),(246,'Nijemirdum'),(247,'Oldeouwer'),(248,'Oosterzee'),(249,'Oudehaske'),(250,'Ouwster-Nijega'),(251,'Ouwsterhaule'),(252,'Rijs'),(253,'Rohel'),(254,'Rotstergaast'),(255,'Rotsterhaule'),(256,'Rottum'),(257,'Ruigahuizen'),(258,'Scharsterbrug'),(259,'Sint Nicolaasga'),(260,'Sintjohannesga'),(261,'Sloten'),(262,'Snikzwaag'),(263,'Sondel'),(264,'Terherne'),(265,'Terkaple'),(266,'Teroele'),(267,'Tjerkgaast'),(268,'Vegelinsoord'),(269,'Wijckel'),(270,'Harlingen'),(271,'Midlum'),(272,'Wijnaldum'),(273,'Akkrum'),(274,'Aldeboarn'),(275,'Bontebok'),(276,'De Knipe'),(277,'Gersloot'),(278,'Haskerdijken'),(279,'Heerenveen'),(280,'Hoornsterzwaag'),(281,'Hoarnstersweach'),(282,'Jubbega'),(283,'Katlijk'),(284,'Luinjeberd'),(285,'Mildam'),(286,'Nieuwebrug'),(287,'Nieuwehorne'),(288,'Nieuweschoot'),(289,'Oranjewoud'),(290,'Oudehorne'),(291,'Oudeschoot'),(292,'Terband'),(293,'Tjalleberd'),(294,'Alde Leie'),(295,'Baard'),(296,'Bears'),(297,'Britsum'),(298,'Eagum'),(299,'Easterlittens'),(300,'Feinsum'),(301,'Friens'),(302,'Goutum'),(303,'Grou'),(304,'Hempens'),(305,'Hijum'),(306,'Hilaard'),(307,'HР вЂњРЎвЂќns'),(308,'Idaerd'),(309,'Jellum'),(310,'Jelsum'),(311,'Jirnsum'),(312,'Jorwert'),(313,'Koarnjum'),(314,'Leeuwarden'),(315,'Lekkum'),(316,'Leons'),(317,'Mantgum'),(318,'Miedum'),(319,'Reduzum'),(320,'Snakkerburen'),(321,'Stiens'),(322,'Swichum'),(323,'Teerns'),(324,'Warstiens'),(325,'Warten'),(326,'Weidum'),(327,'Wergea'),(328,'Wirdum'),(329,'Wytgaard'),(330,'Aalsum'),(331,'Anjum'),(332,'Augsbuurt'),(333,'Blije'),(334,'Bornwird'),(335,'Brantgum'),(336,'Burdaard'),(337,'Burum'),(338,'Dokkum'),(339,'Ee'),(340,'Engwierum'),(341,'Ferwert'),(342,'Foudgum'),(343,'Ginnum'),(344,'Hallum'),(345,'Hantum'),(346,'Hantumeruitburen'),(347,'Hantumhuizen'),(348,'Hegebeintum'),(349,'Hiaure'),(350,'Holwerd'),(351,'Jannum'),(352,'Jislum'),(353,'Jouswier'),(354,'Kollum'),(355,'Kollumerpomp'),(356,'Kollumerzwaag'),(357,'Lichtaard'),(358,'Lioessens'),(359,'Marrum'),(360,'Metslawier'),(361,'Moddergat'),(362,'Morra'),(363,'Munnekezijl'),(364,'Nes'),(365,'Niawier'),(366,'Oosternijkerk'),(367,'Oostrum'),(368,'Oudwoude'),(369,'Paesens'),(370,'Raard'),(371,'Reitsum'),(372,'Ternaard'),(373,'Triemen'),(374,'Veenklooster'),(375,'Waaxens'),(376,'WР вЂњРЎС›nswert'),(377,'Warfstermolen'),(378,'Westergeest'),(379,'Wetsens'),(380,'Wierum'),(381,'Zwagerbosch'),(382,'Appelscha'),(383,'Donkerbroek'),(384,'Elsloo'),(385,'Fochteloo'),(386,'Haule'),(387,'Haulerwijk'),(388,'Langedijke'),(389,'Makkinga'),(390,'Nijeberkoop'),(391,'Oldeberkoop'),(392,'Oosterwolde'),(393,'Ravenswoud'),(394,'Waskemeer'),(395,'Bakkeveen'),(396,'Beetsterzwaag'),(397,'Drachten-Azeven'),(398,'Frieschepalen'),(399,'Gorredijk'),(400,'Hemrik'),(401,'JonkerslР вЂњРЎС›n'),(402,'Langezwaag'),(403,'Lippenhuizen'),(404,'Luxwoude'),(405,'Nij Beets'),(406,'Olterterp'),(407,'Siegerswoude'),(408,'Terwispel'),(409,'Tijnje'),(410,'Ureterp'),(411,'Wijnjewoude'),(412,'Schiermonnikoog'),(413,'Boornbergum'),(414,'De Tike'),(415,'De Veenhoop'),(416,'De Wilgen'),(417,'Drachten'),(418,'Drachtstercompagnie'),(419,'GoР вЂњР’В«ngahuizen'),(420,'Houtigehage'),(421,'Kortehemmen'),(422,'Nijega'),(423,'Opeinde'),(424,'Rottevalle'),(425,'Smalle Ee'),(426,'Abbega'),(427,'Oudega'),(428,'Allingawier'),(429,'Arum'),(430,'Blauwhuis'),(431,'Boazum'),(432,'Bolsward'),(433,'Breezanddijk'),(434,'Britswert'),(435,'Burgwerd'),(436,'Cornwerd'),(437,'Hommerts'),(438,'Dearsum'),(439,'Dedgum'),(440,'IJlst'),(441,'Easterein'),(442,'Easterwierrum'),(443,'Exmorra'),(444,'Ferwoude'),(445,'Folsgare'),(446,'Gaast'),(447,'Gaastmeer'),(448,'Gauw'),(449,'GoР вЂњР’В«nga'),(450,'Greonterp'),(451,'Hartwerd'),(452,'Heeg'),(453,'Hichtum'),(454,'Hidaard'),(455,'Hieslum'),(456,'Hemelum'),(457,'Hinnaard'),(458,'Hindeloopen'),(459,'Idsegahuizum'),(460,'Idzega'),(461,'Iens'),(462,'It Heidenskip'),(463,'Itens'),(464,'Jutrijp'),(465,'Kimswerd'),(466,'Kornwerderzand'),(467,'Koudum'),(468,'Koufurderrige'),(469,'KР вЂњР’В»baard'),(470,'LoР вЂњР’В«nga'),(471,'Lollum'),(472,'Longerhouw'),(473,'Lytsewierrum'),(474,'Makkum'),(475,'Molkwerum'),(476,'Nijhuizum'),(477,'Nijland'),(478,'Offingawier'),(479,'Oosthem'),(480,'Parrega'),(481,'Piaam'),(482,'Pingjum'),(483,'Poppenwier'),(484,'Raerd'),(485,'ReahР вЂњР’В»s'),(486,'Rien'),(487,'Sandfirden'),(488,'Schettens'),(489,'Schraard'),(490,'Sibrandabuorren'),(491,'Scharnegoutum'),(492,'Smallebrugge'),(493,'Sneek'),(494,'Stavoren'),(495,'Tersoal'),(496,'Tjerkwerd'),(497,'Oppenhuizen'),(498,'Tjalhuizum'),(499,'Tirns'),(500,'Uitwellingerga'),(501,'Waaksens'),(502,'Woudsend'),(503,'Workum'),(504,'Warns'),(505,'Westhem'),(506,'Witmarsum'),(507,'Wiuwert'),(508,'Wolsum'),(509,'Wommels'),(510,'Wons'),(511,'Indijk'),(512,'Ypecolsga'),(513,'Ysbrechtum'),(514,'Zurich'),(515,'Baaiduinen'),(516,'Formerum'),(517,'Hee'),(518,'Hoorn'),(519,'Kaard'),(520,'Kinnum'),(521,'Landerum'),(522,'Lies'),(523,'Midsland'),(524,'Oosterend'),(525,'Striep'),(526,'West-Terschelling'),(527,'Aldtsjerk'),(528,'Burgum'),(529,'EarnewР вЂњРЎС›ld'),(530,'Eastermar'),(531,'Garyp'),(532,'Gytsjerk'),(533,'Hurdegaryp'),(534,'Jistrum'),(535,'MР вЂњР’В»nein'),(536,'Noardburgum'),(537,'Oentsjerk'),(538,'Ryptsjerk'),(539,'Sumar'),(540,'SuwР вЂњРЎС›ld'),(541,'Tytsjerk'),(542,'Wyns'),(543,'Vlieland'),(544,'Achlum'),(545,'Baaium'),(546,'Berltsum'),(547,'Bitgum'),(548,'Bitgummole'),(549,'Blessum'),(550,'Boer'),(551,'Boksum'),(552,'Deinum'),(553,'Dongjum'),(554,'Dronryp'),(555,'Firdgum'),(556,'Franeker'),(557,'Herbaijum'),(558,'Hitzum'),(559,'Ingelum'),(560,'Klooster Lidlum'),(561,'Marsum'),(562,'Menaam'),(563,'Minnertsga'),(564,'Nij Altoenae'),(565,'Oosterbierum'),(566,'Oudebildtzijl'),(567,'Peins'),(568,'Pietersbierum'),(569,'Ried'),(570,'Schalsum'),(571,'Sexbierum'),(572,'Skingen'),(573,'Slappeterp'),(574,'Spannum'),(575,'St.-Annaparochie'),(576,'St.-Jacobiparochie'),(577,'Tzum'),(578,'Tzummarum'),(579,'Vrouwenparochie'),(580,'Westhoek'),(581,'Wier'),(582,'Winsum'),(583,'Wjelsryp'),(584,'Zweins'),(585,'Blesdijke'),(586,'Boijl'),(587,'De Blesse'),(588,'De Hoeve'),(589,'Langelille'),(590,'Munnekeburen'),(591,'Nijeholtpade'),(592,'Nijeholtwolde'),(593,'Nijelamer'),(594,'Nijetrijne'),(595,'Noordwolde'),(596,'Oldeholtpade'),(597,'Oldeholtwolde'),(598,'Oldelamer'),(599,'Oldetrijne'),(600,'Oosterstreek'),(601,'Peperga'),(602,'Scherpenzeel'),(603,'Slijkenburg'),(604,'Sonnega'),(605,'Spanga'),(606,'Steggerda'),(607,'Ter Idzard'),(608,'Vinkega'),(609,'Wolvega'),(610,'Zandhuizen'),(611,'Amen'),(612,'Anderen'),(613,'Anloo'),(614,'Annen'),(615,'Annerveenschekanaal'),(616,'BalloР вЂњР’В«rveld'),(617,'Balloo'),(618,'Deurze'),(619,'Eext'),(620,'Eexterveen'),(621,'Eexterveenschekanaal'),(622,'Eexterzandvoort'),(623,'Ekehaar'),(624,'Eldersloo'),(625,'Eleveld'),(626,'Gasselte'),(627,'Gasselternijveen'),(628,'Gasselternijveensche'),(629,'Gasteren'),(630,'Geelbroek'),(631,'Gieten'),(632,'Gieterveen'),(633,'Grolloo'),(634,'Marwijksoord'),(635,'Nieuw Annerveen'),(636,'Nieuwediep'),(637,'Nijlande'),(638,'Nooitgedacht'),(639,'Oud Annerveen'),(640,'Papenvoort'),(641,'Rolde'),(642,'Schipborg'),(643,'Schoonloo'),(644,'Spijkerboor'),(645,'Vredenheim'),(646,'Assen'),(647,'Loon'),(648,'Rhee'),(649,'Ter Aard'),(650,'Ubbena'),(651,'Zeijerveen'),(652,'Zeijerveld'),(653,'1e ExloР вЂњР’В«rmon'),(654,'2e ExloР вЂњР’В«rmon'),(655,'2e Valthermond'),(656,'Borger'),(657,'Bronneger'),(658,'Bronnegerveen'),(659,'Buinen'),(660,'Buinerveen'),(661,'Drouwen'),(662,'Drouwenermond'),(663,'Drouwenerveen'),(664,'Ees'),(665,'Eesergroen'),(666,'Eeserveen'),(667,'Ellertshaar'),(668,'ExloР вЂњР’В«rveen'),(669,'Exloo'),(670,'Klijndijk'),(671,'Nieuw-Buinen'),(672,'Odoorn'),(673,'Odoornerveen'),(674,'Valthe'),(675,'Valthermond'),(676,'Westdorp'),(677,'Zandberg'),(678,'\'t Haantje'),(679,'Aalden'),(680,'Benneveld'),(681,'Coevorden'),(682,'Dalen'),(683,'Dalerpeel'),(684,'Dalerveen'),(685,'De Kiel'),(686,'Diphoorn'),(687,'Erm'),(688,'Gees'),(689,'Geesbrug'),(690,'Holsloot'),(691,'Meppen'),(692,'Nieuwlande Coevorden'),(693,'Noord-Sleen'),(694,'Oosterhesselen'),(695,'Schoonoord'),(696,'Sleen'),(697,'Stieltjeskanaal'),(698,'Wachtum'),(699,'Wezup'),(700,'Wezuperbrug'),(701,'Zweeloo'),(702,'Zwinderen'),(703,'de Wijk'),(704,'Drogteropslagen'),(705,'Echten'),(706,'Kerkenveld'),(707,'Koekange'),(708,'Linde'),(709,'Ruinerwold'),(710,'Veeningen'),(711,'Zuidwolde'),(712,'Barger-Compascuum'),(713,'Emmen'),(714,'Emmer-Compascuum'),(715,'Erica'),(716,'Klazienaveen'),(717,'Klazienaveen-Noord'),(718,'Nieuw-Amsterdam'),(719,'Nieuw-Dordrecht'),(720,'Nieuw-Schoonebeek'),(721,'Nieuw-Weerdinge'),(722,'Roswinkel'),(723,'Schoonebeek'),(724,'Veenoord'),(725,'Weiteveen'),(726,'Zandpol'),(727,'Zwartemeer'),(728,'Alteveer gem Hoogeve'),(729,'Elim'),(730,'Fluitenberg'),(731,'Hollandscheveld'),(732,'Hoogeveen'),(733,'Nieuwlande'),(734,'Noordscheschut'),(735,'Broekhuizen'),(736,'De Schiphorst'),(737,'Meppel'),(738,'Nijeveen'),(739,'Rogat'),(740,'Balinge'),(741,'Beilen'),(742,'Bovensmilde'),(743,'Bruntinge'),(744,'Drijber'),(745,'Elp'),(746,'Eursinge'),(747,'Garminge'),(748,'Hijken'),(749,'Hooghalen'),(750,'Mantinge'),(751,'Nieuw-Balinge'),(752,'Nieuweroord'),(753,'Oranje'),(754,'Orvelte'),(755,'Smilde'),(756,'Stuifzand'),(757,'Tiendeveen'),(758,'Westerbork'),(759,'Wijster'),(760,'Witteveen'),(761,'Zuidveld'),(762,'Zwiggelte'),(763,'Alteveer'),(764,'Een'),(765,'Een-West'),(766,'Foxwolde'),(767,'Huis ter Heide'),(768,'Langelo'),(769,'Leutingewolde'),(770,'Lieveren'),(771,'Matsloot'),(772,'Nietap'),(773,'Nieuw-Roden'),(774,'Norg'),(775,'Peest'),(776,'Peize'),(777,'Roden'),(778,'Roderesch'),(779,'Roderwolde'),(780,'Steenbergen'),(781,'Veenhuizen'),(782,'Westervelde'),(783,'Zuidvelde'),(784,'Bunne'),(785,'De Groeve'),(786,'De Punt'),(787,'Donderen'),(788,'Eelde'),(789,'Eelderwolde'),(790,'Midlaren'),(791,'Oudemolen'),(792,'Paterswolde'),(793,'Taarlo'),(794,'Tynaarlo'),(795,'Vries'),(796,'Winde'),(797,'Yde'),(798,'Zeegse'),(799,'Zeijen'),(800,'Zuidlaarderveen'),(801,'Zuidlaren'),(802,'Ansen'),(803,'Boschoord'),(804,'Darp'),(805,'Diever'),(806,'Dieverbrug'),(807,'Doldersum'),(808,'Dwingeloo'),(809,'Frederiksoord'),(810,'Geeuwenbrug'),(811,'Havelte'),(812,'Havelterberg'),(813,'Hoogersmilde'),(814,'Nijensleek'),(815,'Oude Willem'),(816,'Pesse'),(817,'Ruinen'),(818,'Spier'),(819,'Uffelte'),(820,'Vledder'),(821,'Vledderveen'),(822,'Wapse'),(823,'Wapserveen'),(824,'Wateren'),(825,'Wilhelminaoord'),(826,'Wittelte'),(827,'Zorgvlied'),(828,'Aadorp'),(829,'Almelo'),(830,'Bornerbroek'),(831,'Borne'),(832,'Hertme'),(833,'Zenderen'),(834,'Dalfsen'),(835,'Lemelerveld'),(836,'Nieuwleusen'),(837,'Bathmen'),(838,'Colmschate'),(839,'Deventer'),(840,'Diepenveen'),(841,'Lettele'),(842,'Okkenbroek'),(843,'Schalkhaar'),(844,'Agelo'),(845,'Denekamp'),(846,'Lattrop-Breklenkamp'),(847,'Nutter'),(848,'Ootmarsum'),(849,'Oud Ootmarsum'),(850,'Rossum'),(851,'Saasveld'),(852,'Tilligte'),(853,'Weerselo'),(854,'Enschede'),(855,'Haaksbergen'),(856,'Ane'),(857,'Anerveen'),(858,'Anevelde'),(859,'Balkbrug'),(860,'Bergentheim'),(861,'Brucht'),(862,'Bruchterveld'),(863,'Collendoorn'),(864,'De Krim'),(865,'Dedemsvaart'),(866,'Den Velde'),(867,'Diffelen'),(868,'Gramsbergen'),(869,'Hardenberg'),(870,'Heemserveen'),(871,'Holtheme'),(872,'Holthone'),(873,'Hoogenweg'),(874,'Loozen'),(875,'Lutten'),(876,'MariР вЂњР’В«nberg'),(877,'Radewijk'),(878,'Rheeze'),(879,'Rheezerveen'),(880,'Schuinesloot'),(881,'Slagharen'),(882,'Venebrugge'),(883,'Daarle'),(884,'Daarlerveen'),(885,'Hellendoorn'),(886,'Nijverdal'),(887,'Hengelo'),(888,'Ambt Delden'),(889,'Bentelo'),(890,'Delden'),(891,'Diepenheim'),(892,'Goor'),(893,'Hengevelde'),(894,'Markelo'),(895,'\'s-Heerenbroek'),(896,'Grafhorst'),(897,'IJsselmuiden'),(898,'Kampen'),(899,'Kamperveen'),(900,'Wilsum'),(901,'Zalk'),(902,'Beuningen'),(903,'de Lutte'),(904,'Glane'),(905,'Losser'),(906,'Overdinkel'),(907,'Deurningen'),(908,'Oldenzaal'),(909,'Marle'),(910,'Olst'),(911,'Welsum'),(912,'Wesepe'),(913,'Wijhe'),(914,'ArriР вЂњР’В«n'),(915,'Beerze'),(916,'Beerzerveld'),(917,'Dalmsholte'),(918,'Giethmen'),(919,'Lemele'),(920,'Ommen'),(921,'Stegeren'),(922,'Vilsteren'),(923,'Vinkenbuurt'),(924,'Witharen'),(925,'Broekland'),(926,'Heeten'),(927,'Heino'),(928,'Laag Zuthem'),(929,'Lierderholthuis'),(930,'Luttenberg'),(931,'MariР вЂњР’В«nheem'),(932,'Nieuw-Heeten'),(933,'Raalte'),(934,'Holten'),(935,'Rijssen'),(936,'IJhorst'),(937,'Punthorst'),(938,'Rouveen'),(939,'Staphorst'),(940,'Baarlo'),(941,'Baars'),(942,'Basse'),(943,'Belt-Schutsloot'),(944,'Blankenham'),(945,'Blokzijl'),(946,'De Bult'),(947,'De Pol'),(948,'Eesveen'),(949,'Giethoorn'),(950,'IJsselham'),(951,'Kalenberg'),(952,'Kallenkote'),(953,'Kuinre'),(954,'Marijenkampen'),(955,'Nederland'),(956,'Oldemarkt'),(957,'Onna'),(958,'Ossenzijl'),(959,'Paasloo'),(960,'Scheerwolde'),(961,'Sint Jansklooster'),(962,'Steenwijk'),(963,'Steenwijkerwold'),(964,'Tuk'),(965,'Vollenhove'),(966,'Wanneperveen'),(967,'Wetering'),(968,'Willemsoord'),(969,'Witte Paarden'),(970,'Zuidveen'),(971,'Albergen'),(972,'Fleringen'),(973,'Geesteren'),(974,'Haarle'),(975,'Harbrinkhoek'),(976,'Hezingen'),(977,'Langeveen'),(978,'Mander'),(979,'Manderveen'),(980,'Mariaparochie'),(981,'Reutum'),(982,'Tubbergen'),(983,'Vasse'),(984,'Bruinehaar'),(985,'Den Ham'),(986,'Geerdijk'),(987,'Kloosterhaar'),(988,'Sibculo'),(989,'Vriezenveen'),(990,'Vroomshoop'),(991,'Westerhaar-Vriezenve'),(992,'Enter'),(993,'Hoge Hexel'),(994,'Notter'),(995,'Wierden'),(996,'Zuna'),(997,'Genemuiden'),(998,'Hasselt'),(999,'Mastenbroek'),(1000,'Zwartsluis'),(1001,'Zwolle'),(1002,'Almere'),(1003,'Biddinghuizen'),(1004,'Dronten'),(1005,'Swifterbant'),(1006,'Lelystad'),(1007,'Bant'),(1008,'Creil'),(1009,'Emmeloord'),(1010,'Ens'),(1011,'Espel'),(1012,'Kraggenburg'),(1013,'Luttelgeest'),(1014,'Marknesse'),(1015,'Nagele'),(1016,'Rutten'),(1017,'Schokland'),(1018,'Tollebeek'),(1019,'Urk'),(1020,'Zeewolde'),(1021,'Aalten'),(1022,'Bredevoort'),(1023,'De Heurne'),(1024,'Dinxperlo'),(1025,'Apeldoorn'),(1026,'Beekbergen'),(1027,'Beemte Broekland'),(1028,'Hoog Soeren'),(1029,'Lieren'),(1030,'Loenen'),(1031,'Radio Kootwijk'),(1032,'Uddel'),(1033,'Ugchelen'),(1034,'Wenum Wiesel'),(1035,'Arnhem'),(1036,'Achterveld'),(1037,'Barneveld'),(1038,'De Glind'),(1039,'Garderen'),(1040,'Kootwijk'),(1041,'Kootwijkerbroek'),(1042,'Stroe'),(1043,'Terschuur'),(1044,'Voorthuizen'),(1045,'Zwartebroek'),(1046,'Berg en Dal'),(1047,'Erlecom'),(1048,'Groesbeek'),(1049,'Heilig Landstichting'),(1050,'Kekerdom'),(1051,'Leuth'),(1052,'Millingen aan de Rij'),(1053,'Ooij'),(1054,'Persingen'),(1055,'Ubbergen'),(1056,'Beltrum'),(1057,'Borculo'),(1058,'Eibergen'),(1059,'Geesteren'),(1060,'Gelselaar'),(1061,'Haarlo'),(1062,'Neede'),(1063,'Rekken'),(1064,'Rietmolen'),(1065,'Ruurlo'),(1066,'Beuningen'),(1067,'Ewijk'),(1068,'Weurt'),(1069,'Winssen'),(1070,'Baak'),(1071,'Bronkhorst'),(1072,'Drempt'),(1073,'Halle'),(1074,'Hengelo (Gld)'),(1075,'Hoog-Keppel'),(1076,'Hummelo'),(1077,'Keijenborg'),(1078,'Laag-Keppel'),(1079,'Olburgen'),(1080,'Rha'),(1081,'Steenderen'),(1082,'Toldijk'),(1083,'Vierakker'),(1084,'Vorden'),(1085,'Wichmond'),(1086,'Zelhem'),(1087,'Brummen'),(1088,'Eerbeek'),(1089,'Empe'),(1090,'Hall'),(1091,'Leuvenheim'),(1092,'Tonden'),(1093,'Asch'),(1094,'Beusichem'),(1095,'Buren'),(1096,'Eck en Wiel'),(1097,'Erichem'),(1098,'Ingen'),(1099,'Kapel-Avezaath'),(1100,'Kerk-Avezaath'),(1101,'Lienden'),(1102,'Maurik'),(1103,'Ommeren'),(1104,'Ravenswaaij'),(1105,'Rijswijk (GLD)'),(1106,'Zoelen'),(1107,'Zoelmond'),(1108,'Culemborg'),(1109,'Doesburg'),(1110,'Doetinchem'),(1111,'Gaanderen'),(1112,'Wehl'),(1113,'Afferden'),(1114,'Deest'),(1115,'Druten'),(1116,'Horssen'),(1117,'Puiflijk'),(1118,'Duiven'),(1119,'Groessen'),(1120,'Bennekom'),(1121,'De Klomp'),(1122,'Deelen'),(1123,'Ede'),(1124,'Ederveen'),(1125,'Harskamp'),(1126,'Hoenderloo'),(1127,'Lunteren'),(1128,'Otterlo'),(1129,'Wekerom'),(1130,'\'t Harde'),(1131,'Doornspijk'),(1132,'Elburg'),(1133,'Emst'),(1134,'Epe'),(1135,'Oene'),(1136,'Vaassen'),(1137,'Ermelo'),(1138,'Harderwijk'),(1139,'Hierden'),(1140,'Hattem'),(1141,'Heerde'),(1142,'Veessen'),(1143,'Vorchten'),(1144,'Wapenveld'),(1145,'Heumen'),(1146,'Malden'),(1147,'Nederasselt'),(1148,'Overasselt'),(1149,'Angeren'),(1150,'Bemmel'),(1151,'Doornenburg'),(1152,'Gendt'),(1153,'Haalderen'),(1154,'Huissen'),(1155,'Loo'),(1156,'Ressen'),(1157,'Almen'),(1158,'Barchem'),(1159,'Eefde'),(1160,'Epse'),(1161,'Gorssel'),(1162,'Harfsen'),(1163,'Joppe'),(1164,'Kring van Dorth'),(1165,'Laren'),(1166,'Lochem'),(1167,'Alem'),(1168,'Ammerzoden'),(1169,'Hedel'),(1170,'Heerewaarden'),(1171,'Hoenzadriel'),(1172,'Hurwenen'),(1173,'Kerkdriel'),(1174,'Rossum'),(1175,'Velddriel'),(1176,'Well'),(1177,'\'s-Heerenberg'),(1178,'Azewijn'),(1179,'Beek'),(1180,'Braamt'),(1181,'Didam'),(1182,'Kilder'),(1183,'Lengel'),(1184,'Loerbeek'),(1185,'Stokkum'),(1186,'Vethuizen'),(1187,'Wijnbergen'),(1188,'Zeddam'),(1189,'Dodewaard'),(1190,'Echteld'),(1191,'IJzendoorn'),(1192,'Kesteren'),(1193,'Ochten'),(1194,'Opheusden'),(1195,'Hoevelaken'),(1196,'Nijkerk'),(1197,'Nijkerkerveen'),(1198,'Lent'),(1199,'Nijmegen'),(1200,'Elspeet'),(1201,'Hulshorst'),(1202,'Nunspeet'),(1203,'Vierhouten'),(1204,'\'t Loo'),(1205,'Hattemerbroek'),(1206,'Noordeinde'),(1207,'Oldebroek'),(1208,'Oosterwolde'),(1209,'Wezep'),(1210,'Groenlo'),(1211,'Harreveld'),(1212,'Lichtenvoorde'),(1213,'Lievelde'),(1214,'MariР вЂњР’В«nvelde'),(1215,'Vragender'),(1216,'Zieuwent'),(1217,'Breedenbroek'),(1218,'Etten'),(1219,'Gendringen'),(1220,'Heelweg'),(1221,'Megchelen'),(1222,'Netterden'),(1223,'Silvolde'),(1224,'Sinderen'),(1225,'Terborg'),(1226,'Ulft'),(1227,'Varsselder'),(1228,'Varsseveld'),(1229,'Westendorp'),(1230,'Andelst'),(1231,'Driel'),(1232,'Elst'),(1233,'Hemmen'),(1234,'Herveld'),(1235,'Heteren'),(1236,'Homoet'),(1237,'Oosterhout'),(1238,'Randwijk'),(1239,'Slijk-Ewijk'),(1240,'Valburg'),(1241,'Zetten'),(1242,'Putten'),(1243,'Doorwerth'),(1244,'Heelsum'),(1245,'Heveadorp'),(1246,'Oosterbeek'),(1247,'Renkum'),(1248,'Wolfheze'),(1249,'De Steeg'),(1250,'Dieren'),(1251,'Ellecom'),(1252,'Laag-Soeren'),(1253,'Rheden'),(1254,'Spankeren'),(1255,'Velp'),(1256,'Rozendaal'),(1257,'Scherpenzeel'),(1258,'Kapel Avezaath'),(1259,'Kerk Avezaath'),(1260,'Tiel'),(1261,'Wadenoijen'),(1262,'Klarenbeek'),(1263,'Nijbroek'),(1264,'Steenenkamer'),(1265,'Terwolde'),(1266,'Teuge'),(1267,'Twello'),(1268,'Voorst'),(1269,'Wilp'),(1270,'Wageningen'),(1271,'Acquoy'),(1272,'Asperen'),(1273,'Beesd'),(1274,'Buurmalsen'),(1275,'Deil'),(1276,'Enspijk'),(1277,'Est'),(1278,'Geldermalsen'),(1279,'Gellicum'),(1280,'Haaften'),(1281,'Heesselt'),(1282,'Hellouw'),(1283,'Herwijnen'),(1284,'Heukelum'),(1285,'Meteren'),(1286,'Neerijnen'),(1287,'Ophemert'),(1288,'Opijnen'),(1289,'Rhenoy'),(1290,'Rumpt'),(1291,'Tricht'),(1292,'Tuil'),(1293,'Varik'),(1294,'Vuren'),(1295,'Waardenburg'),(1296,'Zennewijnen'),(1297,'Alphen'),(1298,'Altforst'),(1299,'Appeltern'),(1300,'Beneden-Leeuwen'),(1301,'Boven-Leeuwen'),(1302,'Dreumel'),(1303,'Maasbommel'),(1304,'Wamel'),(1305,'Westervoort'),(1306,'Balgoij'),(1307,'Batenburg'),(1308,'Bergharen'),(1309,'Hernen'),(1310,'Leur'),(1311,'Niftrik'),(1312,'Wijchen'),(1313,'Winterswijk'),(1314,'Winterswijk Brinkheu'),(1315,'Winterswijk Corle'),(1316,'Winterswijk Henxel'),(1317,'Winterswijk Huppel'),(1318,'Winterswijk Kotten'),(1319,'Winterswijk Meddo'),(1320,'Winterswijk Miste'),(1321,'Winterswijk Ratum'),(1322,'Winterswijk Woold'),(1323,'Aalst'),(1324,'Bern'),(1325,'Brakel'),(1326,'Bruchem'),(1327,'Delwijnen'),(1328,'Gameren'),(1329,'Kerkwijk'),(1330,'Nederhemert'),(1331,'Nieuwaal'),(1332,'Poederoijen'),(1333,'Zaltbommel'),(1334,'Zuilichem'),(1335,'Aerdt'),(1336,'Angerlo'),(1337,'Babberich'),(1338,'Giesbeek'),(1339,'Herwen'),(1340,'Lathum'),(1341,'Lobith'),(1342,'Pannerden'),(1343,'Spijk'),(1344,'Tolkamer'),(1345,'Zevenaar'),(1346,'Warnsveld'),(1347,'Zutphen'),(1348,'Amersfoort'),(1349,'Hoogland'),(1350,'Hooglanderveen'),(1351,'Stoutenburg Noord'),(1352,'Baarn'),(1353,'Lage Vuursche'),(1354,'Bunnik'),(1355,'Odijk'),(1356,'Werkhoven'),(1357,'Bunschoten-Spakenbur'),(1358,'Eemdijk'),(1359,'Bilthoven'),(1360,'De Bilt'),(1361,'Groenekan'),(1362,'Hollandsche Rading'),(1363,'Maartensdijk'),(1364,'Westbroek'),(1365,'Abcoude'),(1366,'Amstelhoek'),(1367,'Baambrugge'),(1368,'de Hoef'),(1369,'Mijdrecht'),(1370,'Vinkeveen'),(1371,'Waverveen'),(1372,'Wilnis'),(1373,'Eemnes'),(1374,'\'t Goy'),(1375,'Houten'),(1376,'Schalkwijk'),(1377,'Tull en \'t Waal'),(1378,'IJsselstein'),(1379,'Achterveld'),(1380,'Leusden'),(1381,'Stoutenburg'),(1382,'Benschop'),(1383,'Jaarsveld'),(1384,'Lopik'),(1385,'Lopikerkapel'),(1386,'Polsbroek'),(1387,'Linschoten'),(1388,'Montfoort'),(1389,'Nieuwegein'),(1390,'Hekendorp'),(1391,'Oudewater'),(1392,'Papekop'),(1393,'Snelrewaard'),(1394,'Renswoude'),(1395,'Elst'),(1396,'Rhenen'),(1397,'Soest'),(1398,'Soesterberg'),(1399,'Breukelen'),(1400,'Kockengen'),(1401,'Loenen aan de Vecht'),(1402,'Loenersloot'),(1403,'Maarssen'),(1404,'Nieuwer Ter Aa'),(1405,'Nieuwersluis'),(1406,'Nigtevecht'),(1407,'Oud Zuilen'),(1408,'Tienhoven'),(1409,'Tienhoven (Everdinge'),(1410,'Vreeland'),(1411,'De Meern'),(1412,'Haarzuilens'),(1413,'Utrecht'),(1414,'Vleuten'),(1415,'Amerongen'),(1416,'Doorn'),(1417,'Driebergen-Rijsenbur'),(1418,'Leersum'),(1419,'Maarn'),(1420,'Maarsbergen'),(1421,'Overberg'),(1422,'Veenendaal'),(1423,'Ameide'),(1424,'Everdingen'),(1425,'Hagestein'),(1426,'Hei- en Boeicop'),(1427,'Hoef en Haag'),(1428,'Kedichem'),(1429,'Leerbroek'),(1430,'Leerdam'),(1431,'Lexmond'),(1432,'Meerkerk'),(1433,'Nieuwland'),(1434,'Oosterwijk'),(1435,'Ossenwaard'),(1436,'Schoonrewoerd'),(1437,'Tienhoven aan de Lek'),(1438,'Vianen'),(1439,'Zijderveld'),(1440,'Cothen'),(1441,'Langbroek'),(1442,'Wijk bij Duurstede'),(1443,'Harmelen'),(1444,'Kamerik'),(1445,'Woerden'),(1446,'Zegveld'),(1447,'Woudenberg'),(1448,'Austerlitz'),(1449,'Bosch en Duin'),(1450,'Den Dolder'),(1451,'Huis ter Heide'),(1452,'Zeist'),(1453,'Aalsmeer'),(1454,'Kudelstaart'),(1455,'Alkmaar'),(1456,'De Rijp'),(1457,'Driehuizen'),(1458,'Graft'),(1459,'Grootschermer'),(1460,'Markenbinnen'),(1461,'Noordeinde'),(1462,'Oost-Graftdijk'),(1463,'Oterleek'),(1464,'Oudorp'),(1465,'Schermerhorn'),(1466,'Starnmeer'),(1467,'Stompetoren'),(1468,'Ursem gem. Schermer'),(1469,'West-Graftdijk'),(1470,'Zuidschermer'),(1471,'Amstelveen'),(1472,'Amsterdam'),(1473,'Middenbeemster'),(1474,'Noordbeemster'),(1475,'Westbeemster'),(1476,'Zuidoostbeemster'),(1477,'Bergen'),(1478,'Bergen aan Zee'),(1479,'Egmond aan den Hoef'),(1480,'Egmond aan Zee'),(1481,'Egmond-Binnen'),(1482,'Groet'),(1483,'Schoorl'),(1484,'Beverwijk'),(1485,'Wijk aan Zee'),(1486,'Blaricum'),(1487,'Aerdenhout'),(1488,'Bennebroek'),(1489,'Bloemendaal'),(1490,'Overveen'),(1491,'Vogelenzang'),(1492,'Akersloot'),(1493,'Castricum'),(1494,'de Woude'),(1495,'Limmen'),(1496,'Den Helder'),(1497,'Huisduinen'),(1498,'Julianadorp'),(1499,'Diemen'),(1500,'Hem'),(1501,'Hoogkarspel'),(1502,'Oosterblokker'),(1503,'Oosterleek'),(1504,'Schellinkhout'),(1505,'Venhuizen'),(1506,'Westwoud'),(1507,'Wijdenes'),(1508,'Beets'),(1509,'Edam'),(1510,'Hobrede'),(1511,'Kwadijk'),(1512,'Middelie'),(1513,'Oosthuizen'),(1514,'Schardam'),(1515,'Volendam'),(1516,'Warder'),(1517,'Enkhuizen'),(1518,'Bussum'),(1519,'Muiden'),(1520,'Muiderberg'),(1521,'Naarden'),(1522,'Haarlem'),(1523,'Spaarndam gem. Haarl'),(1524,'Aalsmeerderbrug'),(1525,'Abbenes'),(1526,'Badhoevedorp'),(1527,'Beinsdorp'),(1528,'Boesingheliede'),(1529,'Buitenkaag'),(1530,'Burgerveen'),(1531,'Cruquius'),(1532,'Haarlemmerliede'),(1533,'Halfweg'),(1534,'Hoofddorp'),(1535,'Leimuiderbrug'),(1536,'Lijnden'),(1537,'Lisserbroek'),(1538,'Nieuw-Vennep'),(1539,'Oude Meer'),(1540,'Rijsenhout'),(1541,'Rozenburg'),(1542,'Schiphol'),(1543,'Schiphol-Rijk'),(1544,'Spaarndam'),(1545,'Vijfhuizen'),(1546,'Weteringbrug'),(1547,'Zwaanshoek'),(1548,'Zwanenburg'),(1549,'Heemskerk'),(1550,'Heemstede'),(1551,'Heerhugowaard'),(1552,'Heiloo'),(1553,'Hilversum'),(1554,'\'t Veld'),(1555,'Anna Paulowna'),(1556,'Barsingerhorn'),(1557,'Breezand'),(1558,'Den Oever'),(1559,'Haringhuizen'),(1560,'Hippolytushoef'),(1561,'Kolhorn'),(1562,'Kreileroord'),(1563,'Lutjewinkel'),(1564,'Middenmeer'),(1565,'Nieuwe Niedorp'),(1566,'Oude Niedorp'),(1567,'Slootdorp'),(1568,'Westerland'),(1569,'Wieringerwaard'),(1570,'Wieringerwerf'),(1571,'Winkel'),(1572,'Zijdewind'),(1573,'Blokker'),(1574,'Hoorn'),(1575,'Zwaag'),(1576,'Huizen'),(1577,'Avenhorn'),(1578,'Berkhout'),(1579,'De Goorn'),(1580,'Hensbroek'),(1581,'Obdam'),(1582,'Oudendijk'),(1583,'Scharwoude'),(1584,'Spierdijk'),(1585,'Ursem'),(1586,'Zuidermeer'),(1587,'Den Ilp'),(1588,'Landsmeer'),(1589,'Purmerland'),(1590,'Broek op Langedijk'),(1591,'Koedijk'),(1592,'Noord-Scharwoude'),(1593,'Sint Pancras'),(1594,'Zuid-Scharwoude'),(1595,'Laren'),(1596,'Abbekerk'),(1597,'Andijk'),(1598,'Benningbroek'),(1599,'Hauwert'),(1600,'Lambertschaag'),(1601,'Medemblik'),(1602,'Midwoud'),(1603,'Nibbixwoud'),(1604,'Oostwoud'),(1605,'Opperdoes'),(1606,'Sijbekarspel'),(1607,'Twisk'),(1608,'Wervershoof'),(1609,'Wognum'),(1610,'Zwaagdijk-Oost'),(1611,'Zwaagdijk-West'),(1612,'Oostzaan'),(1613,'Aartswoud'),(1614,'De Weere'),(1615,'Hoogwoud'),(1616,'Opmeer'),(1617,'Spanbroek'),(1618,'Amsterdam-Duivendrec'),(1619,'Duivendrecht'),(1620,'Ouderkerk aan de Ams'),(1621,'Purmerend'),(1622,'\'t Zand'),(1623,'Burgerbrug'),(1624,'Callantsoog'),(1625,'Dirkshorn'),(1626,'Oudesluis'),(1627,'Oudkarspel'),(1628,'Petten'),(1629,'Schagen'),(1630,'Schagerbrug'),(1631,'Sint Maarten'),(1632,'Sint Maartensbrug'),(1633,'Sint Maartensvlotbru'),(1634,'Tuitjenhorn'),(1635,'Waarland'),(1636,'Warmenhuizen'),(1637,'Bovenkarspel'),(1638,'Grootebroek'),(1639,'Lutjebroek'),(1640,'De Cocksdorp'),(1641,'De Koog'),(1642,'De Waal'),(1643,'Den Burg'),(1644,'Den Hoorn'),(1645,'Oosterend'),(1646,'Oudeschild'),(1647,'Uitgeest'),(1648,'De Kwakel'),(1649,'Uithoorn'),(1650,'Driehuis'),(1651,'IJmuiden'),(1652,'Santpoort-Noord'),(1653,'Santpoort-Zuid'),(1654,'Velsen-Noord'),(1655,'Velsen-Zuid'),(1656,'Velserbroek'),(1657,'Broek in Waterland'),(1658,'Ilpendam'),(1659,'Katwoude'),(1660,'Marken'),(1661,'Monnickendam'),(1662,'Purmer'),(1663,'Uitdam'),(1664,'Watergang'),(1665,'Zuiderwoude'),(1666,'Weesp'),(1667,'\'s-Graveland'),(1668,'Ankeveen'),(1669,'Breukeleveen'),(1670,'Kortenhoef'),(1671,'Loosdrecht'),(1672,'Nederhorst den Berg'),(1673,'Jisp'),(1674,'Oostknollendam'),(1675,'Spijkerboor'),(1676,'Wijdewormer'),(1677,'Wormer'),(1678,'Assendelft'),(1679,'Koog aan de Zaan'),(1680,'Krommenie'),(1681,'Westknollendam'),(1682,'Westzaan'),(1683,'Wormerveer'),(1684,'Zaandam'),(1685,'Zaandijk'),(1686,'Bentveld'),(1687,'Zandvoort'),(1688,'Alblasserdam'),(1689,'Poortugaal'),(1690,'Rhoon'),(1691,'Rotterdam-Albrandswa'),(1692,'Aarlanderveen'),(1693,'Alphen aan den Rijn'),(1694,'Benthuizen'),(1695,'Boskoop'),(1696,'Hazerswoude-Dorp'),(1697,'Hazerswoude-Rijndijk'),(1698,'Koudekerk aan den Ri'),(1699,'Zwammerdam'),(1700,'Barendrecht'),(1701,'Bodegraven'),(1702,'Driebruggen'),(1703,'Nieuwerbrug aan den '),(1704,'Reeuwijk'),(1705,'Waarder'),(1706,'Brielle'),(1707,'Vierpolders'),(1708,'Zwartewaal'),(1709,'Capelle aan den IJss'),(1710,'Delft'),(1711,'\'s-Gravenhage'),(1712,'Den Haag'),(1713,'Dordrecht'),(1714,'Achthuizen'),(1715,'Den Bommel'),(1716,'Dirksland'),(1717,'Goedereede'),(1718,'Herkingen'),(1719,'Melissant'),(1720,'Middelharnis'),(1721,'Nieuwe-Tonge'),(1722,'Ooltgensplaat'),(1723,'Ouddorp'),(1724,'Oude-Tonge'),(1725,'Sommelsdijk'),(1726,'Stad aan \'t Haringvl'),(1727,'Stellendam'),(1728,'Dalem'),(1729,'Gorinchem'),(1730,'Gouda'),(1731,'Hardinxveld-Giessend'),(1732,'Hellevoetsluis'),(1733,'Oudenhoorn'),(1734,'Hendrik-Ido-Ambacht'),(1735,'Hillegom'),(1736,'\'s-Gravendeel'),(1737,'Goudswaard'),(1738,'Heinenoord'),(1739,'Klaaswaal'),(1740,'Maasdam'),(1741,'Mijnsheerenland'),(1742,'Mookhoek'),(1743,'Nieuw-Beijerland'),(1744,'Numansdorp'),(1745,'Oud-Beijerland'),(1746,'Piershil'),(1747,'Puttershoek'),(1748,'Strijen'),(1749,'Strijensas'),(1750,'Westmaas'),(1751,'Zuid-Beijerland'),(1752,'Hoogmade'),(1753,'Kaag'),(1754,'Leimuiden'),(1755,'Nieuwe Wetering'),(1756,'Oud Ade'),(1757,'Oude Wetering'),(1758,'Rijnsaterwoude'),(1759,'Rijpwetering'),(1760,'Roelofarendsveen'),(1761,'Woubrugge'),(1762,'Katwijk'),(1763,'Rijnsburg'),(1764,'Valkenburg'),(1765,'Krimpen aan den IJss'),(1766,'Ammerstol'),(1767,'Bergambacht'),(1768,'Berkenwoude'),(1769,'Gouderak'),(1770,'Haastrecht'),(1771,'Krimpen aan de Lek'),(1772,'Lekkerkerk'),(1773,'Ouderkerk aan den IJ'),(1774,'Schoonhoven'),(1775,'Stolwijk'),(1776,'Vlist'),(1777,'Bergschenhoek'),(1778,'Berkel en Rodenrijs'),(1779,'Bleiswijk'),(1780,'Leiden'),(1781,'Leiderdorp'),(1782,'Leidschendam'),(1783,'Voorburg'),(1784,'Lisse'),(1785,'Maassluis'),(1786,'Den Hoorn'),(1787,'Maasland'),(1788,'Schipluiden'),(1789,'Arkel'),(1790,'Bleskensgraaf ca'),(1791,'Brandwijk'),(1792,'Giessenburg'),(1793,'Goudriaan'),(1794,'Groot-Ammers'),(1795,'Hoogblokland'),(1796,'Hoornaar'),(1797,'Kinderdijk'),(1798,'Langerak'),(1799,'Molenaarsgraaf'),(1800,'Nieuw-Lekkerland'),(1801,'Nieuwpoort'),(1802,'Noordeloos'),(1803,'Ottoland'),(1804,'Oud-Alblas'),(1805,'Schelluinen'),(1806,'Streefkerk'),(1807,'Waal'),(1808,'Wijngaarden'),(1809,'Nieuwkoop'),(1810,'Nieuwveen'),(1811,'Noorden'),(1812,'Ter Aar'),(1813,'Vrouwenakker'),(1814,'Woerdense Verlaat'),(1815,'Zevenhoven'),(1816,'Abbenbroek'),(1817,'Geervliet'),(1818,'Heenvliet'),(1819,'Hekelingen'),(1820,'Simonshaven'),(1821,'Spijkenisse'),(1822,'Zuidland'),(1823,'De Zilk'),(1824,'Noordwijk'),(1825,'Noordwijkerhout'),(1826,'Oegstgeest'),(1827,'Papendrecht'),(1828,'Delfgauw'),(1829,'Nootdorp'),(1830,'Pijnacker'),(1831,'Ridderkerk'),(1832,'Rijswijk'),(1833,'Botlek Rotterdam'),(1834,'Europoort Rotterdam'),(1835,'Hoek van Holland'),(1836,'Hoogvliet Rotterdam'),(1837,'Maasvlakte Rotterdam'),(1838,'Pernis Rotterdam'),(1839,'Rotterdam'),(1840,'Rozenburg'),(1841,'Vondelingenplaat Rot'),(1842,'Schiedam'),(1843,'Sliedrecht'),(1844,'Sassenheim'),(1845,'Voorhout'),(1846,'Warmond'),(1847,'Vlaardingen'),(1848,'Voorschoten'),(1849,'Waddinxveen'),(1850,'Wassenaar'),(1851,'\'s-Gravenzande'),(1852,'De Lier'),(1853,'Honselersdijk'),(1854,'Kwintsheul'),(1855,'Maasdijk'),(1856,'Monster'),(1857,'Naaldwijk'),(1858,'Poeldijk'),(1859,'Ter Heijde'),(1860,'Wateringen'),(1861,'Oostvoorne'),(1862,'Rockanje'),(1863,'Tinte'),(1864,'Zoetermeer'),(1865,'Gelderswoude'),(1866,'Zoeterwoude'),(1867,'Moerkapelle'),(1868,'Moordrecht'),(1869,'Nieuwerkerk aan den '),(1870,'Zevenhuizen'),(1871,'Heerjansdam'),(1872,'Zwijndrecht'),(1873,'\'s-Gravenpolder'),(1874,'\'s-Heer Abtskerke'),(1875,'\'s-Heerenhoek'),(1876,'Baarland'),(1877,'Borssele'),(1878,'Driewegen'),(1879,'Ellewoutsdijk'),(1880,'Heinkenszand'),(1881,'Hoedekenskerke'),(1882,'Kwadendamme'),(1883,'Lewedorp'),(1884,'Nieuwdorp'),(1885,'Nisse'),(1886,'Oudelande'),(1887,'Ovezande'),(1888,'\'s-Heer Arendskerke'),(1889,'\'s-Heer Hendrikskind'),(1890,'Goes'),(1891,'Kattendijke'),(1892,'Wilhelminadorp'),(1893,'Wolphaartsdijk'),(1894,'Clinge'),(1895,'Graauw'),(1896,'Heikant'),(1897,'Hengstdijk'),(1898,'Hulst'),(1899,'Kapellebrug'),(1900,'Kloosterzande'),(1901,'Kuitaart'),(1902,'Lamswaarde'),(1903,'Nieuw-Namen'),(1904,'Ossenisse'),(1905,'Sint Jansteen'),(1906,'Terhole'),(1907,'Vogelwaarde'),(1908,'Walsoorden'),(1909,'Kapelle'),(1910,'Kloetinge'),(1911,'Schore'),(1912,'Wemeldinge'),(1913,'Arnemuiden'),(1914,'Middelburg'),(1915,'Nieuw- en Sint Joosl'),(1916,'Colijnsplaat'),(1917,'Geersdijk'),(1918,'Kamperland'),(1919,'Kats'),(1920,'Kortgene'),(1921,'Wissenkerke'),(1922,'Hansweert'),(1923,'Krabbendijke'),(1924,'Kruiningen'),(1925,'Oostdijk'),(1926,'Rilland'),(1927,'Waarde'),(1928,'Yerseke'),(1929,'Brouwershaven'),(1930,'Bruinisse'),(1931,'Burgh-Haamstede'),(1932,'Dreischor'),(1933,'Ellemeet'),(1934,'Kerkwerve'),(1935,'Nieuwerkerk'),(1936,'Noordgouwe'),(1937,'Noordwelle'),(1938,'Oosterland'),(1939,'Ouwerkerk'),(1940,'Renesse'),(1941,'Scharendijke'),(1942,'Sirjansland'),(1943,'Zierikzee'),(1944,'Zonnemaire'),(1945,'Aardenburg'),(1946,'Breskens'),(1947,'Cadzand'),(1948,'Eede'),(1949,'Groede'),(1950,'Hoofdplaat'),(1951,'IJzendijke'),(1952,'Nieuwvliet'),(1953,'Oostburg'),(1954,'Retranchement'),(1955,'Schoondijke'),(1956,'Sint Kruis'),(1957,'Sluis'),(1958,'Waterlandkerkje'),(1959,'Zuidzande'),(1960,'Axel'),(1961,'Biervliet'),(1962,'Hoek'),(1963,'Koewacht'),(1964,'Overslag'),(1965,'Philippine'),(1966,'Sas van Gent'),(1967,'Sluiskil'),(1968,'Spui'),(1969,'Terneuzen'),(1970,'Westdorpe'),(1971,'Zaamslag'),(1972,'Zuiddorpe'),(1973,'Oud-Vossemeer'),(1974,'Poortvliet'),(1975,'Scherpenisse'),(1976,'Sint-Annaland'),(1977,'Sint-Maartensdijk'),(1978,'Sint Philipsland'),(1979,'Stavenisse'),(1980,'Tholen'),(1981,'Aagtekerke'),(1982,'Biggekerke'),(1983,'Domburg'),(1984,'Gapinge'),(1985,'Grijpskerke'),(1986,'Koudekerke'),(1987,'Meliskerke'),(1988,'Oostkapelle'),(1989,'Serooskerke'),(1990,'Veere'),(1991,'Vrouwenpolder'),(1992,'Westkapelle'),(1993,'Zoutelande'),(1994,'Oost-Souburg'),(1995,'Ritthem'),(1996,'Vlissingen'),(1997,'\'s-Hertogenbosch'),(1998,'Den Bosch'),(1999,'Nuland'),(2000,'Rosmalen'),(2001,'Alphen'),(2002,'Bavel AC'),(2003,'Chaam'),(2004,'Galder'),(2005,'Strijbeek'),(2006,'Ulvenhout AC'),(2007,'Almkerk'),(2008,'Andel'),(2009,'BabyloniР вЂњР’В«nbr'),(2010,'Drongelen'),(2011,'Dussen'),(2012,'Eethen'),(2013,'Genderen'),(2014,'Giessen'),(2015,'Hank'),(2016,'Meeuwen'),(2017,'Nieuwendijk'),(2018,'Rijswijk (NB)'),(2019,'Sleeuwijk'),(2020,'Uitwijk'),(2021,'Veen'),(2022,'Waardhuizen'),(2023,'Werkendam'),(2024,'Wijk en Aalburg'),(2025,'Woudrichem'),(2026,'Asten'),(2027,'Ommel'),(2028,'Baarle-Nassau'),(2029,'Castelre'),(2030,'Ulicoten'),(2031,'Bergeijk'),(2032,'Luyksgestel'),(2033,'Riethoven'),(2034,'Westerhoven'),(2035,'Bergen op Zoom'),(2036,'Halsteren'),(2037,'Lepelstraat'),(2038,'Heesch'),(2039,'Heeswijk-Dinther'),(2040,'Loosbroek'),(2041,'Nistelrode'),(2042,'Vinkel'),(2043,'Vorstenbosch'),(2044,'Best'),(2045,'Bladel'),(2046,'Casteren'),(2047,'Hapert'),(2048,'Hoogeloon'),(2049,'Netersel'),(2050,'Boekel'),(2051,'Venhorst'),(2052,'Beugen'),(2053,'Boxmeer'),(2054,'Groeningen'),(2055,'Holthees'),(2056,'Maashees'),(2057,'Oeffelt'),(2058,'Overloon'),(2059,'Rijkevoort'),(2060,'Sambeek'),(2061,'Vierlingsbeek'),(2062,'Vortum-Mullem'),(2063,'Boxtel'),(2064,'Liempde'),(2065,'Bavel'),(2066,'Breda'),(2067,'Prinsenbeek'),(2068,'Teteringen'),(2069,'Ulvenhout'),(2070,'Budel'),(2071,'Budel-Dorplein'),(2072,'Budel-Schoot'),(2073,'Gastel'),(2074,'Maarheeze'),(2075,'Soerendonk'),(2076,'Beers'),(2077,'Cuijk'),(2078,'Haps'),(2079,'Katwijk'),(2080,'Linden'),(2081,'Sint Agatha'),(2082,'Vianen'),(2083,'Deurne'),(2084,'Helenaveen'),(2085,'Liessel'),(2086,'Neerkant'),(2087,'Vlierden'),(2088,'\'s Gravenmoer'),(2089,'Dongen'),(2090,'Drimmelen'),(2091,'Hooge Zwaluwe'),(2092,'Lage Zwaluwe'),(2093,'Made'),(2094,'Terheijden'),(2095,'Wagenberg'),(2096,'Duizel'),(2097,'Eersel'),(2098,'Knegsel'),(2099,'Steensel'),(2100,'Vessem'),(2101,'Wintelre'),(2102,'Eindhoven'),(2103,'Etten-Leur'),(2104,'Geertruidenberg'),(2105,'Raamsdonk'),(2106,'Raamsdonksveer'),(2107,'Geldrop'),(2108,'Mierlo'),(2109,'Bakel'),(2110,'De Mortel'),(2111,'De Rips'),(2112,'Elsendorp'),(2113,'Gemert'),(2114,'Handel'),(2115,'Milheeze'),(2116,'Gilze'),(2117,'Hulten'),(2118,'Molenschot'),(2119,'Rijen'),(2120,'Goirle'),(2121,'Riel'),(2122,'Escharen'),(2123,'Gassel'),(2124,'Grave'),(2125,'Velp'),(2126,'Biezenmortel'),(2127,'Esch'),(2128,'Haaren'),(2129,'Helvoirt'),(2130,'Bosschenhoofd'),(2131,'Hoeven'),(2132,'Oud Gastel'),(2133,'Oudenbosch'),(2134,'Stampersgat'),(2135,'Heeze'),(2136,'Leende'),(2137,'Sterksel'),(2138,'Helmond'),(2139,'Doeveren'),(2140,'Drunen'),(2141,'Elshout'),(2142,'Haarsteeg'),(2143,'Hedikhuizen'),(2144,'Heesbeen'),(2145,'Herpt'),(2146,'Heusden'),(2147,'Nieuwkuijk'),(2148,'Oudheusden'),(2149,'Vlijmen'),(2150,'Biest-Houtakker'),(2151,'Diessen'),(2152,'Esbeek'),(2153,'Haghorst'),(2154,'Hilvarenbeek'),(2155,'Aarle-Rixtel'),(2156,'Beek en Donk'),(2157,'Lieshout'),(2158,'Mariahout'),(2159,'Reek'),(2160,'Schaijk'),(2161,'Zeeland'),(2162,'De Moer'),(2163,'Kaatsheuvel'),(2164,'Loon op Zand'),(2165,'Erp'),(2166,'Schijndel'),(2167,'Sint-Oedenrode'),(2168,'Veghel'),(2169,'Langenboom'),(2170,'Mill'),(2171,'Sint Hubert'),(2172,'Wilbertoord'),(2173,'Fijnaart'),(2174,'Heijningen'),(2175,'Klundert'),(2176,'Langeweg'),(2177,'Moerdijk'),(2178,'Noordhoek'),(2179,'Oudemolen'),(2180,'Standdaarbuiten'),(2181,'Willemstad'),(2182,'Zevenbergen'),(2183,'Zevenbergschen Hoek'),(2184,'Nuenen'),(2185,'Oirschot'),(2186,'Oost West en Middelb'),(2187,'Heukelom'),(2188,'Moergestel'),(2189,'Oisterwijk'),(2190,'Den Hout'),(2191,'Dorst'),(2192,'Oosteind'),(2193,'Oosterhout'),(2194,'Berghem'),(2195,'Demen'),(2196,'Deursen-Dennenburg'),(2197,'Dieden'),(2198,'Geffen'),(2199,'Haren'),(2200,'Herpen'),(2201,'Huisseling'),(2202,'Keent'),(2203,'Koolwijk'),(2204,'Lith'),(2205,'Lithoijen'),(2206,'Macharen'),(2207,'Maren-Kessel'),(2208,'Megen'),(2209,'Neerlangel'),(2210,'Neerloon'),(2211,'Oijen'),(2212,'Oss'),(2213,'Overlangel'),(2214,'Ravenstein'),(2215,'Teeffelen'),(2216,'Hooge Mierde'),(2217,'Hulsel'),(2218,'Lage Mierde'),(2219,'Reusel'),(2220,'Heerle'),(2221,'Moerstraten'),(2222,'Nispen'),(2223,'Roosendaal'),(2224,'Wouw'),(2225,'Wouwse Plantage'),(2226,'Rucphen'),(2227,'Schijf'),(2228,'Sprundel'),(2229,'St. Willebrord'),(2230,'Zegge'),(2231,'Landhorst'),(2232,'Ledeacker'),(2233,'Oploo'),(2234,'Rijkevoort-De Walser'),(2235,'Sint Anthonis'),(2236,'Stevensbeek'),(2237,'Wanroij'),(2238,'Westerbeek'),(2239,'Berlicum'),(2240,'Den Dungen'),(2241,'Gemonde'),(2242,'Sint-Michielsgestel'),(2243,'Lierop'),(2244,'Someren'),(2245,'Son en Breugel'),(2246,'De Heen'),(2247,'Dinteloord'),(2248,'Kruisland'),(2249,'Nieuw-Vossemeer'),(2250,'Steenbergen'),(2251,'Berkel-Enschot'),(2252,'Tilburg'),(2253,'Udenhout'),(2254,'Odiliapeel'),(2255,'Uden'),(2256,'Volkel'),(2257,'Valkenswaard'),(2258,'Veldhoven'),(2259,'Cromvoirt'),(2260,'Vught'),(2261,'Waalre'),(2262,'Sprang-Capelle'),(2263,'Waalwijk'),(2264,'Waspik'),(2265,'Hoogerheide'),(2266,'Huijbergen'),(2267,'Ossendrecht'),(2268,'Putte'),(2269,'Woensdrecht'),(2270,'Achtmaal'),(2271,'Klein Zundert'),(2272,'Rijsbergen'),(2273,'Wernhout'),(2274,'Zundert'),(2275,'Beek'),(2276,'Maastricht-Airport'),(2277,'Spaubeek'),(2278,'Amstenrade'),(2279,'Bingelrade'),(2280,'Doenrade'),(2281,'Hulsberg'),(2282,'Jabeek'),(2283,'Merkelbeek'),(2284,'Nuth'),(2285,'Oirsbeek'),(2286,'Puth'),(2287,'Schimmert'),(2288,'Schinnen'),(2289,'Schinveld'),(2290,'Sweikhuizen'),(2291,'Wijnandsrade'),(2292,'Beesel'),(2293,'Reuver'),(2294,'Afferden'),(2295,'Bergen'),(2296,'Siebengewald'),(2297,'Well'),(2298,'Wellerlooi'),(2299,'Brunssum'),(2300,'Echt'),(2301,'Koningsbosch'),(2302,'Maria Hoop'),(2303,'Nieuwstadt'),(2304,'Roosteren'),(2305,'Sint Joost'),(2306,'Susteren'),(2307,'Banholt'),(2308,'Bemelen'),(2309,'Cadier en Keer'),(2310,'Eckelrade'),(2311,'Eijsden'),(2312,'Gronsveld'),(2313,'Margraten'),(2314,'Mheer'),(2315,'Noorbeek'),(2316,'Scheulder'),(2317,'Sint Geertruid'),(2318,'Gennep'),(2319,'Heijen'),(2320,'Milsbeek'),(2321,'Ottersum'),(2322,'Ven-Zelderheide'),(2323,'Beutenaken'),(2324,'Elkenrade'),(2325,'Epen'),(2326,'Eys'),(2327,'Gulpen'),(2328,'Heijenrath'),(2329,'Ingber'),(2330,'Mechelen'),(2331,'Reijmerstok'),(2332,'Slenaken'),(2333,'Wijlre'),(2334,'Wittem'),(2335,'Heerlen'),(2336,'Hoensbroek'),(2337,'America'),(2338,'Broekhuizen'),(2339,'Broekhuizenvorst'),(2340,'Evertsoord'),(2341,'Griendtsveen'),(2342,'Grubbenvorst'),(2343,'Hegelsom'),(2344,'Horst'),(2345,'Kronenberg'),(2346,'Lottum'),(2347,'Meerlo'),(2348,'Melderslo'),(2349,'Meterik'),(2350,'Sevenum'),(2351,'Swolgen'),(2352,'Tienray'),(2353,'Eygelshoven'),(2354,'Kerkrade'),(2355,'Landgraaf'),(2356,'Baexem'),(2357,'Buggenum'),(2358,'Ell'),(2359,'Grathem'),(2360,'Haelen'),(2361,'Haler'),(2362,'Heibloem'),(2363,'Heythuysen'),(2364,'Horn'),(2365,'Hunsel'),(2366,'Ittervoort'),(2367,'Kelpen-Oler'),(2368,'Neer'),(2369,'Neeritter'),(2370,'Nunhem'),(2371,'Roggel'),(2372,'Beegden'),(2373,'Heel'),(2374,'Linne'),(2375,'Maasbracht'),(2376,'OhР вЂњР’В© en Laak'),(2377,'Stevensweert'),(2378,'Thorn'),(2379,'Wessem'),(2380,'Maastricht'),(2381,'Bunde'),(2382,'Geulle'),(2383,'Meerssen'),(2384,'Moorveld'),(2385,'Ulestraten'),(2386,'Middelaar'),(2387,'Molenhoek'),(2388,'Mook'),(2389,'Plasmolen'),(2390,'Leveroy'),(2391,'Nederweert'),(2392,'Nederweert-Eind'),(2393,'Ospel'),(2394,'Baarlo'),(2395,'Beringe'),(2396,'Egchel'),(2397,'Grashoek'),(2398,'Helden'),(2399,'Kessel'),(2400,'Koningslust'),(2401,'Maasbree'),(2402,'Meijel'),(2403,'Panningen'),(2404,'Herkenbosch'),(2405,'Melick'),(2406,'Montfort'),(2407,'Posterholt'),(2408,'Sint OdiliР вЂњР’В«n'),(2409,'Vlodrop'),(2410,'Herten'),(2411,'Roermond'),(2412,'Swalmen'),(2413,'Baneheide'),(2414,'Bocholtz'),(2415,'Simpelveld'),(2416,'Born'),(2417,'Buchten'),(2418,'Einighausen'),(2419,'Geleen'),(2420,'Grevenbicht'),(2421,'Guttecoven'),(2422,'Holtum'),(2423,'Limbricht'),(2424,'Munstergeleen'),(2425,'Obbicht'),(2426,'Papenhoven'),(2427,'Sittard'),(2428,'Windraak'),(2429,'Elsloo'),(2430,'Stein'),(2431,'Urmond'),(2432,'Lemiers'),(2433,'Vaals'),(2434,'Vijlen'),(2435,'Berg en Terblijt'),(2436,'Schin op Geul'),(2437,'Valkenburg'),(2438,'Walem'),(2439,'Arcen'),(2440,'Belfeld'),(2441,'Lomm'),(2442,'Steyl'),(2443,'Tegelen'),(2444,'Velden'),(2445,'Venlo'),(2446,'Blitterswijck'),(2447,'Castenray'),(2448,'Geijsteren'),(2449,'Heide'),(2450,'Leunen'),(2451,'Merselo'),(2452,'Oirlo'),(2453,'Oostrum'),(2454,'Smakt'),(2455,'Venray'),(2456,'Veulen'),(2457,'Vredepeel'),(2458,'Wanssum'),(2459,'Ysselsteyn'),(2460,'Klimmen'),(2461,'Ransdaal'),(2462,'Voerendaal'),(2463,'Stramproy'),(2464,'Weert');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credentials`
--

DROP TABLE IF EXISTS `credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `credentials` (
  `customer_id` int DEFAULT NULL,
  `username` varchar(50) NOT NULL,
  `password` char(64) NOT NULL,
  `salt` char(32) NOT NULL,
  PRIMARY KEY (`username`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `credentials_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credentials`
--

LOCK TABLES `credentials` WRITE;
/*!40000 ALTER TABLE `credentials` DISABLE KEYS */;
INSERT INTO `credentials` VALUES (18,'jancik','e95b73b1dcec7abf6c3cf39da301a208ba1081f9a7686ba54f6d505141359a8e','6104297a'),(19,'mw','bb9560804a99c228987b719d5d4c9f4d3bed3e72bcad72461f9600befea1f3ce','4e8a947e'),(16,'nikita','8617c96e1825c193a31ec2f8ab56650bfee01721f59759f6965ebb85440ba001','50ff7907'),(17,'ope','95bedd060987319ae3744b3e6385590e8e1257fe733ffc3a2d74e0910fbd7b4b','07bd7d81'),(15,'tim','2be01e15bbd8891ec1497521b290bd508511eaec94a60405ab17bbe5dd63a41d','dbb7ccb7');
/*!40000 ALTER TABLE `credentials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `gender_id` int NOT NULL,
  `birthdate` date DEFAULT NULL,
  `phone` varchar(18) DEFAULT NULL,
  `address` int NOT NULL,
  `number_orders` int DEFAULT '0',
  `discount_for_next` float DEFAULT '0',
  PRIMARY KEY (`customer_id`),
  KEY `fk_gender` (`gender_id`),
  CONSTRAINT `fk_gender` FOREIGN KEY (`gender_id`) REFERENCES `gender` (`gender_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (15,'Timur','Jercak',1,'1998-06-13','12345',2,11,0),(16,'Nikita','Bulgaru',1,'2004-08-28','+12345',2,39,0),(17,'Robert','Oppenheimer',1,'1904-03-23','43784',3,7,0),(18,'Jana','Olaf',2,'1969-10-30','92834',4,1,0),(19,'Mike','Wazowski',1,'2024-10-03','23421',5,1,0);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_address`
--

DROP TABLE IF EXISTS `customer_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_address` (
  `customer_address_id` int NOT NULL AUTO_INCREMENT,
  `house_number` int DEFAULT NULL,
  `apartment_number` varchar(8) DEFAULT NULL,
  `postal_code_id` int DEFAULT NULL,
  `city_id` int DEFAULT '2380',
  PRIMARY KEY (`customer_address_id`),
  KEY `postal_code_id` (`postal_code_id`),
  KEY `city_id` (`city_id`),
  CONSTRAINT `customer_address_ibfk_1` FOREIGN KEY (`postal_code_id`) REFERENCES `postal_codes` (`ID`),
  CONSTRAINT `customer_address_ibfk_2` FOREIGN KEY (`city_id`) REFERENCES `cities` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_address`
--

LOCK TABLES `customer_address` WRITE;
/*!40000 ALTER TABLE `customer_address` DISABLE KEYS */;
INSERT INTO `customer_address` VALUES (1,23,'4',96,2380),(2,12,'1',12,2380),(3,12,'2',41,2380),(4,2,'1',95,2380),(5,12,'12',97,2380);
/*!40000 ALTER TABLE `customer_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery_status`
--

DROP TABLE IF EXISTS `delivery_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_status` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `status` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_status`
--

LOCK TABLES `delivery_status` WRITE;
/*!40000 ALTER TABLE `delivery_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `delivery_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deliverymen`
--

DROP TABLE IF EXISTS `deliverymen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deliverymen` (
  `employee_id` int NOT NULL,
  `restaurant_id` int NOT NULL,
  `availability` tinyint(1) DEFAULT NULL,
  `number_of_deliveries` int DEFAULT NULL,
  `last_delivery_time` datetime DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `deliverymen_ibfk_1` (`restaurant_id`),
  CONSTRAINT `deliverymen_ibfk_1` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deliverymen`
--

LOCK TABLES `deliverymen` WRITE;
/*!40000 ALTER TABLE `deliverymen` DISABLE KEYS */;
INSERT INTO `deliverymen` VALUES (26,1,1,1,NULL),(27,1,1,1,NULL),(28,1,1,1,NULL),(29,1,1,1,NULL),(30,2,1,1,NULL),(31,2,1,1,NULL),(32,2,1,1,NULL),(33,2,1,1,NULL),(34,3,1,1,NULL),(35,3,1,1,NULL),(36,3,1,1,NULL),(37,3,1,1,NULL),(38,4,1,1,NULL),(39,4,1,1,NULL),(40,4,1,1,NULL),(41,4,1,1,NULL),(42,5,1,1,NULL),(43,5,1,1,NULL),(44,5,1,1,NULL),(45,5,1,1,NULL);
/*!40000 ALTER TABLE `deliverymen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deserts`
--

DROP TABLE IF EXISTS `deserts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deserts` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deserts`
--

LOCK TABLES `deserts` WRITE;
/*!40000 ALTER TABLE `deserts` DISABLE KEYS */;
/*!40000 ALTER TABLE `deserts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drinks`
--

DROP TABLE IF EXISTS `drinks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drinks` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drinks`
--

LOCK TABLES `drinks` WRITE;
/*!40000 ALTER TABLE `drinks` DISABLE KEYS */;
/*!40000 ALTER TABLE `drinks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_address`
--

DROP TABLE IF EXISTS `employee_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_address` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `house_number` int DEFAULT NULL,
  `postal_code_id` int DEFAULT NULL,
  `city_id` int DEFAULT '2380',
  PRIMARY KEY (`ID`),
  KEY `postal_code_id` (`postal_code_id`),
  KEY `city_id` (`city_id`),
  CONSTRAINT `employee_address_ibfk_1` FOREIGN KEY (`postal_code_id`) REFERENCES `postal_codes` (`ID`),
  CONSTRAINT `employee_address_ibfk_2` FOREIGN KEY (`city_id`) REFERENCES `cities` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_address`
--

LOCK TABLES `employee_address` WRITE;
/*!40000 ALTER TABLE `employee_address` DISABLE KEYS */;
INSERT INTO `employee_address` VALUES (1,101,21,2380),(2,102,53,2380),(3,103,4,2380),(4,104,56,2380),(5,105,74,2380),(6,106,6,2380),(7,107,4,2380),(8,108,1,2380),(9,109,90,2380),(10,110,58,2380),(11,111,21,2380),(12,112,26,2380),(13,113,66,2380),(14,114,57,2380),(15,115,85,2380),(16,116,62,2380),(17,117,54,2380),(18,118,84,2380),(19,119,64,2380),(20,120,65,2380),(21,121,37,2380),(22,122,87,2380),(23,123,31,2380),(24,124,87,2380),(25,125,53,2380),(26,101,46,2380),(27,102,47,2380),(28,103,48,2380),(29,104,49,2380),(30,105,50,2380),(31,106,51,2380),(32,107,52,2380),(33,108,53,2380),(34,109,54,2380),(35,110,55,2380),(36,111,56,2380),(37,112,57,2380),(38,113,58,2380),(39,114,59,2380),(40,115,60,2380),(41,116,61,2380),(42,117,62,2380),(43,118,63,2380),(44,119,64,2380),(45,120,65,2380);
/*!40000 ALTER TABLE `employee_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_credentials`
--

DROP TABLE IF EXISTS `employee_credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_credentials` (
  `employee_credentials_id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `password` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`employee_credentials_id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_credentials`
--

LOCK TABLES `employee_credentials` WRITE;
/*!40000 ALTER TABLE `employee_credentials` DISABLE KEYS */;
INSERT INTO `employee_credentials` VALUES (1,'j.doe@lagoal.pizza','12345'),(2,'j.smith@lagoal.pizza','12345'),(3,'b.johnson@lagoal.pizza','12345'),(4,'a.davis@lagoal.pizza','12345'),(5,'c.brown@lagoal.pizza','12345'),(6,'e.wilson@lagoal.pizza','12345'),(7,'f.moore@lagoal.pizza','12345'),(8,'g.taylor@lagoal.pizza','12345'),(9,'h.anderson@lagoal.pizza','12345'),(10,'i.thomas@lagoal.pizza','12345'),(11,'j.jackson@lagoal.pizza','12345'),(12,'k.white@lagoal.pizza','12345'),(13,'l.harris@lagoal.pizza','12345'),(14,'m.martin@lagoal.pizza','12345'),(15,'n.thompson@lagoal.pizza','12345'),(16,'o.garcia@lagoal.pizza','12345'),(17,'p.martinez@lagoal.pizza','12345'),(18,'q.robinson@lagoal.pizza','12345'),(19,'r.clark@lagoal.pizza','12345'),(20,'s.lewis@lagoal.pizza','12345'),(21,'t.lee@lagoal.pizza','12345'),(22,'u.walker@lagoal.pizza','12345'),(23,'v.hall@lagoal.pizza','12345'),(24,'w.allen@lagoal.pizza','12345'),(25,'x.young@lagoal.pizza','12345'),(26,'john.doe@lagoal.pizza','pas21'),(27,'jane.smith@lagoal.pizza','pas22'),(28,'bob.johnson@lagoal.pizza','pas23'),(29,'alice.davis@lagoal.pizza','pas24'),(30,'charlie.brown@lagoal.pizza','pas25'),(31,'emily.wilson@lagoal.pizza','pas26'),(32,'frank.moore@lagoal.pizza','pas27'),(33,'grace.taylor@lagoal.pizza','pas28'),(34,'henry.anderson@lagoal.pizza','pas29'),(35,'isabel.thomas@lagoal.pizza','pas30'),(36,'jack.jackson@lagoal.pizza','pas31'),(37,'katie.white@lagoal.pizza','pas32'),(38,'leo.harris@lagoal.pizza','pas33'),(39,'molly.martin@lagoal.pizza','pas34'),(40,'nina.thompson@lagoal.pizza','pas35'),(41,'oscar.garcia@lagoal.pizza','pas36'),(42,'paul.martinez@lagoal.pizza','pas37'),(43,'quincy.robinson@lagoal.pizza','pas38'),(44,'rachel.clark@lagoal.pizza','pas39'),(45,'sophia.lewis@lagoal.pizza','pas40');
/*!40000 ALTER TABLE `employee_credentials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `position_id` int NOT NULL,
  `address_id` int DEFAULT NULL,
  `restaurant_id` int DEFAULT NULL,
  `employee_credentials_id` int DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `position_id` (`position_id`),
  KEY `address_id` (`address_id`),
  KEY `restaurant_id` (`restaurant_id`),
  KEY `fk_employee_credentials` (`employee_credentials_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`position_id`) REFERENCES `positions` (`position_id`),
  CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`address_id`) REFERENCES `employee_address` (`ID`),
  CONSTRAINT `employees_ibfk_3` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`restaurant_id`),
  CONSTRAINT `fk_employee_credentials` FOREIGN KEY (`employee_credentials_id`) REFERENCES `employee_credentials` (`employee_credentials_id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'John','Doe',1,1,1,1),(2,'Jane','Smith',2,2,1,2),(3,'Bob','Johnson',3,3,1,3),(4,'Alice','Davis',4,4,1,4),(5,'Charlie','Brown',5,5,1,5),(6,'Emily','Wilson',1,6,2,6),(7,'Frank','Moore',2,7,2,7),(8,'Grace','Taylor',3,8,2,8),(9,'Henry','Anderson',4,9,2,9),(10,'Isabel','Thomas',5,10,2,10),(11,'Jack','Jackson',1,11,3,11),(12,'Katie','White',2,12,3,12),(13,'Leo','Harris',3,13,3,13),(14,'Molly','Martin',4,14,3,14),(15,'Nina','Thompson',5,15,3,15),(16,'Oscar','Garcia',1,16,4,16),(17,'Paul','Martinez',2,17,4,17),(18,'Quincy','Robinson',3,18,4,18),(19,'Rachel','Clark',4,19,4,19),(20,'Sophia','Lewis',5,20,4,20),(21,'Tom','Lee',1,21,5,21),(22,'Uma','Walker',2,22,5,22),(23,'Victor','Hall',3,23,5,23),(24,'Wendy','Allen',4,24,5,24),(25,'Xander','Young',5,25,5,25),(26,'John','Doe',3,26,1,26),(27,'Jane','Smith',3,27,1,27),(28,'Bob','Johnson',3,28,1,28),(29,'Alice','Davis',3,29,1,29),(30,'Charlie','Brown',3,30,1,30),(31,'Emily','Wilson',3,31,1,31),(32,'Frank','Moore',3,32,1,32),(33,'Grace','Taylor',3,33,1,33),(34,'Henry','Anderson',3,34,1,34),(35,'Isabel','Thomas',3,35,1,35),(36,'Jack','Jackson',3,36,1,36),(37,'Katie','White',3,37,1,37),(38,'Leo','Harris',3,38,1,38),(39,'Molly','Martin',3,39,1,39),(40,'Nina','Thompson',3,40,1,40),(41,'Oscar','Garcia',3,41,1,41),(42,'Paul','Martinez',3,42,1,42),(43,'Quincy','Robinson',3,43,1,43),(44,'Rachel','Clark',3,44,1,44),(45,'Sophia','Lewis',3,45,1,45);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gender`
--

DROP TABLE IF EXISTS `gender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gender` (
  `gender_id` int NOT NULL AUTO_INCREMENT,
  `gender` varchar(1) NOT NULL,
  PRIMARY KEY (`gender_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gender`
--

LOCK TABLES `gender` WRITE;
/*!40000 ALTER TABLE `gender` DISABLE KEYS */;
INSERT INTO `gender` VALUES (1,'M'),(2,'F');
/*!40000 ALTER TABLE `gender` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredient`
--

DROP TABLE IF EXISTS `ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredient` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `vegetarian` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient`
--

LOCK TABLES `ingredient` WRITE;
/*!40000 ALTER TABLE `ingredient` DISABLE KEYS */;
INSERT INTO `ingredient` VALUES (1,'Tomato Sauce',2,1),(2,'Mozzarella',3,1),(3,'Pepperoni',3,0),(4,'Ham',3,0),(5,'Bacon',3,0),(6,'Mushrooms',1.6,1),(7,'Onions',1,1),(8,'Green Peppers',1.4,1),(9,'Olives',1.4,1),(10,'Pineapple',1.6,1),(11,'Chicken',3.6,0),(12,'Beef',4,0),(13,'Spinach',1.4,1),(14,'Artichoke',1.8,1),(15,'Sausage',3,0),(16,'Parmesan Cheese',2,1),(17,'BBQ Sauce',1.2,1),(18,'Garlic',0.6,1),(19,'Cheddar Cheese',2,1),(20,'Dough',2,1);
/*!40000 ALTER TABLE `ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_deserts`
--

DROP TABLE IF EXISTS `menu_deserts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu_deserts` (
  `desert_id` int NOT NULL,
  `discount` float DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`desert_id`),
  CONSTRAINT `menu_deserts_ibfk_1` FOREIGN KEY (`desert_id`) REFERENCES `deserts` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_deserts`
--

LOCK TABLES `menu_deserts` WRITE;
/*!40000 ALTER TABLE `menu_deserts` DISABLE KEYS */;
/*!40000 ALTER TABLE `menu_deserts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_drinks`
--

DROP TABLE IF EXISTS `menu_drinks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu_drinks` (
  `drink_id` int NOT NULL,
  `discount` float DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`drink_id`),
  CONSTRAINT `menu_drinks_ibfk_1` FOREIGN KEY (`drink_id`) REFERENCES `drinks` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_drinks`
--

LOCK TABLES `menu_drinks` WRITE;
/*!40000 ALTER TABLE `menu_drinks` DISABLE KEYS */;
/*!40000 ALTER TABLE `menu_drinks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_pizza`
--

DROP TABLE IF EXISTS `menu_pizza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu_pizza` (
  `pizza_id` int NOT NULL,
  `discount` float DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`pizza_id`),
  CONSTRAINT `menu_pizza_ibfk_1` FOREIGN KEY (`pizza_id`) REFERENCES `pizza` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_pizza`
--

LOCK TABLES `menu_pizza` WRITE;
/*!40000 ALTER TABLE `menu_pizza` DISABLE KEYS */;
INSERT INTO `menu_pizza` VALUES (1,NULL,4.58),(2,NULL,6.87),(3,NULL,8.09),(4,NULL,7.63),(5,NULL,11.44),(6,NULL,7.48),(7,NULL,7.63),(8,NULL,7.02),(9,NULL,10.38);
/*!40000 ALTER TABLE `menu_pizza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offers`
--

DROP TABLE IF EXISTS `offers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `offers` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `code` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offers`
--

LOCK TABLES `offers` WRITE;
/*!40000 ALTER TABLE `offers` DISABLE KEYS */;
INSERT INTO `offers` VALUES (1,'pizza_and_drink',10,NULL),(2,'desert_and_pizza',14.99,NULL),(3,'buy_two_get_one',0,NULL),(4,'offer_10',0.1,'GOAL10');
/*!40000 ALTER TABLE `offers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_items`
--

DROP TABLE IF EXISTS `order_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_items` (
  `order_item_id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `item_id` int NOT NULL,
  `category` enum('Pizza','Drink','Desert') NOT NULL,
  `quantity` int NOT NULL DEFAULT '1',
  `price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`order_item_id`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_items`
--

LOCK TABLES `order_items` WRITE;
/*!40000 ALTER TABLE `order_items` DISABLE KEYS */;
INSERT INTO `order_items` VALUES (94,71,4,'Pizza',1,7.63),(95,72,2,'Pizza',1,6.87),(96,73,4,'Pizza',1,7.63),(97,74,4,'Pizza',1,7.63);
/*!40000 ALTER TABLE `order_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_status`
--

DROP TABLE IF EXISTS `order_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_status` (
  `status_id` int NOT NULL AUTO_INCREMENT,
  `status_name` varchar(20) NOT NULL,
  PRIMARY KEY (`status_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_status`
--

LOCK TABLES `order_status` WRITE;
/*!40000 ALTER TABLE `order_status` DISABLE KEYS */;
INSERT INTO `order_status` VALUES (1,'Being Prepared'),(2,'Out for Delivery'),(3,'Delivered'),(4,'Cancelled');
/*!40000 ALTER TABLE `order_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `status_id` int NOT NULL DEFAULT '1',
  `delivery_person_id` int DEFAULT NULL,
  `estimated_delivery_time` datetime DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `discount_applied` float DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `customer_id` (`customer_id`),
  KEY `status_id` (`status_id`),
  KEY `delivery_person_id` (`delivery_person_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`status_id`) REFERENCES `order_status` (`status_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`delivery_person_id`) REFERENCES `deliverymen` (`employee_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (71,16,7.63,3,NULL,NULL,'2024-10-06 12:57:35',0),(72,16,6.87,2,26,'2024-10-06 13:39:57','2024-10-06 13:09:08',0),(73,16,7.63,3,26,'2024-10-06 13:39:57','2024-10-06 13:09:52',0),(74,16,7.63,3,26,'2024-10-06 13:41:41','2024-10-06 13:11:36',0);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pizza`
--

DROP TABLE IF EXISTS `pizza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pizza` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `vegetarian` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pizza`
--

LOCK TABLES `pizza` WRITE;
/*!40000 ALTER TABLE `pizza` DISABLE KEYS */;
INSERT INTO `pizza` VALUES (1,'Margherita',1),(2,'Pepperoni',0),(3,'Hawaii',0),(4,'Vegetarian Delight',1),(5,'Meat Feast',0),(6,'BBQ Chicken',0),(7,'Four Cheese',1),(8,'Spinach Artichoke',1),(9,'Beef Delight',0);
/*!40000 ALTER TABLE `pizza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pizza_ingredient`
--

DROP TABLE IF EXISTS `pizza_ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pizza_ingredient` (
  `pizza_id` int NOT NULL,
  `ingredient_id` int NOT NULL,
  `quantity` decimal(5,2) NOT NULL DEFAULT '1.00',
  PRIMARY KEY (`pizza_id`,`ingredient_id`),
  KEY `ingredient_id` (`ingredient_id`),
  CONSTRAINT `pizza_ingredient_ibfk_1` FOREIGN KEY (`pizza_id`) REFERENCES `pizza` (`ID`) ON DELETE CASCADE,
  CONSTRAINT `pizza_ingredient_ibfk_2` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredient` (`ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pizza_ingredient`
--

LOCK TABLES `pizza_ingredient` WRITE;
/*!40000 ALTER TABLE `pizza_ingredient` DISABLE KEYS */;
INSERT INTO `pizza_ingredient` VALUES (1,1,1.00),(1,2,1.00),(1,20,1.00),(2,1,1.00),(2,2,1.00),(2,3,1.00),(2,20,1.00),(3,1,1.00),(3,2,1.00),(3,4,1.00),(3,10,1.00),(3,20,1.00),(4,1,1.00),(4,2,1.00),(4,6,1.00),(4,7,1.00),(4,8,1.00),(4,20,1.00),(5,1,1.00),(5,2,1.00),(5,3,1.00),(5,5,1.00),(5,15,1.00),(5,20,1.00),(6,2,1.00),(6,11,1.00),(6,17,1.00),(6,20,1.00),(7,1,1.00),(7,2,1.00),(7,16,1.00),(7,19,1.00),(7,20,1.00),(8,1,1.00),(8,2,1.00),(8,13,1.00),(8,14,1.00),(8,20,1.00),(9,1,1.00),(9,2,1.00),(9,12,1.00),(9,15,1.00),(9,18,1.00),(9,20,1.00);
/*!40000 ALTER TABLE `pizza_ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `pizza_prices`
--

DROP TABLE IF EXISTS `pizza_prices`;
/*!50001 DROP VIEW IF EXISTS `pizza_prices`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `pizza_prices` AS SELECT 
 1 AS `pizza_id`,
 1 AS `pizza_name`,
 1 AS `total_price`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `positions`
--

DROP TABLE IF EXISTS `positions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `positions` (
  `position_id` int NOT NULL AUTO_INCREMENT,
  `position` varchar(255) DEFAULT NULL,
  `wage` float DEFAULT NULL,
  PRIMARY KEY (`position_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `positions`
--

LOCK TABLES `positions` WRITE;
/*!40000 ALTER TABLE `positions` DISABLE KEYS */;
INSERT INTO `positions` VALUES (1,'Chef',1000),(2,'Cashier',600),(3,'Delivery Driver',600),(4,'Manager',1200),(5,'Assistant Chef',800);
/*!40000 ALTER TABLE `positions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postal_codes`
--

DROP TABLE IF EXISTS `postal_codes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postal_codes` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `postal_code` varchar(8) NOT NULL,
  `street` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postal_codes`
--

LOCK TABLES `postal_codes` WRITE;
/*!40000 ALTER TABLE `postal_codes` DISABLE KEYS */;
INSERT INTO `postal_codes` VALUES (1,'6211AA','Brusselsestraat'),(2,'6211AB','Boschstraat'),(3,'6211AC','Bredestraat'),(4,'6211AD','Hoge Barakken'),(5,'6211AE','Kesselskade'),(6,'6211AG','Maastrichter Brugstraat'),(7,'6211AH','Sint Servaasklooster'),(8,'6211AJ','Mariastraat'),(9,'6211AL','Jodenstraat'),(10,'6211AM','Stokstraat'),(11,'6211AN','Helmstraat'),(12,'6211AP','Kleine Gracht'),(13,'6211AR','Sint Amorsplein'),(14,'6211AS','Onze Lieve Vrouweplein'),(15,'6211AT','Ezelmarkt'),(16,'6211AW','Maastrichter Smedenstraat'),(17,'6211AX','Oeverwal'),(18,'6211AZ','Heidenstraat'),(19,'6211BA','Papengang'),(20,'6211BB','Kapoenstraat'),(21,'6211BC','Vijfkoppenstraat'),(22,'6211BD','Sint Bernardusstraat'),(23,'6211BE','Muntstraat'),(24,'6211BG','Achter de Molens'),(25,'6211BH','Hof van Tilly'),(26,'6211BJ','Heggenstraat'),(27,'6211BK','Bourgognestraat'),(28,'6211BL','Bergstraat'),(29,'6211BM','Raadhuisstraat'),(30,'6211BN','Graanmarkt'),(31,'6211BP','Kommel'),(32,'6211BR','Scharnerweg'),(33,'6211BS','Statensingel'),(34,'6211BT','Batterijstraat'),(35,'6211BV','Van Hasseltkade'),(36,'6211BW','Hof van Lorreinen'),(37,'6211BX','Achter het Vleeshuis'),(38,'6211BY','Hoogbrugstraat'),(39,'6211BZ','Lage Barakken'),(40,'6211CA','Zwingelput'),(41,'6211CB','Bouillonstraat'),(42,'6211CC','Kleine Looiersstraat'),(43,'6211CD','Lenculenstraat'),(44,'6211CE','Oude Tweebergenpoort'),(45,'6211CF','Tongersestraat'),(46,'6211CG','Bieslanderweg'),(47,'6211CH','Bouillonstraat'),(48,'6211CJ','Helstraat'),(49,'6211CK','Binnenstad'),(50,'6211CL','Heggenstraat'),(51,'6211CM','Hoogfrankrijk'),(52,'6211CN','Kapoenstraat'),(53,'6211CP','Minckelersstraat'),(54,'6211CQ','Kleine Looiersstraat'),(55,'6211CR','Onze Lieve Vrouweplein'),(56,'6211CS','Stokstraat'),(57,'6211CT','Scharnerweg'),(58,'6211CV','Wilhelminasingel'),(59,'6211CW','Zwingelput'),(60,'6211CX','Brusselsestraat'),(61,'6211CY','Kesselskade'),(62,'6211CZ','Hoge Barakken'),(63,'6211DA','Statensingel'),(64,'6211DB','Maastrichter Brugstraat'),(65,'6211DC','Raadhuisstraat'),(66,'6211DD','Stokstraat'),(67,'6211DE','Kapoenstraat'),(68,'6211DF','Heggenstraat'),(69,'6211DG','Vijfkoppenstraat'),(70,'6211DH','Sint Bernardusstraat'),(71,'6211DJ','Muntstraat'),(72,'6211DK','Achter de Molens'),(73,'6211DL','Hof van Tilly'),(74,'6211DM','Heggenstraat'),(75,'6211DN','Bourgognestraat'),(76,'6211DP','Bergstraat'),(77,'6211DR','Raadhuisstraat'),(78,'6211DS','Graanmarkt'),(79,'6211DT','Kommel'),(80,'6211DV','Scharnerweg'),(81,'6211DW','Statensingel'),(82,'6211DX','Batterijstraat'),(83,'6211DY','Van Hasseltkade'),(84,'6211DZ','Hof van Lorreinen'),(85,'6211EA','Achter het Vleeshuis'),(86,'6211EB','Hoogbrugstraat'),(87,'6211EC','Lage Barakken'),(88,'6211ED','Zwingelput'),(89,'6211EE','Bouillonstraat'),(90,'6211EF','Kleine Looiersstraat'),(91,'6211EG','Lenculenstraat'),(92,'6211EH','Oude Tweebergenpoort'),(93,'6211EJ','Tongersestraat'),(94,'6211EK','Bieslanderweg'),(95,'6211EL','Bouillonstraat'),(96,'6211EM','Helstraat'),(97,'6221EL','Rechtstraat');
/*!40000 ALTER TABLE `postal_codes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_address`
--

DROP TABLE IF EXISTS `restaurant_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant_address` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `street_number` int DEFAULT NULL,
  `postal_code_id` int DEFAULT NULL,
  `city_id` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `postal_code_id` (`postal_code_id`),
  KEY `city_id` (`city_id`),
  CONSTRAINT `restaurant_address_ibfk_1` FOREIGN KEY (`postal_code_id`) REFERENCES `postal_codes` (`ID`),
  CONSTRAINT `restaurant_address_ibfk_2` FOREIGN KEY (`city_id`) REFERENCES `cities` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_address`
--

LOCK TABLES `restaurant_address` WRITE;
/*!40000 ALTER TABLE `restaurant_address` DISABLE KEYS */;
INSERT INTO `restaurant_address` VALUES (1,12,1,2380),(2,18,50,2380),(3,62,96,2380),(4,34,15,2380),(5,65,79,2380);
/*!40000 ALTER TABLE `restaurant_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurants`
--

DROP TABLE IF EXISTS `restaurants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurants` (
  `restaurant_id` int NOT NULL AUTO_INCREMENT,
  `address_id` int DEFAULT NULL,
  `number_of_employee` int DEFAULT '5',
  `open` tinyint(1) DEFAULT '1',
  `earnings` float DEFAULT '0',
  `postal_code_cover_till` int DEFAULT NULL,
  `postal_code_cover_from` int DEFAULT NULL,
  PRIMARY KEY (`restaurant_id`),
  KEY `address_id` (`address_id`),
  CONSTRAINT `restaurants_ibfk_1` FOREIGN KEY (`address_id`) REFERENCES `restaurant_address` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurants`
--

LOCK TABLES `restaurants` WRITE;
/*!40000 ALTER TABLE `restaurants` DISABLE KEYS */;
INSERT INTO `restaurants` VALUES (1,1,5,1,529.532,20,1),(2,2,5,1,0,40,21),(3,3,5,1,109.814,60,41),(4,4,5,1,0,80,61),(5,5,5,1,24.068,97,81);
/*!40000 ALTER TABLE `restaurants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `pizza_prices`
--

/*!50001 DROP VIEW IF EXISTS `pizza_prices`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `pizza_prices` AS select 1 AS `pizza_id`,1 AS `pizza_name`,1 AS `total_price` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-06 13:19:36
