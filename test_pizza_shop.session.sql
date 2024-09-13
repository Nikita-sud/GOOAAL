CREATE TABLE customer(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    gender INT NOT NULL,
    birthdate DATE,
    phone TINYINT,
    address INT NOT NULL,
    number_orders INT DEFAULT 0
)

SELECT * FROM customer;