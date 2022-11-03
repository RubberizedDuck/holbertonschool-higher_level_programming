-- Task 1: Root user
-- creates user 'user_0d_1' with all privileges
CREATE USER IF NOT EXISTS
       'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
