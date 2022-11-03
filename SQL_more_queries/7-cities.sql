-- Task 3: Always a name
-- Creates table 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- Creates table 'cities' where 'id' is unique auto generated can't be null
-- and is a primary key, 'state_id' cant be null and must be a foreign key
-- that references id of the states table, and 'name' is not null
CREATE TABLE IF NOT EXISTS cities (
       id INT AUTO_INCREMENT PRIMARY KEY,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY (state_id) REFERENCES states(id)
);
