-- CREATE TABLE users 
-- (id INT NOT NULL AUTO_INCREMENT , 
-- username VARCHAR(20) NOT NULL , 
-- password VARCHAR(20) NOT NULL , 
-- PRIMARY KEY (id));

-- ALTER TABLE users ADD date DATE NOT NULL AFTER password;

INSERT INTO users 
(`id`, `username`, `password`, `date`) 
VALUES (NULL, 'davies', '1234', '2024-04-24'), 
(NULL, 'purazi', '1234', '2024-04-01');