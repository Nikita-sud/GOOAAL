-- DESCRIBE credentials;
-- ALTER TABLE customer
-- CHANGE COLUMN ID customer_id INT NOT NULL AUTO_INCREMENT;

-- ALTER TABLE customer
-- MODIFY COLUMN phone varchar(8);

-- INSERT INTO customer (name, last_name, gender, birthdate, phone, address, number_orders)
-- VALUES ('Timur', 'Jercak', 1, '2012-12-12', '+12345', 1, 0);

-- SELECT * FROM order_status;
-- SHOW TABLES;
-- SELECT * FROM orders;
-- ALTER TABLE offers
-- MODIFY COLUMN name varchar(40);
-- INSERT INTO offers(name, price)
-- VALUES
-- ("pizza_and_drink", 10.00),
-- ("desert_and_pizza", 14.99),
-- ("buy_two_get_one", 0.00);

-- ALTER TABLE offers 
-- CHANGE COLUMN discount price FLOAT;

-- UPDATE pizza 
-- SET name = "Hawaii"
-- WHERE id = 3;
-- ALTER TABLE pizza
-- ADD COLUMN pizza_img CHAR(64);
-- DESCRIBE credentials;
-- SHOW TABLES;
-- DESCRIBE customer;

-- UPDATE customer
-- SET address = 2
-- WHERE customer_id = 2;

-- CREATE TABLE credentials (
--     customer_id INT,
--     username VARCHAR(10) NOT NULL,
--     password VARCHAR(8) NOT NULL,
--     salt VARCHAR(4) NOT NULL,
--     FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
--     ON DELETE CASCADE
--     ON UPDATE CASCADE
-- );

-- INSERT INTO credentials VALUES (2, "test", "12345", "A3@X");
-- ALTER TABLE credentials MODIFY salt BLOB;

-- SELECT * FROM credentials;
-- DESCRIBE credentials;

-- CREATE TABLE postal_code(
--     postal_code_id INT AUTO_INCREMENT PRIMARY KEY,
--     postal_code VARCHAR(6) NOT NULL,
--     street VARCHAR(50) NOT NULL
-- )

-- SELECT * FROM customer AS c
-- JOIN gender AS g ON c.gender_id=g.gender_id;

-- ALTER TABLE customer
-- RENAME COLUMN gender TO gender_id;

-- CREATE TABLE gender(
--     gender_id INT AUTO_INCREMENT PRIMARY KEY,
--     gender VARCHAR(1) NOT NULL
-- )
-- INSERT INTO gender (gender) VALUES
-- ('M'),
-- ('F');

-- ALTER TABLE customer
-- ADD CONSTRAINT fk_gender
-- FOREIGN KEY (gender) REFERENCES gender(gender_id);

