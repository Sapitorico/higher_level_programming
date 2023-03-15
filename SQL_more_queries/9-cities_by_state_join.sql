-- list all cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id AND states.name
ORDER BY cities.id;