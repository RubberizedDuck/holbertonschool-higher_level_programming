-- Task 16: Say my name
-- Lists all records that have a 'name' value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