-- INSERT INTO postal_code (postal_code, street) VALUES
-- ('6211AA', 'Brusselsestraat'),
-- ('6211AB', 'Boschstraat'),
-- ('6211AC', 'Bredestraat'),
-- ('6211AD', 'Hoge Barakken'),
-- ('6211AE', 'Kesselskade'),
-- ('6211AG', 'Maastrichter Brugstraat'),
-- ('6211AH', 'Sint Servaasklooster'),
-- ('6211AJ', 'Mariastraat'),
-- ('6211AL', 'Jodenstraat'),
-- ('6211AM', 'Stokstraat'),
-- ('6211AN', 'Helmstraat'),
-- ('6211AP', 'Kleine Gracht'),
-- ('6211AR', 'Sint Amorsplein'),
-- ('6211AS', 'Onze Lieve Vrouweplein'),
-- ('6211AT', 'Ezelmarkt'),
-- ('6211AW', 'Maastrichter Smedenstraat'),
-- ('6211AX', 'Oeverwal'),
-- ('6211AZ', 'Heidenstraat'),
-- ('6211BA', 'Papengang'),
-- ('6211BB', 'Kapoenstraat'),
-- ('6211BC', 'Vijfkoppenstraat'),
-- ('6211BD', 'Sint Bernardusstraat'),
-- ('6211BE', 'Muntstraat'),
-- ('6211BG', 'Achter de Molens'),
-- ('6211BH', 'Hof van Tilly'),
-- ('6211BJ', 'Heggenstraat'),
-- ('6211BK', 'Bourgognestraat'),
-- ('6211BL', 'Bergstraat'),
-- ('6211BM', 'Raadhuisstraat'),
-- ('6211BN', 'Graanmarkt'),
-- ('6211BP', 'Kommel'),
-- ('6211BR', 'Scharnerweg'),
-- ('6211BS', 'Statensingel'),
-- ('6211BT', 'Batterijstraat'),
-- ('6211BV', 'Van Hasseltkade'),
-- ('6211BW', 'Hof van Lorreinen'),
-- ('6211BX', 'Achter het Vleeshuis'),
-- ('6211BY', 'Hoogbrugstraat'),
-- ('6211BZ', 'Lage Barakken'),
-- ('6211CA', 'Zwingelput'),
-- ('6211CB', 'Bouillonstraat'),
-- ('6211CC', 'Kleine Looiersstraat'),
-- ('6211CD', 'Lenculenstraat'),
-- ('6211CE', 'Oude Tweebergenpoort'),
-- ('6211CF', 'Tongersestraat'),
-- ('6211CG', 'Bieslanderweg'),
-- ('6211CH', 'Bouillonstraat'),
-- ('6211CJ', 'Helstraat'),
-- ('6211CK', 'Binnenstad'),
-- ('6211CL', 'Heggenstraat'),
-- ('6211CM', 'Hoogfrankrijk'),
-- ('6211CN', 'Kapoenstraat'),
-- ('6211CP', 'Minckelersstraat'),
-- ('6211CQ', 'Kleine Looiersstraat'),
-- ('6211CR', 'Onze Lieve Vrouweplein'),
-- ('6211CS', 'Stokstraat'),
-- ('6211CT', 'Scharnerweg'),
-- ('6211CV', 'Wilhelminasingel'),
-- ('6211CW', 'Zwingelput'),
-- ('6211CX', 'Brusselsestraat'),
-- ('6211CY', 'Kesselskade'),
-- ('6211CZ', 'Hoge Barakken'),
-- ('6211DA', 'Statensingel'),
-- ('6211DB', 'Maastrichter Brugstraat'),
-- ('6211DC', 'Raadhuisstraat'),
-- ('6211DD', 'Stokstraat'),
-- ('6211DE', 'Kapoenstraat'),
-- ('6211DF', 'Heggenstraat'),
-- ('6211DG', 'Vijfkoppenstraat'),
-- ('6211DH', 'Sint Bernardusstraat'),
-- ('6211DJ', 'Muntstraat'),
-- ('6211DK', 'Achter de Molens'),
-- ('6211DL', 'Hof van Tilly'),
-- ('6211DM', 'Heggenstraat'),
-- ('6211DN', 'Bourgognestraat'),
-- ('6211DP', 'Bergstraat'),
-- ('6211DR', 'Raadhuisstraat'),
-- ('6211DS', 'Graanmarkt'),
-- ('6211DT', 'Kommel'),
-- ('6211DV', 'Scharnerweg'),
-- ('6211DW', 'Statensingel'),
-- ('6211DX', 'Batterijstraat'),
-- ('6211DY', 'Van Hasseltkade'),
-- ('6211DZ', 'Hof van Lorreinen'),
-- ('6211EA', 'Achter het Vleeshuis'),
-- ('6211EB', 'Hoogbrugstraat'),
-- ('6211EC', 'Lage Barakken'),
-- ('6211ED', 'Zwingelput'),
-- ('6211EE', 'Bouillonstraat'),
-- ('6211EF', 'Kleine Looiersstraat'),
-- ('6211EG', 'Lenculenstraat'),
-- ('6211EH', 'Oude Tweebergenpoort'),
-- ('6211EJ', 'Tongersestraat'),
-- ('6211EK', 'Bieslanderweg'),
-- ('6211EL', 'Bouillonstraat'),
-- ('6211EM', 'Helstraat'),
-- ('6221EL', 'Rechtstraat');


SELECT * FROM customer;