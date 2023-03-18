-- script that lists all genres displays the number of shows linked to each
SELECT genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_shows_genres ON genres.id = GROUP BY genre ORDER BY number_of_shows DESC;