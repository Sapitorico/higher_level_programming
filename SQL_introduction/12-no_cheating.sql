-- update the score
UPDATE second_table SET score = 10 WHERE name = "Bob"
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;