-- script that lists all genres displays the number of shows linked to each
SELECT genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
JOIN tv_shows_genres ON genres.id = shows_genres.genre_id
JOIN tv_shows ON shows_genres.show_id = tv_shows.id
GROUP BY genres.name
HAVING COUNT(tv_shows.id) > 0
ORDER BY number_of_shows DESC;