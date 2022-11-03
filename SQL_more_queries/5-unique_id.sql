-- Task 3: Always a name
-- Creates table 'unique_id' where id defaults to 1 if no value is set
-- and id is unique
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
