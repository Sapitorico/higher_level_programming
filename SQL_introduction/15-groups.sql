-- list the number of recors whit same score in the table
SELECT score, COUNT(*) FROM second_table GROUP BY score;