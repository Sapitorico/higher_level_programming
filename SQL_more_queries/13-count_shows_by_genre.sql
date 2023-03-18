-- script that lists all genres displays the number of shows linked to each
SELECT g.name AS genre, COUNT(tsg.show_id) AS number_of_shows
FROM genres AS g
JOIN tv_show_genres AS tsg ON g.id = tsg.genre_id
WHERE EXISTS (
    ELECT 1
    FROM tv_shows AS ts
    WHERE ts.id = tsg.show_id
)
GROUP BY g.name
ORDER BY number_of_shows DESC;