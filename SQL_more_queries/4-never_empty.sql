-- Task 3: Always a name
-- Creates table 'id_not_null' where id defaults to 1 if no value set
CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
