-- Task 9: Cities by States
-- Returns ordered list of cities including state name
SELECT cities.id, cities.name, states.name FROM cities
LEFT JOIN states ON states.id = cities.state_id;
