-- task 
SELECT cities.id, cities.name, states.name
FROM cities inner join states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
