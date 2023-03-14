-- list all cities of california
SELECT name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;