-- list all cities of california
SELECT cities.name
FROM cities
JOIN states ON cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;