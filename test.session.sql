-- DESCRIBE credentials;
-- ALTER TABLE customer
-- CHANGE COLUMN ID customer_id INT NOT NULL AUTO_INCREMENT;
-- SELECT * FROM customer;
-- SELECT * FROM cust;
-- SELECT * FROM customer;
-- ALTER TABLE customer
-- ADD COLUMN discount_for_next FLOAT DEFAULT 0.00;

-- INSERT INTO offers(name, price, code) VALUES 
-- ('offer_10', 0.1, 'GOAL10');
-- CREATE TABLE employees(
--     employee_id INT AUTO_INCREMENT PRIMARY KEY,
--     first_name VARCHAR(20),
--     last_name VARCHAR(20),
--     position_id INT NOT NULL,
--     address_id INT,
--     restaurant_id INT,
--     FOREIGN KEY (position_id) REFERENCES positions(position_id),
--     FOREIGN KEY (address_id) REFERENCES employee_address(ID),
--     FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
-- )
-- ALTER TABLE employees
-- MODIFY employee_credentials_id INT;
-- CREATE TABLE employee_credentials(
--     employee_credentials_id INT AUTO_INCREMENT PRIMARY KEY,
--     email VARCHAR(100) NOT NULL,
--     password VARCHAR(5)
-- );
-- INSERT INTO employees (first_name, last_name, position_id, address_id, restaurant_id, employee_credentials_id)
-- VALUES
-- -- Для ресторана 1
-- ('John', 'Doe', 1, 1, 1, 1),
-- ('Jane', 'Smith', 2, 2, 1, 2),
-- ('Bob', 'Johnson', 3, 3, 1, 3),
-- ('Alice', 'Davis', 4, 4, 1, 4),
-- ('Charlie', 'Brown', 5, 5, 1, 5),

-- -- Для ресторана 2
-- ('Emily', 'Wilson', 1, 6, 2, 6),
-- ('Frank', 'Moore', 2, 7, 2, 7),
-- ('Grace', 'Taylor', 3, 8, 2, 8),
-- ('Henry', 'Anderson', 4, 9, 2, 9),
-- ('Isabel', 'Thomas', 5, 10, 2, 10),

-- -- Для ресторана 3
-- ('Jack', 'Jackson', 1, 11, 3, 11),
-- ('Katie', 'White', 2, 12, 3, 12),
-- ('Leo', 'Harris', 3, 13, 3, 13),
-- ('Molly', 'Martin', 4, 14, 3, 14),
-- ('Nina', 'Thompson', 5, 15, 3, 15),

-- -- Для ресторана 4
-- ('Oscar', 'Garcia', 1, 16, 4, 16),
-- ('Paul', 'Martinez', 2, 17, 4, 17),
-- ('Quincy', 'Robinson', 3, 18, 4, 18),
-- ('Rachel', 'Clark', 4, 19, 4, 19),
-- ('Sophia', 'Lewis', 5, 20, 4, 20),

-- -- Для ресторана 5
-- ('Tom', 'Lee', 1, 21, 5, 21),
-- ('Uma', 'Walker', 2, 22, 5, 22),
-- ('Victor', 'Hall', 3, 23, 5, 23),
-- ('Wendy', 'Allen', 4, 24, 5, 24),
-- ('Xander', 'Young', 5, 25, 5, 25);

-- INSERT INTO employee_credentials (email, password)
-- VALUES
-- ('j.doe@lagoal.pizza', '12345'),
-- ('j.smith@lagoal.pizza', '12345'),
-- ('b.johnson@lagoal.pizza', '12345'),
-- ('a.davis@lagoal.pizza', '12345'),
-- ('c.brown@lagoal.pizza', '12345'),

