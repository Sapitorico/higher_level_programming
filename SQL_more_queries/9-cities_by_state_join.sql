-- list all cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.id
ORDER BY cities.id;