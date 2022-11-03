-- Task 8: Cities of California
-- Lists all cities from the state of California
SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY id ASC;
