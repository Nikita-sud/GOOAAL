-- DESCRIBE credentials;
-- ALTER TABLE customer
-- CHANGE COLUMN ID customer_id INT NOT NULL AUTO_INCREMENT;

-- ALTER TABLE customer
-- MODIFY COLUMN phone varchar(8);

-- INSERT INTO customer (name, last_name, gender, birthdate, phone, address, number_orders)
-- VALUES ('Timur', 'Jercak', 1, '2012-12-12', '+12345', 1, 0);

-- SELECT * FROM customer;

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

SELECT * FROM credentials;
-- DESCRIBE credentials;