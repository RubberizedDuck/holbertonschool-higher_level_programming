-- Task 3: Always a name
-- Creates table 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- Creates table 'states' where 'id' is unique auto generated can't be null
-- and is a primary key, and 'name' is not null
CREATE TABLE IF NOT EXISTS states (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL
);
