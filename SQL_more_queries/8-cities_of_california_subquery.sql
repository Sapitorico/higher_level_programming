-- list all cities of california
SELECT id, name
FROM cities
WHERE states_id IN(
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ;