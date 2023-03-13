-- list the number of recors whit same score in the table
SELECT score, COUNT(*) 'number' FROM second_table GROUP BY score ORDER BY score DESC;