-- ('e.wilson@lagoal.pizza', '12345'),
-- ('f.moore@lagoal.pizza', '12345'),
-- ('g.taylor@lagoal.pizza', '12345'),
-- ('h.anderson@lagoal.pizza', '12345'),
-- ('i.thomas@lagoal.pizza', '12345'),
-- ('j.jackson@lagoal.pizza', '12345'),
-- ('k.white@lagoal.pizza', '12345'),
-- ('l.harris@lagoal.pizza', '12345'),
-- ('m.martin@lagoal.pizza', '12345'),
-- ('n.thompson@lagoal.pizza', '12345'),


-- ('o.garcia@lagoal.pizza', '12345'),
-- ('p.martinez@lagoal.pizza', '12345'),
-- ('q.robinson@lagoal.pizza', '12345'),
-- ('r.clark@lagoal.pizza', '12345'),
-- ('s.lewis@lagoal.pizza', '12345'),

-- ('t.lee@lagoal.pizza', '12345'),
-- ('u.walker@lagoal.pizza', '12345'),
-- ('v.hall@lagoal.pizza', '12345'),
-- ('w.allen@lagoal.pizza', '12345'),
-- ('x.young@lagoal.pizza', '12345');

-- INSERT INTO employees (first_name, last_name, position_id, address_id, restaurant_id, email)
-- VALUES
-- -- Для ресторана 1
-- ('John', 'Doe', 1, 1, 1, 'j.doe@lagoal.pizza'),
-- ('Jane', 'Smith', 2, 2, 1, 'j.smith@lagoal.pizza'),
-- ('Bob', 'Johnson', 3, 3, 1, 'b.johnson@lagoal.pizza'),
-- ('Alice', 'Davis', 4, 4, 1, 'a.davis@lagoal.pizza'),
-- ('Charlie', 'Brown', 5, 5, 1, 'c.brown@lagoal.pizza'),

-- -- Для ресторана 2
-- ('Emily', 'Wilson', 1, 6, 2, 'e.wilson@lagoal.pizza'),
-- ('Frank', 'Moore', 2, 7, 2, 'f.moore@lagoal.pizza'),
-- ('Grace', 'Taylor', 3, 8, 2, 'g.taylor@lagoal.pizza'),
-- ('Henry', 'Anderson', 4, 9, 2, 'h.anderson@lagoal.pizza'),
-- ('Isabel', 'Thomas', 5, 10, 2, 'i.thomas@lagoal.pizza'),

-- -- Для ресторана 3
-- ('Jack', 'Jackson', 1, 11, 3, 'j.jackson@lagoal.pizza'),
-- ('Katie', 'White', 2, 12, 3, 'k.white@lagoal.pizza'),
-- ('Leo', 'Harris', 3, 13, 3, 'l.harris@lagoal.pizza'),
-- ('Molly', 'Martin', 4, 14, 3, 'm.martin@lagoal.pizza'),
-- ('Nina', 'Thompson', 5, 15, 3, 'n.thompson@lagoal.pizza'),

-- -- Для ресторана 4
-- ('Oscar', 'Garcia', 1, 16, 4, 'o.garcia@lagoal.pizza'),
-- ('Paul', 'Martinez', 2, 17, 4, 'p.martinez@lagoal.pizza'),
-- ('Quincy', 'Robinson', 3, 18, 4, 'q.robinson@lagoal.pizza'),
-- ('Rachel', 'Clark', 4, 19, 4, 'r.clark@lagoal.pizza'),
-- ('Sophia', 'Lewis', 5, 20, 4, 's.lewis@lagoal.pizza'),

-- -- Для ресторана 5
-- ('Tom', 'Lee', 1, 21, 5, 't.lee@lagoal.pizza'),
-- ('Uma', 'Walker', 2, 22, 5, 'u.walker@lagoal.pizza'),
-- ('Victor', 'Hall', 3, 23, 5, 'v.hall@lagoal.pizza'),
-- ('Wendy', 'Allen', 4, 24, 5, 'w.allen@lagoal.pizza'),
-- ('Xander', 'Young', 5, 25, 5, 'x.young@lagoal.pizza');



-- SELECT * FROM employee_address;
-- INSERT 
-- INSERT INTO employee_address (house_number, postal_code_id, city_id)
-- VALUES
-- (101, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (102, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (103, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (104, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (105, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (106, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (107, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (108, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (109, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (110, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (111, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (112, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (113, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (114, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (115, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (116, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (117, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (118, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (119, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (120, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (121, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (122, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (123, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (124, FLOOR(1 + (RAND() * 97)), DEFAULT),
-- (125, FLOOR(1 + (RAND() * 97)), DEFAULT);

-- ALTER TABLE employee_address 
-- RENAME COLUMN street_number TO house number;
-- CREATE TABLE customer_address (
--     customer_address_id INT AUTO_INCREMENT PRIMARY KEY,
--     street_number INT,
--     apartment_number VARCHAR(8),
--     postal_code_id INT,
--     city_id INT DEFAULT 2380,
--     FOREIGN KEY (postal_code_id) REFERENCES postal_codes(ID),
--     FOREIGN KEY (city_id) REFERENCES cities(ID)
-- );
-- SELECT * FROM employee;
-- ALTER TABLE position
-- ADD COLUMN wage FLOAT;
-- CREATE TABLE positions (
--     position_id INT AUTO_INCREMENT PRIMARY KEY,
--     position VARCHAR(255),
--     wage FLOAT
-- );
-- INSERT INTO positions (position, wage)
-- VALUES
-- ('Chef', 20.0),
-- ('Cashier', 12.5),
-- ('Delivery Driver', 15.0),
-- ('Manager', 25.0),
-- ('Assistant Chef', 17.0);
-- UPDATE positions
-- SET wage = 1000
-- WHERE position_id = 1;

-- UPDATE positions
-- SET wage = 600
-- WHERE position_id = 2;

-- UPDATE positions
-- SET wage = 600
-- WHERE position_id = 3;

-- UPDATE positions
-- SET wage = 1200
-- WHERE position_id = 4;

-- UPDATE positions
-- SET wage = 800
-- WHERE position_id = 5;
-- DELETE FROM orders;

-- INSERT INTO customer_address(customer_address_id, street_number, apartment_number, postal_code_id, city_id) VALUES
-- (1, 23, 4, 96, 2380),
-- (2, 12, 1, 12, 2380);

-- ALTER TABLE customer
-- MODIFY COLUMN phone varchar(8);
-- SELECT * FROM postal_codes;
-- INSERT INTO customer (name, last_name, gender, birthdate, phone, address, number_orders)
-- VALUES ('Timur', 'Jercak', 1, '2012-12-12', '+12345', 1, 0);
-- CREATE TABLE restaurants(
--     restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
--     address_id INT,
--     number_of_employee INT DEFAULT 5,
--     open BOOLEAN DEFAULT TRUE,
--     earnings FLOAT DEFAULT 0.0,
--     FOREIGN KEY (address_id) REFERENCES restaurant_address(ID)
--     ON DELETE CASCADE
--     ON UPDATE CASCADE
-- )
-- ALTER TABLE restaurants
-- ADD COLUMN postal_code_cover_from INT;
-- UPDATE restaurants
-- SET postal_code_cover_from = 81
-- WHERE restaurant_id=5;
-- UPDATE restaurants
-- SET postal_code_cover_till = 97
-- WHERE restaurant_id=5;
-- SELECT * FROM restaurants;
-- INSERT INTO restaurants (restaurant_id, address_id)
-- VALUES
-- (1, 1),
-- (2,2),
-- (3,3),
-- (4,4),
-- (5,5)
-- DESCRIBE restaurant_address;
-- 2380 Maastricht
-- 1 - 5
-- INSERT INTO restaurant_address (ID, street_number, postal_code_id, city_id)
-- VALUES
-- (1, 12, 1, 2380),
-- (2, 18, 50, 2380),
-- (3, 62, 96, 2380),
-- (4, 34, 15, 2380),
-- (5, 65, 79, 2380);

-- ALTER TABLE positions
-- MODIFY COLUMN position VARCHAR(50);

-- DELETE FROM orders;
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


-- SELECT * FROM customer;