-- Task 15:
-- Returns the count of score and how many occurances
SELECT score, COUNT(score) AS 'number'
FROM second_table
GROUP BY score
ORDER BY number DESC
